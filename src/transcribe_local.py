"""
src/transcribe_local.py — Tier-2 ASR: transcribe caption-LESS videos with Whisper (local, free).

The hybrid's second tier. For each video that still has no real transcript it:
  1) tries the YouTube caption track once (fast/free);
  2) if captions are DEFINITIVELY absent (disabled / none), downloads the audio with yt-dlp
     and transcribes it with faster-whisper (CPU, int8 — no GPU needed);
  3) if the caption fetch only hit a transient rate-limit, it SKIPS the video so the caption
     backfill can retry later (no point burning CPU on a video that does have captions).
Then it re-queues the record into data/_pending/ for deep re-analysis. No API key, no cost.

Whisper transcribes ONLY this video's audio into text — it never pulls from the description,
comments, or other videos. Slow on a CPU-only machine, so use a small --limit per run.

Setup once:  powershell -ExecutionPolicy Bypass -File sync/install-transcription.ps1
Usage:       python -m src.transcribe_local --limit 15 --model base
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import shutil
import subprocess
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
PENDING = DATA / "_pending"
PROCESSED = DATA / "processed"
MAX_CHARS = 120000
_MODEL: list = []  # lazy single-load holder


def caption_status(vid: str, langs: list[str]) -> tuple[str, str, bool]:
    """(text, lang, definitely_absent). text='' if no caption. definitely_absent=True when the
    caption track is disabled/none (Whisper it); False on a transient error (let backfill retry)."""
    try:
        from src.backfill_transcripts import get_transcript
        txt, lang = get_transcript(vid, langs)
        if txt:
            return txt, lang, False
        return "", "", True  # no exception but empty -> treat as absent
    except Exception as e:  # noqa: BLE001
        name = type(e).__name__.lower()
        if any(k in name for k in ("disabled", "notranscript", "novalid", "unavailable", "notranslat")):
            return "", "", True
        return "", "", False  # transient (rate-limit/network) -> skip, retry later


def get_model(size: str):
    if not _MODEL:
        from faster_whisper import WhisperModel
        _MODEL.append(WhisperModel(size, device="cpu", compute_type="int8"))
    return _MODEL[0]


def whisper_text(audio_path: str, size: str) -> str:
    segments, _info = get_model(size).transcribe(str(audio_path), vad_filter=True)
    return " ".join(s.text.strip() for s in segments).strip()


def download_audio(vid: str, dest_dir: str) -> str | None:
    out = os.path.join(dest_dir, f"{vid}.%(ext)s")
    subprocess.run(
        ["yt-dlp", "-f", "bestaudio", "--no-playlist", "-o", out,
         f"https://www.youtube.com/watch?v={vid}"],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    for f in glob.glob(os.path.join(dest_dir, f"{vid}.*")):
        return f
    return None


def deps_ok() -> bool:
    miss = []
    if shutil.which("yt-dlp") is None:
        try:
            import yt_dlp  # noqa: F401
        except Exception:
            miss.append("yt-dlp")
    try:
        import faster_whisper  # noqa: F401
    except Exception:
        miss.append("faster-whisper")
    if miss:
        print("Missing dependencies:", ", ".join(miss))
        print("Install once:  powershell -ExecutionPolicy Bypass -File sync/install-transcription.ps1")
        print("        (or:  pip install faster-whisper yt-dlp )")
        return False
    return True


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=15, help="max videos this run (CPU-bound; keep small)")
    ap.add_argument("--model", default="base", help="tiny | base | small (bigger = better + slower)")
    ap.add_argument("--langs", default="en,he")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not deps_ok():
        return
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
    todo = todo[: args.limit] if args.limit > 0 else todo
    print(f"videos lacking a real transcript: attempting {len(todo)} (whisper model={args.model})")

    now = datetime.now(timezone.utc).isoformat()
    cap = whisp = skip = 0
    with tempfile.TemporaryDirectory() as tmp:
        for r in todo:
            vid = r["video_id"]
            time.sleep(0.5)
            txt, lang, absent = caption_status(vid, langs)
            if txt:
                r.update(transcript=txt[:MAX_CHARS], transcript_lang=lang,
                         transcript_source="transcript", backfilled_at=now)
                cap += 1
            elif not absent:
                skip += 1
                continue  # transient -> let the caption backfill retry
            else:
                try:
                    audio = download_audio(vid, tmp)
                    if not audio:
                        skip += 1
                        continue
                    wt = whisper_text(audio, args.model)
                    try:
                        os.remove(audio)
                    except OSError:
                        pass
                except Exception as e:  # noqa: BLE001
                    print(f"  {vid}: whisper failed {type(e).__name__}: {str(e)[:80]}")
                    skip += 1
                    continue
                if not wt:
                    skip += 1
                    continue
                r.update(transcript=wt[:MAX_CHARS], transcript_lang="",
                         transcript_source="whisper", transcribed_at=now,
                         transcribe_model=f"faster-whisper-{args.model}")
                whisp += 1
                print(f"  {vid}: WHISPER {len(wt)} chars")
            if not args.dry_run:
                with open(PENDING / f"{vid}.json", "w", encoding="utf-8") as fh:
                    json.dump(r, fh, ensure_ascii=False, indent=2)
    print(f"\ncaptions {cap}, whisper {whisp}, skipped/transient {skip}; "
          f"re-queued {cap + whisp} for deep re-analysis.")


if __name__ == "__main__":
    main()
