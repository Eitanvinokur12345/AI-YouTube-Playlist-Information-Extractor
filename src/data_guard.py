"""
src/data_guard.py — never lose the library again. Auto-snapshot + auto-restore on collapse.

A cloud run once truncated tools/skills/models to a handful of items. The old backup guard missed it
because it compared against a snapshot that had already been overwritten with the bad counts. This
guard is bulletproof: it keeps a FULL copy of each data file in backups/snapshot/, and on every run
(FIRST and LAST in the pipeline) it checks each file. If a file has collapsed to < 55% of its healthy
snapshot count (and the snapshot had > 50 items), it RESTORES the file from the snapshot and logs a
CRITICAL event — the snapshot is only refreshed UP when the file is healthy, so a bad write can never
become the new baseline. Free, mechanical, no Claude tokens.

Run:  python -m src.data_guard
"""
from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
SNAP = ROOT / "backups" / "snapshot"
OUT = DATA / "data_guard.json"
NOW = datetime.now(timezone.utc).isoformat()
FILES = [("tools.json", "tools"), ("skills.json", "skills"), ("models.json", "models"),
         ("connectors.json", "connectors"), ("prompts.json", "prompts"), ("commands.json", "commands")]
FLOOR = 0.55          # a file under 55% of its snapshot count = catastrophic collapse
MIN_GUARD = 50        # only guard files that were sizable, so early growth isn't blocked


def _count(p: Path, key: str) -> int:
    try:
        d = json.load(open(p, encoding="utf-8"))
        return len(d.get(key, [])) if isinstance(d, dict) else (len(d) if isinstance(d, list) else 0)
    except Exception:
        return -1     # unreadable/corrupt


def main() -> int:
    SNAP.mkdir(parents=True, exist_ok=True)
    report = []
    restored = 0
    for fname, key in FILES:
        cur = DATA / fname
        snap = SNAP / fname
        cur_n = _count(cur, key)
        snap_n = _count(snap, key) if snap.exists() else -1
        collapsed = snap_n >= MIN_GUARD and (cur_n < 0 or cur_n < snap_n * FLOOR)
        if collapsed:
            # collapse (or corrupt) -> restore from the healthy snapshot
            shutil.copy2(snap, cur)
            restored += 1
            report.append({"file": fname, "action": "RESTORED", "was": cur_n, "restored_to": snap_n})
        else:
            # healthy -> refresh the snapshot upward (never let a smaller file become the baseline)
            if cur_n >= snap_n and cur_n >= 0:
                shutil.copy2(cur, snap)
            report.append({"file": fname, "action": "ok", "count": cur_n, "snapshot": max(snap_n, cur_n)})

    OUT.write_text(json.dumps({"generated_at": NOW, "restored": restored, "files": report},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    tag = "CRITICAL — restored " + str(restored) if restored else "all files healthy"
    print(f"data_guard: {tag}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
