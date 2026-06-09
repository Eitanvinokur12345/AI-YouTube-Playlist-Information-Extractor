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


def _end_seconds(fetched) -> float:
    """The end timestamp of the last caption snippet = how much of the video the caption covers."""
    end = 0.0
    for s in fetched:
        st = getattr(s, "start", None)
        du = getattr(s, "duration", None)
        if st is None and isinstance(s, dict):
            st, du = s.get("start"), s.get("duration")
        try:
            e = float(st or 0) + float(du or 0)
            end = max(end, e)
        except (TypeError, ValueError):
            pass
    return end


def _iso_dur_seconds(iso: str) -> int:
    """Parse an ISO-8601 duration like 'PT12M3S' to seconds (0 if unknown)."""
    import re
    if not iso:
        return 0
    m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso)
    if not m:
        return 0
    h, mi, s = (int(x) if x else 0 for x in m.groups())
    return h * 3600 + mi * 60 + s


def get_transcript(video_id: str, languages: list[str]) -> tuple[str, str, bool, float]:
    """(text, lang, is_complete_caption, end_seconds). Prefers the AUTO-generated caption
    (which always spans the whole video); a manual track may be partial, so the caller checks
    coverage. Works with youtube-transcript-api 1.x and 0.6.x. ('','',False,0) on miss."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except Exception:
        return "", "", False, 0.0

    def _try(tl):
        # auto-generated FIRST (full-video); fall back to manual (may be partial -> flagged)
        for lang in languages:
            for finder in ("find_generated_transcript", "find_manually_created_transcript"):
                try:
                    t = getattr(tl, finder)([lang])
                    fetched = t.fetch()
                    raw = _text(fetched)
                    if raw.strip():
                        is_gen = bool(getattr(t, "is_generated", finder.startswith("find_generated")))
                        return raw[:MAX_CHARS], lang, is_gen, _end_seconds(fetched)
                except Exception:
                    pass
        return None

    if not hasattr(YouTubeTranscriptApi, "list_transcripts"):  # 1.x instance API
        api = YouTubeTranscriptApi()
        try:
            r = _try(api.list(video_id))
            if r:
                return r
        except Exception:
            pass
        try:  # direct fetch (auto-translated tracks the finders miss) — treat as full-video
            fetched = api.fetch(video_id, languages=languages)
            raw = _text(fetched)
            if raw.strip():
                return raw[:MAX_CHARS], (languages[0] if languages else ""), True, _end_seconds(fetched)
        except Exception:
            return "", "", False, 0.0
        return "", "", False, 0.0

    try:  # 0.6.x classmethod API
        r = _try(YouTubeTranscriptApi.list_transcripts(video_id))
        if r:
            return r
    except Exception:
        return "", "", False, 0.0
    return "", "", False, 0.0


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

    ok = fail = incomplete = 0
    now = datetime.now(timezone.utc).isoformat()
    for r in todo:
        vid = r["video_id"]
        time.sleep(args.sleep)
        txt, lang, is_complete_caption, end_sec = get_transcript(vid, langs)
        if not txt:
            fail += 1
            continue
        # The owner's rule: accept a caption ONLY if it is a COMPLETE transcript of the whole
        # video; otherwise leave it for Whisper. Auto-generated captions span the full video;
        # a manual track is accepted only if it covers >=90% of the known duration.
        dur = _iso_dur_seconds(r.get("duration", ""))
        if is_complete_caption:
            complete = True
        elif dur and end_sec:
            complete = (end_sec / dur) >= 0.90
        else:
            complete = False  # manual caption, coverage unverifiable -> Whisper it
        if not complete:
            incomplete += 1
            continue  # leave transcript_source as-is so transcribe (mode=gaps) Whispers it
        r["transcript"] = txt
        r["transcript_lang"] = lang
        r["transcript_source"] = "transcript"
        r["caption_complete"] = True
        r["backfilled_at"] = now
        ok += 1
        if not args.dry_run:
            with open(PENDING / f"{vid}.json", "w", encoding="utf-8") as fh:
                json.dump(r, fh, ensure_ascii=False, indent=2)
        if ok <= 12 or ok % 25 == 0:
            print(f"  {vid}: complete caption {len(txt)} chars ({lang})")
    print(f"\nbackfilled {ok} COMPLETE captions; {incomplete} incomplete -> Whisper; {fail} no caption -> Whisper.")
    if not args.dry_run and ok:
        print(f"re-queued {ok} into data/_pending/ for deep re-analysis by the cloud.")


if __name__ == "__main__":
    main()
