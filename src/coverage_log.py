"""
src/coverage_log.py — record daily LINK coverage so the "+5%/day" target is visible and tracked.

Writes data/coverage_log.json: the latest coverage %, the delta vs the previous day, and a 120-day
history. The links lane runs this each cycle; the same-day entry updates in place, so each day shows
its real net progress. Free, mechanical. Run:  python -m src.coverage_log
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "coverage_log.json"


def _load(p):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return {}


def main() -> int:
    tot = lk = 0
    for f, k in [("tools.json", "tools"), ("skills.json", "skills"), ("connectors.json", "connectors")]:
        for it in _load(DATA / f).get(k, []):
            tot += 1
            if it.get("homepage") or it.get("github") or it.get("install_or_source"):
                lk += 1
    pct = round(100 * lk / max(tot, 1), 2)
    log = _load(OUT)
    days = log.get("days", []) if isinstance(log, dict) else []
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    prior = [d for d in days if d.get("date") != today]           # today updates in place
    prev = prior[-1] if prior else None
    delta = round(pct - (prev.get("pct") if prev else pct), 2)
    prior.append({"date": today, "linked": lk, "total": tot, "pct": pct})
    out = {"updated_at": datetime.now(timezone.utc).isoformat(),
           "latest": {"linked": lk, "total": tot, "pct": pct},
           "delta_pct_vs_prev_day": delta, "target_pct_per_day": 5.0,
           "on_track": delta >= 5.0, "days": prior[-120:]}
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"coverage_log: {lk}/{tot} = {pct}% (delta {delta:+}% vs prev day; target +5%/day).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
