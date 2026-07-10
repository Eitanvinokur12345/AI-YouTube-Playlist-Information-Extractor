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
        name, kind = spec[0], spec[5] if len(spec) > 5 else ""
        eng = next((e for e in engines.available() if e["name"] == name), None)
        if not eng:
            results.append({"engine": name, "status": "no-key",
                            "note": "no API key in this environment (keys live in CI secrets)"})
            continue
        t0 = time.time()
        try:
            r = engines.complete(GOLDEN, engine=eng, max_tokens=12)
            ms = int((time.time() - t0) * 1000)
            if r.get("ok"):
                valid = "benchmark ok" in (r.get("text") or "").lower()
                results.append({"engine": name, "status": "healthy" if valid else "answering-but-sloppy",
                                "valid": valid, "ms": ms, "model": r.get("model", "")})
            else:
                results.append({"engine": name, "status": "failing", "ms": ms,
                                "note": str(r.get("text") or r.get("error") or "no answer")[:120]})
        except Exception as ex:
            err = str(ex)[:120]
            klass = ("quota-429" if "429" in err else "bad-model-404" if "404" in err
                     else "auth" if "401" in err or "403" in err else "error")
            results.append({"engine": name, "status": klass, "ms": int((time.time() - t0) * 1000),
                            "note": err})
    order = {"healthy": 0, "answering-but-sloppy": 1, "error": 2, "quota-429": 3,
             "failing": 3, "auth": 4, "bad-model-404": 4, "no-key": 5}
    ranking = [r["engine"] for r in sorted(
        results, key=lambda r: (order.get(r["status"], 9), r.get("ms", 99999)))]
    report = {"generated_at": _now(), "experiment": "engine-benchmark (golden-task canary)",
              "golden_prompt": GOLDEN, "results": results, "ranking": ranking,
              "note": "Hourly canary. The chat layer prefers engines by this ranking; "
                      "'no-key' here is normal on a PC — real numbers come from the CI beat."}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
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
