"""
src/improve_log.py — a short, human one-liner after each self-improvement cycle.

The owner wants to see, in a couple of short sentences, what the self-improvement system did each
time it ran (proof it's alive, without reading everything). This reads the outputs the other
mechanical protocols just wrote and appends ONE compact sentence to data/improve_log.json (last 30
kept). Run it LAST in the self-improvement step. Free, mechanical.

Run:  python -m src.improve_log
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "improve_log.json"
NOW = datetime.now(timezone.utc)


def _load(name, default):
    try:
        return json.load(open(DATA / name, encoding="utf-8"))
    except Exception:
        return default


def main() -> int:
    sc = _load("self_check.json", {}) or {}
    mt = _load("maintenance.json", {}) or {}
    ps = _load("pipeline_status.json", {}) or {}
    bk = _load("backup_status.json", {}) or {}
    tr = _load("trends.json", {}) or {}

    parts = []
    if sc.get("score") is not None:
        parts.append(f"self-check {sc.get('score')}/{sc.get('total', 50)}")
    if mt.get("grade"):
        parts.append(f"maintenance {mt.get('grade')} ({mt.get('issue_count', 0)} issues)")
    d24 = ps.get("deltas_24h") or {}
    moved = ", ".join(f"+{d24[k]} {k.replace('videos_with_transcript', 'transcripts')}"
                      for k in ("tools", "skills", "videos_with_transcript") if d24.get(k, 0) > 0)
    if moved:
        parts.append(f"24h: {moved}")
    regs = len(bk.get("regressions", []) or [])
    parts.append("0 regressions" if regs == 0 else f"{regs} REGRESSION(S)")
    props = tr.get("proposals") or []
    if props:
        parts.append(f"top trend: {props[0].get('proposed_feature', '')[:48]}")

    text = " · ".join(parts) if parts else "self-improvement cycle ran"
    log = _load("improve_log.json", {}) or {}
    entries = log.get("entries", [])
    # avoid duplicate back-to-back identical lines
    if not entries or entries[-1].get("text") != text:
        entries.append({"at": NOW.isoformat(), "text": text})
    entries = entries[-30:]
    OUT.write_text(json.dumps({"generated_at": NOW.isoformat(), "entries": entries},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"improve_log: {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
