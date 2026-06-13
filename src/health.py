"""
src/health.py — a TINY, mechanical progress readout (Phase 1). NO Claude, NO network,
stdlib only. Writes data/health.json with the numbers the owner watches climb:

    transcripts  X / Y  (pct)        — videos that now have a REAL transcript
    pending      N                   — recovered transcripts queued for the free analysis lane
    library      skills / tools / models / connectors / prompts / commands

"Has a real transcript" is counted across BOTH data/processed/ and data/_pending/ (a freshly
backfilled video sits in _pending with transcript_source=="transcript" until the analyze lane
re-processes it), so the count rises the moment a transcript is recovered — not hours later.

Usage:
    python -m src.health           # write data/health.json + print the one-line summary
"""
from __future__ import annotations

import glob
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
REAL = ("transcript", "whisper")  # a real transcript (caption or ASR), not description-only


def _load(path):
    try:
        return json.load(open(path, encoding="utf-8"))
    except Exception:
        return None


def _count(path: Path, key: str) -> int:
    d = _load(path)
    return len(d.get(key, [])) if isinstance(d, dict) else 0


def main() -> int:
    total_ids: set[str] = set()
    recovered: set[str] = set()

    for f in glob.glob(str(DATA / "processed" / "*.json")):
        r = _load(f)
        if not isinstance(r, dict):
            continue
        vid = r.get("video_id")
        if not vid:
            continue
        total_ids.add(vid)
        if r.get("transcript_source") in REAL:
            recovered.add(vid)

    pending = sorted(glob.glob(str(DATA / "_pending" / "*.json")))
    for f in pending:
        r = _load(f)
        if isinstance(r, dict) and r.get("transcript_source") in REAL:
            vid = r.get("video_id")
            if vid:
                recovered.add(vid)

    total = len(total_ids)
    have = len(recovered)
    health = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "videos": {
            "total": total,
            "with_transcript": have,
            "transcript_pct": round(100 * have / total, 1) if total else 0.0,
            "lacking_transcript": max(total - have, 0),
            "pending_analysis": len(pending),
        },
        "library": {
            "skills": _count(DATA / "skills.json", "skills"),
            "tools": _count(DATA / "tools.json", "tools"),
            "models": _count(DATA / "models.json", "models"),
            "connectors": _count(DATA / "connectors.json", "connectors"),
            "prompts": _count(DATA / "prompts.json", "prompts"),
            "commands": _count(DATA / "commands.json", "commands"),
        },
    }
    out = DATA / "health.json"
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(health, fh, ensure_ascii=False, indent=2)

    v, lib = health["videos"], health["library"]
    print(f"transcripts {v['with_transcript']}/{v['total']} ({v['transcript_pct']}%) | "
          f"pending {v['pending_analysis']} | skills {lib['skills']} tools {lib['tools']} "
          f"models {lib['models']} connectors {lib['connectors']} prompts {lib['prompts']} "
          f"commands {lib['commands']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
