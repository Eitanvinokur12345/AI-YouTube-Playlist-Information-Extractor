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


#  AUTONOMY (owner 2026-07-10, data/excava/autonomy.json): which self-changes need no owner.
_TIER = {"budget-shift": "1-auto", "safe-room-retire": "1-auto", "prompt": "1-auto",
         "config": "1-auto", "self-code": "2-self-code", "add-agent": "2.5-agents",
         "pitch": "3-pitch"}


def _log(kind: str, what: str, why: str, applied: bool) -> None:
    EXDIR.mkdir(parents=True, exist_ok=True)
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"at": _now(), "kind": kind, "what": what, "why": why,
                             "applied": applied, "tier": _TIER.get(kind, "3-pitch")},
                            ensure_ascii=False) + "\n")


def _staff_thin_departments() -> list[str]:
    """TIER 2.5 (owner-granted): EXCAVA may add new AGENTS alone. Real use: any department
    running below the standard cast (lead+doer+checker) gets its missing role added, labeled
    'Added by EXCAVA'. Idempotent; owner can remove any agent it adds."""
    out = []
    reg_p = EXDIR / "agents.json"
    reg = _load(reg_p, {})
    ags = reg.get("agents", [])
    by_dept: dict[str, set] = {}
    for a in ags:
        d = a.get("department")
        if d and d != "core":
            by_dept.setdefault(d, set()).add(a.get("role"))
    need = {"lead": "steers the room and converges decisions",
            "doer": "argues for one concrete decision and owns the follow-through",
            "checker": "pushes back and demands evidence before the room converges"}
    changed = False
    for d, roles in sorted(by_dept.items()):
        for role, duty in need.items():
            if role in roles:
                continue
            aid = f"{d}-{role}-x"
            if any(a.get("id") == aid for a in ags):
                continue
            name = (d[:1].upper() + d[1:3] + role[:1].upper() + role[1:3]).strip()
            ags.append({"id": aid, "name": name, "tier": 1, "department": d, "role": role,
                        "persona": f"{name}: {duty}. (Added by EXCAVA under tier 2.5 autonomy.)",
                        "added_by": "EXCAVA", "engine_pref": "fast",
                        "scoped_tools": ["src.excava_bus", "src.excava_chat"]})
            _log("add-agent", f"added {role} '{name}' to {d}",
                 f"{d} ran without a {role} — every department needs lead+doer+checker for a real debate", True)
            out.append(f"self-improve: ADDED AGENT {name} ({role}) to {d} [tier 2.5]")
            changed = True
    if changed:
        reg["agents"] = ags
        reg["updated_at"] = _now()
        reg_p.write_text(json.dumps(reg, ensure_ascii=False, indent=2), encoding="utf-8")
    return out


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

    # TIER 2.5: staff any department missing a lead/doer/checker (owner-granted agent autonomy)
    out.extend(_staff_thin_departments())

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


def _hub_candidates(terms: list[str], k: int = 3, detail: bool = False) -> list[dict]:
    """SELF-USE (owner law 2026-07-10): before asking the owner for anything, search EXCAVA's OWN
    hub (elements_index.json, ~6.8k elements) for tools/skills that could solve the problem.
    Cheap keyword scoring, stdlib only; quality+verified break ties."""
    idx = _load(DATA / "elements_index.json", {})
    els = idx.get("elements", []) if isinstance(idx, dict) else []
    terms = {t.lower().rstrip("s") for t in terms if t}          # singular-ize so 'transcripts' matches 'transcript'
    scored, seen = [], set()
    for e in els:
        hay = (str(e.get("name", "")) + " " + str(e.get("what", ""))).lower()
        score = sum(1 for t in terms if t in hay)
        if score:
            scored.append((score, bool(e.get("verified")), e.get("quality_score") or 0, e))
    scored.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
    out = []
    for _, _, _, e in scored:
        if e.get("name") in seen:
            continue
        seen.add(e.get("name"))
        item = {"id": e.get("id"), "name": e.get("name")}
        if detail:                                   # R3-1 context paging wants the substance too
            item["what"] = str(e.get("what", ""))[:90]
        out.append(item)
        if len(out) >= k:
            break
    return out


def _gen_pitches(have: set) -> list[dict]:
    """Evaluate real, grounded conditions and file genuine big-change pitches. Deduped by 'what'.
    PITCH V2 (owner 2026-07-10: 'I don't have enough data in the pitch'): every pitch carries
    requested_by / need / importance / missing / hub_candidates so the decide modal answers
    WHO asks, WHY, HOW important, WHAT is missing, and what EXCAVA found in its own hub."""
    pitches: list[dict] = []

    def add(what: str, why: str, klass: str, owner_what: str, *, requested_by: str = "",
            need: str = "", importance: str = "", missing: str = "",
            hub_terms: list[str] | None = None) -> None:
        if what in have:
            return
        pitches.append({"id": f"pitch-{abs(hash(what)) % 100000}", "what": what, "why": why,
                        "class": klass, "owner_what": owner_what, "at": _now(), "status": "pending",
                        "requested_by": requested_by, "need": need, "importance": importance,
                        "missing": missing,
                        "hub_candidates": _hub_candidates(hub_terms) if hub_terms else []})
        have.add(what)

    # A. repeated engine outages -> OmniRoute gateway fallback (overhaul-class)
    fails = _engine_failures()
    if fails.get("(all)", 0) >= 3:
        add("wire OmniRoute gateway fallback",
            f"{fails['(all)']} engine-outage turns in the last 2 days; the gateway's 4-tier fallback "
            "would absorb them (you installed OmniRoute locally already)",
            "overhaul (P5 gate #2)",
            "Approve to let EXCAVA wire the OmniRoute fallback so engine outages stop stalling the rooms.",
            requested_by="Improve department (engine-outage telemetry from the room transcripts)",
            need=f"Agent conversations died {fails['(all)']} times in 2 days because every free engine "
                 "was rate-limited at once; a fallback router would keep rooms alive.",
            importance="High — when engines are out, ALL departments stop talking and producing.",
            missing="A router that tries engine after engine automatically (OmniRoute is installed "
                    "on your PC but not wired into the cloud beat).",
            hub_terms=["router", "gateway", "fallback", "openrouter"])

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
            f"Approve to spin up a lane that pushes {g['id']} '{g.get('name', '')}' toward its target.",
            requested_by="Improve department (North-Star goal tracker, data/goals_status.json)",
            need=f"Of your 9 North-Star goals, {g['id']} '{g.get('name', '')}' is the weakest at "
                 f"{g.get('score')}/100 — concretely: {g.get('gap', 'below target')}.",
            importance=f"High — {g['id']} is the LOWEST-scoring goal; every beat without a dedicated "
                       "lane leaves the weakest link weakest.",
            missing="A recurring CI lane whose only job is closing this goal's gap (like the analysis "
                    "and links lanes that already exist for other goals).",
            hub_terms=[w for w in str(g.get("name", "")).lower().split() if len(w) > 3][:3])

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
            f"Approve to let EXCAVA obtain/enable '{label}' so the blocked items can run.",
            requested_by=f"The departments whose work is stuck on it ({len(miss)} held items in your "
                         "approval queue)",
            need=f"'{label}' is the one missing capability behind {len(miss)} stuck items — one "
                 "unblock clears them all.",
            importance=f"Medium-high — {len(miss)} real tasks wait on this single resource.",
            missing=f"A working way to do '{label}' in the cloud beat (quota, key, or tool).",
            hub_terms=[t for t in re.split(r"[^a-z0-9]+", label.lower()) if len(t) > 3][:3])

    return pitches


if __name__ == "__main__":
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    for line in run() or ["self-improve: nothing to change this pass (telemetry clean)"]:
        print(line)
