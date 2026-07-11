"""
src/excava_experiments.py — SI step 2 (owner 2026-07-10): PROFESSIONAL EXPERIMENTS the
self-improvement department runs ON EXCAVA ITSELF. First experiment: ENGINE BENCHMARK.

Why this first: the proven bottleneck is engine quota (rooms stalled 5.5h on 2026-07-10 with
every free engine 429'd). A benchmark turns "engines feel dead" into data — and the chat layer
uses the ranking to prefer healthy engines, so the experiment IMPROVES the system, not just
measures it (owner law: captured != built != used).

Method (golden-task canary, the professional standard for API health):
  one tiny fixed prompt per engine, every ~hour (not per-beat — that would eat the very quota
  it measures). Records latency, validity (did it follow the instruction), and the error class
  (429 quota / 404 bad-model / auth). Engines without a key here are recorded honestly as
  "no-key" (keys live in CI secrets).

Output: data/excava/engine_health.json — {results per engine, ranking} — read by
excava_engines (prefer healthy) and the dashboard (honest engine panel).
Free, stdlib-only. Run: python -m src.excava_experiments [--force]
"""
from __future__ import annotations

import json
import time
from datetime import datetime, timezone
from pathlib import Path

from src import excava_engines as engines

ROOT = Path(__file__).parent.parent
OUT = ROOT / "data" / "excava" / "engine_health.json"
GOLDEN = "Reply with exactly these two words and nothing else: benchmark ok"
FRESH_S = 55 * 60          # re-run at most hourly; the beat calls this every cycle


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _stale() -> bool:
    try:
        prev = json.load(open(OUT, encoding="utf-8"))
        # a report with zero healthy engines must NOT block a re-run in a place that HAS keys
        # (e.g. the owner's PC wrote all-no-key, then CI — with keys — inherits it via git)
        if not any(r.get("status") == "healthy" for r in prev.get("results", [])) \
                and engines.available():
            return True
        age = (datetime.now(timezone.utc)
               - datetime.fromisoformat(prev["generated_at"])).total_seconds()
        return age > FRESH_S
    except Exception:
        return True


#  THE EXPERIMENT ROSTER (owner 2026-07-10: 'professional experiments… think a lot about what
#  to do'). Honest statuses — 'live' means running now; 'next' means designed, not yet built.
ROSTER = [
    {"id": "engine-benchmark", "status": "live",
     "what": "Hourly golden-task canary over every free engine; agents prefer the healthy ones.",
     "method": "canary testing (the standard for API health)"},
    {"id": "hub-self-use", "status": "live",
     "what": "When something blocks EXCAVA, it searches its OWN 6.8k-element hub for a tool that "
             "solves it and attaches the candidates to the pitch.",
     "method": "retrieval-augmented self-repair"},
    {"id": "agent-staffing", "status": "live",
     "what": "Departments missing a lead/doer/checker get the missing role added automatically "
             "(tier 2.5 autonomy, labeled 'Added by EXCAVA').",
     "method": "structural invariant enforcement"},
    {"id": "formation-ab", "status": "next",
     "what": "Run the same goal with two team shapes (e.g. 2 vs 5 agents, debate vs solo) and an "
             "independent judge picks the better artifact; the winner becomes the default.",
     "method": "A/B testing with blind judging"},
    {"id": "huge-task-splitting", "status": "next",
     "what": "Take one huge goal, decompose into small verified steps, execute step-by-step with "
             "a checkpoint after each — the skill EXCAVA needs for big jobs.",
     "method": "hierarchical decomposition with checkpoints"},
    {"id": "golden-task-regression", "status": "next",
     "what": "A fixed suite of tasks EXCAVA once did well, re-run after every self-change; any "
             "score drop auto-reverts the change (tier-2 self-code gate).",
     "method": "regression testing (how real software ships safely)"},
]


def write_roster() -> None:
    p = ROOT / "data" / "excava" / "experiments.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    roster = [dict(x) for x in ROSTER]
    try:                                              # flip golden-task-regression to live + show score
        reg = json.load(open(ROOT / "data" / "excava" / "regression.json", encoding="utf-8"))
        for x in roster:
            if x["id"] == "golden-task-regression":
                x["status"] = "live"
                x["what"] += f" Latest score: {reg.get('score')}% ({reg.get('passed')}/{reg.get('total')} tasks)."
    except Exception:
        pass
    try:                                              # flip huge-task-splitting to live + progress
        ht = json.load(open(HT_OUT, encoding="utf-8"))
        for x in roster:
            if x["id"] == "huge-task-splitting":
                x["status"] = "live"
                done = sum(1 for s in ht.get("steps", []) if s.get("status") == "done")
                x["what"] += f" Walking: '{ht.get('goal', '')[:60]}' — {done}/{len(ht.get('steps', []))} checkpoints done."
    except Exception:
        pass
    try:                                              # flip formation-ab to live + show the tally
        ab = json.load(open(AB_OUT, encoding="utf-8"))
        for x in roster:
            if x["id"] == "formation-ab":
                x["status"] = "live"
                w = ab.get("wins", {})
                x["what"] += (f" Tally: debate {w.get('debate', 0)} — solo {w.get('solo', 0)}; "
                              f"latest winner: {ab.get('winner_today') or 'no verdict'}.")
    except Exception:
        pass
    p.write_text(json.dumps({"generated_at": _now(), "experiments": roster,
                             "autonomy": "see data/excava/autonomy.json (owner-agreed tiers)"},
                            ensure_ascii=False, indent=1), encoding="utf-8")


REG_OUT = ROOT / "data" / "excava" / "regression.json"


def run_regression(force: bool = False) -> dict | None:
    """SI-4a GOLDEN-TASK REGRESSION (gates tier-2 self-code): six fixed, engine-free tasks EXCAVA
    must always do correctly. Runs hourly in the beat; a self-code change that drops the score
    must be reverted (the autonomy.json tier-2 rule, now enforceable with real numbers).
    Side-effect-safe: file-writing subsystems run against sandbox copies."""
    if not force:
        try:
            prev = json.load(open(REG_OUT, encoding="utf-8"))
            age = (datetime.now(timezone.utc)
                   - datetime.fromisoformat(prev["generated_at"])).total_seconds()
            if age < FRESH_S:
                return None
        except Exception:
            pass
    import shutil, tempfile
    results = []

    def task(name, fn):
        try:
            ok, note = fn()
        except Exception as ex:
            ok, note = False, f"{type(ex).__name__}: {str(ex)[:80]}"
        results.append({"task": name, "ok": bool(ok), "note": str(note)[:120]})

    def t_hub_candidates():
        from src.excava_selfimprove import _hub_candidates
        c = _hub_candidates(["transcript"])
        return bool(c) and all(x.get("id") and x.get("name") for x in c), f"{len(c)} candidates"

    def t_pitch_v2_fields():
        from src.excava_selfimprove import _gen_pitches
        ps = _gen_pitches(set())
        need = ("requested_by", "need", "importance", "missing", "owner_what")
        ok = bool(ps) and all(all(k in p for k in need) for p in ps)
        return ok, f"{len(ps)} pitches, v2 fields present"

    def t_pitch_survival():
        from src import excava
        raw = (ROOT / "data" / "excava_approvals.json").read_text(encoding="utf-8")
        try:
            res = excava._approvals_sync([], "run")
            want = {p.get("id") for p in json.load(open(ROOT / "data/excava/pitches.json",
                    encoding="utf-8")).get("pitches", []) if p.get("status") == "pending"}
            got = {p.get("id") for p in res.get("pending", [])}
            missing = want - got - set(res.get("granted", [])) - set(res.get("declined", []))
            return not missing, f"{len(want)} pitches, {len(missing)} lost"
        finally:                                       # never mutate the real queue from a test
            (ROOT / "data" / "excava_approvals.json").write_text(raw, encoding="utf-8")

    def t_package_assembly():
        from src import excava_creators as cr
        tmp = Path(tempfile.mkdtemp())
        shutil.copy(ROOT / "data" / "elements_index.json", tmp / "elements_index.json")
        (tmp / "packages.json").write_text('{"packages": []}', encoding="utf-8")
        old = cr.DATA
        try:
            cr.DATA = tmp                              # sandbox: never touches real packages.json
            made = cr.assemble_packages(max_new=1)
            ok = bool(made) and len(made[0].get("elements", [])) >= 3
            return ok, f"assembled {len(made)} kit(s) in sandbox"
        finally:
            cr.DATA = old

    def t_bus_invariants():
        from src import excava_bus as bus
        b = bus.read_bus()
        bad = [t["id"] for t in b.get("tasks", [])
               if t.get("status") == "working" and not t.get("claimed_by")]
        return not bad and all(t.get("id") and t.get("status") for t in b.get("tasks", [])), \
            f"{len(b.get('tasks', []))} tasks, {len(bad)} working-unclaimed"

    def t_stable_ids():
        from src.excava import _hold_id
        a, b = _hold_id("Some Held Priority"), _hold_id("Some Held Priority")
        return a == b and a.startswith("hold-"), a

    task("hub-candidates", t_hub_candidates)
    task("pitch-v2-fields", t_pitch_v2_fields)
    task("pitch-survival-in-approvals", t_pitch_survival)
    task("package-assembly-sandbox", t_package_assembly)
    task("bus-invariants", t_bus_invariants)
    task("stable-hold-ids", t_stable_ids)
    passed = sum(1 for r in results if r["ok"])
    report = {"generated_at": _now(), "experiment": "golden-task-regression",
              "passed": passed, "total": len(results),
              "score": round(100 * passed / len(results)),
              "results": results,
              "note": "Six fixed engine-free tasks. A self-code change that drops this score gets "
                      "auto-reverted (autonomy tier-2 rule)."}
    REG_OUT.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    write_roster()                                     # flip the roster entry to live with the score
    return report


def benchmark_engines(force: bool = False) -> dict | None:
    """One golden-task pass over every catalog engine. Returns the report (or None if fresh)."""
    write_roster()                                     # keep the experiment roster visible in-app
    if not force and not _stale():
        return None
    results = []
    for spec in engines.CATALOG:
        name = spec[0]
        eng = next((e for e in engines.available() if e["name"] == name), None)
        if not eng:
            results.append({"engine": name, "status": "no-key",
                            "note": "no API key in this environment (keys live in CI secrets)"})
            continue
        # ISOLATION: call THIS engine directly — no fallthrough, so a survivor can't be credited
        # to a dead engine (the canary used to mislabel). _call_one carries the real HTTP status.
        r = engines._call_one(eng, GOLDEN, max_tokens=12)
        if r["ok"]:
            valid = "benchmark ok" in r["text"].lower()
            results.append({"engine": name, "status": "healthy" if valid else "answering-but-sloppy",
                            "valid": valid, "ms": r["ms"], "model": eng["model"]})
        else:
            # status label = the real reason (quota-429 / bad-model-404 / bad-key-401 / timeout…)
            label = (r["note"].split(":")[0].strip() or "failing") if r["note"] else "failing"
            results.append({"engine": name, "status": label, "ms": r["ms"],
                            "model": eng["model"], "note": r["note"]})
    order = {"healthy": 0, "answering-but-sloppy": 1}
    ranking = [r["engine"] for r in sorted(
        results, key=lambda r: (order.get(r["status"], 9), r.get("ms", 99999)))]
    report = {"generated_at": _now(), "experiment": "engine-benchmark (golden-task canary)",
              "golden_prompt": GOLDEN, "results": results, "ranking": ranking,
              "note": "Hourly canary. The chat layer prefers engines by this ranking; "
                      "'no-key' here is normal on a PC — real numbers come from the CI beat."}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    return report


HT_OUT = ROOT / "data" / "excava" / "huge_task.json"


def run_huge_task_split(force: bool = False) -> dict | None:
    """SI-4c HUGE-TASK SPLITTING (hierarchical decomposition with checkpoints): take the biggest
    real goal — G3 link coverage (thousands of unlinked elements) — and turn it into small bus
    tasks, each with a done-criterion and a VERIFY step, so a huge job becomes checkpoints the
    OS can actually walk. Step 1 (measure) executes immediately; batch steps are consumed by the
    existing links lane; the final step re-verifies the goal number. Idempotent + daily cap."""
    try:
        prev = json.load(open(HT_OUT, encoding="utf-8"))
        age = (datetime.now(timezone.utc)
               - datetime.fromisoformat(prev["generated_at"])).total_seconds()
        if not force and age < 22 * 3600:
            return None
    except Exception:
        pass
    from src import excava_bus as bus
    els = json.load(open(ROOT / "data" / "elements_index.json", encoding="utf-8")).get("elements", [])
    unlinked = sum(1 for e in els if not ((e.get("links") or {}).get("website")
                                          or (e.get("links") or {}).get("github")))
    total = len(els)
    goal = f"Close the link gap: {unlinked} of {total} elements have no verified link (G3)"
    steps = [{"n": 1, "title": f"Measure the gap: {unlinked}/{total} unlinked",
              "done_criterion": "the number is measured and recorded", "status": "done",
              "result": f"{unlinked} unlinked of {total} ({round(100 * unlinked / max(total, 1))}%)"}]
    batch = 400
    for i in range(4):                                   # 4 checkpointed batches ≈ 1600 elements
        steps.append({"n": i + 2,
                      "title": f"Resolve links batch {i + 1} (~{batch} elements, links lane)",
                      "done_criterion": f"unlinked count drops below {unlinked - batch * (i + 1)}",
                      "verify": "recount unlinked in elements_index.json", "status": "queued"})
    steps.append({"n": 6, "title": "Re-verify G3: coverage pct + goal score moved",
                  "done_criterion": "G3 score in goals_status.json rises", "status": "queued"})
    enq = 0
    for s in steps:
        if s["status"] != "queued":
            continue
        t = bus.enqueue(s["title"], detail=f"Huge-task checkpoint {s['n']}/6 of: {goal}",
                        department="mining", source="huge-task-split", priority=1,
                        done_criteria=s["done_criterion"])
        if t:
            s["bus_id"] = t["id"]
            enq += 1
    report = {"generated_at": _now(), "experiment": "huge-task-splitting",
              "goal": goal, "steps": steps, "enqueued_now": enq,
              "note": "A huge goal walked as small verified checkpoints on the bus — "
                      "step 1 executed immediately; batches feed the existing links lane."}
    HT_OUT.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    write_roster()
    return report


AB_OUT = ROOT / "data" / "excava" / "formation_ab.json"
AB_GOAL = ("Name the single most valuable improvement EXCAVA could make to how it presents "
           "results to its owner, and say concretely what to change.")


def run_formation_ab(force: bool = False, _complete=None) -> dict | None:
    """SI-4b FORMATION A/B (blind judging): the same goal answered by two team shapes —
    A) SOLO: one doer answers directly (1 call).
    B) DEBATE: doer proposes → checker attacks → doer revises (3 calls).
    A judge on a DIFFERENT engine sees both artifacts in random order WITHOUT knowing which
    formation made them, and picks the better one. Wins accumulate; at 3 net wins the winner
    becomes the default room depth (formation_policy.json → open_room max_turns), so the
    experiment IMPROVES the system, not just measures it. Daily cap. CI-only (needs engines)."""
    prev = {}
    try:
        prev = json.load(open(AB_OUT, encoding="utf-8"))
        age = (datetime.now(timezone.utc)
               - datetime.fromisoformat(prev["generated_at"])).total_seconds()
        if not force and age < 22 * 3600:
            return None
    except Exception:
        pass
    comp = _complete or engines.complete
    pool = engines.healthy()
    if len(pool) < 2:
        return None                                     # honest: needs >=2 live engines (CI)
    import random
    a = comp(f"You are a capable solo agent. {AB_GOAL} Answer in 4-6 sentences.",
             engine=pool[0], max_tokens=280)
    prop = comp(f"You are the proposer in a two-agent debate. {AB_GOAL} Propose in 3-4 sentences.",
                engine=pool[0], max_tokens=220)
    crit = comp("You are the challenger. Attack this proposal's weakest point in 2 sentences:\n"
                + (prop.get("text") or ""), engine=pool[1 % len(pool)], max_tokens=120)
    b = comp("Revise your proposal to survive this attack. Final answer in 4-6 sentences.\n"
             f"PROPOSAL: {prop.get('text', '')}\nATTACK: {crit.get('text', '')}",
             engine=pool[0], max_tokens=280)
    if not (a.get("ok") and b.get("ok")):
        return None
    arts = [("solo", a["text"]), ("debate", b["text"])]
    random.shuffle(arts)                                # BLIND: judge can't infer from order
    judge_eng = pool[-1] if len(pool) > 2 else pool[1 % len(pool)]
    j = comp("You are an impartial judge. Two anonymous teams answered the same question. "
             "Reply with exactly 'ARTIFACT 1' or 'ARTIFACT 2' then one sentence why the winner "
             f"is more concrete and actionable.\nARTIFACT 1:\n{arts[0][1]}\n\nARTIFACT 2:\n{arts[1][1]}",
             engine=judge_eng, max_tokens=90)
    txt = (j.get("text") or "").upper()
    winner = arts[0][0] if "ARTIFACT 1" in txt else arts[1][0] if "ARTIFACT 2" in txt else None
    wins = prev.get("wins", {"solo": 0, "debate": 0})
    if winner:
        wins[winner] += 1
    report = {"generated_at": _now(), "experiment": "formation-ab (blind judging)",
              "goal": AB_GOAL, "winner_today": winner, "wins": wins,
              "judge": {"engine": judge_eng["name"], "said": (j.get("text") or "")[:200]},
              "artifacts": {k: v[:400] for k, v in arts},
              "engines_used": [pool[0]["name"], pool[1 % len(pool)]["name"], judge_eng["name"]]}
    AB_OUT.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    if winner and wins[winner] - wins["solo" if winner == "debate" else "debate"] >= 3:
        (ROOT / "data" / "excava" / "formation_policy.json").write_text(json.dumps(
            {"default_formation": winner, "room_max_turns": 8 if winner == "debate" else 4,
             "decided_by": "formation-ab, 3 net wins", "at": _now()}, indent=1), encoding="utf-8")
    return report


def main() -> int:
    import argparse, sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    r = benchmark_engines(force=ap.parse_args().force)
    if not r:
        print("engine benchmark: fresh (<55min) — skipped")
    else:
        for x in r["results"]:
            print(f"  {x['engine']:<12} {x['status']:<20} {x.get('ms','')}ms  {x.get('note','')[:60]}")
        print("ranking:", ", ".join(r["ranking"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
