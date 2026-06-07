"""
src/backfill_transcripts.py — recover REAL transcripts from a RESIDENTIAL IP.

THE big fix. YouTube blocks youtube-transcript-api from datacenter/cloud IPs, so the cloud
(GitHub Actions) got a real transcript for only ~0.3% of videos — the other 99.7% fell back
to the description/title, which is why the library was "much smaller than what's in the videos"
(the analyzer never actually read them).

This runs from your HOME machine (residential IP), where transcripts DO fetch. For every
already-processed video that lacks a real transcript, it pulls the transcript now, updates the
record, and re-queues it into data/_pending/ so the cloud analyze stage re-extracts it deeply
under the anti-boilerplate gate.

No YOUTUBE_API_KEY needed (transcripts are public). Dependency-light: youtube-transcript-api + stdlib.

Usage:
    python -m src.backfill_transcripts --limit 120        # one batch
    python -m src.backfill_transcripts --limit 0          # everything (slow)
    python -m src.backfill_transcripts --dry-run
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
PENDING = DATA / "_pending"
PROCESSED = DATA / "processed"
MAX_CHARS = 120000


def _text(fetched) -> str:
    parts = []
    for s in fetched:
        if hasattr(s, "text"):
            parts.append(s.text or "")
        elif isinstance(s, dict):
            parts.append(s.get("text", "") or "")
    return " ".join(p for p in parts if p)


def get_transcript(video_id: str, languages: list[str]) -> tuple[str, str]:
    """Return (text, lang) or ('','') — works with youtube-transcript-api 1.x and 0.6.x."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except Exception:
        return "", ""
    # 1.x instance API
    if not hasattr(YouTubeTranscriptApi, "list_transcripts"):
        api = YouTubeTranscriptApi()
        try:
            tl = api.list(video_id)
            for lang in languages:
                for finder in ("find_manually_created_transcript", "find_generated_transcript"):
                    try:
                        t = getattr(tl, finder)([lang])
                        raw = _text(t.fetch())
                        if raw.strip():
                            return raw[:MAX_CHARS], lang
                    except Exception:
                        pass
        except Exception:
            pass
        try:
            raw = _text(api.fetch(video_id, languages=languages))
            if raw.strip():
                return raw[:MAX_CHARS], (languages[0] if languages else "")
        except Exception:
            return "", ""
        return "", ""
    # 0.6.x classmethod API
    try:
        tl = YouTubeTranscriptApi.list_transcripts(video_id)
        for lang in languages:
            for finder in ("find_manually_created_transcript", "find_generated_transcript"):
                try:
                    t = getattr(tl, finder)([lang])
                    raw = _text(t.fetch())
                    if raw.strip():
                        return raw[:MAX_CHARS], lang
                except Exception:
                    pass
    except Exception:
        return "", ""
    return "", ""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=120, help="max videos this run (0 = all)")
    ap.add_argument("--langs", default="en,he")
    ap.add_argument("--sleep", type=float, default=1.0,
                    help="seconds between videos; raise if YouTube rate-limits (fails spike after a burst)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    langs = [x.strip() for x in args.langs.split(",") if x.strip()]
    PENDING.mkdir(parents=True, exist_ok=True)

    todo = []
    for f in sorted(glob.glob(str(PROCESSED / "*.json"))):
        try:
            r = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        if r.get("transcript_source") == "transcript":
            continue
        vid = r.get("video_id")
        if not vid or (PENDING / f"{vid}.json").exists():
            continue
        todo.append(r)
    print(f"videos lacking a real transcript: {len(todo)}")
    if args.limit and args.limit > 0:
        todo = todo[: args.limit]
    print(f"attempting {len(todo)} this run...")

    ok = fail = 0
    now = datetime.now(timezone.utc).isoformat()
    for r in todo:
        vid = r["video_id"]
        time.sleep(args.sleep)
        txt, lang = get_transcript(vid, langs)
        if not txt:
            fail += 1
            continue
        r["transcript"] = txt
        r["transcript_lang"] = lang
        r["transcript_source"] = "transcript"
        r["backfilled_at"] = now
        ok += 1
        if not args.dry_run:
            with open(PENDING / f"{vid}.json", "w", encoding="utf-8") as fh:
                json.dump(r, fh, ensure_ascii=False, indent=2)
        if ok <= 12 or ok % 25 == 0:
            print(f"  {vid}: transcript {len(txt)} chars ({lang})")
    print(f"\nbackfilled {ok} real transcripts; {fail} still unavailable.")
    if not args.dry_run and ok:
        print(f"re-queued {ok} into data/_pending/ for deep re-analysis by the cloud.")


if __name__ == "__main__":
    main()
