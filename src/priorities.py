"""
src/priorities.py — DYNAMIC PRIORITIES: keep the dashboard focused on what matters NOW.

The owner wanted the Effectiveness / Self-improvement / Developer tabs to stay relevant and re-order
problem priorities by what's actually happening. This reads the live state every cycle and ranks the
system's current problems by impact into data/priorities.json, which those tabs show at the top. As
the underlying numbers change (links get resolved, a lane stalls, a regression appears), the order
changes on its own. Free, mechanical.

Run:  python -m src.priorities
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "priorities.json"
NOW = datetime.now(timezone.utc).isoformat()


def _load(name, d=None):
    try:
        return json.load(open(DATA / name, encoding="utf-8"))
    except Exception:
        return d if d is not None else {}


def _items(name, key):
    d = _load(name, {})
    return d.get(key, []) if isinstance(d, dict) else (d if isinstance(d, list) else [])


def main() -> int:
    P = []  # each: (impact 0-100, area, title, detail)

    # 1) ACCESS — items with no usable link (the owner's top pain). Impact scales with how many.
    tools = _items("tools.json", "tools"); skills = _items("skills.json", "skills")
    no_link = sum(1 for x in tools + skills
                  if not (x.get("homepage") or x.get("github") or x.get("run_url")))
    total = len(tools) + len(skills)
    if no_link:
        pct = round(100 * no_link / max(total, 1), 1)
        P.append((min(100, 40 + no_link // 30), "access",
                  f"{no_link} tools/skills still have no real link ({pct}%)",
                  "The link-resolver runs each cycle; this falls as it works. Add Gemini keys to speed it."))

    # 2) REGRESSIONS — something was lost (highest urgency).
    for r in (_load("backup_status.json", {}).get("regressions") or []):
        P.append((98, "regression", f"'{r.get('type')}' dropped {r.get('dropped')} records",
                  "Restore from the last good backup; investigate what removed them."))

    # 3) PIPELINE — stalled/slow lanes.
    for l in (_load("pipeline_status.json", {}).get("lanes") or []):
        if l.get("status") in ("stale", "idle"):
            P.append((85, "pipeline", f"Lane '{l.get('label')}' is {l.get('status')}",
                      "Check the workflow logs; re-dispatch if blocked."))
        elif l.get("status") == "slow":
            P.append((55, "pipeline", f"Lane '{l.get('label')}' is slow", "Overdue vs its cadence."))

    # 4) MAINTENANCE — high-severity integrity issues.
    for i in (_load("maintenance.json", {}).get("issues") or []):
        if i.get("severity") == "high":
            P.append((70, "maintenance", f"{i.get('issue')} ({i.get('count')})", i.get("fix", "")))

    # 5) EFFECTIVENESS — the weakest lane to improve next.
    eff = _load("effectiveness.json", {})
    weak = (eff.get("summary") or {}).get("weakest_lane")
    if weak:
        P.append((45, "effectiveness", f"Weakest lane: {weak}",
                  f"Lowest effectiveness ({(eff.get('summary') or {}).get('weakest_effectiveness','?')}/10) — the improve stage targets it."))

    # 6) BACKLOG — analysis coverage.
    snap = _load("pipeline_status.json", {}).get("snapshot", {})
    tot, anz = snap.get("videos_total", 0), snap.get("videos_analyzed", 0)
    if tot and anz / tot < 0.5:
        P.append((50, "backlog", f"Only {anz}/{tot} videos analyzed ({round(100*anz/tot,1)}%)",
                  "Add free Gemini keys (GEMINI_API_KEY_2/_3) to multiply throughput."))

    # 7) OPEN self-improvement tasks queued.
    open_tasks = sum(1 for t in _items("improvement_tasks.json", "tasks")
                     if (t.get("status") or "open") != "done")
    if open_tasks:
        P.append((35, "self-improve", f"{open_tasks} self-improvement tasks queued",
                  "The improve stage works these on its 2×/week pass."))

    P.sort(key=lambda x: x[0], reverse=True)
    out = [{"rank": i + 1, "impact": s, "area": a, "title": t, "detail": d}
           for i, (s, a, t, d) in enumerate(P[:8])]
    OUT.write_text(json.dumps({"generated_at": NOW, "priorities": out},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"priorities: {len(out)} ranked (top = {out[0]['title'] if out else 'all clear'}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
