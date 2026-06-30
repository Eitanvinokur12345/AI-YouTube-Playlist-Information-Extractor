"""
src/visual_extract.py — THE VISUAL protocol: a SEPARATE pass that watches each video's SCREEN.

The owner wanted a dedicated protocol for the VISUAL information in every video (not the transcript),
to improve finding designs, tool UIs, on-screen URLs and reusable FORMATS. Gemini accepts a YouTube
URL as video input and Google fetches it server-side, so the cloud can WATCH the pixels. This pass is
vision-focused (ignores narration unless it labels something on screen) and writes:
  - data/designs.json     — designs SHOWN (name, the exact URL on screen, concrete look, style tags)
  - data/formats.json     — reusable UI/layout FORMATS worth copying (hero/dashboard/pricing patterns)
  - data/screen_urls.json — every URL visible on screen (feeds collect_designs + resolve_links)

Own state + daily budget in data/visual_state.json so it stays inside the FREE Gemini video quota, and
round-robins ALL Gemini keys (each key carries its own quota → N keys = N× free throughput, $0). Full
backfill, newest/least-covered first. More vision engines can be slotted into KEYS later for speed.

Run:  python -m src.visual_extract --limit 20
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from src.bulk_analyze import load, save, NOW, CATEGORIES
from src.mine_feeds import merge

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
PROCESSED = DATA / "processed"
STATE = DATA / "visual_state.json"
SCREEN = DATA / "screen_urls.json"
MODEL = "gemini-2.5-flash"
DAILY_MINUTES = 300          # leave headroom under the ~8h/day free quota for the main analysis lane
STYLE_ALLOWED = ["bold", "colorful", "playful", "brutalist", "minimal", "retro", "glassy", "dark", "gradient"]

PROMPT = (
    "WATCH this video for VISUAL information (the pixels on screen). Capture things SHOWN on screen that "
    "the narration may NOT say — tool names in the browser/UI, terminal commands, websites visited, "
    "dashboards and app UIs. Extract, as STRICT JSON ONLY:\n"
    '{"designs":[{"name":"","source_url":"exact URL shown for this site/app or empty","look":"concrete: '
    'layout, colors, typography, components, spacing, motion, vibe","style_tags":[],"section":"hero|landing|'
    'dashboard|pricing|app|portfolio|other"}],'
    '"formats":[{"name":"","kind":"layout|section|component|flow","description":"the reusable UI/layout '
    'pattern seen","rebuild_hint":"how to recreate the look"}],'
    '"tools":[{"name":"","slug":"","category":"","description":"what it does (from what is shown)","quality_score":1,"homepage":"","github":""}],'
    '"skills":[{"skill_name":"","slug":"","category":"","description":"","quality_score":1,"target_tool":"claude"}],'
    '"connectors":[{"name":"","what_it_does":"","works_in":"both","free":true,"url":""}],'
    '"commands":[{"command":"","description":""}],'
    '"screen_urls":[""],'
    '"tool_ui":[{"name":"","url":"the tool site/app URL shown on screen or empty"}]}\n'
    "- designs = any website/app/dashboard/UI SHOWN worth replicating; describe what you SEE.\n"
    "- tools/skills/connectors/commands = capture ones VISIBLE on screen (browser, terminal, slide) even "
    "if not spoken. A product that EXISTS is a TOOL; a technique you DO is a SKILL; exact CLI/slash text is "
    "a COMMAND. Empty arrays are fine.\n"
    f"- category MUST be one of: {', '.join(CATEGORIES)}.\n"
    f"- style_tags only from this list: {', '.join(STYLE_ALLOWED)}.\n"
    "- URLs (source_url / screen_urls / tool_ui.url / homepage / github): ONLY ones ACTUALLY VISIBLE on "
    "screen. Never invent a URL. Empty arrays/strings are fine.\n"
    "If the video shows nothing visual worth capturing, return all empty arrays."
)


def _keys() -> list[str]:
    ks = []
    for n in ["EXTERNAL_REVIEW_API_KEY", "GEMINI_API_KEY"] + [f"GEMINI_API_KEY_{i}" for i in range(2, 9)]:
        v = (os.environ.get(n) or "").strip()
        if v and v not in ks:
            ks.append(v)
    return ks


def _mins(r: dict) -> int:
    import re
    m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", r.get("duration", "") or "")
    if not m:
        return 12
    h, mi, s = (int(x) if x else 0 for x in m.groups())
    return max(1, round(h * 60 + mi + s / 60))


def watch(video_id: str, key: str, timeout: int = 180) -> dict:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={key}"
    body = {"contents": [{"parts": [
        {"fileData": {"fileUri": f"https://www.youtube.com/watch?v={video_id}"}}, {"text": PROMPT}]}],
        "generationConfig": {"temperature": 0.2, "responseMimeType": "application/json"}}
    req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"),
                                 headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = json.loads(resp.read().decode("utf-8", "replace"))
        return json.loads(payload["candidates"][0]["content"]["parts"][0]["text"])
    except Exception as e:  # noqa: BLE001
        return {"_error": f"{type(e).__name__}: {str(e)[:140]}"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--sleep", type=float, default=2.0)
    args = ap.parse_args()
    keys = _keys()
    if not keys:
        print("visual_extract: no Gemini key — skipped (graceful)."); return 0
    daily_budget = DAILY_MINUTES * len(keys)
    ki = 0

    st = load(STATE, {}) or {}
    done = set(st.get("video_ids", []))
    failed = set(st.get("failed_ids", []))
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    used = (st.get("daily", {}) or {}).get(today, 0)

    todo = []
    for f in sorted(glob.glob(str(PROCESSED / "*.json"))):
        r = load(Path(f), None)
        if isinstance(r, dict) and r.get("video_id") and r["video_id"] not in done and r["video_id"] not in failed:
            todo.append(r)
    print(f"visual_extract: {len(todo)} videos to watch ({len(failed)} unfetchable skipped); "
          f"{used}m of ~{daily_budget}m used today across {len(keys)} key(s).")

    designs = load(DATA / "designs.json", {"designs": []})
    formats = load(DATA / "formats.json", {"formats": []})
    tools = load(DATA / "tools.json", {"tools": []})
    skills = load(DATA / "skills.json", {"skills": []})
    conns = load(DATA / "connectors.json", {"connectors": []})
    cmds = load(DATA / "commands.json", {"commands": []})
    screen = load(SCREEN, {"urls": []})
    have_url = {(u.get("url") if isinstance(u, dict) else u) for u in screen.get("urls", [])}
    nd = nf = nu = nt = ns = nc = ncm = ok = skip = err = 0
    consecutive = 0

    for r in todo[: max(args.limit, 0)]:
        mins = _mins(r)
        if used + mins > daily_budget:
            print("  daily free quota reached — stopping; resumes tomorrow."); break
        vid = r["video_id"]
        time.sleep(args.sleep)
        ki = (ki + 1) % len(keys)
        res = watch(vid, keys[ki])
        backoff, tries = max(args.sleep, 4.0), 0
        while (isinstance(res, dict) and res.get("_error") and tries < 4
               and any(c in res["_error"] for c in ("429", "503", "Too Many", "Unavailable", "timed out", "timeout", "500"))):
            ki = (ki + 1) % len(keys)
            backoff = min(backoff * 2 + 6, 90)
            time.sleep(backoff if len(keys) == 1 else min(backoff, 8))
            res = watch(vid, keys[ki])
            tries += 1
        if not isinstance(res, dict) or res.get("_error"):
            emsg = res.get("_error", "") if isinstance(res, dict) else "bad response"
            if any(c in emsg for c in ("403", "404", "Forbidden", "Not Found", "PERMISSION_DENIED")):
                failed.add(vid); skip += 1; consecutive = 0; continue
            err += 1; consecutive += 1
            if consecutive >= 4:
                print("  persistent systemic errors — stopping (quota/auth)."); break
            continue
        done.add(vid); used += mins; ok += 1; consecutive = 0
        url = f"https://www.youtube.com/watch?v={vid}"
        # designs: keep only allowed style tags
        for ds in (res.get("designs") or []):
            ds["style_tags"] = [s for s in (ds.get("style_tags") or []) if s in STYLE_ALLOWED]
        nd += merge(designs, "designs", "name", res.get("designs"), url, "visual")
        nf += merge(formats, "formats", "name", res.get("formats"), url, "visual")
        # things SHOWN on screen (not necessarily spoken) → route to their own tabs too
        nt += merge(tools, "tools", "name", res.get("tools"), url, "visual-seen")
        ns += merge(skills, "skills", "skill_name", res.get("skills"), url, "visual-seen")
        nc += merge(conns, "connectors", "name", res.get("connectors"), url, "visual-seen")
        ncm += merge(cmds, "commands", "command", res.get("commands"), url, "visual-seen")
        # screen URLs queue (+ tool UI urls) — feeds collect_designs + resolve_links
        urls = list(res.get("screen_urls") or [])
        urls += [t.get("url") for t in (res.get("tool_ui") or []) if isinstance(t, dict) and t.get("url")]
        for u in urls:
            u = (u or "").strip()
            if u.startswith(("http://", "https://")) and u not in have_url:
                screen["urls"].append({"url": u, "from_video": vid, "at": NOW})
                have_url.add(u); nu += 1
        r["visual_extracted"] = True
        save(PROCESSED / f"{vid}.json", r)

    if nd:
        save(DATA / "designs.json", designs)
    if nf:
        save(DATA / "formats.json", formats)
    if nt:
        save(DATA / "tools.json", tools)
    if ns:
        save(DATA / "skills.json", skills)
    if nc:
        save(DATA / "connectors.json", conns)
    if ncm:
        save(DATA / "commands.json", cmds)
    if nu:
        screen["urls"] = screen["urls"][-4000:]
        save(SCREEN, screen)
    daily = st.get("daily", {}) or {}
    daily[today] = used
    save(STATE, {"updated_at": NOW, "video_ids": sorted(done), "failed_ids": sorted(failed), "daily": daily})
    print(f"visual_extract: watched {ok} videos -> +{nd} designs, +{nf} formats, +{nt} tools, +{ns} skills, "
          f"+{nc} connectors, +{ncm} commands, +{nu} screen-URLs ({skip} unfetchable, {err} errors). NO Claude tokens.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
