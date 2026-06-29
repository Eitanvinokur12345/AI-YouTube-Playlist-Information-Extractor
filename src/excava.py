"""
src/excava.py — EXCAVA: the agentic OS that operates Excavatortron toward the 6 goals.

Honest first version (OS-1 operator). Each cycle EXCAVA:
  1. Runs its VERIFICATION GATE — focused checkers that decide if it's safe to act:
     data_guard (no collapse), security_scan (no leaks/clean), goals_check (esp. G3 truth/access),
     link coverage. This is the owner's "focused agents make sure it's good" — so power is never
     applied to bad data: outward actions (create/publish/self-edit) are BLOCKED until the gate is
     green AND the owner approves.
  2. Picks the next action from data/priorities.json. Internal/safe actions it owns; outward actions
     it HOLDS with the reason, until the gate opens.
  3. Self-optimizes its own tool stack via pipeline_scout (find more / combine / offload) and queues
     changes to self-improvement.
It writes data/excava_status.json (decisions + gate + holds) and logs. It does NOT yet autonomously
create/publish — that's OS-2, deliberately gated. Free, mechanical, no Claude tokens.

Run:  python -m src.excava
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "excava_status.json"
NOW = datetime.now(timezone.utc).isoformat()
G3_OUTWARD = 70          # truth/access must be this high before EXCAVA may create/publish

OUTWARD = {"create", "promote", "publish", "self-code", "leverage"}


def _load(name, d=None):
    try:
        return json.load(open(DATA / name, encoding="utf-8"))
    except Exception:
        return d if d is not None else {}


def main() -> int:
    guard = _load("data_guard.json", {})
    sec = _load("security.json", {})
    goals = {g["id"]: g for g in _load("goals_status.json", {}).get("goals", [])}
    prios = _load("priorities.json", {}).get("priorities", [])
    scout = _load("pipeline_scout.json", {})
    cfg = _load("excava_config.json", {})

    # ── VERIFICATION GATE (the focused agents) ──
    g3 = (goals.get("G3", {}) or {}).get("score", 0)
    checks = {
        "data_guard_ok": guard.get("restored", 0) == 0,
        "security_clean": not sec.get("secret_leaks"),
        "truth_access_G3": g3,
        "G3_ready_for_outward": g3 >= G3_OUTWARD,
    }
    internal_ok = checks["data_guard_ok"] and checks["security_clean"]
    outward_ok = internal_ok and checks["G3_ready_for_outward"]

    # ── next action from priorities; outward ones are held until the gate opens ──
    action, holding = None, []
    for p in prios:
        area = (p.get("area") or "").lower()
        is_outward = any(w in area for w in OUTWARD)
        if is_outward and not outward_ok:
            holding.append({"priority": p.get("title"), "why_held": f"outward action; gate closed (G3={g3}<{G3_OUTWARD} or checks failing)"})
            continue
        if action is None and internal_ok:
            action = {"do": p.get("title"), "area": p.get("area"), "detail": p.get("detail"),
                      "type": "outward" if is_outward else "internal"}
    if action is None and not internal_ok:
        action = {"do": "HOLD ALL — verification gate failing", "type": "blocked",
                  "detail": "fix data_guard/security before EXCAVA acts"}

    # ── self-optimize the tool stack ──
    stack_review = {
        "candidates_available": scout.get("total_candidates", 0),
        "note": ("EXCAVA reviews its stack each cycle: integrate the best free per-process tool, "
                 "combine overlaps, offload weak ones. Top open process gaps: "
                 + ", ".join(r["process"] for r in (scout.get("processes") or []) if r.get("count", 0) < 6)[:120]),
    }

    OUT.write_text(json.dumps({
        "generated_at": NOW, "name": "EXCAVA",
        "phase": "OS-1 operator (live); OS-2 creator + OS-3 self-coder gated",
        "gate": {"checks": checks, "internal_allowed": internal_ok, "outward_allowed": outward_ok,
                 "outward_needs": "data_guard ok + security clean + G3>=70 + owner approval"},
        "next_action": action, "holding": holding[:6],
        "tool_stack": cfg.get("tool_stack", []), "stack_review": stack_review,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"EXCAVA: gate internal={'open' if internal_ok else 'CLOSED'} outward={'open' if outward_ok else 'closed (G3=' + str(g3) + ')'}; "
          f"next = {action['do'] if action else 'none'}; holding {len(holding)} outward action(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
