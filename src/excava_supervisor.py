"""
src/excava_supervisor.py — THE SUPERVISOR (owner law 2026-07-07: super-strict criticism of every
external-tool result; a facade must not survive one beat).

After the workers run, the supervisor judges each department's REAL-tool result with a hostile eye:
  • real    — the tool ran and produced substantive output (positive counts / findings).
  • no-op    — the tool ran but accomplished NOTHING this cycle (warmed 0, queued 0, built for 0…);
               either the wrong tool, no real input, or theatre. FLAGGED.
  • failed   — the tool errored / timed out / produced nothing usable. FLAGGED.
  • planned  — still just a plan, not execution (the hollow-work facade). FLAGGED HARD.
Writes data/excava/supervisor.json (verdicts + a harsh summary + a grade) for the beat + dashboard.
Default stance: SKEPTICAL — a result is theatre until its output proves otherwise.
Run:  python -m src.excava_supervisor
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "excava" / "supervisor.json"

FAIL = ("timed out", "traceback", "error", "exception", "(no output)", "no engines", "failed")
NOOP = ("warmed 0", "queued 0", "for 0 ", " 0 items", "0 proposals", "0 design", "0 new", "nothing")


def judge(result: str, dept: str) -> tuple[str, str]:
    r = (result or "").strip().lower()
    if not r:
        return "planned", "empty result — nothing was actually done"
    if r.startswith("execution plan") or "not executed" in r or "plan written" in r:
        return "planned", "STILL A PLAN, not execution — the hollow-work facade"
    if not r.startswith("ran "):
        return "planned", "not a real-tool run — no external tool executed"
    if any(f in r for f in FAIL):
        return "failed", "the external tool ran but FAILED or returned nothing usable"
    # 'no-op', but a clean security/verify scan ('0 leaks') is a REAL good result, not a no-op.
    good_zero = dept in ("security",) and ("leak" in r or "clean" in r or "flagged" in r)
    if not good_zero and any(n in r for n in NOOP):
        return "noop", "tool ran but ACCOMPLISHED NOTHING this cycle — wrong tool, no input, or theatre"
    return "real", "produced substantive real output"


def run() -> list[str]:
    try:
        bus = json.loads((DATA / "excava" / "bus.json").read_text(encoding="utf-8"))
    except Exception:
        return ["supervisor: no bus to inspect"]
    done = [t for t in bus.get("tasks", []) if t.get("status") == "done"]
    recent = sorted(done, key=lambda t: t.get("updated_at", ""), reverse=True)[:40]
    verdicts, counts = [], {"real": 0, "noop": 0, "failed": 0, "planned": 0}
    for t in recent:
        v, note = judge(str(t.get("result", "")), t.get("department", ""))
        counts[v] += 1
        verdicts.append({"task": t.get("id"), "dept": t.get("department"), "verdict": v,
                         "note": note, "result": str(t.get("result", ""))[:160]})
    n = max(len(recent), 1)
    real_pct = round(100 * counts["real"] / n)
    flagged = counts["noop"] + counts["failed"] + counts["planned"]
    if real_pct >= 80:
        crit = f"Acceptable: {real_pct}% of the last {n} completions did real work. Stay strict."
    elif real_pct >= 40:
        crit = (f"WEAK: only {real_pct}% real of the last {n}. {flagged} were hollow/failed/planned — "
                "that is theatre wearing a 'done' badge. Fix the flagged departments before adding anything.")
    else:
        crit = (f"FACADE ALERT: only {real_pct}% of the last {n} completions did real work; {flagged} were "
                "hollow. The counter is lying again. STOP building features — make the flagged work real.")
    doc = {"generated_at": datetime.now(timezone.utc).isoformat(), "checked": n,
           "real_pct": real_pct, "counts": counts, "criticism": crit, "verdicts": verdicts}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    worst = [v for v in verdicts if v["verdict"] in ("planned", "failed", "noop")][:3]
    lines = [f"supervisor: {real_pct}% real of last {n} ({counts['real']}✓ {counts['noop']}no-op "
             f"{counts['failed']}fail {counts['planned']}plan)"]
    for w in worst:
        lines.append(f"  ⚠ {w['dept']}/{w['task']}: {w['verdict']} — {w['note']}")
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
