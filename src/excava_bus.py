"""
src/excava_bus.py — THE FILE BUS: the hand-off layer that makes EXCAVA an OS, not a tab pile.

Phase 0 of EXCAVA_PROGRAM.md. Goldbach's rule: without a hand-off layer between agents you
don't have an OS — and the biggest mistake is skipping shared memory. This bus is both:
  - hand-off layer:  enqueue → claim → (handoff | complete | fail) with a VALIDATED hand-off
    doc on every pass between departments (no doc, no hand-off — guardrail G-4);
  - shared memory (write side): agents write facts to data/excava/state.json through
    remember(); the read side stays the semantic index (data/memory_index.json).

Everything is plain JSON on disk (data/excava/), committed by CI, so the cron heartbeat
(D1: GitHub Actions cycles hourly) resumes exactly where the last beat stopped. Every task
has a trace (data/excava/traces/<id>.jsonl) recording WHY each decision happened — the
Phase-5 trace viewer reads these. Free, mechanical, no Claude tokens, never raises out of
a beat (the cron must not break).

Not a daemon: one beat touches the bus, writes atomically (tmp+rename), exits.
"""
from __future__ import annotations

import json
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
EXDIR = ROOT / "data" / "excava"
BUS = EXDIR / "bus.json"
STATE = EXDIR / "state.json"
HANDOFFS = EXDIR / "handoffs"
TRACES = EXDIR / "traces"

# G-4: a hand-off without ALL of these (non-empty) is REJECTED. This is the gate that keeps
# context flowing between departments instead of evaporating between cron beats.
REQUIRED_HANDOFF_FIELDS = ("what_was_done", "artifacts", "what_remains", "context_for_next")

MAX_STEPS_DEFAULT = 8          # G-5: nothing loops silently
ESCALATE_TO_OWNER_AT = 3       # G-6: tier 3 exhausted -> held for the owner


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _slug(s: str, n: int = 24) -> str:
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")[:n] or "task"


def _atomic_write(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + f".tmp{os.getpid()}")
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(tmp, path)


def _read(path: Path, default):
    try:
        return json.load(open(path, encoding="utf-8"))
    except Exception:
        return default


def read_bus() -> dict:
    bus = _read(BUS, {"version": 1, "tasks": []})
    bus.setdefault("tasks", [])
    return bus


def _write_bus(bus: dict) -> None:
    bus["updated_at"] = _now()
    _atomic_write(BUS, bus)


def event(task_id: str, kind: str, data: dict | None = None) -> None:
    """Append one trace event. Traces answer 'why X over Y' — never deleted, one file per task."""
    TRACES.mkdir(parents=True, exist_ok=True)
    rec = {"at": _now(), "kind": kind, **(data or {})}
    with open(TRACES / f"{task_id}.jsonl", "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def enqueue(title: str, detail: str = "", department: str = "", source: str = "auto",
            priority: int = 1, done_criteria: str = "", max_steps: int = MAX_STEPS_DEFAULT) -> dict | None:
    """Add a task (priority 0 = owner, 1 = auto, 2 = agent-spawned). Dedupes on open same-title.
    done_criteria is REQUIRED thinking, not decoration: default is honest ('output committed')."""
    bus = read_bus()
    for t in bus["tasks"]:
        if t.get("title") == title and t.get("status") in ("queued", "working"):
            return None                       # already on the bus — the beat resumes it
    tid = f"{_slug(title)}-{int(time.time()) % 100000}"
    task = {
        "id": tid, "title": title, "detail": detail, "department": department,
        "source": source, "priority": priority, "status": "queued",
        "steps": 0, "max_steps": max_steps,
        "done_criteria": done_criteria or "output written to data/ and committed by CI",
        "escalation_tier": 1, "claimed_by": None, "handoff_docs": [],
        "created_at": _now(), "updated_at": _now(),
    }
    bus["tasks"].append(task)
    _write_bus(bus)
    event(tid, "enqueued", {"title": title, "source": source, "priority": priority,
                            "department": department or "(unrouted)"})
    return task


def route(task_id: str, department: str, why: str, over: list[str] | None = None) -> bool:
    """Core assigns a department. 'why' + 'over' land in the trace (Phase-5 trace viewer)."""
    bus = read_bus()
    for t in bus["tasks"]:
        if t["id"] == task_id and t["status"] == "queued":
            t["department"], t["updated_at"] = department, _now()
            _write_bus(bus)
            event(task_id, "routed", {"chose": department, "over": over or [], "why": why})
            return True
    return False


def claim(agent_id: str, department: str) -> dict | None:
    """A worker claims the highest-priority queued task of its department. Owner tasks first (G-8)."""
    bus = read_bus()
    todo = [t for t in bus["tasks"] if t["status"] == "queued" and t.get("department") == department]
    if not todo:
        return None
    todo.sort(key=lambda t: (t.get("priority", 1), t.get("created_at", "")))
    t = todo[0]
    t.update(status="working", claimed_by=agent_id, updated_at=_now())
    _write_bus(bus)
    event(t["id"], "claimed", {"by": agent_id, "department": department})
    return t


def handoff(task_id: str, from_agent: str, to_department: str, doc: dict) -> tuple[bool, str]:
    """Pass a task to another department WITH a real hand-off doc. G-4: the bus validates the
    doc and REJECTS the hand-off if any required field is missing/empty — the task stays with
    the sender, and the rejection is traced. Returns (ok, path-or-reason)."""
    missing = [f for f in REQUIRED_HANDOFF_FIELDS
               if not str(doc.get(f, "")).strip() and not doc.get(f)]
    if missing:
        reason = f"hand-off REJECTED (guardrail G-4): missing {', '.join(missing)}"
        event(task_id, "handoff_rejected", {"from": from_agent, "to": to_department, "missing": missing})
        return False, reason

    bus = read_bus()
    task = next((t for t in bus["tasks"] if t["id"] == task_id), None)
    if task is None:
        return False, f"unknown task {task_id}"
    if task.get("steps", 0) + 1 > task.get("max_steps", MAX_STEPS_DEFAULT):
        return False, _escalate(bus, task, f"max_steps {task.get('max_steps')} exceeded at hand-off")

    HANDOFFS.mkdir(parents=True, exist_ok=True)
    n = len(task.get("handoff_docs", [])) + 1
    path = HANDOFFS / f"{task_id}--{n:02d}--{_slug(from_agent)}--to--{_slug(to_department)}.md"
    artifacts = doc.get("artifacts")
    art_lines = "\n".join(f"- `{a}`" for a in (artifacts if isinstance(artifacts, list) else [artifacts]))
    path.write_text(f"""# Hand-off — {task['title']}

| | |
|---|---|
| task | `{task_id}` (step {task.get('steps', 0) + 1}/{task.get('max_steps')}) |
| from | **{from_agent}** |
| to | **{to_department}** department |
| at | {_now()} |

## What was done
{doc['what_was_done']}

## Artifacts (where the work lives)
{art_lines}

## What remains
{doc['what_remains']}

## Context the next agent needs
{doc['context_for_next']}

## Done criteria (unchanged unless stated)
{doc.get('done_criteria') or task.get('done_criteria')}
""", encoding="utf-8")

    try:
        rel = str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:                     # bus redirected off-repo (selftest scratch dir)
        rel = str(path).replace("\\", "/")
    task["department"] = to_department
    task["status"] = "queued"
    task["claimed_by"] = None
    task["steps"] = task.get("steps", 0) + 1
    task.setdefault("handoff_docs", []).append(rel)
    if doc.get("done_criteria"):
        task["done_criteria"] = doc["done_criteria"]
    task["updated_at"] = _now()
    _write_bus(bus)
    event(task_id, "handoff", {"from": from_agent, "to": to_department, "doc": rel})
    return True, rel


def complete(task_id: str, agent_id: str, result: str) -> bool:
    bus = read_bus()
    for t in bus["tasks"]:
        if t["id"] == task_id:
            t.update(status="done", result=result, updated_at=_now())
            _write_bus(bus)
            event(task_id, "completed", {"by": agent_id, "result": result})
            return True
    return False


def fail(task_id: str, agent_id: str, reason: str) -> str:
    """Failure bumps the escalation tier (G-6): 1 worker → 2 lead → 3 core → held for owner."""
    bus = read_bus()
    t = next((x for x in bus["tasks"] if x["id"] == task_id), None)
    if t is None:
        return "unknown task"
    return _escalate(bus, t, reason, by=agent_id)


def _escalate(bus: dict, t: dict, reason: str, by: str = "") -> str:
    t["escalation_tier"] = t.get("escalation_tier", 1) + 1
    if t["escalation_tier"] > ESCALATE_TO_OWNER_AT:
        t.update(status="held", hold_reason=reason, updated_at=_now())
        msg = f"escalated past tier {ESCALATE_TO_OWNER_AT} → HELD for owner: {reason}"
    else:
        t.update(status="queued", claimed_by=None, updated_at=_now())
        msg = f"escalated to tier {t['escalation_tier']}: {reason}"
    _write_bus(bus)
    event(t["id"], "escalated", {"tier": t["escalation_tier"], "reason": reason, "by": by})
    return msg


def remember(key: str, value, who: str = "excava-core") -> None:
    """Shared-memory WRITE (G-9). Facts survive between beats; the read side is the vector index."""
    st = _read(STATE, {"version": 1, "facts": {}, "beats": 0})
    st.setdefault("facts", {})[key] = {"value": value, "by": who, "at": _now()}
    _atomic_write(STATE, st)


def beat_state(dept_load: dict) -> dict:
    """Called once per orchestrator beat: bump the counter, persist load, return the state."""
    st = _read(STATE, {"version": 1, "facts": {}, "beats": 0})
    st["beats"] = st.get("beats", 0) + 1
    st["last_beat"] = _now()
    st["dept_load"] = dept_load
    _atomic_write(STATE, st)
    return st


def snapshot() -> dict:
    """Cheap summary for excava_status.json / the cockpit."""
    bus = read_bus()
    per, last_h = {}, None
    for t in bus["tasks"]:
        d = t.get("department") or "(unrouted)"
        per.setdefault(d, {"queued": 0, "working": 0, "done": 0, "held": 0, "failed": 0})
        per[d][t["status"]] = per[d].get(t["status"], 0) + 1
        if t.get("handoff_docs"):
            last_h = t["handoff_docs"][-1]
    open_tasks = [t for t in bus["tasks"] if t["status"] in ("queued", "working", "held")]
    return {"open": len(open_tasks), "total": len(bus["tasks"]),
            "per_department": per, "last_handoff": last_h}
