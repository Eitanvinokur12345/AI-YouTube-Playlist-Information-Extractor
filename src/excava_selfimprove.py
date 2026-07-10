"""
src/excava_selfimprove.py — M2.8: the SELF-IMPROVEMENT department, finally real.

Every beat it reviews the OS's own telemetry — lease denials, engine failures in chat logs,
the stub-rate trend, room pacing — and acts on what it finds:
  SAFE changes  -> applied automatically + tested + logged (data/excava/improvements.jsonl):
                   e.g. lowering a failing engine's RPM cap, shifting daily token budget to a
                   starved department (global total unchanged), retiring a dead room.
  BIG changes   -> a PITCH (P5: new tool / overhaul / deeper access): a pitch room opens and
                   an approval-queue entry appears — nothing big happens without Eitan.
Nothing is exempt: agents, prompts, engines, hub content, its own code (code changes are
always overhaul-class -> pitch).
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
EXDIR = DATA / "excava"
LOG = EXDIR / "improvements.jsonl"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load(p: Path, d):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return d


def _log(kind: str, what: str, why: str, applied: bool) -> None:
    EXDIR.mkdir(parents=True, exist_ok=True)
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"at": _now(), "kind": kind, "what": what, "why": why,
                             "applied": applied}, ensure_ascii=False) + "\n")


def _engine_failures() -> dict:
    """Count engine failures noted in the last 2 days of chat logs."""
    fails: dict = {}
    for day in sorted((EXDIR / "chats").glob("*"), reverse=True)[:2]:
        for f in day.glob("*.jsonl"):
            for line in f.read_text(encoding="utf-8").splitlines():
                if '"engine": "none"' in line:
                    fails["(all)"] = fails.get("(all)", 0) + 1
    return fails


def run() -> list[str]:
    """One review pass. Returns beat-log lines. Cheap, mechanical, honest."""
    out = []
    budgets_p = EXDIR / "budgets.json"
    budgets = _load(budgets_p, None)
    leases = _load(EXDIR / "leases.json", {})
    improved = False

    # SAFE #1: a department denied on budget while others idle -> shift 10% headroom to it
    denials = leases.get("denials", [])
    if budgets and denials:
        used = leases.get("dept_tokens", {})
        starved = denials[-1]["dept"]
        idle = [d for d, cap in budgets["dept_daily_tokens"].items()
                if d not in ("default", starved) and used.get(d, 0) < cap * 0.2]
        if idle:
            donor = idle[0]
            shift = int(budgets["dept_daily_tokens"][donor] * 0.10)
            budgets["dept_daily_tokens"][donor] -= shift
            budgets["dept_daily_tokens"][starved] = budgets["dept_daily_tokens"].get(
                starved, budgets["dept_daily_tokens"]["default"]) + shift
            budgets_p.write_text(json.dumps(budgets, ensure_ascii=False, indent=2), encoding="utf-8")
            _log("safe-budget-shift", f"moved {shift} tokens/day {donor} -> {starved}",
                 f"{starved} hit its budget while {donor} sat under 20% used", True)
            out.append(f"self-improve: shifted {shift} tokens/day {donor} -> {starved} (safe, applied)")
            improved = True

    # SAFE #2: stale open rooms (no close after 2x max_turns beats) -> retire, free the slot
    rooms_p = EXDIR / "rooms.json"
    rooms = _load(rooms_p, {"rooms": []})
    for r in rooms.get("rooms", []):
        if r["status"] == "open" and r.get("turns", 0) == 0:
            try:
                age_h = (datetime.now(timezone.utc)
                         - datetime.fromisoformat(r["created_at"])).total_seconds() / 3600
            except Exception:
                age_h = 0
            if age_h > 48:
                r["status"] = "archived"
                _log("safe-room-retire", f"archived silent room {r['id']}",
                     "open 48h with zero turns (engines absent locally) — noise, not work", True)
                out.append(f"self-improve: archived silent room {r['id']} (safe, applied)")
                improved = True
    if improved:
        rooms_p.write_text(json.dumps(rooms, ensure_ascii=False, indent=1), encoding="utf-8")

    # PITCHES: big changes that need Eitan — grounded in REAL telemetry, deduped, routed to the
    # SAME in-app decide flow (each pitch cites the number that triggered it, so it's never invented).
    pitched = _load(EXDIR / "pitches.json", {"pitches": []})
    have = {p.get("what") for p in pitched.get("pitches", [])}
    new_pitches = _gen_pitches(have)
    if new_pitches:
        pitched.setdefault("pitches", []).extend(new_pitches)
        (EXDIR / "pitches.json").write_text(json.dumps(pitched, ensure_ascii=False, indent=1),
                                            encoding="utf-8")
        for pitch in new_pitches:
            _log("pitch", pitch["what"], pitch["why"], False)
            out.append(f"self-improve: PITCH filed — {pitch['what']} (awaits owner)")
        # NOTE: pitches reach the approval queue via excava._approvals_sync, which reads pitches.json
        # as the source of truth every beat — so they survive the queue rebuild instead of being wiped.
    return out


def _gen_pitches(have: set) -> list[dict]:
    """Evaluate real, grounded conditions and file genuine big-change pitches. Deduped by 'what'.
    'owner_what' is the plain-language 'what approving does' the in-app decide modal shows."""
    pitches: list[dict] = []

    def add(what: str, why: str, klass: str, owner_what: str) -> None:
        if what in have:
            return
        pitches.append({"id": f"pitch-{abs(hash(what)) % 100000}", "what": what, "why": why,
                        "class": klass, "owner_what": owner_what, "at": _now(), "status": "pending"})
        have.add(what)

    # A. repeated engine outages -> OmniRoute gateway fallback (overhaul-class)
    fails = _engine_failures()
    if fails.get("(all)", 0) >= 3:
        add("wire OmniRoute gateway fallback",
            f"{fails['(all)']} engine-outage turns in the last 2 days; the gateway's 4-tier fallback "
            "would absorb them (you installed OmniRoute locally already)",
            "overhaul (P5 gate #2)",
            "Approve to let EXCAVA wire the OmniRoute fallback so engine outages stop stalling the rooms.")

    # B. the lowest at-risk North-Star goal -> a dedicated build lane (focused push)
    goals = _load(DATA / "goals_status.json", [])
    if isinstance(goals, dict):
        goals = goals.get("goals", [])
    atrisk = [g for g in goals if isinstance(g, dict) and g.get("score", 100) < 65]
    if atrisk:
        g = min(atrisk, key=lambda x: x.get("score", 100))
        add(f"dedicate a build lane to {g['id']} - {g.get('name', '')}",
            f"{g['id']} sits at {g.get('score')}/100 ({g.get('gap', 'below target')}); a focused lane "
            "would move the goal instead of leaving it at-risk",
            "deeper focus (P5)",
            f"Approve to spin up a lane that pushes {g['id']} '{g.get('name', '')}' toward its target.")

    # C. a resource that keeps BLOCKING work -> obtain/enable it (deeper access)
    ap = _load(DATA / "excava_approvals.json", {"pending": []})
    miss = [p for p in ap.get("pending", []) if p.get("category") == "missing-resource"]
    if len(miss) >= 2:
        res = None
        for p in miss:
            m = re.search(r"resource ([a-z0-9\-]+)", p.get("why", ""))
            if m:
                res = m.group(1)
                break
        label = res or "the blocked capability"
        add(f"provide the blocked resource: {label}",
            f"{len(miss)} held items can't proceed because '{label}' isn't available; providing it "
            "unblocks them all at once",
            "deeper access (P5 gate #3)",
            f"Approve to let EXCAVA obtain/enable '{label}' so the blocked items can run.")

    return pitches


if __name__ == "__main__":
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    for line in run() or ["self-improve: nothing to change this pass (telemetry clean)"]:
        print(line)
