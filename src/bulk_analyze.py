"""
src/bulk_analyze.py — FREE bulk analyzer (the two-tier "bulk lane").

Why: deep-reading 1,100 transcripts with the Claude Pro subscription token blows the weekly
limit. This drains the backlog (and any future big burst) on a FREE model instead — Gemini Flash
free tier — touching ZERO Claude tokens. Claude stays the premium lane for incremental new
videos + the improve/review curation.

How: for each video in data/_pending with a REAL transcript, ask Gemini to extract structured
JSON (skills/tools/prompts/connectors) following the same rules as CLAUDE.md (anti-boilerplate,
skills-vs-tools). Then deterministic Python MERGES it into the data files (dedup by slug/name,
union endorsements) and moves the file to data/processed. Stdlib only, graceful on errors.

Key: read from the env var named by config.bulk_analyze.secret_name (default EXTERNAL_REVIEW_API_KEY,
the Gemini key the review feature already uses). Never printed.

    python -m src.bulk_analyze --limit 200
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PENDING = DATA / "_pending"
PROCESSED = DATA / "processed"
CONFIG = ROOT / "config.json"
NOW = datetime.now(timezone.utc).isoformat()
CATEGORIES = ["design", "code", "automation", "agents", "image creation", "video creation",
              "writing", "marketing", "social", "music", "integration", "research",
              "productivity", "other"]
PROMPT_CATS = ["master", "system_guardrail", "creation", "coding", "agents", "research", "marketing", "other"]


def load(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def save(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")


def slugify(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-") or "item"


def norm(s: str) -> str:
    # alphanumeric-only dedup key so naming variants collapse: "Deep Seek" / "Deepseek" /
    # "deep-seek" -> "deepseek"; "GPT 5.5" / "GPT-5.5" -> "gpt55". Prevents cross-engine dupes.
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


# ── Gemini call (stdlib, same shape as src/external_review.py) ──────────────────
def call_gemini(api_key: str, model: str, prompt: str, timeout: int) -> dict:
    url = (f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
           f"?key={api_key}")
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.2, "responseMimeType": "application/json"},
    }
    req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"),
                                headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    text = payload["candidates"][0]["content"]["parts"][0]["text"]
    return json.loads(text)


def call_openai_compatible(base_url: str, api_key: str, model: str, prompt: str, timeout: int) -> dict:
    """OpenAI-compatible chat/completions — works for GitHub Models (Claude Sonnet 4.6, free),
    Cerebras, OpenRouter, DeepSeek, etc. Lets us run CLAUDE-QUALITY extraction for free."""
    url = base_url.rstrip("/") + "/chat/completions"
    body = {"model": model, "temperature": 0.2,
            "messages": [{"role": "user", "content": prompt}],
            "response_format": {"type": "json_object"}}
    req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"),
                                headers={"Content-Type": "application/json",
                                         "Authorization": f"Bearer {api_key}"}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    return json.loads(payload["choices"][0]["message"]["content"])


def extract(provider: str, base_url: str, api_key: str, model: str, prompt: str, timeout: int) -> dict:
    if provider == "openai_compatible":
        return call_openai_compatible(base_url, api_key, model, prompt, timeout)
    return call_gemini(api_key, model, prompt, timeout)


def build_prompt(rec: dict, transcript_chars: int) -> str:
    content = (rec.get("transcript") or rec.get("description") or rec.get("title") or "")[:transcript_chars]
    comments = rec.get("top_comments") or []
    ctext = "\n".join(f"- {c.get('text','')[:300]}" for c in comments[:15])
    return (
        "You extract structured data from an AI YouTube video for a skills/tools dashboard. "
        "Return STRICT JSON ONLY (no prose) with this shape:\n"
        '{"relevant":true,'
        '"skills":[{"skill_name":"","slug":"","category":"","description":"","use_case":"",'
        '"output":"","quality_score":1,"target_tool":"claude","tips":[],"slash_commands":[]}],'
        '"tools":[{"name":"","slug":"","category":"","company":"","country":"","open_source":false,'
        '"description":"","quality_score":1,"model_version":"","release_status":"released",'
        '"is_open_source":false,"is_mcp":false}],'
        '"prompts":[{"title":"","category":"","purpose":"","prompt_text":""}],'
        '"connectors":[{"name":"","source":"","what_it_does":"","works_in":"both","free":true,"url":""}]}\n\n'
        "RULES:\n"
        f"- category MUST be one of: {', '.join(CATEGORIES)}.\n"
        f"- prompt category MUST be one of: {', '.join(PROMPT_CATS)}.\n"
        "- SKILLS = reusable techniques/workflows (a way of DOING something). TOOLS = products/"
        "models/apps (a thing that EXISTS). Keep them separate; a product is a TOOL, not a skill.\n"
        "- ANTI-BOILERPLATE: never output a skill that is just a bare vendor name (e.g. 'Claude', "
        "'ChatGPT') or a template like 'Using X for productivity'. A skill must be a SPECIFIC "
        "method actually shown. If the video only mentions a product, put it in tools and emit no skill.\n"
        "- Extract EVERY distinct tool named (roundup videos name many). Use exact names with version.\n"
        "- quality_score 1-10 from the evidence. release_status 'upcoming' if announced-but-unreleased.\n"
        "- If the video is not about AI tools/skills, return {\"relevant\":false}.\n"
        "- Empty arrays are fine. Do NOT invent facts; use only what the content supports.\n\n"
        f"TITLE: {rec.get('title','')}\nCHANNEL: {rec.get('channel_name','')}\n"
        f"TRANSCRIPT (verbatim, may be truncated):\n{content}\n\n"
        + (f"TOP COMMENTS (may name the real tool/link):\n{ctext}\n" if ctext else "")
    )


# ── merges (deterministic, dedup) ──────────────────────────────────────────────
def merge_skills(store: dict, items: list, vid: str) -> int:
    arr = store.setdefault("skills", [])
    by = {norm(s.get("skill_name")): s for s in arr}
    by_slug = {s.get("slug") for s in arr}
    added = 0
    for it in items or []:
        name = it.get("skill_name", "").strip()
        if not name or norm(name) in {"claude", "chatgpt", "gemini", "make", "anthropic", "openai", "mcp"}:
            continue  # anti-boilerplate guard on our side too
        key = norm(name)
        if key in by:
            ev = by[key].setdefault("endorsement_video_ids", [])
            if vid not in ev:
                ev.append(vid)
            continue
        slug = slugify(it.get("slug") or name)
        i = 2
        while slug in by_slug:
            slug = f"{slugify(name)}-{i}"; i += 1
        by_slug.add(slug)
        rec = {**it, "slug": slug, "endorsement_video_ids": [vid], "source_type": "youtube",
               "source_video_id": vid, "source_url": f"https://www.youtube.com/watch?v={vid}",
               "discovered_via": "bulk_analyze (gemini)", "added_at": NOW}
        if rec.get("category") not in CATEGORIES:
            rec["category"] = "other"
        arr.append(rec); by[key] = rec; added += 1
    return added


def merge_tools(store: dict, items: list, vid: str) -> int:
    arr = store.setdefault("tools", [])
    by = {norm(t.get("name")): t for t in arr}
    added = 0
    for it in items or []:
        name = it.get("name", "").strip()
        if not name:
            continue
        key = norm(name)
        if key in by:
            ev = by[key].setdefault("endorsement_video_ids", [])
            if vid not in ev:
                ev.append(vid)
            by[key]["mentions"] = len(ev)
            continue
        rec = {**it, "slug": slugify(it.get("slug") or name), "endorsement_video_ids": [vid],
               "mentions": 1, "source_video_id": vid, "discovered_via": "bulk_analyze (gemini)",
               "source_url": it.get("source_url") or f"https://www.youtube.com/watch?v={vid}", "added_at": NOW}
        if rec.get("category") not in CATEGORIES:
            rec["category"] = "other"
        arr.append(rec); by[key] = rec; added += 1
    return added


def merge_prompts(store: dict, items: list, vid: str) -> int:
    arr = store.setdefault("prompts", [])
    have = {norm(p.get("title")) for p in arr} | {norm(p.get("prompt_text"))[:80] for p in arr}
    added = 0
    for it in items or []:
        title = it.get("title", "").strip()
        ptext = it.get("prompt_text", "").strip()
        if not title or not ptext or norm(title) in have or norm(ptext)[:80] in have:
            continue
        cat = it.get("category") if it.get("category") in PROMPT_CATS else "other"
        arr.append({"title": title, "category": cat, "purpose": it.get("purpose", ""),
                    "prompt_text": ptext, "source_video_id": vid,
                    "source_url": f"https://www.youtube.com/watch?v={vid}", "added_at": NOW})
        have.add(norm(title)); added += 1
    return added


def merge_connectors(store: dict, items: list, vid: str) -> int:
    arr = store.setdefault("connectors", [])
    by = {norm(c.get("name")) for c in arr}
    added = 0
    for it in items or []:
        name = it.get("name", "").strip()
        if not name or norm(name) in by:
            continue
        arr.append({"name": name, "source": it.get("source", ""), "what_it_does": it.get("what_it_does", ""),
                    "works_in": it.get("works_in", "both"), "free": it.get("free", True),
                    "url": it.get("url", ""), "source_video_id": vid, "added_at": NOW})
        by.add(norm(name)); added += 1
    return added


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=200, help="max videos this run (0 = all pending)")
    ap.add_argument("--sleep", type=float, default=4.5, help="seconds between calls (free-tier RPM)")
    args = ap.parse_args()

    cfg = load(CONFIG, {})
    bc = cfg.get("bulk_analyze", {}) or {}
    if not bc.get("enabled", True):
        print("bulk_analyze disabled in config."); return 0
    provider = bc.get("provider", "gemini")            # "gemini" | "openai_compatible"
    base_url = bc.get("base_url", "")                   # for openai_compatible (e.g. GitHub Models)
    secret = bc.get("secret_name", "EXTERNAL_REVIEW_API_KEY")
    model = bc.get("model", "gemini-2.5-flash")
    tchars = int(cfg.get("extraction", {}).get("transcript_chars", 120000))
    timeout = int(cfg.get("news", {}).get("request_timeout_seconds", 30))
    require_transcript = bool(bc.get("require_transcript", True))

    # ENGINE POOL: combine every free engine you have a key for. Their daily quotas ADD UP
    # (more throughput) and you can list the strongest models (better quality). Engines whose
    # secret is absent are auto-skipped, so the pool grows as you add keys.
    engines = []
    for e in (bc.get("engines") or []):
        k = os.environ.get(e.get("secret_name", ""), "").strip()
        if k:
            engines.append({"name": e.get("name") or e.get("model", "engine"),
                            "provider": e.get("provider", "gemini"), "base_url": e.get("base_url", ""),
                            "model": e.get("model", ""), "key": k})
    if not engines:  # fall back to the single provider block
        k = os.environ.get(secret, "").strip()
        if k:
            engines.append({"name": model, "provider": provider, "base_url": base_url, "model": model, "key": k})
    if not engines:
        print("No engine keys present (set EXTERNAL_REVIEW_API_KEY and/or others). Skipped."); return 0
    print("engine pool:", ", ".join(e["name"] for e in engines))
    per_engine = {e["name"]: 0 for e in engines}

    # pick pending videos (prefer ones with a REAL transcript — that's the whole point)
    todo = []
    for f in sorted(PENDING.glob("*.json")):
        rec = load(f, None)
        if not rec:
            continue
        if require_transcript and rec.get("transcript_source") not in ("transcript", "whisper"):
            continue
        todo.append((f, rec))
    if args.limit > 0:
        todo = todo[: args.limit]
    print(f"bulk-analyzing {len(todo)} pending videos with {model} (free)...")

    skills = load(DATA / "skills.json", {"skills": []})
    tools = load(DATA / "tools.json", {"tools": []})
    prompts = load(DATA / "prompts.json", {"prompts": []})
    connectors = load(DATA / "connectors.json", {"connectors": []})
    seen = set(skills.get("videos_seen", []))

    done = skip = ns = nt = npr = nc = 0
    ERR_LIMIT = 3                                # drop an engine after this many errors in a row
    errs = {e["name"]: 0 for e in engines}
    disabled: set = set()
    idx = 0
    for f, rec in todo:
        vid = rec.get("video_id", "")
        active = [e for e in engines if e["name"] not in disabled]
        if not active:
            print("  all engines disabled (rate-limited/forbidden) — stopping; the rest stay pending.")
            break
        eng = active[idx % len(active)]          # round-robin among ENGINES THAT STILL WORK
        idx += 1
        time.sleep(args.sleep)
        try:
            result = extract(eng["provider"], eng["base_url"], eng["key"], eng["model"],
                             build_prompt(rec, tchars), timeout)
        except Exception as e:  # noqa: BLE001 — never crash the batch
            errs[eng["name"]] += 1
            note = ""
            if errs[eng["name"]] >= ERR_LIMIT:
                disabled.add(eng["name"])
                note = f"  -> dropping {eng['name']} for this run"
            print(f"  {vid}: {eng['name']} error {type(e).__name__}: {str(e)[:70]} (left pending){note}")
            skip += 1
            continue
        errs[eng["name"]] = 0                     # a success clears the streak
        per_engine[eng["name"]] += 1
        if result.get("relevant") is not False:
            ns += merge_skills(skills, result.get("skills"), vid)
            nt += merge_tools(tools, result.get("tools"), vid)
            npr += merge_prompts(prompts, result.get("prompts"), vid)
            nc += merge_connectors(connectors, result.get("connectors"), vid)
        seen.add(vid)
        PROCESSED.mkdir(parents=True, exist_ok=True)
        (PROCESSED / f"{vid}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")
        f.unlink(missing_ok=True)
        done += 1
        if done % 25 == 0:
            print(f"  ...{done} done (+{ns} skills +{nt} tools)")

    skills["videos_seen"] = sorted(seen)
    save(DATA / "skills.json", skills)
    save(DATA / "tools.json", tools)
    save(DATA / "prompts.json", prompts)
    save(DATA / "connectors.json", connectors)
    by_eng = ", ".join(f"{n}:{c}" for n, c in per_engine.items())
    print(f"\nbulk_analyze done: {done} videos [{by_eng}] | +{ns} skills, +{nt} tools, "
          f"+{npr} prompts, +{nc} connectors | {skip} left pending. NO Claude-Pro tokens used.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
