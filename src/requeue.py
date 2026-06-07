"""
src/requeue.py — re-queue shallow/boilerplate videos for DEEP re-analysis.

Why: an early catch-up fast-drain analyzed ~950 content-rich videos shallowly, emitting
generic vendor stubs (skill_name="Claude", use_case="Using Claude for productivity tasks.")
that dedup then collapsed into a few vendor buckets. The real techniques those videos taught
were never extracted. The fix is the two-phase engine (CLAUDE.md anti-boilerplate gate); this
script feeds it the affected videos again.

How: the original transcript is still stored in data/processed/<id>.json, so we can re-analyze
WITHOUT re-fetching — copy a content-rich processed record back to data/_pending/<id>.json and
the analyze stage will re-extract it deeply. We only re-queue videos that (a) produced a
boilerplate stub, and (b) actually have a real transcript worth re-mining.

Usage:
    python -m src.requeue --limit 80          # re-queue up to 80 (default)
    python -m src.requeue --limit 0           # re-queue ALL eligible
    python -m src.requeue --dry-run           # just report, write nothing
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
PENDING = DATA / "_pending"
PROCESSED = DATA / "processed"
DELETED = DATA / "deleted_skills.json"

VENDORS = {
    "claude", "chatgpt", "gemini", "make", "anthropic", "openai", "mcp", "deepseek", "gpt",
    "grok", "llama", "claude code", "claude opus", "claude sonnet", "gemini ai", "gpt-5",
    "cursor", "cursor ai", "perplexity", "mistral", "qwen", "copilot", "github copilot",
    "notebooklm", "ollama", "openrouter",
}
TPL_USE = re.compile(r"^using .+ for .+ tasks\.?$", re.I)
TPL_DESC = re.compile(r" is an ai (tool|model) by .+\. it (enhances|automates|powers|generates)", re.I)
MIN_TRANSCRIPT = 1500  # only re-mine videos with real content


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def is_boilerplate(e: dict) -> bool:
    if _norm(e.get("skill_name")) in VENDORS:
        return True
    if TPL_USE.search(e.get("use_case", "") or ""):
        return True
    if TPL_DESC.search(e.get("description", "") or ""):
        return True
    return False


def shallow_video_ids() -> set[str]:
    """Video ids whose analysis collapsed into a boilerplate stub."""
    if not DELETED.exists():
        return set()
    try:
        deleted = json.load(open(DELETED, encoding="utf-8"))
    except Exception:
        return set()
    ids: set[str] = set()
    for e in deleted:
        if is_boilerplate(e):
            vid = e.get("source_video_id") or (e.get("endorsement_video_ids") or [None])[0]
            if vid:
                ids.add(vid)
    return ids


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=80, help="max videos to re-queue (0 = all)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    PENDING.mkdir(parents=True, exist_ok=True)
    candidates = shallow_video_ids()
    print(f"shallow (boilerplate) videos referenced: {len(candidates)}")

    eligible: list[str] = []
    for vid in sorted(candidates):
        pend = PENDING / f"{vid}.json"
        proc = PROCESSED / f"{vid}.json"
        if pend.exists() or not proc.exists():
            continue
        try:
            rec = json.load(open(proc, encoding="utf-8"))
        except Exception:
            continue
        # only re-mine content-rich videos (a real transcript), else re-analysis won't help
        if rec.get("transcript_source") != "transcript":
            continue
        if len(rec.get("transcript", "")) < MIN_TRANSCRIPT:
            continue
        eligible.append(vid)

    if args.limit and args.limit > 0:
        eligible = eligible[: args.limit]

    print(f"eligible to re-queue (real transcript, not already pending): {len(eligible)}")
    if args.dry_run:
        for vid in eligible:
            print("  would re-queue:", vid)
        print("DRY RUN — nothing written.")
        return

    n = 0
    for vid in eligible:
        shutil.copy2(PROCESSED / f"{vid}.json", PENDING / f"{vid}.json")
        n += 1
    print(f"re-queued {n} videos into data/_pending/ for deep re-analysis.")
    print("The analyze stage will re-extract them with the anti-boilerplate engine.")


if __name__ == "__main__":
    sys.exit(main())
