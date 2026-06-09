"""
src/transcribe_local.py — local Whisper ASR (free, CPU-only, no GPU).

Whisper is the source of truth for the RAW spoken content of every video, because YouTube's
caption track is not guaranteed to be complete or accurate. It transcribes ONLY this video's
own audio into text — never the description, comments, or other videos.

Modes:
  --mode all   (default) → Whisper EVERY video not yet Whisper-transcribed. Priority: videos
                with no transcript at all first, then upgrade caption-only videos to Whisper.
  --mode gaps  → only videos that have no caption track (Whisper fills the gap; caption videos
                are left as-is).

Light by design (you asked for minimal load): the small `tiny` model + int8 + capped CPU
threads. Bump --model to base/small later if you want more accuracy. Slow on a CPU-only
machine, so use a small --limit per run. No API key, no cost.

Setup once:  powershell -ExecutionPolicy Bypass -File sync/install-transcription.ps1
Usage:       python -m src.transcribe_local --limit 15           # gentle nightly batch
             python -m src.transcribe_local --mode gaps          # only caption-less videos
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
    """(text, lang, definitely_absent) — used by --mode gaps to decide if a caption exists."""
    try:
        from src.backfill_transcripts import get_transcript
        txt, lang, _complete, _end = get_transcript(vid, langs)
        if txt:
            return txt, lang, False
        return "", "", True
    except Exception as e:  # noqa: BLE001
        name = type(e).__name__.lower()
        if any(k in name for k in ("disabled", "notranscript", "novalid", "unavailable", "notranslat")):
            return "", "", True
        return "", "", False  # transient -> skip, retry later


def get_model(size: str, cpu_threads: int):
    if not _MODEL:
        from faster_whisper import WhisperModel
        # int8 + capped threads = lightest footprint (you asked for minimal load).
        _MODEL.append(WhisperModel(size, device="cpu", compute_type="int8", cpu_threads=cpu_threads))
    return _MODEL[0]


def whisper_text(audio_path: str, size: str, cpu_threads: int) -> str:
    segments, _info = get_model(size, cpu_threads).transcribe(str(audio_path), vad_filter=True)
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


def select(mode: str) -> list[dict]:
    """Videos to Whisper this run. mode=all: no-transcript first, then caption upgrades.
    mode=gaps: only videos with no real transcript."""
    no_transcript, upgrades = [], []
    for f in sorted(glob.glob(str(PROCESSED / "*.json"))):
        try:
            r = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        src = r.get("transcript_source")
        vid = r.get("video_id")
        if not vid or src == "whisper":
            continue  # already the high-fidelity source
        if (PENDING / f"{vid}.json").exists():
            continue
        if src == "transcript":
            if mode == "all":
                upgrades.append(r)   # caption -> upgrade to Whisper
        else:
            no_transcript.append(r)  # caption-less / never fetched -> highest priority
    return no_transcript + upgrades


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=15, help="max videos this run (CPU-bound; keep small)")
    ap.add_argument("--mode", default="gaps", choices=["all", "gaps"],
                    help="gaps (default) = Whisper only videos WITHOUT an accepted complete caption "
                         "(the backfill keeps complete captions; Whisper fills the rest); "
                         "all = Whisper every video, overriding even complete captions")
    ap.add_argument("--model", default="tiny", help="tiny (default, lightest) | base | small")
    ap.add_argument("--cpu-threads", type=int, default=4, help="CPU threads for Whisper (gentle default)")
    ap.add_argument("--langs", default="en,he")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not deps_ok():
        return
    langs = [x.strip() for x in args.langs.split(",") if x.strip()]
    PENDING.mkdir(parents=True, exist_ok=True)

    todo = select(args.mode)
    todo = todo[: args.limit] if args.limit > 0 else todo
    print(f"mode={args.mode} model={args.model} threads={args.cpu_threads} — attempting {len(todo)} videos")

    now = datetime.now(timezone.utc).isoformat()
    done = skip = 0
    with tempfile.TemporaryDirectory() as tmp:
        for r in todo:
            vid = r["video_id"]
            time.sleep(0.5)
            # select() already excludes videos that have an accepted complete transcript, so in
            # 'gaps' mode every remaining video genuinely needs Whisper (no caption / incomplete).
            try:
                audio = download_audio(vid, tmp)
                if not audio:
                    skip += 1
                    continue
                wt = whisper_text(audio, args.model, args.cpu_threads)
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
            r.update(transcript=wt[:MAX_CHARS], transcript_lang="", transcript_source="whisper",
                     transcribed_at=now, transcribe_model=f"faster-whisper-{args.model}")
            done += 1
            print(f"  {vid}: WHISPER {len(wt)} chars")
            if not args.dry_run:
                with open(PENDING / f"{vid}.json", "w", encoding="utf-8") as fh:
                    json.dump(r, fh, ensure_ascii=False, indent=2)
    print(f"\nwhispered {done}, skipped {skip}; re-queued {done} for deep re-analysis.")


if __name__ == "__main__":
    main()
