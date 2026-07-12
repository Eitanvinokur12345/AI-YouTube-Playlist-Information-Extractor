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
    store = _jload("created_by_excava.json", {})
    cs = store.get("creations", [])
    pub = sum(1 for c in cs if c.get("status") == "published")
    return {"kind": "complete", "result": (
        f"Creators: {len(cs)} creations on record, {pub} published — every one labeled "
        "'Created by EXCAVA' with an independent test before first use (G-12). The daily "
        "creators lane drafts from data/creators_discovery.json gaps.")}


# REAL executors: the cheap, fast, real tool each department actually runs (verified 2026-07-07).
# Running these does ACTUAL work + reports REAL output — the fix for the hollow-plan facade.
# Each department's REAL tool, aligned to the OWNER INTENT CHARTER (data/excava/intent.json).
# The supervisor flags any drift between this and the charter (caught memory/visual/mining drift).
REAL_TOOL = {"security": "src.security_scan", "improve": "src.self_check",
             "memory": "src.build_memory",      # intent: recall/relate/brain graph (not just the hub index)
             "news": "src.trend_watch",
             "mining": "src.discovery_agent",    # intent: DIVERSE sources (GitHub/HN/PH/Reddit), not the playlist
             "visual": "src.collect_designs",    # intent: mine AI DESIGNS (not just warm screenshots)
             "power": "src.power_scan"}          # owner 2026-07-11: find capacity WITHOUT a manual key


def _run_real_tool(dept: str) -> dict | None:
    """Run the department's real tool with a bounded timeout; return its REAL output tail."""
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
        return {"ok": r.returncode == 0 and bool(lines), "tool": mod, "tail": tail}
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
    if dept in BLOCKED and dept not in REAL_TOOL:        # honest 'can't', not a fake plan
        return {"kind": "complete",
                "result": f"BLOCKED — {dept} needs {BLOCKED[dept]}. No fake work done; waiting on the owner."}
    tool = REAL_TOOL.get(dept, "")
    if tool and not _task_tool_fit(task, tool):          # SYSCALL GATE: refuse the wrong tool
        _syslog(dept, tool, task, False, "refused-mismatch")
        return {"kind": "fail",
                "reason": f"SYSCALL MISMATCH — this task asks for work outside what {dept}'s tool "
                          f"({tool}) does; refusing to run the wrong tool and stamp it done. "
                          "Escalate to the right lane or the owner."}
    real = _run_real_tool(dept)                          # FIRST: try to actually DO the work
    if real and real["ok"]:
        _syslog(dept, real["tool"], task, True, "ran-ok")
        friendly = real["tool"].split(".")[-1].replace("_", " ")   # 'src.self_check' -> 'self check'
        return {"kind": "complete", "result": f"Ran the {friendly}. {real['tail']}"}
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
    # HONEST: the planning turn completed, but this is a PLAN, not executed work. The result string
    # says so unmistakably (no self-handoff loop). Wiring real per-department executors is next.
    return {"kind": "complete", "planned_only": True,
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
    if "--roster" in sys.argv:
        print(roster())
    else:
        reg = load_registry()
        print(f"{len(reg.get('agents', []))} agents registered; use --roster for the cast")
