"""
src/gemini_video_analyze.py — analyze videos DIRECTLY (audio + VISUAL) via Gemini's YouTube-URL input.

The big unblock. YouTube blocks transcript/audio fetches from datacenter IPs, but the Gemini API
accepts a YouTube URL as video input and Google fetches it server-side — so the cloud can have
Gemini WATCH each video (no transcript, no IP block) and extract skills/tools/connectors PLUS the
VISUAL things a transcript misses (on-screen tools, UIs, demos). Free tier: ~8h of YouTube/day.

Uses the existing Gemini key (EXTERNAL_REVIEW_API_KEY). Stdlib only. State + a daily-minutes budget
in data/gemini_analyzed.json so we stay inside the free quota.

Usage:  GEMINI/EXTERNAL_REVIEW_API_KEY=...  python -m src.gemini_video_analyze --limit 20
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from src.bulk_analyze import CATEGORIES, load, save, slugify, norm, NOW
from src.mine_feeds import merge

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
PROCESSED = DATA / "processed"
STATE = DATA / "gemini_analyzed.json"
MODEL = "gemini-2.5-flash"
DAILY_MINUTES = 440          # stay safely under the ~8h (480m)/day free YouTube quota


def _iso_minutes(iso: str) -> int:
    m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    if not m:
        return 12
    h, mi, s = (int(x) if x else 0 for x in m.groups())
    return max(1, round(h * 60 + mi + s / 60))


def analyze_video(video_id: str, key: str, timeout: int = 180) -> dict | None:
    url = (f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={key}")
    prompt = (
        "You are WATCHING this AI YouTube video (audio AND on-screen visuals). Extract structured data "
        "for a skills/tools dashboard, including things shown ONLY on screen (UIs, tool names in the "
        "browser, terminal commands, websites visited) that narration may not say. STRICT JSON ONLY:\n"
        '{"relevant":true,'
        '"skills":[{"skill_name":"","slug":"","category":"","description":"","use_case":"","quality_score":1,"target_tool":"claude","tips":[]}],'
        '"tools":[{"name":"","slug":"","category":"","company":"","open_source":false,"description":"","quality_score":1,"model_version":"","release_status":"released","homepage":"","github":""}],'
        '"connectors":[{"name":"","what_it_does":"","works_in":"both","free":true,"url":""}],'
        '"prompts":[{"title":"","purpose":"","prompt_text":"","category":""}],'
        '"commands":[{"command":"","description":""}],'
        '"designs":[{"name":"","kind":"website|app|dashboard|landing|system","look":"describe the visual design: layout, colors, typography, components, vibe","tech":[],"rebuild_with":["tools/skills to build something like it"]}],'
        '"visual_notes":["short notes on things seen on screen but not said"]}\n'
        "- DESIGNS = whenever the video SHOWS a website/app/dashboard/UI worth replicating, capture its "
        "look (layout/colors/typography/components/vibe) + how to rebuild it. This is for cloning good UIs.\n"
        f"- category MUST be one of: {', '.join(CATEGORIES)}.\n"
        "- SKILLS = techniques you DO; TOOLS = products that EXIST. A product is a TOOL not a skill.\n"
        "- PROMPTS = reusable prompt text shown/dictated; COMMANDS = exact slash-commands or CLI "
        "commands shown on screen (e.g. '/compact', 'claude mcp add ...'). Capture them verbatim.\n"
        "- Capture EXACT tool names + versions seen on screen. Never invent. Empty arrays are fine.\n"
        "- homepage/github: fill ONLY with a URL ACTUALLY VISIBLE on screen (browser bar, terminal, "
        "description shown). If no real URL is shown, leave them empty. NEVER guess a URL.\n"
        'If not about AI tools/skills, return {"relevant":false}.'
    )
    body = {
        "contents": [{"parts": [
            {"fileData": {"fileUri": f"https://www.youtube.com/watch?v={video_id}"}},
            {"text": prompt},
        ]}],
        "generationConfig": {"temperature": 0.2, "responseMimeType": "application/json"},
    }
    req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"),
                                headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = json.loads(resp.read().decode("utf-8", "replace"))
        text = payload["candidates"][0]["content"]["parts"][0]["text"]
        return json.loads(text)
    except Exception as e:  # noqa: BLE001
        return {"_error": f"{type(e).__name__}: {str(e)[:140]}"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=20, help="max videos this run")
    ap.add_argument("--sleep", type=float, default=2.0)
    args = ap.parse_args()
    # MULTI-KEY (free throughput multiplier): each free Gemini key has its own ~8h/day video quota,
    # so round-robining N keys multiplies the daily free budget by N — $0. Add keys as secrets named
    # EXTERNAL_REVIEW_API_KEY, GEMINI_API_KEY, GEMINI_API_KEY_2, GEMINI_API_KEY_3, … (any number).
    keys = []
    for n in ["EXTERNAL_REVIEW_API_KEY", "GEMINI_API_KEY"] + [f"GEMINI_API_KEY_{i}" for i in range(2, 9)]:
        v = (os.environ.get(n) or "").strip()
        if v and v not in keys:
            keys.append(v)
    if not keys:
        print("No Gemini key (EXTERNAL_REVIEW_API_KEY / GEMINI_API_KEY[_n]) — skipped (graceful)."); return 0
    daily_budget = DAILY_MINUTES * len(keys)    # each key carries its own free quota
    ki = 0                                       # round-robin index across keys

    st = load(STATE, {}) or {}
    done = set(st.get("video_ids", []))
    failed = set(st.get("failed_ids", []))      # videos Gemini can't fetch (403/404) — never retry
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    used_today = (st.get("daily", {}) or {}).get(today, 0)

    todo = []
    for f in sorted(glob.glob(str(PROCESSED / "*.json"))):
        r = load(Path(f), None)
        if not isinstance(r, dict):
            continue
        vid = r.get("video_id")
        if not vid or vid in done or vid in failed:
            continue
        # prioritise videos with NO real transcript (no analysis at all)
        todo.append((0 if r.get("transcript_source") != "transcript" else 1, r))
    todo.sort(key=lambda x: x[0])
    todo = [r for _, r in todo]
    print(f"gemini-video: {len(todo)} candidates ({len(failed)} known-unfetchable skipped), "
          f"{used_today}m of ~{daily_budget}m used today across {len(keys)} key(s)")

    tools = load(DATA / "tools.json", {"tools": []})
    conns = load(DATA / "connectors.json", {"connectors": []})
    skills = load(DATA / "skills.json", {"skills": []})
    prompts = load(DATA / "prompts.json", {"prompts": []})
    cmds = load(DATA / "commands.json", {"commands": []})
    designs = load(DATA / "designs.json", {"designs": []})
    ns = nt = nc = npr = ncm = nd = ok = err = skip = 0
    consecutive = 0          # consecutive SYSTEMIC errors (quota/auth); a few bad videos don't count
    visual = st.get("visual_notes", [])
    for r in todo[: max(args.limit, 0)]:
        mins = _iso_minutes(r.get("duration", ""))
        if used_today + mins > daily_budget:
            print("  daily free quota reached across all keys — stopping; resumes tomorrow."); break
        vid = r["video_id"]
        time.sleep(args.sleep)
        ki = (ki + 1) % len(keys)                 # round-robin keys to spread the load/quota
        res = analyze_video(vid, keys[ki])
        # TRANSIENT rate-limit / overload (429/503) -> rotate to the NEXT key first (its quota is
        # separate), then exponential backoff + retry. So one key hitting its limit doesn't stall us.
        backoff, tries = max(args.sleep, 4.0), 0
        while (isinstance(res, dict) and res.get("_error") and tries < 4
               and any(c in res["_error"] for c in ("429", "503", "Too Many", "Unavailable",
                                                    "timed out", "timeout", "500"))):
            ki = (ki + 1) % len(keys)
            backoff = min(backoff * 2 + 6, 90)
            if tries == 0:
                print(f"  {vid}: transient ({res['_error']}) — next key + backing off up to {backoff:.0f}s")
            time.sleep(backoff if len(keys) == 1 else min(backoff, 8))   # with >1 key, mostly just rotate
            res = analyze_video(vid, keys[ki])
            tries += 1
        if not isinstance(res, dict) or res.get("_error"):
            emsg = res.get("_error", "") if isinstance(res, dict) else "bad response"
            # Per-VIDEO failure (this video isn't fetchable) -> skip it forever, keep going.
            if any(c in emsg for c in ("403", "404", "Forbidden", "Not Found", "PERMISSION_DENIED")):
                failed.add(vid); skip += 1; consecutive = 0
                if skip <= 3:
                    print(f"  {vid}: unfetchable ({emsg}) — skipping permanently.")
                continue
            # SYSTEMIC failure (quota/auth/network) -> back off; stop only if it persists.
            err += 1; consecutive += 1
            if err <= 3:
                print(f"  {vid}: systemic error ({emsg})")
            if consecutive >= 4:      # each already retried w/ backoff, so 4 in a row = quota spent
                print("  persistent systemic errors after backoff (daily quota/auth) — stopping."); break
            continue
        done.add(vid); used_today += mins; ok += 1; consecutive = 0
        if not res.get("relevant", True):
            continue
        url = f"https://www.youtube.com/watch?v={vid}"
        ns += merge(skills, "skills", "skill_name", res.get("skills"), url, "gemini-video")
        nt += merge(tools, "tools", "name", res.get("tools"), url, "gemini-video")
        nc += merge(conns, "connectors", "name", res.get("connectors"), url, "gemini-video")
        npr += merge(prompts, "prompts", "title", res.get("prompts"), url, "gemini-video")
        ncm += merge(cmds, "commands", "command", res.get("commands"), url, "gemini-video")
        nd += merge(designs, "designs", "name", res.get("designs"), url, "gemini-video")
        for v in (res.get("visual_notes") or [])[:3]:
            visual.append({"video_id": vid, "note": str(v)[:200], "at": NOW})
        r["gemini_video_analyzed"] = True            # mark covered even without a transcript
        save(PROCESSED / f"{vid}.json", r)

    if ns:
        save(DATA / "skills.json", skills)
    if nt:
        save(DATA / "tools.json", tools)
    if nc:
        save(DATA / "connectors.json", conns)
    if npr:
        save(DATA / "prompts.json", prompts)
    if ncm:
        save(DATA / "commands.json", cmds)
    if nd:
        save(DATA / "designs.json", designs)
    daily = st.get("daily", {}) or {}
    daily[today] = used_today
    save(STATE, {"updated_at": NOW, "video_ids": sorted(done), "failed_ids": sorted(failed),
                 "daily": daily, "visual_notes": visual[-500:]})
    print(f"gemini-video: watched {ok} videos -> +{ns} skills, +{nt} tools, +{nc} connectors, "
          f"+{npr} prompts, +{ncm} commands, +{nd} designs ({skip} unfetchable skipped, {err} systemic errors). "
          f"NO Claude-Pro tokens used.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
