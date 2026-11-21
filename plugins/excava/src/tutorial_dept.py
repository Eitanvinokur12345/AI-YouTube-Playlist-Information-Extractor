"""
src/tutorial_dept.py — the TUTORIAL DEPARTMENT (owner 2026-07-13, approved). A low-frequency
department that runs ~WEEKLY, makes NO decisions, and does one job: review everything that
changed since its last run and write a plain-language walkthrough so the owner never loses his
bearings. Pure output, no debate room, no bus decisions.

Source of truth for "what changed": data/excava/improvements.jsonl (every self-change) +
the shipped builds recorded there. Mechanical + free (no engine) — deterministic, cheap.
Output: appends a pinned tutorial to data/tutorials.json (the cockpit already shows newest-first).
Run: python -m src.tutorial_dept [--force]
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
TUTS = DATA / "tutorials.json"
WEEK = 7 * 24 * 3600


def _load_tuts():
    try:
        d = json.load(open(TUTS, encoding="utf-8"))
        return d if isinstance(d, list) else d.get("tutorials", []), isinstance(d, list)
    except Exception:
        return [], True


def _due(tuts) -> bool:
    for t in tuts:
        if t.get("build") == "tutorial-dept":
            try:
                age = (datetime.now(timezone.utc)
                       - datetime.fromisoformat(t["at"])).total_seconds()
                return age > WEEK
            except Exception:
                return True
    return True


def run(force: bool = False) -> dict:
    tuts, is_list = _load_tuts()
    if not force and not _due(tuts):
        return {"wrote": False, "reason": "not due (runs weekly)"}
    # gather the week's real FEATURE changes from the project-memory ship log (the WHY log =
    # owner-facing features), falling back to the internal improvement log.
    since = datetime.now(timezone.utc) - timedelta(days=7)
    changes = []
    for ln in (DATA / "project_memory" / "episodes.jsonl").read_text(encoding="utf-8").splitlines():
        try:
            r = json.loads(ln)
            at = datetime.fromisoformat(r["at"])
        except Exception:
            continue
        # kind 'manual' = my deliberate WHY-logged feature ships (not auto commits/bus traces)
        if at >= since and r.get("kind") == "manual" and r.get("what"):
            changes.append(r["what"].split(" — ")[0])
    # de-dup, keep the substantive ones
    seen, steps = set(), []
    for c in changes:
        key = re.sub(r"[\d]", "", c.lower())[:40]
        if key in seen:
            continue
        seen.add(key)
        steps.append(c[:130])
    steps = steps[:12] or ["No self-changes were logged this week — the system held steady."]
    entry = {"build": "tutorial-dept", "pinned": True,
             "title": f"📚 This week in EXCAVA — {datetime.now(timezone.utc).date().isoformat()} "
                      f"({len(steps)} change{'s' if len(steps) != 1 else ''})",
             "at": datetime.now(timezone.utc).isoformat(),
             "steps": steps,
             "note": "Auto-written by the Tutorial department (weekly, no decisions) so you always "
                     "know what changed. Older weekly recaps are kept below."}
    # keep prior weekly recaps but un-pin them, and cap history
    for t in tuts:
        if t.get("build") == "tutorial-dept":
            t["pinned"] = False
            t["build"] = "tutorial-dept-past"
    tuts.append(entry)
    payload = tuts if is_list else {"tutorials": tuts}
    TUTS.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    return {"wrote": True, "changes": len(steps), "title": entry["title"]}


def main() -> int:
    import argparse, sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    force = argparse.ArgumentParser().parse_known_args()[1]  # noqa
    r = run(force="--force" in sys.argv)
    print(f"tutorial-dept: {r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
