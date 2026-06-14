"""
src/supadata_fetch.py — UNATTENDED, PC-free transcript recovery via Supadata's free tier.

The cloud (GitHub Actions datacenter IP) is permanently blocked by YouTube, and the owner's
home PC can't be left on for the residential backfill. Supadata fetches the caption on THEIR
infrastructure (and AI-transcribes audio when a video has no caption), so this works from the
cloud with no PC. Free tier: ~100 credits/month, no credit card. Graceful-skip if no key.

Stdlib only (urllib) — no pip, matches the other free cloud steps. Writes recovered transcripts
to data/_pending/ exactly like src/backfill_transcripts, so the free analysis lane picks them up.

Usage:
    SUPADATA_API_KEY=...  python -m src.supadata_fetch --limit 3
    python -m src.supadata_fetch --limit 3        # prints "skipped" and exits 0 if no key
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
PENDING = DATA / "_pending"
PROCESSED = DATA / "processed"
DEAD = DATA / "dead_videos.json"   # permanently-unavailable videos (deleted/private) — never retry
MAX_CHARS = 120000
ENDPOINT = "https://api.supadata.ai/v1/youtube/transcript"


def _load_dead() -> set:
    try:
        return set(json.load(open(DEAD, encoding="utf-8")).get("video_ids", []))
    except Exception:
        return set()


def _save_dead(ids: set) -> None:
    json.dump({"video_ids": sorted(ids),
               "note": "Videos that returned 404/not-found (deleted/private) — skipped so the "
                       "scarce Supadata free quota and residential fetches aren't wasted retrying them."},
              open(DEAD, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def _text_from_content(content) -> str:
    """Supadata returns content as a list of {text,offset,duration} segments, or (with text=true)
    a plain string. Handle both, plus a top-level 'text' field, and cap length."""
    if isinstance(content, str):
        return content[:MAX_CHARS]
    if isinstance(content, list):
        parts = []
        for s in content:
            if isinstance(s, dict):
                parts.append(s.get("text", "") or "")
            elif isinstance(s, str):
                parts.append(s)
        return " ".join(p for p in parts if p)[:MAX_CHARS]
    return ""


def fetch_transcript(video_id: str, key: str, timeout: int = 45) -> tuple[str, str, str]:
    """Return (text, lang, status). status: 'ok' | 'empty' | 'quota' | 'async' | 'error:<code>'."""
    url = ENDPOINT + "?" + urllib.parse.urlencode({
        "url": f"https://www.youtube.com/watch?v={video_id}",
        "lang": "en",
        "text": "true",
        "mode": "native",   # existing captions only = 1 credit each (88% of videos have them);
    })                       # stays inside the ~100/month free tier far longer than AI-gen.
    # Supadata's API is behind Cloudflare, which 1010-blocks urllib's default "Python-urllib"
    # User-Agent. A normal browser UA gets through (it's not an auth issue).
    req = urllib.request.Request(url, headers={
        "x-api-key": key,
        "Accept": "application/json",
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"),
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            if resp.status == 202:          # async AI job queued — skip; native mode shouldn't hit this
                return "", "", "async"
            body = json.loads(resp.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        if e.code in (402, 429):           # payment required / rate-limited = out of free credits
            return "", "", "quota"
        detail = ""
        try:
            detail = e.read().decode("utf-8", "replace")[:160].replace("\n", " ")
        except Exception:
            pass
        return "", "", f"error:{e.code} {detail}".strip()
    except Exception as e:
        return "", "", f"error:net {type(e).__name__}"
    # Long AI-fallback transcriptions can come back as an async job — skip; retried next run.
    if isinstance(body, dict) and body.get("jobId") and not (body.get("content") or body.get("text")):
        return "", "", "async"
    text = _text_from_content(body.get("content") if isinstance(body, dict) else None)
    if not text and isinstance(body, dict):
        text = (body.get("text") or "")[:MAX_CHARS]
    lang = (body.get("lang") if isinstance(body, dict) else "") or "en"
    return (text, lang, "ok") if text.strip() else ("", lang, "empty")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=3, help="max videos this run (free tier ~100/mo)")
    ap.add_argument("--sleep", type=float, default=1.5)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    key = os.environ.get("SUPADATA_API_KEY", "").strip()
    if not key:
        print("SUPADATA_API_KEY not set — skipping unattended Supadata fetch (graceful).")
        return 0

    PENDING.mkdir(parents=True, exist_ok=True)
    dead = _load_dead()
    todo = []
    for f in sorted(glob.glob(str(PROCESSED / "*.json"))):
        try:
            r = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        if r.get("transcript_source") in ("transcript", "whisper"):
            continue
        vid = r.get("video_id")
        if vid and vid not in dead and not (PENDING / f"{vid}.json").exists():
            todo.append(r)
    print(f"videos lacking a real transcript: {len(todo)} ({len(dead)} known-dead skipped); "
          f"attempting up to {args.limit} via Supadata")
    todo = todo[: max(args.limit, 0)]

    ok = empty = err = 0
    dead_added = 0
    now = datetime.now(timezone.utc).isoformat()
    for r in todo:
        vid = r["video_id"]
        time.sleep(args.sleep)
        text, lang, status = fetch_transcript(vid, key)
        if status == "quota":
            print("  Supadata free credits exhausted for this period — stopping (resets monthly).")
            break
        if status.startswith("error:404") or "not-found" in status:
            dead.add(vid); dead_added += 1   # deleted/private — never waste quota on it again
        if status != "ok" or not text:
            if status in ("empty", "async"):
                empty += 1
            else:
                err += 1
                if err <= 2:                       # surface the real cause for diagnosis
                    print(f"  {vid}: {status}")
            continue
        r["transcript"] = text
        r["transcript_lang"] = lang
        r["transcript_source"] = "transcript"
        r["caption_complete"] = True
        r["backfilled_at"] = now
        r["backfill_via"] = "supadata"
        ok += 1
        if not args.dry_run:
            with open(PENDING / f"{vid}.json", "w", encoding="utf-8") as fh:
                json.dump(r, fh, ensure_ascii=False, indent=2)
        print(f"  {vid}: {len(text)} chars ({lang}) via Supadata")
    if dead_added and not args.dry_run:
        _save_dead(dead)
    print(f"\nSupadata recovered {ok}; {empty} empty/async; {err} errors "
          f"({dead_added} newly marked dead). "
          f"{'re-queued to data/_pending for the free analysis lane.' if ok else ''}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
