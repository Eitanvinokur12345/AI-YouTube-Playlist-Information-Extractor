"""
src/excava_agents.py — the agent registry + the WORKER CONTRACT.

Phase 0 of EXCAVA_PROGRAM.md. The registry (data/excava/agents.json) declares 3 tiers —
workers, department leads, core — and every agent's scoped tools (guardrail G-7: no scope,
no work). The Worker contract every department obeys:

    claim one task from the bus  →  do bounded mechanical work (≤ max_steps)
    →  COMPLETE with an honest result, or HAND OFF with a full doc (G-4), or FAIL
    →  every decision traced.

Phase-0 workers are ASSESSORS: they read the real data files their department owns and move
tasks with honest, grounded hand-off docs — the heavy lifting still happens in the dedicated
CI lanes. Later phases give workers their own execution muscles; the contract stays the same.
"""
from __future__ import annotations

import glob
import json
from pathlib import Path

from src import excava_bus as bus

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
REGISTRY = DATA / "excava" / "agents.json"


def load_registry() -> dict:
    try:
        return json.load(open(REGISTRY, encoding="utf-8"))
    except Exception:
        return {"departments": {}, "agents": []}


def worker_for(reg: dict, department: str) -> dict | None:
    """The tier-1 agent registered for a department — None means G-7 blocks routing there."""
    for a in reg.get("agents", []):
        if a.get("department") == department and a.get("tier") == 1 and a.get("scoped_tools"):
            return a
    return None


def pick_department(text: str, reg: dict, can_do: dict) -> tuple[str | None, str, list[str]]:
    """Specialization routing: score keyword hits per department, filter gated/uncapable/
    unstaffed ones. Returns (department, why, runners_up) — 'why' + runners-up go to the
    trace so the owner can always see why X was chosen over Y."""
    tl = (text or "").lower()
    scores: dict[str, int] = {}
    for dept, spec in (reg.get("departments") or {}).items():
        hits = sum(1 for kw in spec.get("specialization", []) if kw in tl)
        if hits:
            scores[dept] = hits
    if not scores:
        return None, "no department specialization matched", []
    ranked = sorted(scores, key=lambda d: -scores[d])
    over, reasons = [], []
    for dept in ranked:
        spec = reg["departments"][dept]
        if spec.get("gated"):
            reasons.append(f"{dept} is gated (Phase 3)"); over.append(dept); continue
        cap = spec.get("capability")
        if cap and can_do and not (can_do.get(cap) or {}).get("ok", True):
            reasons.append(f"{dept} lacks resource {cap}"); over.append(dept); continue
        if worker_for(load_registry(), dept) is None:
            reasons.append(f"{dept} has no scoped worker (G-7)"); over.append(dept); continue
        why = f"best specialization match ({scores[dept]} hits)"
        if reasons:
            why += "; skipped: " + "; ".join(reasons)
        return dept, why, [d for d in ranked if d != dept]
    return None, "all matching departments blocked: " + "; ".join(reasons), ranked


def _jload(name, d=None):
    try:
        return json.load(open(DATA / name, encoding="utf-8"))
    except Exception:
        return d if d is not None else {}


# ── Phase-0 department work: honest assessments over the department's REAL data files. ──
# Each returns an action: {"kind": "handoff", "to":..., "doc": {...}} | {"kind": "complete",
# "result":...} | {"kind": "fail", "reason":...}

def _work_links(task: dict) -> dict:
    cov = _jload("coverage_log.json", {})
    latest = cov.get("latest", {})
    pct, linked, total = latest.get("pct", 0), latest.get("linked", 0), latest.get("total", 0)
    delta = cov.get("delta_pct_vs_prev_day", 0)
    return {"kind": "handoff", "to": "memory", "doc": {
        "what_was_done": (f"Link-coverage pass assessed: **{linked}/{total} linked ({pct}%)**, "
                          f"moving {delta:+.2f}%/day against the +{cov.get('target_pct_per_day', 5)}%/day target "
                          f"({'on track' if cov.get('on_track') else 'NOT on track — resolver budget is the lever'}). "
                          "The resolver lane (batch+parallel+fast-engine) keeps running hourly in CI."),
        "artifacts": ["data/coverage_log.json", "data/skills.json", "data/tools.json"],
        "what_remains": (f"{total - linked} items still unlinked. After each resolver batch the semantic index "
                         "must be re-embedded so EXCAVA's recall sees the NEW links, not last week's."),
        "context_for_next": ("Re-embed via src.build_memory (GEMINI key from CI secrets). Only changed items need "
                             "re-embedding. When the index lags the hub, EXCAVA recommends stale/dead items."),
        "done_criteria": "memory confirms index freshness vs the hub; standing goal (100% coverage) continues in CI",
    }}


def _work_memory(task: dict) -> dict:
    idx = _jload("memory_index.json", {})
    vecs = len(idx.get("vectors", {}) or {})
    # the hub universe = what the links dept reports coverage over (hub.json only holds sections)
    items = (_jload("coverage_log.json", {}).get("latest") or {}).get("total", 0)
    lag = (items - vecs) if isinstance(items, int) and items > vecs else 0
    return {"kind": "complete", "result": (
        f"Semantic index: {vecs} vectors (model {idx.get('model', '?')}); hub {items or '?'} items"
        + (f" → {lag} not yet embedded — embed lane (hourly CI) owns the catch-up." if lag
           else " — index fresh enough for recall.")
        + " Pass complete; the standing coverage goal continues in the CI lanes.")}


def _work_transcripts(task: dict) -> dict:
    pending = len(glob.glob(str(DATA / "_pending" / "*.json")))
    lacking = 0
    for f in glob.glob(str(DATA / "processed" / "*.json")):
        try:
            if json.load(open(f, encoding="utf-8")).get("transcript_source") != "transcript":
                lacking += 1
        except Exception:
            continue
    if pending == 0 and lacking:
        return {"kind": "fail", "reason": (f"{lacking} videos lack a real transcript and 0 are re-queued: "
                                           "the drain needs a RESIDENTIAL IP (owner's PC) — cloud is blocked")}
    return {"kind": "handoff", "to": "analysis", "doc": {
        "what_was_done": (f"Residential drain state assessed: **{pending} videos re-queued** in data/_pending/ "
                          f"with recovered/updated records awaiting deep re-analysis; {lacking} still lack a real "
                          "transcript. Today's drain auto-stopped on an IP block (correct behavior — bursting "
                          "escalates the block); the remainder retries next residential session."),
        "artifacts": ["data/_pending/", "data/processed/", "src/backfill_transcripts.py"],
        "what_remains": (f"Deep re-extraction of the {pending} pending records under the anti-boilerplate gate, "
                         f"then draining the remaining {lacking} on future residential sessions (gentle pacing)."),
        "context_for_next": ("bulk_analyze consumes data/_pending hourly. Records carry transcript_source="
                             "'transcript' + caption_complete=true when the caption spans the full video; "
                             "incomplete captions were deliberately left for Whisper."),
    }}


def _work_analysis(task: dict) -> dict:
    pending = len(glob.glob(str(DATA / "_pending" / "*.json")))
    if pending:
        return {"kind": "complete", "result": (
            f"{pending} re-queued records are in data/_pending; the bulk-analyze lane (hourly, free pool) "
            "consumes them — lane is live. Done per criteria: queue owned + lane running; "
            "the queue itself drains across the next beats.")}
    return {"kind": "complete", "result": "data/_pending is empty — nothing awaiting re-analysis."}


def _work_creators(task: dict) -> dict:
    """CREATORS must BUILD, not report. Owner, 2026-08-16: "the creators are still just making
    decisions rather than actually building."

    He was right, and this function was the proof: it read created_by_excava.json, printed how
    many creations already existed, and returned kind='complete'. 115 creators tasks were closed
    that way while the store held exactly ONE creation (2026-07-03). A count of yesterday's work
    is not today's work. The real builder — excava_creators.assemble_packages() — already existed
    and ran in its own lane; the creators WORKER simply never called it (P-Ponytail: the tool was
    there, it just wasn't wired). Now the worker calls it and is judged on the DELTA it produced."""
    def _pkg_count() -> int:
        d = _jload("packages.json", {}) or {}         # assemble_packages() writes HERE, not to
        p = d if isinstance(d, list) else d.get("packages", [])   # created_by_excava.json
        return len(p)

    before = _pkg_count()
    built, err = [], ""
    try:
        from src import excava_creators as creators
        gate = creators._gate_open()
        if gate:            # a closed P5 gate is a BLOCK, never a silent skip stamped done
            return {"kind": "blocked", "needs": f"Eitan's verdict on P5 gate {gate.get('id')}",
                    "result": f"Creators is gated: {str(gate.get('blocks', ''))[:150]} "
                              "— no creation published. Only Eitan lifts this."}
        built = creators.assemble_packages(max_new=1) or []
    except Exception as e:                      # a builder that crashes has not built anything
        err = f"{type(e).__name__}: {e}"[:160]
    after = _pkg_count()
    delta = after - before
    # Judged on the STORE, not on the return value: a builder that returns a list but writes
    # nothing has still built nothing, and that is the exact failure mode this function had.
    if delta > 0:
        names = ", ".join(str(p.get("name", "?")) for p in built[:3]) or f"{delta} new"
        tested = sum(1 for p in built if (p.get("self_test") or {}).get("ok"))
        return {"kind": "complete",
                "result": f"Creators BUILT {delta}: {names} (packages {before}→{after}; "
                          f"{tested}/{len(built)} passed an independent self-test before first "
                          "use, G-12; labeled 'Created by EXCAVA')."}
    # Nothing landed in the store. That is a blocked task, not a completed one.
    return {"kind": "blocked", "needs": "a buildable gap in data/creators_discovery.json"
                                        + (f" (builder errored: {err})" if err else ""),
            "result": f"Creators built NOTHING this turn (packages still {after}); "
                      f"assemble_packages() wrote no package"
                      + (f" — {err}" if err else " — no gap above the quality bar to build from")}


# REAL executors: the cheap, fast, real tool each department actually runs (verified 2026-07-07).
# Running these does ACTUAL work + reports REAL output — the fix for the hollow-plan facade.
# Each department's REAL tool, aligned to the OWNER INTENT CHARTER (data/excava/intent.json).
# The supervisor flags any drift between this and the charter (caught memory/visual/mining drift).
REAL_TOOL = {"security": "src.security_scan", "improve": "src.self_check",
             "memory": "src.build_memory",      # intent: recall/relate/brain graph (not just the hub index)
             "news": "src.trend_watch",
             "mining": "src.discovery_agent",    # intent: DIVERSE sources (GitHub/HN/PH/Reddit), not the playlist
             "visual": "src.collect_designs",    # intent: mine AI DESIGNS (not just warm screenshots)
             "power": "src.power_scan",          # owner 2026-07-11: find capacity WITHOUT a manual key
             "accessibility": "src.accessibility_scan",  # 2026-07-25: WCAG lint over EXCAVA's own shell
             "visualization": "src.liveliness_scan"}  # 2026-07-27: broken-asset/placeholder/empty-data lint over EXCAVA's own shell


EVIDENCE_STATE = "excava/tool_evidence.json"   # _jload resolves names against DATA/, not DATA/excava


def _evidence_seen(dept: str, tail: str) -> dict | None:
    """The task this exact tool output ALREADY closed, or None if this output is new.

    WHY (measured 2026-08-16): 797 of the 892 surviving completions — 89% — were closed by output
    BYTE-IDENTICAL to a completion that came before them. 153 different `improve` tasks all closed
    on the same string: "self-check: 45/50 (mechanical) | 0 new tasks | 0 resolved". Only ~95 of
    1161 recorded completions were ever distinct work.

    The cause is structural: _run_real_tool takes a DEPARTMENT, never the task, so it cannot do the
    task in front of it — it re-runs one dept-wide script and whatever was claimed gets stamped.
    Identical output means the second task learned nothing and changed nothing, so it received no
    work. Evidence may close a task exactly ONCE."""
    import hashlib
    h = hashlib.sha256(tail.encode("utf-8", "replace")).hexdigest()[:16]
    st = _jload(EVIDENCE_STATE, {}) or {}
    prev = (st.get(dept) or {})
    return {"hash": h, "prior": prev} if prev.get("hash") == h else {"hash": h, "prior": None}


def _evidence_record(dept: str, h: str, task_id: str) -> None:
    from datetime import datetime, timezone          # module-level import is inside _syslog only
    st = _jload(EVIDENCE_STATE, {}) or {}
    st[dept] = {"hash": h, "task": task_id,
                "at": datetime.now(timezone.utc).isoformat()}
    p = DATA / EVIDENCE_STATE
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")


def _run_real_tool(dept: str, task: dict | None = None) -> dict | None:
    """Run the department's real tool with a bounded timeout; return its REAL output tail.

    `task` is accepted so the run is TRACEABLE to the task it was meant to serve. It is not yet
    passed INTO the tool — none of the REAL_TOOL scripts take a task argument, which is the deeper
    half of this defect and is recorded as the next carry-over. Tracing it is what makes the
    duplicate-evidence check possible in the meantime."""
    import subprocess
    import sys
    mod = REAL_TOOL.get(dept)
    if not mod:
        return None
    try:
        r = subprocess.run([sys.executable, "-m", mod], cwd=str(ROOT),
                           capture_output=True, text=True, timeout=90)
        lines = [ln for ln in (r.stdout or "").strip().splitlines() if ln.strip()]
        tail = lines[-1][:220] if lines else ((r.stderr or "").strip()[:160] or "(no output)")
        return {"ok": r.returncode == 0 and bool(lines), "tool": mod, "tail": tail,
                "for_task": (task or {}).get("id", "")}
    except subprocess.TimeoutExpired:
        return {"ok": False, "tool": mod, "tail": "timed out (>90s) — heavy lane runs in its own CI"}
    except Exception as e:
        return {"ok": False, "tool": mod, "tail": type(e).__name__}


# Departments that genuinely CANNOT do real work in CI (missing an owner resource). They report an
# HONEST 'BLOCKED — needs you' instead of faking a plan. This tells the owner exactly what he must add.
BLOCKED = {"watch": "video-analysis engine capacity (Gemini free quota is exhausted / needs an owner key)",
           "transcripts": "a residential IP (your PC) — cloud CI is IP-blocked from draining captions"}


# R3-4 SYSCALL LAYER (AIOS's idea; owner-ranked #4): every generic tool run passes ONE gate that
# checks the TASK actually matches what the tool DOES. Root cause it kills: mining "completed"
# 8 'Resolve links batch' checkpoints by running its discovery agent (+0 links, coverage fell) —
# a tool ran, so the supervisor saw "real work", but it was the WRONG tool for the task.
TOOL_DOMAIN = {
    "src.security_scan":  {"secret", "leak", "scan", "security", "malware", "injection", "guard"},
    "src.self_check":     {"self-improvement", "improve", "check", "stack", "review", "optimize"},
    "src.build_memory":   {"memory", "embed", "index", "recall", "vector", "semantic"},
    "src.trend_watch":    {"news", "announce", "release", "trend", "changelog"},
    "src.discovery_agent": {"mine", "mining", "source", "discover", "competitor", "directory", "gather"},
    "src.collect_designs": {"design", "screenshot", "visual", "taste", "arena"},
    "src.power_scan":     {"power", "capability", "engine", "key", "capacity", "upgrade"},
    "src.accessibility_scan": {"accessibility", "a11y", "wcag", "contrast", "keyboard", "screen-reader",
                               "aria", "alt", "label", "reduced-motion"},
    "src.liveliness_scan": {"visualization", "liveliness", "clarity", "visibility", "broken", "stale",
                            "placeholder", "screen", "dashboard-health"},
    # the links LANE is a CI workflow, not a department tool — its vocabulary is foreign to
    # every department tool, so link-resolution tasks can never be "completed" by a wrong tool
    "(links-lane, external)": {"link", "links", "resolve", "coverage", "unlinked"},
}


def _task_tool_fit(task: dict, tool: str) -> bool:
    """True when running `tool` can plausibly serve `task`. Generic department-advancement tasks
    pass; a task whose words clearly belong to a DIFFERENT tool's domain fails the gate.
    Word-boundary matching ('check' must not match inside 'checkpoint')."""
    import re as _re
    words = set(_re.findall(r"[a-z][a-z-]+", (str(task.get("title", "")) + " "
                                              + str(task.get("detail", ""))).lower()))
    dom = TOOL_DOMAIN.get(tool)
    if not dom:
        return True
    if words & dom:
        return True
    foreign = set().union(*TOOL_DOMAIN.values()) - dom
    return len(words & foreign) < 2                      # 2+ foreign-domain words = wrong tool


def _syslog(dept: str, tool: str, task: dict, fit: bool, outcome: str) -> None:
    """The kernel's uniform tool-call trace (data/excava/syscalls.jsonl) — the supervisor can
    audit EVERY tool call the same way, which is the whole point of a syscall layer."""
    import json as _j
    from datetime import datetime, timezone
    p = DATA / "excava" / "syscalls.jsonl"
    with open(p, "a", encoding="utf-8") as fh:
        fh.write(_j.dumps({"at": datetime.now(timezone.utc).isoformat(), "dept": dept,
                           "tool": tool, "task": task.get("id", ""), "fit": fit,
                           "outcome": outcome}, ensure_ascii=False) + "\n")


def _work_generic(task: dict) -> dict:
    """Do REAL work when the department has a runnable tool (run it, report real output). If the
    department is truly BLOCKED (needs an owner resource) say so honestly. Otherwise produce an HONEST
    execution PLAN labelled 'not yet executed' — never a false 'DONE'."""
    import re
    tid = task.get("id", "task")
    dept = task.get("department", "core")
    if dept in BLOCKED and dept not in REAL_TOOL:        # honest 'can't' — and NOT a completion
        # 2026-08-16 owner audit: this used to return kind='complete', so tick() stamped 153
        # "I cannot do this" admissions as status='done'. An admission is not a completion.
        return {"kind": "blocked", "needs": BLOCKED[dept],
                "result": f"BLOCKED — {dept} needs {BLOCKED[dept]}. No fake work done; waiting on the owner."}
    tool = REAL_TOOL.get(dept, "")
    if tool and not _task_tool_fit(task, tool):          # SYSCALL GATE: refuse the wrong tool
        _syslog(dept, tool, task, False, "refused-mismatch")
        return {"kind": "fail",
                "reason": f"SYSCALL MISMATCH — this task asks for work outside what {dept}'s tool "
                          f"({tool}) does; refusing to run the wrong tool and stamp it done. "
                          "Escalate to the right lane or the owner."}
    real = _run_real_tool(dept, task)                    # FIRST: try to actually DO the work
    if real and real["ok"]:
        friendly = real["tool"].split(".")[-1].replace("_", " ")   # 'src.self_check' -> 'self check'
        ev = _evidence_seen(dept, real["tail"])
        if ev["prior"]:      # this exact output already closed another task — it cannot close two
            _syslog(dept, real["tool"], task, True, "refused-duplicate-evidence")
            return {"kind": "blocked",
                    "needs": f"a task-specific executor for {dept} "
                             f"({real['tool']} takes no task and re-ran identically)",
                    "result": f"Ran the {friendly}, but its output is BYTE-IDENTICAL to the run "
                              f"that closed {ev['prior'].get('task', 'an earlier task')} — nothing "
                              f"new was learned or changed, so this task got no work. Evidence: "
                              f"{real['tail'][:120]}"}
        _syslog(dept, real["tool"], task, True, "ran-ok")
        _evidence_record(dept, ev["hash"], task.get("id", ""))
        return {"kind": "complete", "evidence": ev["hash"],
                "result": f"Ran the {friendly}. {real['tail']}"}
    slug = re.sub(r"[^a-z0-9]+", "-", str(task.get("title", tid)).lower())[:48].strip("-") or tid
    body, src = "", "task-summary (no engine)"
    try:
        from src import excava_engines as engines
        reg = load_registry()
        lead = next((a for a in reg.get("agents", []) if a.get("department") == dept and a.get("role") == "lead"), {})
        prompt = (f"You are {lead.get('name', dept + ' lead')} ({str(lead.get('persona', ''))[:120]}).\n"
                  f"TASK: {task.get('title', '')}\nCONTEXT: {str(task.get('detail', ''))[:300]}\n\n"
                  "Write an EXECUTION PLAN in GitHub markdown ONLY — the concrete steps to ACTUALLY do "
                  "this (real files/tools/commands). Do NOT claim it is already done; this is a plan to "
                  "be executed. One-line '**Approach:**', a numbered '**Steps:**' (3-5), '**Needs:**' "
                  "(the real tool/data/access required). No preamble, no invented repos or metrics.")
        r = engines.complete(prompt, dept=dept, difficulty="normal", max_tokens=360)
        if r.get("ok") and (r.get("text") or "").strip():
            body, src = r["text"].strip(), f"{r['engine']}/{r['model']}"
    except Exception:
        pass
    if not body:
        body = (f"**Approach:** {task.get('title', '')}\n\n**Steps:**\n"
                f"1. {str(task.get('detail', '')) or 'assess the gap'}\n2. Run the real tool for this domain\n"
                "3. Verify the gap actually closed\n\n**Needs:** a real executor wired for this department.")
    adir = DATA / "excava" / "artifacts"
    adir.mkdir(parents=True, exist_ok=True)
    path = adir / f"task-{slug}.md"
    path.write_text(f"# {task.get('title', 'task')}\n\n> {dept} · task `{tid}` · **EXECUTION PLAN — NOT yet "
                    f"executed** · by {src}\n\n{body}\n", encoding="utf-8")
    # HONEST: the planning turn produced a PLAN, not executed work. Until 2026-08-16 this returned
    # kind='complete' and the planned_only flag was computed and then thrown away — so a plan closed
    # the task and nothing ever retried it. A plan is a blocked task with homework attached.
    return {"kind": "blocked", "planned_only": True,
            "needs": f"a wired {dept} executor",
            "result": f"EXECUTION PLAN written (NOT executed) → data/excava/artifacts/{path.name}; "
                      f"real execution still needs a wired {dept} tool"}


WORK: dict = {"links": _work_links, "memory": _work_memory,
              "transcripts": _work_transcripts, "analysis": _work_analysis,
              "creators": _work_creators}


def roster(reg: dict | None = None) -> str:
    """M2.3 done-criterion: print the named cast with engines+roles+personas."""
    reg = reg or load_registry()
    lines = []
    for a in reg.get("agents", []):
        if a.get("tier") == 3:
            continue
        lines.append(f"{a.get('name', '?'):<9} {a['id']:<22} {a.get('role', '?'):<9} "
                     f"engine:{a.get('engine_pref', '-'):<10} {'👔' if a.get('suit') else '  '} "
                     f"{str(a.get('persona', ''))[:70]}")
    return "\n".join(lines)


def evidence_report() -> str:
    """VISIBLE: how many completions were closed by evidence already used on an earlier task.

    This is the number the duplicate-evidence rule exists to drive down. It reads history, so it
    keeps scoring the completions recorded BEFORE the rule existed — the backlog is not rewritten
    (only the 269 outright false completions were, on 2026-08-16); these are merely counted, so the
    line moves only as new, genuinely distinct work lands."""
    import collections
    try:
        b = json.loads((DATA / "excava" / "bus.json").read_text(encoding="utf-8"))
    except Exception:
        return "evidence: no bus to inspect"
    done = [t for t in b.get("tasks", []) if t.get("status") == "done"]
    per = collections.defaultdict(collections.Counter)
    for t in done:
        per[t.get("department") or "(none)"][str(t.get("result", ""))] += 1
    rows, dup_total = [], 0
    for d, c in sorted(per.items()):
        dup = sum(n - 1 for n in c.values() if n > 1)
        dup_total += dup
        if dup:
            rows.append(f"  {d:<14} {sum(c.values()):>4} done · {dup:>4} closed on REUSED evidence "
                        f"({round(100 * dup / max(sum(c.values()), 1))}%)")
    n = len(done)
    distinct = n - dup_total
    head = (f"COMPLETION EVIDENCE — {distinct} of {n} completions ({round(100 * distinct / max(n, 1))}%) "
            f"are backed by output no earlier task already used.")
    return "\n".join([head, ""] + rows + ["",
            f"  {dup_total} reused-evidence closes remain in history (counted, never rewritten).",
            "  Going forward tick() refuses them: identical output closes exactly ONE task."])


def tick(department: str, reg: dict) -> tuple[str, str] | None:
    """One Worker-contract turn for a department: claim → work → complete/handoff/fail.
    Returns (one-line summary, outcome) for the beat log + usage accounting, or None."""
    agent = worker_for(reg, department)
    if agent is None:                       # no scoped worker => G-7 blocks (notify, not freeze)
        return None
    task = bus.claim(agent["id"], department)
    if task is None:
        return None
    act = WORK.get(department, _work_generic)(task)   # every dept executes; generic = real artifact
    if act["kind"] == "handoff":
        ok, ref = bus.handoff(task["id"], agent["id"], act["to"], act["doc"])
        return ((f"{agent['id']}: {task['id']} -> {act['to']} ({ref})", "handoffs") if ok
                else (f"{agent['id']}: {task['id']} {ref}", "fails"))
    if act["kind"] == "blocked":        # honest third outcome — never counted as a completion
        bus.block(task["id"], agent["id"], act.get("needs", "an owner resource"), act.get("result", ""))
        return f"{agent['id']}: {task['id']} BLOCKED ({act.get('needs', '?')})", "blocked"
    if act["kind"] == "complete":
        bus.complete(task["id"], agent["id"], act["result"])
        return f"{agent['id']}: {task['id']} DONE", "done"
    msg = bus.fail(task["id"], agent["id"], act.get("reason", "failed"))
    return f"{agent['id']}: {task['id']} {msg}", "fails"


if __name__ == "__main__":          # python -m src.excava_agents --roster
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    if "--evidence" in sys.argv:
        print(evidence_report())
    elif "--roster" in sys.argv:
        print(roster())
    else:
        reg = load_registry()
        print(f"{len(reg.get('agents', []))} agents registered; use --roster for the cast")
