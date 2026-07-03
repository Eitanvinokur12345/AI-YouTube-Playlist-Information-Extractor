"""
src/excava.py — EXCAVA: the agentic-OS ORCHESTRATOR (Phase 0 spine).

Was: OS-1, a single operator picking one action per cycle (a tab pile with a status file).
Now: the core (tier 3) of a real OS. Each cron beat (hourly, .github/workflows/bulk_analyze.yml
— D1: cron heartbeat, free forever) it:

  1. Runs the VERIFICATION GATE (data_guard, security, G3) — guardrail G-2. Nothing is
     claimed while the gate fails; outward work additionally needs G3>=70 + owner approval.
  2. Syncs the owner's inbox (outranks everything, G-8) and the auto-priorities onto the
     FILE BUS (src/excava_bus.py) — tasks persist between beats and resume where they stopped.
  3. ROUTES unrouted tasks to departments by specialization + resources + load
     (src/excava_agents.py), tracing WHY each department won over the runners-up.
  4. TICKS workers under the Worker contract: claim → bounded work → complete, or hand off
     with a VALIDATED hand-off doc (G-4: no doc, no hand-off), or fail → 3-tier escalation
     ending at the owner (G-6).
  5. Writes shared memory (data/excava/state.json — write side; the semantic vector index
     stays the read side) and data/excava_status.json for the cockpit.

Run:   python -m src.excava              (one beat)
       python -m src.excava --recall "task"   (probe the semantic memory)
       python -m src.excava --selftest        (prove the spine on a scratch bus: enqueue →
                                              route → claim → REJECTED hand-off (gate) →
                                              valid hand-off → second department → done)
Free, mechanical, no Claude tokens; a beat never raises (the cron must not break).
"""
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path

from src import excava_agents as agents
from src import excava_bus as bus
from src.build_memory import embed as _embed, search as _search

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "excava_status.json"
NOW = datetime.now(timezone.utc).isoformat()
G3_OUTWARD = 70          # truth/access must be this high before EXCAVA may create/publish
OUTWARD = {"create", "promote", "publish", "self-code", "leverage"}
MAX_TICKS_PER_BEAT = 4   # a beat is cheap and bounded; the next beat resumes (cron heartbeat)
REDONE_WINDOW_H = 20     # don't re-enqueue a same-title task finished within this window
FAIL_STREAK = 3          # Phase 2 backpressure: this many straight failures rests a department
COOLDOWN_H = 6           # ...for this long (self-healing: it resumes on its own, traced)
# Phase 1 priority-weights dial (owner-tunable in data/excava_config.json -> priority_weights):
# higher weight = that area's auto-priorities reach the bus first. Owner inbox always outranks (G-8).
DEFAULT_WEIGHTS = {"access": 90, "backlog": 70, "pipeline": 60, "maintenance": 40}


def _load(name, d=None):
    try:
        return json.load(open(DATA / name, encoding="utf-8"))
    except Exception:
        return d if d is not None else {}


def _keys() -> list:
    ks = []
    for n in ["EXTERNAL_REVIEW_API_KEY", "GEMINI_API_KEY"] + [f"GEMINI_API_KEY_{i}" for i in range(2, 9)]:
        v = (os.environ.get(n) or "").strip()
        if v and v not in ks:
            ks.append(v)
    return ks


def semantic_recall(query: str, idx: dict, keys: list, k: int = 6) -> list:
    """MEANING-based recall (shared memory, read side): embed the task, return the hub items
    closest in meaning. Free + graceful: no key or empty index -> [] (the cron never breaks)."""
    if not query or not keys or not idx.get("vectors"):
        return []
    emb = _embed(query, keys[0])
    if not isinstance(emb, list):
        return []
    return _search(emb, idx, k)


def _norm_title(s) -> str:
    """Counts inside priority titles change hourly ('1665 tools still…' -> '1674 tools…');
    compare with digits collapsed so the same standing task isn't re-enqueued every beat."""
    import re
    return re.sub(r"[\d.,%]+", "#", str(s or "").lower()).strip()


def _recently_done(all_tasks: list, title: str) -> bool:
    """True if a normalized-same task is OPEN already or finished within the window."""
    nt = _norm_title(title)
    for t in all_tasks:
        if _norm_title(t.get("title")) != nt:
            continue
        if t.get("status") in ("queued", "working", "held"):
            return True
        if t.get("status") == "done":
            try:
                dt = datetime.fromisoformat(t["updated_at"])
                if (datetime.now(timezone.utc) - dt).total_seconds() < REDONE_WINDOW_H * 3600:
                    return True
            except Exception:
                continue
    return False


def _sync_to_bus(inbox_tasks: list, prios: list, outward_ok: bool, g3, holding: list,
                 weights: dict | None = None) -> bool:
    """Owner inbox first (G-8, priority 0), then top auto-priorities (priority 1) ordered by
    the owner's priority-weights dial. Outward work is held at the door while the gate is
    closed — it never reaches the bus."""
    w = {**DEFAULT_WEIGHTS, **(weights or {})}
    prios = sorted(prios, key=lambda p: -w.get((p.get("area") or "").lower(), 50))
    existing = bus.read_bus()["tasks"]
    changed_inbox = False
    for t in inbox_tasks:
        if t.get("status") in ("done", "held"):
            continue
        title = str(t.get("task", "")).strip()
        if not title or _recently_done(existing, title):
            continue
        if any(w in title.lower() for w in OUTWARD) and not outward_ok:
            if t.get("status") != "held":
                t["status"] = "held"; changed_inbox = True
            holding.append({"priority": title, "why_held": "owner task is outward; gate closed"})
            continue
        if bus.enqueue(title, department="", source="owner", priority=0,
                       done_criteria=str(t.get("done_criteria", "") or "")):
            if t.get("status") != "working":
                t["status"] = "working"; changed_inbox = True
    for p in prios[:5]:
        title = str(p.get("title", "")).strip()
        if not title or _recently_done(existing, title):
            continue
        if any(w in (p.get("area") or "").lower() for w in OUTWARD) and not outward_ok:
            holding.append({"priority": title,
                            "why_held": f"outward action; gate closed (G3={g3}<{G3_OUTWARD} or checks failing)"})
            continue
        bus.enqueue(title, detail=str(p.get("detail", "") or ""), source="auto", priority=1)
    return changed_inbox


def _route_all(reg: dict, can_do: dict, holding: list) -> int:
    routed = 0
    for t in bus.read_bus()["tasks"]:
        if t["status"] != "queued" or t.get("department"):
            continue
        text = f"{t['title']} {t.get('detail', '')}"
        dept, why, over = agents.pick_department(text, reg, can_do)
        if dept is None:
            holding.append({"priority": t["title"], "why_held": why})
            bus.event(t["id"], "unroutable", {"why": why})
            continue
        bus.route(t["id"], dept, why, over)
        routed += 1
    return routed


def _audit_spine() -> list[str]:
    """Phase 2 continuous self-audit: every beat, verify the coded spine still matches
    guardrails.md and the bus invariants hold. Any violation forces SAFE mode for the beat
    (assess, don't act) and surfaces to the owner — the OS never runs on a broken law."""
    problems = []
    try:
        law = (DATA / "excava" / "guardrails.md").read_text(encoding="utf-8").lower()
        for f in bus.REQUIRED_HANDOFF_FIELDS:
            if f not in law:
                problems.append(f"guardrails.md no longer names required hand-off field '{f}' (G-4 drift)")
    except Exception:
        problems.append("guardrails.md missing/unreadable — the law is gone (G-4/G-7 unverifiable)")
    reg = agents.load_registry()
    for a in reg.get("agents", []):
        if not a.get("scoped_tools"):
            problems.append(f"agent {a.get('id')} has no scoped tools (G-7 violation)")
    b = bus.read_bus()
    for t in b["tasks"]:
        if t["status"] == "working" and not t.get("claimed_by"):
            problems.append(f"bus invariant: {t['id']} working but unclaimed")
        for d in t.get("handoff_docs", []):
            if not (ROOT / d).exists():
                problems.append(f"bus invariant: {t['id']} hand-off doc missing on disk: {d}")
    return problems


def _approvals_sync(holding: list, mode: str) -> dict:
    """Phase 1 approval queue: everything waiting on the OWNER lands in
    data/excava_approvals.json with a category; the owner grants by id (cockpit issue link,
    Claude, or editing the file). Granted ids un-hold the matching bus task next beat."""
    prev = _load("excava_approvals.json", {})
    granted = set(prev.get("granted", []))
    applied = []
    if granted:
        b = bus.read_bus()
        for t in b["tasks"]:
            if t["status"] == "held" and t["id"] in granted:
                t.update(status="queued", claimed_by=None, escalation_tier=1,
                         hold_reason=None, updated_at=NOW)
                bus.event(t["id"], "owner_approved", {"via": "excava_approvals.json"})
                applied.append(t["id"])
        if applied:
            bus._write_bus(b)
    pending, seen = [], set()
    for t in bus.read_bus()["tasks"]:
        if t["status"] == "held" and t["id"] not in granted:
            pending.append({"id": t["id"], "title": t["title"], "category": "escalated",
                            "why": t.get("hold_reason", "escalated past tier 3"),
                            "since": t.get("updated_at")})
            seen.add(t["title"])
    for h in holding:
        if h.get("priority") in seen:
            continue
        why = h.get("why_held", "")
        cat = ("outward" if "outward" in why else
               "missing-resource" if "resource" in why else
               "unroutable" if "specialization" in why or "unroutable" in why else "needs-owner")
        pending.append({"id": None, "title": h.get("priority"), "category": cat, "why": why})
    out = {"generated_at": NOW, "mode": mode,
           "note": ("Approve by id: tell Claude 'EXCAVA: approve <id>', open the cockpit's approve "
                    "link (GitHub issue), or add the id to 'granted' here. Granted ids are applied "
                    "and re-queued on the next beat."),
           "pending": pending[:20], "granted": sorted(granted), "applied_last_beat": applied}
    (DATA / "excava_approvals.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    return out


def _beat(args) -> int:
    mem = _load("memory_index.json", {})
    keys = _keys()
    guard = _load("data_guard.json", {})
    sec = _load("security.json", {})
    goals = {g["id"]: g for g in _load("goals_status.json", {}).get("goals", [])}
    prios = _load("priorities.json", {}).get("priorities", [])
    scout = _load("pipeline_scout.json", {})
    cfg = _load("excava_config.json", {})
    reg = agents.load_registry()

    # ── 1. VERIFICATION GATE (G-2) ──
    g3 = (goals.get("G3", {}) or {}).get("score", 0)
    checks = {
        "data_guard_ok": guard.get("restored", 0) == 0,
        "security_clean": not sec.get("secret_leaks"),
        "truth_access_G3": g3,
        "G3_ready_for_outward": g3 >= G3_OUTWARD,
    }
    internal_ok = checks["data_guard_ok"] and checks["security_clean"]
    outward_ok = internal_ok and checks["G3_ready_for_outward"]

    # ── resources (G-3): written hourly by resource_check in CI, where the secrets live ──
    res = _load("resources.json", {})
    can = res.get("can_do", {}) or {}
    holding: list = []

    beat_log: list[str] = []
    changed_inbox = False
    usage_delta: dict = {}

    # ── kill switch / safe-mode (Phase 1) + continuous self-audit (Phase 2) ──
    mode = (cfg.get("mode") or "run").lower()
    audit = _audit_spine()
    if audit and mode == "run":
        mode = "safe"
        beat_log.append(f"AUTO SAFE-MODE — self-audit found {len(audit)} problem(s); acting is frozen "
                        "until the spine matches the law again")
    if mode == "kill":
        beat_log.append("KILL SWITCH ON (data/excava_config.json mode=kill) — bus untouched this beat")

    if internal_ok and mode != "kill":
        # ── crash recovery + memory pruning (Phase 2): the bus is the checkpoint ──
        for tid in bus.recover_leases():
            beat_log.append(f"lease expired -> re-queued {tid} (crash recovery)")
        pruned = bus.prune()
        if pruned:
            beat_log.append(f"pruned {pruned} finished task(s) to data/excava/archive/")

        # ── 2. sync owner inbox + auto-priorities onto the bus (weights dial, Phase 1) ──
        inbox = _load("excava_inbox.json", {})
        inbox_tasks = inbox.get("tasks", []) if isinstance(inbox, dict) else []
        changed_inbox = _sync_to_bus(inbox_tasks, prios, outward_ok, g3, holding,
                                     cfg.get("priority_weights"))
        if changed_inbox:
            (DATA / "excava_inbox.json").write_text(
                json.dumps(inbox, ensure_ascii=False, indent=2), encoding="utf-8")

        # ── 3. route by specialization + resources (+ load via claim order) ──
        _route_all(reg, can, holding)

        # ── 4. tick workers — unless safe-mode (assess, don't act) or a cooling-off
        #      department (Phase 2 backpressure: 3 straight fails => rest, then self-heal) ──
        if mode == "safe":
            beat_log.append("SAFE MODE — bus synced + routed, but no worker acted this beat")
        else:
            st0 = _load("excava/state.json", {})
            bp = (st0.get("facts", {}).get("backpressure", {}) or {}).get("value", {})
            per = bus.snapshot()["per_department"]
            busiest_first = sorted((d for d in per if per[d].get("queued") and d != "(unrouted)"),
                                   key=lambda d: (-per[d]["queued"], d))
            ticked = 0
            for dept in busiest_first:
                if ticked >= MAX_TICKS_PER_BEAT:
                    break
                cool = (bp.get(dept) or {}).get("cooldown_until", "")
                if cool and cool > NOW:
                    beat_log.append(f"{dept}: cooling off until {cool[:16]} (backpressure)")
                    continue
                r = agents.tick(dept, reg)
                if r:
                    line, outcome = r
                    beat_log.append(line)
                    usage_delta[dept] = outcome
                    ticked += 1
                    d = bp.setdefault(dept, {"streak": 0})
                    if outcome == "fails":
                        d["streak"] = d.get("streak", 0) + 1
                        if d["streak"] >= FAIL_STREAK:
                            until = datetime.fromtimestamp(
                                datetime.now(timezone.utc).timestamp() + COOLDOWN_H * 3600,
                                tz=timezone.utc).isoformat()
                            d["cooldown_until"], d["streak"] = until, 0
                            beat_log.append(f"{dept}: {FAIL_STREAK} straight fails -> resting {COOLDOWN_H}h")
                    else:
                        d["streak"], d["cooldown_until"] = 0, ""
            bus.remember("backpressure", bp)
    elif not internal_ok:
        beat_log.append("HOLD ALL — verification gate failing (fix data_guard/security first)")

    # bus-held tasks surface to the owner via the same holding list the cockpit shows
    snap = bus.snapshot()
    for t in bus.read_bus()["tasks"]:
        if t["status"] == "held":
            holding.append({"priority": t["title"],
                            "why_held": t.get("hold_reason", "escalated past tier 3 — needs owner")})

    # ── approval queue (Phase 1): everything owner-blocked, one file, categorized ──
    approvals = _approvals_sync(holding, mode)
    for tid in approvals.get("applied_last_beat", []):
        beat_log.append(f"owner approval applied -> {tid} re-queued")

    # ── next action = the top open bus task, grounded in the semantic memory ──
    open_tasks = [t for t in bus.read_bus()["tasks"] if t["status"] in ("queued", "working")]
    open_tasks.sort(key=lambda t: (t.get("priority", 1), t.get("created_at", "")))
    action = None
    if open_tasks:
        t = open_tasks[0]
        action = {"do": t["title"], "area": t.get("department") or "unrouted",
                  "type": "internal", "source": t["source"], "task_id": t["id"]}
        q = " ".join(x for x in [t["title"], t.get("detail")] if x)
        action["use_tools"] = [{"id": h["id"], "name": h.get("name"), "type": h.get("type"),
                                "score": h["score"]} for h in semantic_recall(q, mem, keys, 6)]
    elif not internal_ok:
        action = {"do": "HOLD ALL — verification gate failing", "type": "blocked",
                  "detail": "fix data_guard/security before EXCAVA acts"}
    mem_wired = bool(keys and mem.get("vectors"))

    # ── 5. shared memory write side + status for the cockpit ──
    dept_load = {d: v.get("queued", 0) + v.get("working", 0) for d, v in snap["per_department"].items()}
    st = bus.beat_state(dept_load, usage_delta)

    stack_review = {
        "candidates_available": scout.get("total_candidates", 0),
        "note": ("EXCAVA reviews its stack each cycle: integrate the best free per-process tool, "
                 "combine overlaps, offload weak ones. Top open process gaps: "
                 + ", ".join(r["process"] for r in (scout.get("processes") or []) if r.get("count", 0) < 6)[:120]),
    }
    OUT.write_text(json.dumps({
        "generated_at": NOW, "name": "EXCAVA",
        "phase": "OS spine (Phase 0): bus + departments + hand-offs live; creators (OS-2) gated",
        "gate": {"checks": checks, "internal_allowed": internal_ok, "outward_allowed": outward_ok,
                 "outward_needs": "data_guard ok + security clean + G3>=70 + owner approval"},
        "memory": {"vectors": len(mem.get("vectors", {})), "model": mem.get("model"), "wired": mem_wired},
        "resources": {"missing": res.get("missing", []), "checked_at": res.get("generated_at"),
                      "can_do": {k: v.get("ok") for k, v in can.items()}},
        "next_action": action, "holding": holding[:6],
        "os": {"beats": st.get("beats"), "mode": mode, "bus": snap, "beat_log": beat_log,
               "departments": sorted((reg.get("departments") or {}).keys()),
               "usage": st.get("usage", {}), "audit": {"ok": not audit, "problems": audit[:8]},
               "approvals_pending": len(approvals.get("pending", [])),
               "guardrails": "data/excava/guardrails.md", "traces": "data/excava/traces/"},
        "tool_stack": cfg.get("tool_stack", []), "stack_review": stack_review,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"EXCAVA beat #{st.get('beats')} [{mode}]: gate internal={'open' if internal_ok else 'CLOSED'} "
          f"outward={'open' if outward_ok else 'closed (G3=' + str(g3) + ')'}; "
          f"bus {snap['open']} open/{snap['total']} total; audit {'OK' if not audit else 'FAIL'}; "
          f"next = {action['do'] if action else 'none'}; holding {len(holding)}.")
    for line in beat_log:
        print(f"  · {line}")
    return 0


def _selftest() -> int:
    """Prove the Phase-0 spine on a SCRATCH bus (real code paths, throwaway files):
    two departments must pass one task via the bus with a real hand-off doc, and the
    doc gate must visibly reject a doc-less hand-off. Exit 0 only if every step holds."""
    import tempfile
    tmp = Path(tempfile.mkdtemp(prefix="excava-selftest-"))
    bus.EXDIR, bus.BUS = tmp, tmp / "bus.json"
    bus.STATE, bus.HANDOFFS, bus.TRACES = tmp / "state.json", tmp / "handoffs", tmp / "traces"

    reg = agents.load_registry()
    t = bus.enqueue("selftest: drain the transcript backfill, then hand to analysis", source="owner",
                    priority=0, done_criteria="task crosses two departments with a validated hand-off doc")
    assert t, "enqueue failed"
    dept, why, over = agents.pick_department(t["title"], reg, {})
    assert dept == "transcripts", f"routing picked {dept!r}, expected transcripts"
    assert bus.route(t["id"], dept, why, over), "route failed"

    w1 = agents.worker_for(reg, "transcripts")
    claimed = bus.claim(w1["id"], "transcripts")
    assert claimed and claimed["id"] == t["id"], "claim failed"

    ok, reason = bus.handoff(t["id"], w1["id"], "analysis", {"what_was_done": "x"})   # doc-less
    assert not ok and "REJECTED" in reason, "gate FAILED to reject an incomplete hand-off doc"

    ok, ref = bus.handoff(t["id"], w1["id"], "analysis", {
        "what_was_done": "assessed the drain: N pending re-queued",
        "artifacts": ["data/_pending/"], "what_remains": "deep re-extraction of the pending records",
        "context_for_next": "bulk_analyze consumes data/_pending hourly"})
    assert ok and (bus.HANDOFFS / Path(ref).name).exists(), "valid hand-off did not produce a doc"

    w2 = agents.worker_for(reg, "analysis")
    claimed2 = bus.claim(w2["id"], "analysis")
    assert claimed2 and claimed2["id"] == t["id"], "second department failed to claim"
    assert bus.complete(t["id"], w2["id"], "selftest pass"), "complete failed"

    kinds = [json.loads(l)["kind"] for l in open(bus.TRACES / f"{t['id']}.jsonl", encoding="utf-8")]
    for k in ("enqueued", "routed", "claimed", "handoff_rejected", "handoff", "completed"):
        assert k in kinds, f"trace missing {k}"
    print("SELFTEST PASS -- enqueue -> route(transcripts) -> claim -> hand-off REJECTED without doc "
          "-> hand-off WITH doc -> analysis claim -> done; full trace present.")
    return 0


def main() -> int:
    import sys
    try:                                   # Windows console defaults to cp1252 -> emoji crash
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--recall", default="", help="print the hub items semantically closest to a task, then exit")
    ap.add_argument("--selftest", action="store_true", help="prove the OS spine on a scratch bus")
    args, _ = ap.parse_known_args()
    if args.selftest:
        return _selftest()
    if args.recall:                                  # manual / activator probe of the semantic memory
        for h in semantic_recall(args.recall, _load("memory_index.json", {}), _keys(), 10):
            print(f"  {h['score']:.3f}  {h.get('type')}: {h.get('name')}  [{h['id']}]")
        return 0
    return _beat(args)


if __name__ == "__main__":
    raise SystemExit(main())
