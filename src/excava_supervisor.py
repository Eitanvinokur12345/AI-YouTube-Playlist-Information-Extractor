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
    if r.startswith("blocked"):
        return "blocked", "honestly BLOCKED — needs an owner resource; not faking work (this is the truth, not a facade)"
    # HOLLOW-PLAN signature only: the _work_generic facade labels itself a plan / writes a task-artifact.
    # (Bespoke WORK functions — analysis/memory/links/creators — do real assessments that don't say 'RAN';
    # those are REAL, not plans. Only the explicit plan/task-artifact outputs are hollow.)
    if ("not executed" in r or r.startswith("execution plan") or "plan written" in r
            or "artifacts/task-" in r):
        return "planned", "STILL A PLAN, not execution — the hollow-work facade"
    if any(f in r for f in FAIL):
        return "failed", "the external tool ran but FAILED or returned nothing usable"
    # 'no-op', but a clean security/verify scan ('0 leaks') is a REAL good result, not a no-op.
    good_zero = dept in ("security",) and ("leak" in r or "clean" in r or "flagged" in r)
    if not good_zero and any(n in r for n in NOOP):
        return "noop", "tool ran but ACCOMPLISHED NOTHING this cycle — wrong tool, no input, or theatre"
    return "real", "produced substantive real output"


def check_intent_alignment() -> list[dict]:
    """Strict intent check (owner law): is each department wired to the RIGHT tool for what Eitan
    actually wants it to do (data/excava/intent.json), or is it doing the wrong job — the
    mining→source_bundles / visual→warm_shots class of drift?"""
    try:
        intent = json.loads((DATA / "excava" / "intent.json").read_text(encoding="utf-8")).get("departments", {})
        from src.excava_agents import REAL_TOOL
    except Exception:
        return []
    flags = []
    for dept, charter in intent.items():
        want = charter.get("right_tool")
        wired = REAL_TOOL.get(dept)
        if want and wired and wired != want:
            flags.append({"dept": dept, "wants": want, "wired": wired,
                          "should_do": charter.get("should_do", ""),
                          "note": f"WRONG TOOL for intent — {dept} should run {want} ({charter.get('should_do','')[:60]}) but is wired to {wired}"})
        elif want and not wired and dept in REAL_TOOL:
            flags.append({"dept": dept, "wants": want, "wired": None,
                          "note": f"{dept} has no real executor wired though its intent needs {want}"})
    return flags


def _history() -> dict:
    """The supervisor's memory of the WHOLE project: the owner's full message history (all 5
    sessions), ingested to the repo by src.ingest_history so even the CI supervisor knows the
    entire history + the owner's true desires (owner law 2026-07-07, non-negotiable)."""
    try:
        return json.loads((DATA / "excava" / "history_index.json").read_text(encoding="utf-8"))
    except Exception:
        return {}


def run() -> list[str]:
    try:
        bus = json.loads((DATA / "excava" / "bus.json").read_text(encoding="utf-8"))
    except Exception:
        return ["supervisor: no bus to inspect"]
    intent_flags = check_intent_alignment()
    hist = _history()
    done = [t for t in bus.get("tasks", []) if t.get("status") == "done"]
    recent = sorted(done, key=lambda t: t.get("updated_at", ""), reverse=True)[:40]
    verdicts, counts = [], {"real": 0, "noop": 0, "failed": 0, "planned": 0, "blocked": 0}
    for t in recent:
        v, note = judge(str(t.get("result", "")), t.get("department", ""))
        counts[v] += 1
        verdicts.append({"task": t.get("id"), "dept": t.get("department"), "verdict": v,
                         "note": note, "result": str(t.get("result", ""))[:160]})
    n = max(len(recent), 1)
    gradable = max(n - counts["blocked"], 1)   # 'blocked' = honest 'can't' (owner resource), not graded
    real_pct = round(100 * counts["real"] / gradable)
    flagged = counts["noop"] + counts["failed"] + counts["planned"]
    if real_pct >= 80:
        crit = f"Acceptable: {real_pct}% of the last {n} completions did real work. Stay strict."
    elif real_pct >= 40:
        crit = (f"WEAK: only {real_pct}% real of the last {n}. {flagged} were hollow/failed/planned — "
                "that is theatre wearing a 'done' badge. Fix the flagged departments before adding anything.")
    else:
        crit = (f"FACADE ALERT: only {real_pct}% of the last {n} completions did real work; {flagged} were "
                "hollow. The counter is lying again. STOP building features — make the flagged work real.")
    if intent_flags:
        crit += f" · INTENT DRIFT: {len(intent_flags)} dept(s) wired to the WRONG tool for what you wanted — " \
                + "; ".join(f"{f['dept']}→wants {f['wants']} not {f['wired']}" for f in intent_flags[:3])
    doc = {"generated_at": datetime.now(timezone.utc).isoformat(), "checked": n,
           "real_pct": real_pct, "counts": counts, "criticism": crit,
           "history": {"records": hist.get("records", 0), "owner_messages": hist.get("owner_messages", 0),
                       "questions": hist.get("questions", 0), "answers": hist.get("answers", 0),
                       "sessions": hist.get("session_count", 0), "since": hist.get("first", "")[:10]},
           "intent_drift": intent_flags, "verdicts": verdicts}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    worst = [v for v in verdicts if v["verdict"] in ("planned", "failed", "noop")][:3]
    lines = [f"supervisor: {real_pct}% real of last {n} ({counts['real']}✓ {counts['noop']}no-op "
             f"{counts['failed']}fail {counts['planned']}plan) · knows history: "
             f"{hist.get('records', 0)} recs ({hist.get('owner_messages', 0)} msgs, {hist.get('questions', 0)} Qs, "
             f"{hist.get('answers', 0)} answer-sets) / {hist.get('session_count', 0)} sessions"]
    for f in intent_flags:
        lines.append(f"  ⚠ INTENT: {f['note']}")
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
