"""
src/excava_systemcheck.py — SYSTEMATIC "DOES EVERYTHING WORK?" CHECK (owner law 2026-07-07).
Runs every beat: probes every functional subsystem of EXCAVA and reports PASS/FAIL/WARN with a
real reason, so nothing can silently rot. Writes data/excava/systemcheck.json (working/total + the
failures). Fast: it verifies things LOAD and recent data is HEALTHY; it does not run heavy lanes.
Run: python -m src.excava_systemcheck
"""
from __future__ import annotations

import importlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"


def _load(p, d=None):
    try:
        return json.loads((DATA / p).read_text(encoding="utf-8"))
    except Exception:
        return d if d is not None else {}


def _fresh(p, hours=6) -> bool:
    f = DATA / p
    return f.exists() and (time.time() - f.stat().st_mtime) < hours * 3600


def _c(system, ok, detail, sev="warn"):
    return {"system": system, "ok": bool(ok), "detail": detail, "severity": sev}


def check() -> list[dict]:
    out = []
    # 1. beat modules import (the OS can boot at all)
    mods = ["src.excava", "src.excava_agents", "src.excava_chat", "src.excava_backlog",
            "src.excava_supervisor", "src.excava_engines", "src.build_capabilities", "src.goals_check"]
    bad = []
    for m in mods:
        try:
            importlib.import_module(m)
        except Exception as e:
            bad.append(f"{m}:{type(e).__name__}")
    out.append(_c("beat modules import", not bad, "all core modules import" if not bad else f"BROKEN: {bad}", "critical"))

    # 2. engines configured (catalog present; availability needs CI keys)
    try:
        from src.excava_engines import CATALOG, available
        av = len(available())
        out.append(_c("engines", len(CATALOG) >= 5, f"{len(CATALOG)} in catalog, {av} available here"
                      + (" (keys live in CI)" if av == 0 else ""), "critical"))
    except Exception as e:
        out.append(_c("engines", False, f"engine layer broken: {e}", "critical"))

    # 3. departments can execute (every dept has a worker + a real tool or work fn)
    try:
        from src import excava_agents as ag
        reg = ag.load_registry()
        depts = sorted({a.get("department") for a in reg.get("agents", []) if a.get("department") not in (None, "core")})
        staffed = [d for d in depts if ag.worker_for(reg, d)]
        executable = [d for d in depts if d in ag.WORK or d in ag.REAL_TOOL]
        out.append(_c("departments executable", len(executable) >= len(depts) - 2,
                      f"{len(executable)}/{len(depts)} depts have a real executor; {len(staffed)}/{len(depts)} staffed"))
    except Exception as e:
        out.append(_c("departments executable", False, f"agent layer broken: {e}", "critical"))

    # 4. work is REAL (supervisor real_pct)
    sup = _load("excava/supervisor.json")
    rp = sup.get("real_pct", 0)
    out.append(_c("work is real (supervisor)", rp >= 25, f"real_pct={rp}% ({sup.get('counts', {})})"
                  + ("" if rp >= 25 else " — mostly hollow, drive it up")))

    # 5. movement rising (not stalled at 0)
    mv = _load("excava/movement.json")
    hist = mv.get("history", [])
    dones = [h.get("done", 0) for h in hist[-5:]]
    rising = len(dones) < 2 or dones[-1] > dones[0]
    out.append(_c("movement rising", rising, f"done trend {dones}" if dones else "no movement history yet"))

    # 6. intent charter + no drift
    intent = _load("excava/intent.json").get("departments", {})
    drift = len(sup.get("intent_drift", []))
    out.append(_c("intent aligned", bool(intent) and drift == 0,
                  f"{len(intent)} depts chartered, {drift} tool-drift" if intent else "no intent charter"))

    # 7. full owner history present
    hi = _load("excava/history_index.json")
    out.append(_c("owner history captured", hi.get("records", 0) > 100,
                  f"{hi.get('records', 0)} records / {hi.get('session_count', 0)} sessions"))

    # 8. bus + backlog flowing
    bus = _load("excava/bus.json")
    tasks = bus.get("tasks", [])
    done = sum(1 for t in tasks if t.get("status") == "done")
    out.append(_c("bus + backlog", bool(tasks) and (DATA / "excava" / "backlog.json").exists(),
                  f"{len(tasks)} tasks ({done} done); backlog {'present' if (DATA / 'excava' / 'backlog.json').exists() else 'MISSING'}"))

    # 9. goals scored (the 9 North-Star)
    goals = _load("goals_status.json").get("goals", [])
    met = sum(1 for g in goals if g.get("status") == "met")
    out.append(_c("north-star goals scored", len(goals) >= 9,
                  f"{len(goals)} goals, {met} met, overall {_load('goals_status.json').get('overall', '?')}"))

    # 10. guardrails + JSON integrity
    grd = _load("guardrails_status.json")
    out.append(_c("guardrails", grd.get("critical_failures", 1) == 0,
                  f"{grd.get('passing', '?')}/{grd.get('total', '?')} passing, {grd.get('critical_failures', '?')} critical"))
    return out


def run() -> list[str]:
    results = check()
    working = sum(1 for r in results if r["ok"])
    crit = [r for r in results if not r["ok"] and r["severity"] == "critical"]
    doc = {"generated_at": datetime.now(timezone.utc).isoformat(), "working": working,
           "total": len(results), "critical_broken": len(crit), "systems": results}
    (DATA / "excava" / "systemcheck.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    lines = [f"systemcheck: {working}/{len(results)} systems working"
             + (f" · {len(crit)} CRITICAL broken" if crit else " · all critical OK")]
    for r in results:
        if not r["ok"]:
            lines.append(f"  {'✗' if r['severity'] == 'critical' else '!'} {r['system']}: {r['detail']}")
    return lines


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    for ln in run():
        print(ln)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
