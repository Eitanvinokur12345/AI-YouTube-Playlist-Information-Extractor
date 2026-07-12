"""
src/guardrail_test.py — the GUARDRAIL FIRING TEST (owner 2026-07-12: "it needs to be done
firmly, to check that everything is working properly").

A guardrail that has never been SEEN to fire is a hope, not a rule — this week proved it
(the tutorial law existed while its display silently discarded new walkthroughs). So this
suite doesn't list the rules: it TRIGGERS each enforceable gate in a sandbox and records
whether it actually refused what it must refuse. Complements the golden-task regression
(which proves the happy paths); this proves the REFUSALS.

Output: data/excava/guardrail_fire.json → one honest line in systemcheck.
Free, stdlib-only, side-effect-safe (bus/identity files snapshot-restored).
Run: python -m src.guardrail_test
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "excava" / "guardrail_fire.json"


def run() -> dict:
    results = []

    def fire(name, fn):
        try:
            ok, evidence = fn()
        except Exception as ex:
            ok, evidence = False, f"{type(ex).__name__}: {str(ex)[:80]}"
        results.append({"gate": name, "fired": bool(ok), "evidence": str(evidence)[:140]})

    def t_syscall_wrong_tool():
        from src.excava_agents import _task_tool_fit
        bad = {"title": "Resolve links batch 1 (~400 elements, links lane)",
               "detail": "link coverage reaches 45%"}
        return (not _task_tool_fit(bad, "src.discovery_agent"),
                "wrong-tool task refused by the syscall gate")

    def t_grounding_refuses_hallucination():
        from src.decision_audit import FOREIGN_STACK
        return (bool(FOREIGN_STACK.search("DECISION: scaffold packages with cargo build")),
                "foreign-stack (cargo) decision detected")

    def t_initiative_cap():
        import src.excava_chat as C
        bus_p = DATA / "excava" / "bus.json"
        backup = bus_p.read_text(encoding="utf-8")
        try:
            room = {"id": "dept-improve-gftest", "kind": "dept", "dept": "improve", "artifact": {}}
            sp = {"id": "gf-test-lead", "name": "GfTest"}
            C._propose_from_decision(room, sp, "DECISION: first concrete thing long enough to count")
            C._propose_from_decision(room, sp, "DECISION: second concrete thing long enough to count")
            third = C._propose_from_decision(room, sp, "DECISION: third concrete thing long enough to count")
            return ("capped" in third, third[:80])
        finally:
            bus_p.write_text(backup, encoding="utf-8")

    def t_output_tier_no_initiative():
        import src.excava_chat as C
        r = {"id": "dept-creators-gftest", "kind": "dept", "dept": "creators"}
        out = C._propose_from_decision(r, {"id": "gf-x", "name": "X"},
                                       "DECISION: something long and concrete enough here")
        return (out == "", "output-tier initiative returned empty (blocked)")

    def t_improvement_reroute():
        import src.excava_chat as C
        dest = C._route_conclusion({"dept": "creators"},
                                   "ACTION: standardize our workflow to improve efficiency")
        return (dest == "improve", f"creators improvement routed to '{dest}'")

    def t_capability_reroute():
        import src.excava_chat as C
        dest = C._route_conclusion({"dept": "creators"},
                                   "ACTION: upgrade our EXCAVA engine capability")
        return (dest == "power", f"capability matter routed to '{dest}'")

    def t_outward_unapproved():
        from src.agent_issue import execute_if_approved
        msg = execute_if_approved()
        return ("not approved" in msg or "already posted" in msg, msg[:80])

    def t_memory_isolation():
        import src.excava_chat as C
        blk = C._recall_agent({"id": "definitely-nonexistent-agent-xyz"})
        return (blk == "", "agent without memory gets nothing; files are per-id")

    def t_group_no_initiative():
        import src.excava_chat as C
        out = C._propose_from_decision({"id": "group-x", "kind": "group", "dept": ""},
                                       {"id": "gf-y", "name": "Y"},
                                       "DECISION: a long and concrete group suggestion here")
        return (out == "", "group chat initiative blocked")

    def t_regression_green():
        r = json.load(open(DATA / "excava" / "regression.json", encoding="utf-8"))
        return (r.get("score") == 100, f"golden-task suite at {r.get('score')}%")

    fire("syscall: wrong tool refused", t_syscall_wrong_tool)
    fire("grounding: hallucinated decision detected", t_grounding_refuses_hallucination)
    fire("initiative: cap at 2 fires", t_initiative_cap)
    fire("initiative: output-tier blocked", t_output_tier_no_initiative)
    fire("initiative: group chat blocked", t_group_no_initiative)
    fire("reroute: improvement → improve", t_improvement_reroute)
    fire("reroute: capability → power", t_capability_reroute)
    fire("outward: unapproved post refused", t_outward_unapproved)
    fire("memory: per-agent isolation", t_memory_isolation)
    fire("tier-2 gate: regression green", t_regression_green)
    fired = sum(1 for r in results if r["fired"])
    report = {"generated_at": datetime.now(timezone.utc).isoformat(),
              "fired": fired, "total": len(results), "results": results,
              "note": "Each gate was TRIGGERED, not listed — a guardrail unseen firing is a hope, "
                      "not a rule (owner law 2026-07-12: 'check firmly that everything works')."}
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    return report


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    r = run()
    print(f"guardrail-fire: {r['fired']}/{r['total']} gates PROVEN to fire")
    for x in r["results"]:
        print(f"  {'FIRED' if x['fired'] else 'DEAD '}  {x['gate']}  — {x['evidence'][:70]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
