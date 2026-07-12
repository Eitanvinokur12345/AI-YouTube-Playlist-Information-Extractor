"""
src/temporal_validity.py — R3-2 TEMPORAL VALIDITY (owner-ranked #2 from the Agentic-OS study,
Zep/Graphiti's idea): hub facts should know WHEN they were last confirmed true, not just
whether. Reuses data/elements_verified.json (already tracks per-element {at, status,
link_alive}) — no new plumbing, just makes age a first-class signal.

Two honest outputs:
  1. age distribution — how fresh the verified store actually is right now.
  2. a durable STALENESS EVENTS LOG — capability-level facts that stopped being true, caught
     this week (openrouter's free model going paid, cerebras model id dying). Before this,
     each was a one-off fix noted only in project memory; now they accumulate in one place
     so the pattern ("free things go paid, models get deprecated") is visible over time.

Free, stdlib-only. Run: python -m src.temporal_validity
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUT = ROOT / "data" / "excava" / "temporal_validity.json"
EVENTS_LOG = ROOT / "data" / "excava" / "staleness_events.jsonl"

STALE_DAYS = 14  # a verified-true fact older than this needs re-confirming before citing hard


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def age_report() -> dict:
    try:
        rec = json.load(open(ROOT / "data" / "elements_verified.json", encoding="utf-8"))["verified"]
    except Exception:
        rec = {}
    now = datetime.now(timezone.utc)
    buckets = {"fresh_0-3d": 0, "recent_4-14d": 0, "stale_15d+": 0, "unparseable": 0}
    stale_ids = []
    for eid, v in rec.items():
        try:
            age = (now - datetime.fromisoformat(v["at"])).days
        except Exception:
            buckets["unparseable"] += 1
            continue
        if age <= 3:
            buckets["fresh_0-3d"] += 1
        elif age <= STALE_DAYS:
            buckets["recent_4-14d"] += 1
        else:
            buckets["stale_15d+"] += 1
            stale_ids.append(eid)
    return {"total": len(rec), "buckets": buckets, "stale_ids_sample": stale_ids[:10]}


def log_staleness_event(what: str, was_true_until: str, now_true: str, caught_by: str) -> None:
    """Call this whenever a fact is caught having gone stale (a free tier going paid, a model
    id dying, a docs claim outdated). Durable — the pattern accumulates instead of vanishing
    into a one-off git commit message."""
    EVENTS_LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(EVENTS_LOG, "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"at": _now(), "what": what, "was_true_until": was_true_until,
                             "now_true": now_true, "caught_by": caught_by},
                            ensure_ascii=False) + "\n")


def build() -> dict:
    ar = age_report()
    events = []
    if EVENTS_LOG.exists():
        for ln in EVENTS_LOG.read_text(encoding="utf-8").splitlines():
            try:
                events.append(json.loads(ln))
            except Exception:
                pass
    report = {"generated_at": _now(), "age_report": ar,
              "stale_threshold_days": STALE_DAYS,
              "staleness_events_total": len(events),
              "recent_staleness_events": events[-10:],
              "note": ("Zep's idea, adapted free: hub facts carry a WHEN, not just a WHAT. "
                      "Right now the verify lane runs often enough that nothing is element-stale "
                      "(honest — see age_report). The real staleness so far has been at the "
                      "CAPABILITY layer (engine catalog), logged in staleness_events.jsonl so the "
                      "pattern is visible over time instead of a one-off fix each time.")}
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    return report


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    r = build()
    print(f"temporal-validity: {r['age_report']['total']} verified records, "
          f"buckets={r['age_report']['buckets']}, {r['staleness_events_total']} staleness events logged")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
