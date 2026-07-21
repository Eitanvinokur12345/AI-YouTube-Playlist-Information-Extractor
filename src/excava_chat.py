"""
src/excava_chat.py — M2.5 + M2.4 + M2.6: CONVERSATIONS are the work mechanism.

Rooms (dept | cross | group | war) hold real multi-turn conversations between the NAMED
agents (data/excava/agents.json): the DOER proposes with real work detail, the CHECKER
pushes back (productive debate — owner rule), the LEAD converges and closes. Every message
= one REAL engine call (src.excava_engines) behind the lease arbiter (src.excava_leases),
tagged {agent, engine, model, ms} — the "agent · engine" badge in the chat UI is the truth.

M2.4 WORKERS: when a doer needs legwork it dispatches ephemeral generic workers (worker-xxxx)
that each do one unit and dissolve; they're tracked in state.json while alive and traced.

M2.6 ARTIFACTS: a room's convergence produces a real committed thing —
  kind=package  -> a package assembled into data/packages.json from real index elements
  kind=bus-task -> a routed task on the EXCAVA bus (real machinery does it)
  kind=element  -> a creators-department draft (labeled, tested — G-12)
The transcript is proof; the artifact is the point. Chats archive by day under
data/excava/chats/YYYY-MM-DD/<room>.jsonl — scrollable, replayable, identical offline/online.

Run: python -m src.excava_chat --demo | --advance [--turns 4]
"""
from __future__ import annotations

import argparse
import json
import random
import re
import time
from datetime import datetime, timezone
from pathlib import Path

from src import excava_agents as agents
from src import excava_bus as bus
from src import excava_engines as engines
from src import excava_leases as leases

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
EXDIR = DATA / "excava"
ROOMS = EXDIR / "rooms.json"
CHATS = EXDIR / "chats"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load(p: Path, d):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return d


def load_rooms() -> dict:
    return _load(ROOMS, {"rooms": []})


def save_rooms(state: dict) -> None:
    EXDIR.mkdir(parents=True, exist_ok=True)
    ROOMS.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")


def open_room(kind: str, goal: str, dept: str = "", done_criteria: str = "",
              max_turns: int = 10, artifact_kind: str = "bus-task") -> dict:
    state = load_rooms()
    rid = f"{kind}-{re.sub(r'[^a-z0-9]+', '-', goal.lower())[:28].strip('-')}-{random.randint(100, 999)}"
    for r in state["rooms"]:
        if r["goal"] == goal and r["status"] == "open":
            return r
    room = {"id": rid, "kind": kind, "goal": goal, "dept": dept,
            "done_criteria": done_criteria or "the lead states the decision and the artifact exists",
            "max_turns": max_turns, "turns": 0, "status": "open",
            "artifact_kind": artifact_kind, "artifact": None,
            "created_at": _now(), "last_turn_ms": 0}
    state["rooms"].append(room)
    save_rooms(state)
    _post(room, "system", "room", "", f"Room opened — goal: {goal}", 0)
    return room


def _post(room: dict, agent_id: str, name: str, engine: str, text: str, ms: int) -> None:
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    d = CHATS / day
    d.mkdir(parents=True, exist_ok=True)
    with open(d / f"{room['id']}.jsonl", "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"at": _now(), "agent": agent_id, "name": name,
                             "engine": engine, "ms": ms, "text": text[:1500]},
                            ensure_ascii=False) + "\n")


def _history(room: dict, n: int = 6) -> list[dict]:
    out = []
    for day_dir in sorted(CHATS.glob("*"), reverse=True)[:3]:
        f = day_dir / f"{room['id']}.jsonl"
        if f.exists():
            for line in f.read_text(encoding="utf-8").splitlines():
                try:
                    out.append(json.loads(line))
                except Exception:
                    pass
    return out[-n:]


def _cast(room: dict, reg: dict) -> list[dict]:
    dept = room.get("dept") or ""
    pool = [a for a in reg.get("agents", []) if a.get("tier") in (1, 2)
            and (room["kind"] in ("group", "war") or a.get("department") == dept)]
    if room["kind"] in ("group", "war"):
        by_role = {}
        for a in pool:
            by_role.setdefault(a.get("role"), []).append(a)
        pool = (by_role.get("doer", [])[:3] + by_role.get("checker", [])[:2]
                + by_role.get("lead", [])[:2])
    return pool or reg.get("agents", [])[:3]


def _speaker(room: dict, cast: list[dict]) -> dict:
    """Debate order: doer opens, checker challenges, doer answers, lead converges at the end."""
    t = room["turns"]
    doers = [a for a in cast if a.get("role") == "doer"]
    checkers = [a for a in cast if a.get("role") == "checker"]
    leads = [a for a in cast if a.get("role") == "lead"]
    if t >= room["max_turns"] - 2 and leads:
        return leads[t % len(leads)]
    order = []
    for i in range(max(len(doers), 1)):
        if doers:
            order.append(doers[i % len(doers)])
        if checkers:
            order.append(checkers[i % len(checkers)])
    return order[t % len(order)] if order else cast[t % len(cast)]


def _dispatch_workers(room: dict, doer: dict, n: int) -> str:
    """M2.4: ephemeral generic workers — tracked while alive, then dissolved + traced."""
    st = _load(EXDIR / "state.json", {})
    live = st.setdefault("live_workers", [])
    ids = [f"worker-{random.randint(1000, 9999)}" for _ in range(n)]
    live.extend([{"id": w, "for": doer["id"], "room": room["id"], "at": _now()} for w in ids])
    (EXDIR / "state.json").write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")
    bus.event(room["id"], "workers_dispatched", {"by": doer["id"], "n": n, "ids": ids})
    st = _load(EXDIR / "state.json", {})
    st["live_workers"] = [w for w in st.get("live_workers", []) if w["id"] not in ids]
    (EXDIR / "state.json").write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")
    bus.event(room["id"], "workers_dissolved", {"by": doer["id"], "n": n})
    return f"[dispatched {n} workers: {', '.join(ids[:3])}{'…' if n > 3 else ''} — done, dissolved]"


#  AGENT-PLATFORM LAYER 1 (owner build order 2026-07-12): PER-AGENT PERSISTENT MEMORY.
#  An agent that remembers its own positions across rooms and days stops being an
#  interchangeable engine-borrower and starts being a colleague (AGENTIC_OS_STUDY §6).
#  Store: data/excava/agent_memory/<agent-id>.jsonl · read into its turns, capped tight.
AGENT_MEM_DIR = DATA / "excava" / "agent_memory"
AGENT_MEM_KEEP = 30          # last N remembered items per agent
AGENT_MEM_RECALL = 2         # how many the agent re-reads per turn (token diet is watching)


def _remember_turn(sp: dict, room: dict, text: str) -> None:
    """After an agent speaks, keep the essence of what it argued — its first substantive
    sentence, or its DECISION line — so tomorrow's turns can be consistent with today's."""
    try:
        aid = sp.get("id", "")
        if not aid:
            return
        core = ""
        for ln in text.splitlines():
            ln = ln.strip()
            if ln.upper().startswith("DECISION"):
                core = ln
                break
            if len(ln) > 30 and not core:
                core = ln
        if not core:
            return
        AGENT_MEM_DIR.mkdir(parents=True, exist_ok=True)
        p = AGENT_MEM_DIR / f"{aid}.jsonl"
        rows = p.read_text(encoding="utf-8").splitlines() if p.exists() else []
        rows.append(json.dumps({"at": datetime.now(timezone.utc).isoformat()[:16],
                                "room": room.get("id", "")[:34], "said": core[:160]},
                               ensure_ascii=False))
        p.write_text("\n".join(rows[-AGENT_MEM_KEEP:]) + "\n", encoding="utf-8")
    except Exception:
        pass                                             # memory must never break a turn


def _recall_agent(sp: dict) -> str:
    """The agent's own memory, injected into its turn — capped hard (diet law)."""
    try:
        p = AGENT_MEM_DIR / f"{sp.get('id', '')}.jsonl"
        if not p.exists():
            return ""
        rows = [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines()[-AGENT_MEM_RECALL:]]
        if not rows:
            return ""
        return ("YOUR OWN MEMORY (be consistent with what you argued before): "
                + " | ".join(r["said"][:80] for r in rows))[:220] + "\n"
    except Exception:
        return ""


#  AGENT-PLATFORM LAYER 3 (owner build order 2026-07-12): INITIATIVE — when a room closes on a
#  decision, the agent who converged it may put ONE follow-up task on the bus, attributed to it.
#  Outcome links from BIRTH (the layer-2 lesson: never ship autonomy without outcome tracking):
#  source='agent:<id>' + the decision artifact in detail → agent_record can compute a real
#  hit-rate (proposed vs completed). Capped: max 2 open initiative tasks per agent, ever.
INITIATIVE_CAP = 2


def _propose_from_decision(room: dict, sp: dict, decision_text: str) -> str:
    try:
        aid = sp.get("id", "")
        if not aid or room.get("kind") == "group":       # group chat audits 100% SI — no initiative
            return ""
        heavy, _o = _tiers()
        if room.get("kind") == "dept" and room.get("dept") not in heavy:
            return ""                                    # output tier acts via _act_on_close instead
        m = re.search(r"DECISION:\s*(.+?)(?:\.|$)", decision_text, re.I)
        core = (m.group(1).strip() if m else "").strip()
        if len(core) < 20:
            return ""                                    # nothing concrete enough to act on
        # PROPOSAL-TIME GROUNDING (2026-07-12, non-negotiable before external action): a decision
        # that hallucinates a foreign tech stack (the Creators Rust/cargo theater) must NOT become
        # real bus work. Same detector the decision audit uses — one law, two enforcement points.
        try:
            from src.decision_audit import FOREIGN_STACK
            if FOREIGN_STACK.search(decision_text):
                from src.excava_agents import _syslog
                _syslog(room.get("dept", ""), "initiative", {"id": room.get("id", "")}, False,
                        "initiative-refused-ungrounded")
                return (f"{room['id']}: initiative REFUSED — {sp.get('name')}'s decision mentions a "
                        "foreign tech stack (likely hallucinated); not putting it on the bus")
        except Exception:
            pass
        b = bus.read_bus()
        mine_open = sum(1 for t in b.get("tasks", [])
                        if t.get("source") == f"agent:{aid}"
                        and t.get("status") in ("queued", "working", "held"))
        if mine_open >= INITIATIVE_CAP:
            return f"{room['id']}: initiative capped for {sp.get('name')} ({mine_open} open)"
        t = bus.enqueue(f"[{sp.get('name', aid)}'s initiative] {core[:120]}",
                        detail=f"Proposed by agent {aid} from the decision of room {room.get('id')} "
                               f"(artifact: {json.dumps(room.get('artifact') or {})[:120]}). "
                               "Outcome feeds this agent's hit-rate.",
                        department=room.get("dept", ""), source=f"agent:{aid}", priority=2,
                        done_criteria="the decision's concrete step is done and verifiable")
        if t:
            return f"{room['id']}: INITIATIVE — {sp.get('name')} proposed {t['id']}"
        return ""
    except Exception:
        return ""                                        # initiative must never break a close


#  DECISION-VOLUME LAW, ENFORCED IN THE MACHINE (owner 2026-07-12, third time asking):
#  output-tier departments make as FEW decisions as possible — their rooms are ACTION-shaped
#  (short, converge on 'ACTION:', and the action becomes real bus work). Any improvement-
#  flavored conclusion is REROUTED to Self-Improvement (or Power if it's about EXCAVA's own
#  capabilities) — departments never keep improvement work. Decision-heavy tier (improve,
#  power, visualization, accessibility) keeps the debate shape: deciding IS their mission.
def _tiers() -> tuple[set, set]:
    try:
        d = json.loads((DATA / "excava" / "dept_tiers.json").read_text(encoding="utf-8"))
        return set(d.get("decision_heavy", [])), set(d.get("output_tier", []))
    except Exception:
        return {"improve", "power", "visualization", "accessibility"}, set()


def _route_conclusion(room: dict, line: str) -> str:
    """Where an output-tier room's converged ACTION belongs (owner's law):
    improvement of an action/system/technical aspect -> improve; EXCAVA-capability -> power;
    otherwise it is real department work and goes to the department's own bus queue."""
    low = line.lower()
    if any(w in low for w in ("excava", "capability", "engine", "power level", "upgrade our")):
        return "power"
    if any(w in low for w in ("improve", "optimi", "refactor", "streamlin", "standardiz",
                              "workflow", "process", "our prompts", "our rooms", "efficien")):
        return "improve"
    return room.get("dept", "") or "core"


def _act_on_close(room: dict, line: str) -> str:
    """Output-tier close: the conclusion becomes REAL bus work (the bus + syscall gate execute
    it), never a decision.md that goes nowhere. Rerouting is visible + traced."""
    dest = _route_conclusion(room, line)
    core = re.sub(r"^(ACTION|DECISION):\s*", "", line.strip(), flags=re.I)[:120]
    src_dept = room.get("dept", "")
    rerouted = dest != src_dept
    t = bus.enqueue((f"[rerouted {src_dept}→{dest}] " if rerouted else f"[{src_dept} room action] ") + core,
                    detail=f"From room {room.get('id')} (action-shaped close). "
                           + ("Improvement matter — belongs to the "
                              f"{dest} department by owner law 2026-07-12." if rerouted else
                              "Mission action from the department's own room."),
                    department=dest, source=f"room-action:{src_dept}", priority=2,
                    done_criteria="the stated action is done and verifiable")
    try:
        from src.excava_agents import _syslog
        _syslog(src_dept, "room-close", {"id": room.get("id", "")}, True,
                f"rerouted-to-{dest}" if rerouted else "action-queued")
    except Exception:
        pass
    if t:
        return f"{room['id']}: {'REROUTED to ' + dest.upper() if rerouted else 'ACTION queued'} → {t['id']}"
    return f"{room['id']}: action already on the bus (deduped)"


_PAGE_CACHE: dict = {}


def _page_context(room: dict) -> str:
    """R3-1 CONTEXT PAGING (owner-ranked #1 from the Agentic-OS study, Letta's idea): pull the
    most relevant HUB knowledge into the debate so agents argue from what the project KNOWS,
    not just recent chat. Keyword recall (quota-free), 2 items, hard-capped ~200 chars —
    the token diet is watching. Cached per room (the goal doesn't change)."""
    rid = room.get("id", "")
    if rid in _PAGE_CACHE:
        return _PAGE_CACHE[rid]
    try:
        from src.excava_selfimprove import _hub_candidates
        terms = [w for w in re.findall(r"[a-z]{5,}", room.get("goal", "").lower())][:4]
        hits = _hub_candidates(terms, k=2, detail=True) if terms else []
        block = ""
        if hits:
            block = ("KNOWN FROM THE HUB (use if relevant): " + "; ".join(
                f"{h['name']} — {h.get('what', '')[:55]}" for h in hits))[:200] + "\n"
        # R3-2 TEMPORAL VALIDITY (Zep's idea): only capability/power rooms need to know facts
        # can go stale (a free model going paid, a key losing access) — noise everywhere else.
        goal_l = room.get("goal", "").lower()
        if any(w in goal_l for w in ("power", "capability", "engine", "model", "self-improve")):
            try:
                ev = json.loads((ROOT / "data" / "excava" / "temporal_validity.json")
                                .read_text(encoding="utf-8")).get("recent_staleness_events", [])
                if ev:
                    last = ev[-1]
                    block += (f"FACTS CAN GO STALE: {last['what']} just did ({last['now_true']}) — "
                             f"don't assume a capability still works; check first.\n")[:220]
            except Exception:
                pass
        _PAGE_CACHE[rid] = block
        return block
    except Exception:
        _PAGE_CACHE[rid] = ""
        return ""


def _prompt(room: dict, sp: dict, hist: list[dict]) -> str:
    role = sp.get("role", "agent")
    closing = room["turns"] >= room["max_turns"] - 2
    convo = "\n".join(f"{m['name']} ({m['agent']}): {m['text'][:300]}" for m in hist) or "(room just opened)"
    heavy, _out = _tiers()
    if room.get("kind") == "dept" and room.get("dept") not in heavy:
        # ACTION-shaped (output tier): as few decisions as possible — the room exists to DO
        inst = {
            "doer": ("State the ONE action you will take NOW with this department's real tool and "
                     "what it will produce. If it's about IMPROVING a process/system, say so — that "
                     "belongs to Self-Improvement, not us. 2 sentences, in character."),
            "checker": ("Verify the action is MISSION work our tool can actually do (not an "
                        "improvement matter — those go to Self-Improvement/Power). One sentence "
                        "verdict, one fix if needed."),
            "improver": "One way to do the SAME action faster or with less. 1 sentence.",
            "lead": ("CLOSE now: one line starting 'ACTION:' — the concrete act, its output, who does it."
                     if closing else "Keep it on the act, not on opinions. 1-2 sentences."),
        }.get(role, "One clear point about the action. 1 sentence.")
    else:
        # DEBATE-shaped (decision-heavy tier: improve/power/visualization/accessibility + war/group)
        inst = {
            "doer": ("Make the case for ONE concrete decision: what we should DO and why it's the best "
                     "option for the goal. Name the trade-off you're accepting. 2-4 sentences, in character."),
            "checker": ("Push back on the last idea: name the real risk or a better alternative, and what "
                        "would settle the argument. 2-3 sentences, in character."),
            "improver": "Offer one concrete way to make the plan better, cheaper, or faster. 2 sentences.",
            "lead": ("CONVERGE now: state the call in one line starting 'DECISION:', then what the result "
                     "must deliver and who owns it. In character."
                     if closing else "Steer: weigh the debate so far, keep it on the goal. 2 sentences."),
        }.get(role, "Contribute one clear point. 2 sentences.")
    return (f"You are {sp.get('name')} — {sp.get('persona', '')}\n"
            f"Team law (obey): free-only; real-not-display; quality first; task-relative value.\n"
            f"STYLE (obey): speak in PLAIN LANGUAGE a non-engineer can follow — talk about DECISIONS, "
            f"reasons, and trade-offs, NOT shell commands, code, regex, or file paths. Full sentences. "
            f"NO FILLER (Caveman law): no preamble, no restating the goal, no 'I think we should' — "
            f"every sentence carries new content.\n"
            f"ROOM ({room['kind']}): {room['goal']}\nDone-criteria: {room['done_criteria']}\n"
            + _page_context(room) + _recall_agent(sp) +
            f"Conversation so far:\n{convo}\n\nYour turn. {inst}")


def _artifact(room: dict, decision: str) -> dict | None:
    """M2.6 / Part 3 (owner: 'smallest real thing first'): the room's conclusion becomes a REAL
    committed decision.md — what was decided + a concrete plan, synthesized by the lead from the
    ACTUAL debate. Always produced (engine-written when possible, transcript-summarized as a
    fallback) so a room never closes empty. No commands run; just a written, committed output."""
    hist = [m for m in _history(room, 14) if m.get("agent") != "system"]
    convo = "\n".join(f"{m['name']}: {m['text'][:280]}" for m in hist) or "(brief debate)"
    reg = agents.load_registry()
    cast = _cast(room, reg)
    lead = next((a for a in cast if a.get("role") == "lead"), (cast[0] if cast else {"name": "Lead"}))
    prompt = (f"You are {lead.get('name')}, closing this room. Synthesize the debate into a decision.\n"
              f"GOAL: {room['goal']}\nDEBATE:\n{convo}\n\n"
              "Output GitHub markdown ONLY, no preamble: a one-line '**Decision:**', then a numbered "
              "'**Plan:**' of 3-6 concrete steps drawn from the debate, then '**What changed:**' one line.")
    r = engines.complete(prompt, dept=room.get("dept", ""), difficulty="hard", max_tokens=420)
    body = (r.get("text") or "").strip() if r.get("ok") else ""
    src = f"{r.get('engine', '?')}/{r.get('model', '')}" if r.get("ok") else "transcript-summary (no engine)"
    if not body:                                          # never leave a room without an artifact
        steps = [m["text"][:200] for m in hist][-5:]
        body = ("**Decision:** " + (decision[:200] or room["goal"]) + "\n\n**Plan (from the debate):**\n"
                + "\n".join(f"{i + 1}. {s}" for i, s in enumerate(steps)) + "\n\n**What changed:** first real room artifact.")
    who = ", ".join(dict.fromkeys(m["name"] for m in hist)) or "the room"
    md = (f"# {room['goal']}\n\n"
          f"> Decision artifact · room `{room['id']}` ({room.get('kind', '')}) · {_now()}\n"
          f"> Participants: {who} · synthesized by {src}\n\n{body}\n")
    adir = DATA / "excava" / "artifacts"
    adir.mkdir(parents=True, exist_ok=True)
    (adir / f"{room['id']}.md").write_text(md, encoding="utf-8")
    return {"kind": "decision", "ref": f"data/excava/artifacts/{room['id']}.md",
            "at": _now(), "title": room["goal"][:80], "by": lead.get("name", "lead")}


def advance(room_id: str, turns: int = 2) -> list[str]:
    """Advance one room by up to N real turns. Returns human-readable lines for the beat log."""
    state = load_rooms()
    room = next((r for r in state["rooms"] if r["id"] == room_id), None)
    if not room or room["status"] != "open":
        return []
    reg = agents.load_registry()
    cast = _cast(room, reg)
    log = []
    for _ in range(turns):
        if room["turns"] >= room["max_turns"]:
            break
        sp = _speaker(room, cast)
        dept = sp.get("department", room.get("dept", ""))
        ok, why = leases.acquire(dept or "core", "any")
        if not ok:
            log.append(f"{room['id']}: held — {why}")
            break
        # REAL cross-model debate (owner 2026-07-11: 'it all happens through one engine — Mistral').
        # Round-robin over the canary-HEALTHY pool with a PER-ROOM OFFSET: without the offset,
        # every room's first turn indexed pool[0], so 17 rooms burst the same engine at once and
        # fell through to the lone survivor. The offset spreads rooms across engines while keeping
        # consecutive speakers in one room on DIFFERENT models.
        # Distinct model LINEAGES only (§2) — never two providers of the same llama, never the same
        # family twice in one debate. debate_engines() dedups by lineage; the offset spreads rooms.
        av = engines.debate_engines(4)
        off = sum(ord(ch) for ch in room["id"][-6:])
        eng = av[(off + room["turns"]) % len(av)] if av else None
        r = engines.complete(_prompt(room, sp, _history(room)), engine=eng,
                             dept=dept, difficulty="hard" if sp.get("role") == "lead" else "normal",
                             max_tokens=260)
        if not r["ok"]:
            log.append(f"{room['id']}: no engine here ({r.get('error', '')[:50]}) — resumes in CI")
            break
        time.sleep(2)   # pace: let free-tier per-minute quotas breathe across ~50 turns/cycle
        leases.record(dept or "core", r["engine"], len(r["text"]) // 3 + 200)
        text = r["text"]
        if sp.get("role") == "doer" and room["turns"] == 2:
            text += "\n" + _dispatch_workers(room, sp, random.randint(2, 4))
        _post(room, sp["id"], sp.get("name", sp["id"]), f"{r['engine']}/{r['model']}", text, r["ms"])
        _remember_turn(sp, room, text)      # layer-1 agent memory: what it argued persists
        room["turns"] += 1
        room["last_turn_ms"] = r["ms"]
        log.append(f"{room['id']}: {sp.get('name')} spoke ({r['engine']}, {r['ms']}ms) t{room['turns']}")
        _up = text.strip().upper()
        if _up.startswith(("DECISION:", "ACTION:")) or "DECISION:" in text[:60] or "ACTION:" in text[:60]:
            art = _artifact(room, text)
            room["status"] = "done"
            room["artifact"] = art
            _post(room, "system", "room", "", f"Room closed. Artifact: {json.dumps(art)}", 0)
            bus.event(room["id"], "room_closed", {"artifact": art, "turns": room["turns"]})
            log.append(f"{room['id']}: CLOSED with artifact {art}")
            heavy, _o = _tiers()
            if room.get("kind") == "dept" and room.get("dept") not in heavy:
                # OUTPUT TIER (owner law): the conclusion becomes REAL bus work — mission acts go
                # to the department's own queue; improvement matters REROUTE to improve/power.
                log.append(_act_on_close(room, text.strip().splitlines()[0]))
            else:
                init = _propose_from_decision(room, sp, text)   # initiative: decision-heavy only
                if init:
                    log.append(init)
            break
    if room["turns"] >= room["max_turns"] and room["status"] == "open":
        art = _artifact(room, _history(room, 2)[-1]["text"] if _history(room, 2) else room["goal"])
        room["status"] = "done"
        room["artifact"] = art
        _post(room, "system", "room", "", f"Max turns — lead converged by rule. Artifact: {json.dumps(art)}", 0)
        log.append(f"{room['id']}: max-turns close, artifact {art}")
    save_rooms(state)
    return log


def ensure_default_rooms() -> list[str]:
    """Owner 2026-07-07: rooms are organized BY DEPARTMENT — one live room per department (all 13),
    each labelled by its department + its real focus; plus a cross-department WAR ROOM for the top
    owner task. Idempotent: only opens a department's room if it has none open."""
    opened = []
    reg = agents.load_registry()
    depts = sorted({a.get("department") for a in reg.get("agents", [])
                    if a.get("department") and a.get("department") != "core"})
    intent = _load(DATA / "excava" / "intent.json", {}).get("departments", {})
    state = load_rooms()
    # SELF-HEAL (owner 2026-07-13, complaint persisted): the reshape set NEW output-tier rooms to
    # 3 turns, but rooms opened BEFORE it were grandfathered at 6 and kept debating. Clamp every
    # open output-tier dept room to 3 turns each beat so old rooms actually ACT, not debate.
    heavy, _o = _tiers()
    _clamped = False
    for r in state["rooms"]:
        if (r.get("status") == "open" and r.get("kind") == "dept"
                and r.get("dept") not in heavy and r.get("max_turns", 6) > 3):
            r["max_turns"] = 3
            _clamped = True
    if _clamped:
        save_rooms(state)
    open_depts = {r.get("dept") for r in state["rooms"] if r["status"] == "open" and r.get("kind") == "dept"}
    for d in depts:
        if d in open_depts:
            continue
        focus = (intent.get(d, {}) or {}).get("should_do") or f"advance the {d} department's mission"
        heavy, _o = _tiers()
        r = open_room("dept", f"{d}: {focus[:90]}", dept=d,
                      max_turns=6 if d in heavy else 3,   # output tier: brief, then ACT (owner law)
                      artifact_kind="bus-task")
        opened.append(r["id"])
    # a persistent GROUP CHAT — ANY agent, ANY department (owner's spec: "any agent regardless of
    # department can talk and create the best thing… scroll through all the chats, marked by day").
    if not any(r.get("kind") == "group" and r["status"] == "open" for r in state["rooms"]):
        r = open_room("group", "Open floor — any agent from any department: name the single best "
                      "cross-department improvement to make right now, and who should do it.",
                      dept="", max_turns=60, artifact_kind="bus-task")
        opened.append(r["id"])
    b = bus.read_bus()                                  # a cross-department WAR ROOM for the top owner task
    owner = [t for t in b.get("tasks", []) if t.get("priority") == 0 and t["status"] in ("queued", "working")]
    if owner and not any(r.get("kind") == "war" and r["status"] == "open" for r in load_rooms()["rooms"]):
        r = open_room("war", f"Deliver: {owner[0]['title'][:80]}", dept=owner[0].get("department", ""),
                      done_criteria="a concrete artifact exists and the bus task can complete",
                      max_turns=8, artifact_kind="package")
        opened.append(r["id"])
    return opened


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--demo", action="store_true", help="open+advance a war room now")
    ap.add_argument("--advance", action="store_true", help="advance all open rooms")
    ap.add_argument("--turns", type=int, default=4)
    a = ap.parse_args()
    if a.demo:
        ensure_default_rooms()
    state = load_rooms()
    for r in [x for x in state["rooms"] if x["status"] == "open"]:
        for line in advance(r["id"], a.turns):
            print(" ", line)
    st = load_rooms()
    print(f"rooms: {sum(1 for r in st['rooms'] if r['status'] == 'open')} open, "
          f"{sum(1 for r in st['rooms'] if r['status'] == 'done')} done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
