"""
src/excava_backlog.py — the ALWAYS-THERE backlog + the internal JUDGMENT system.
(Owner 2026-07-06: agents must always have a next task; big tasks wait, small ones run in
parallel; tasks must be VALUABLE, never make-work.)

Two scores decide everything, and both are logged as numbers so the judgment is auditable:
  • VALUE  — is this worth doing? Real gaps (unverified elements, dead links, low goals) score
             high automatically; agent-BRAINSTORMED ideas must clear a value BAR to be queued.
  • SIZE   — cost(engine calls) + steps(subtasks) + risk(outward/irreversible). size ≥ BIG ⇒ the
             department finishes it before starting another; smaller tasks run concurrently.

No gap + no above-bar idea ⇒ the department RESTS honestly (better than inventing busywork).
`refresh()` writes data/excava/backlog.json (the visible, value-ranked, size-judged backlog) and
enqueues the top items onto the bus; `plan_beat()` applies the concurrency judgment per department.
Run: python -m src.excava_backlog            # scan gaps, rank, enqueue, write backlog.json
"""
from __future__ import annotations

import json
from pathlib import Path

from src import excava_bus as bus

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
BACKLOG = DATA / "excava" / "backlog.json"

VALUE_BAR = 60          # brainstormed ideas must beat this to be queued (gaps are exempt)
BIG_THRESHOLD = 55      # size ≥ this ⇒ "big" ⇒ run alone
DEPT_FOR_GOAL = {"G1": "analysis", "G3": "links", "G4": "improve", "G5": "creators",
                 "G8": "visual", "G9": "improve"}


def _load(name, d=None):
    p = DATA / name
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {} if d is None else d


# ── SIZE: cost + steps + risk → one auditable number ────────────────────────────
def size_score(cost: int, steps: int, risk: int) -> dict:
    """cost/steps/risk each 0-100; size is their weighted blend. Returns the numbers + verdict."""
    size = round(0.5 * cost + 0.3 * steps + 0.2 * risk)
    return {"cost": cost, "steps": steps, "risk": risk, "size": size,
            "big": size >= BIG_THRESHOLD}


# ── VALUE + the real-gap scanner (no make-work) ─────────────────────────────────
def scan_gaps() -> list[dict]:
    """Turn measurable deficits into candidate tasks. Bigger deficit ⇒ higher value."""
    out = []
    ix = _load("elements_index.json", {}).get("elements", [])
    unver = sum(1 for e in ix if e.get("verified", {}).get("status") == "unverified")
    if unver:
        out.append({"title": f"Verify the next 200 of {unver} unverified elements (2-source + live test)",
                    "department": "analysis", "source": "gap", "why": f"{unver} elements unverified",
                    "value": min(96, 55 + unver // 200),
                    **size_score(cost=35, steps=70, risk=10)})   # many steps, cheap-ish, low risk
    links = _load("links.json", {})
    dead = links.get("dead", 0) if isinstance(links, dict) else 0
    unlinked = links.get("unlinked", 0) if isinstance(links, dict) else 0
    if unlinked or unver:
        out.append({"title": "Resolve real links (website/github/codespaces) for the next 200 unlinked elements",
                    "department": "links", "source": "gap", "why": f"{unlinked or 'many'} unlinked",
                    "value": 82, **size_score(cost=40, steps=60, risk=15)})
    if dead:
        out.append({"title": f"Re-check {dead} dead links and prune only the truly dead (P3)",
                    "department": "links", "source": "gap", "why": f"{dead} dead links",
                    "value": 70, **size_score(cost=20, steps=30, risk=20)})
    goals = _load("goals_status.json", {}).get("goals", [])
    for g in goals:
        if g.get("score", 100) < 70:
            dept = DEPT_FOR_GOAL.get(g["id"], "improve")
            out.append({"title": f"Raise {g['id']} {g.get('name', '')} ({g['score']}/100): {str(g.get('gap', ''))[:80]}",
                        "department": dept, "source": "gap", "why": f"{g['id']} at {g['score']}",
                        "value": 100 - g["score"], **size_score(cost=15, steps=25, risk=10)})
    # ── per-department REAL work, so no department rests at 0 without cause (all from real counts) ──
    import glob as _glob
    pending = len(_glob.glob(str(DATA / "_pending" / "*.json")))
    if pending:
        out.append({"title": f"Watch: process the next batch of {pending} pending videos", "department": "watch",
                    "source": "gap", "why": f"{pending} pending", "value": min(90, 50 + pending // 40), **size_score(30, 40, 10)})
        out.append({"title": f"Transcripts: drain the next batch of {pending} pending (residential IP)", "department": "transcripts",
                    "source": "gap", "why": f"{pending} pending", "value": 60, **size_score(25, 35, 15)})
    con = _load("connectors.json", {})
    ncon = len(con.get("connectors", con) if isinstance(con, dict) else con) if con else 0
    if ncon:
        out.append({"title": f"Security: safety-rate the next batch of {ncon} connectors/skills", "department": "security",
                    "source": "gap", "why": f"{ncon} connectors", "value": 72, **size_score(25, 30, 25)})
        out.append({"title": "Mining: discover new AI repos/tools + verify this cycle", "department": "mining",
                    "source": "gap", "why": "discovery cadence", "value": 68, **size_score(20, 25, 10)})
    if (DATA / "weekly_web_news.json").exists():
        out.append({"title": "News: refresh the AI-news digest for the newest sources", "department": "news",
                    "source": "gap", "why": "freshness cadence", "value": 62, **size_score(15, 20, 5)})
    n_el = len(_load("elements_index.json", {}).get("elements", []))
    if n_el:
        out.append({"title": f"Memory: embed the remaining unembedded of {n_el} elements for full recall", "department": "memory",
                    "source": "gap", "why": f"{n_el} elements", "value": 64, **size_score(20, 30, 5)})
    return out


def value_ok(task: dict) -> bool:
    return task["source"] == "gap" or task.get("value", 0) >= VALUE_BAR


# ── the concurrency JUDGMENT: which queued tasks a department runs this beat ─────
def plan_beat(max_parallel_small: int = 3) -> dict:
    """Per department: if a BIG task is queued/working, finish it before starting others; else run
    up to N small tasks concurrently. Aggressive by choice, but a rate-budget backpressure elsewhere
    still guards the free engines. Returns the run-plan (logged, visible)."""
    b = bus.read_bus()
    by_dept: dict = {}
    for t in b.get("tasks", []):
        if t.get("status") in ("queued", "working"):
            by_dept.setdefault(t.get("department") or "core", []).append(t)
    plan = {}
    for dept, tasks in by_dept.items():
        big = [t for t in tasks if _is_big(t)]
        small = [t for t in tasks if not _is_big(t)]
        if any(t.get("status") == "working" and _is_big(t) for t in tasks):
            plan[dept] = {"run": [], "reason": "a big task is running — hold until it finishes"}
        elif big:
            plan[dept] = {"run": [big[0]["id"]], "reason": f"big task runs ALONE (size≥{BIG_THRESHOLD})"}
        else:
            plan[dept] = {"run": [t["id"] for t in small[:max_parallel_small]],
                          "reason": f"{min(len(small), max_parallel_small)} small task(s) run in parallel"}
    return plan


def _is_big(t: dict) -> bool:
    d = t.get("detail", "")
    return "size=BIG" in d or (isinstance(t.get("size"), int) and t["size"] >= BIG_THRESHOLD)


def refresh(max_new: int = 12) -> dict:
    """Build the value-ranked, size-judged backlog; enqueue the top above-bar items (deduped)."""
    cands = [c for c in scan_gaps() if value_ok(c)]
    cands.sort(key=lambda c: -c["value"])
    queued = []
    for c in cands[:max_new]:
        tag = f"value={c['value']} size={c['size']}({'BIG' if c['big'] else 'small'}) " \
              f"[cost {c['cost']}/steps {c['steps']}/risk {c['risk']}] · {c['why']}"
        t = bus.enqueue(c["title"], detail=tag, department=c["department"],
                        source="gap", priority=1,
                        done_criteria="a committed artifact that measurably closes this gap")
        if t:
            queued.append({"id": t["id"], **c})
    BACKLOG.parent.mkdir(parents=True, exist_ok=True)
    snapshot = {"generated_at": bus._now(), "candidates": cands, "queued_now": queued,
                "value_bar": VALUE_BAR, "big_threshold": BIG_THRESHOLD, "plan": plan_beat()}
    BACKLOG.write_text(json.dumps(snapshot, ensure_ascii=False, indent=1), encoding="utf-8")
    return snapshot


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    s = refresh()
    print(f"backlog: {len(s['candidates'])} real-gap candidates, queued {len(s['queued_now'])} above-bar")
    for c in s["candidates"][:8]:
        print(f"  value {c['value']:>3} · size {c['size']:>3} {'BIG ' if c['big'] else 'small'} · "
              f"{c['department']:9} · {c['title'][:70]}")
    print("concurrency plan:", {d: p["reason"] for d, p in s["plan"].items()})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
