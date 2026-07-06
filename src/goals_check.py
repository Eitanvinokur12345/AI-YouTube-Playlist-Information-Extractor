"""
src/goals_check.py — GOALS AS LAW. Check the system against the 6 North-Star goals every cycle.

The owner: the main goals are above all else; after any self-improvement or change, look there and if
it doesn't fulfill them, change so it does. This reads data/north_star.json + the live state, scores
conformance to each goal (0-100, met/at-risk/unmet), writes data/goals_status.json, and queues every
unmet/at-risk goal into improvement_tasks.json so the system self-corrects toward the goals. Free.

Run:  python -m src.goals_check
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "goals_status.json"
TASKS = DATA / "improvement_tasks.json"
NOW = datetime.now(timezone.utc).isoformat()


def _load(name, d=None):
    try:
        return json.load(open(DATA / name, encoding="utf-8"))
    except Exception:
        return d if d is not None else {}


def _items(name, key):
    d = _load(name, {})
    return d.get(key, []) if isinstance(d, dict) else []


def main() -> int:
    ns = _load("north_star.json", {}).get("goals", [])
    ps = _load("pipeline_status.json", {})
    snap = ps.get("snapshot", {})
    lanes = ps.get("lanes", [])
    live = sum(1 for l in lanes if l.get("status") == "live")
    sc = _load("self_check.json", {})
    tools = _items("tools.json", "tools"); skills = _items("skills.json", "skills")
    allts = tools + skills
    linked = sum(1 for x in allts if x.get("homepage") or x.get("github") or x.get("install_or_source"))
    link_pct = round(100 * linked / max(len(allts), 1), 1)
    tot, anz = snap.get("videos_total", 0), snap.get("videos_analyzed", 0)
    cov = round(100 * anz / max(tot, 1), 1)
    hub = _load("hub.json", {})

    # signal per goal -> (score 0-100, the gap text)
    def band(x):  # score -> status
        return "met" if x >= 75 else ("at-risk" if x >= 45 else "unmet")

    sig = {
        "G1": (min(100, cov + 30 if live >= 4 else cov),
               f"{anz}/{tot} videos analyzed ({cov}%); {live}/{len(lanes)} lanes live"),
        "G2": (int((sc.get("score", 0) / max(sc.get("total", 50), 1)) * 100) if sc else 40,
               f"self-check {sc.get('score','?')}/{sc.get('total',50)}"),
        "G3": (link_pct, f"{link_pct}% of tools/skills have a real link (target: ~100%)"),
        "G4": (min(100, 50 + live * 8), f"{live} lanes self-running"),
        "G5": (link_pct, "leverage needs real, usable links first (= G3); then the OS creation agent"),
        "G6": (90 if hub.get("generated_at") else 20,
               "hub.json is live + machine-readable" if hub.get("generated_at") else "hub.json missing"),
    }

    # G7 Security & trust — scan clean + pre-flight scanner + activator security gate all in place
    sec = _load("security.json", {})
    g7 = 0
    g7 += 40 if not sec.get("secret_leaks") else 0
    g7 += 30 if (ROOT / "src" / "security_preflight.py").exists() else 0
    try:
        act = (ROOT / "activator" / "SKILL.md").read_text(encoding="utf-8")
    except Exception:
        act = ""
    g7 += 30 if "Security pre-flight" in act else 0
    sig["G7"] = (g7, f"scan {'clean' if not sec.get('secret_leaks') else 'LEAKS FOUND'}; "
                     f"pre-flight scanner {'present' if g7 >= 70 else 'missing'}; activator gate "
                     f"{'wired' if 'Security pre-flight' in act else 'missing'} (behavioral sandbox = next level)")

    # G8 Personal fit — taste-tagged designs + Arena taste-learning + NOSG protocol
    designs = _items("designs.json", "designs")
    tagged = sum(1 for x in designs if x.get("style_tags"))
    tag_pct = round(100 * tagged / max(len(designs), 1))
    try:
        dash = (ROOT / "docs" / "dashboard.js").read_text(encoding="utf-8")
    except Exception:
        dash = ""
    g8 = (40 * tag_pct // 100) + (30 if "arenaVote" in dash else 0) + (30 if "NOSG" in act else 0)
    sig["G8"] = (g8, f"{tag_pct}% of designs taste-tagged; Arena learning "
                     f"{'live' if 'arenaVote' in dash else 'missing'}; NOSG "
                     f"{'wired' if 'NOSG' in act else 'missing'} (next: taste beyond designs)")

    # G9 Agency/Orchestration (added 2026-07-03, owner-approved): is the OS truly agentic?
    ex = _load("excava_status.json", {})
    osx = ex.get("os", {}) or {}
    bus_ = _load("excava/bus.json", {})
    handoff_docs = sum(len(t.get("handoff_docs", [])) for t in bus_.get("tasks", []))
    done = sum(1 for t in bus_.get("tasks", []) if t.get("status") == "done")
    depts = len(osx.get("departments", []) or [])
    g9 = ((20 if (osx.get("beats") or 0) > 0 else 0)
          + (20 if handoff_docs else 0)
          + (20 if depts >= 10 else depts * 2)
          + (20 if (osx.get("audit") or {}).get("ok") else 0)
          + (20 if done else 0))
    sig["G9"] = (g9, f"beats {osx.get('beats', 0)}; {handoff_docs} hand-off docs; {done} tasks done; "
                     f"{depts} departments; audit {'ok' if (osx.get('audit') or {}).get('ok') else 'failing/missing'} "
                     "(next: more departments executing, not just assessing)")

    # ── HONESTY CAP (owner order 2026-07-06): G4 Autonomy + G9 Agency scored off PROXIES (lanes,
    #    beats, dept count) while the actual agentic behaviour — agents CONVERSING and PRODUCING —
    #    has never happened (every engine call fails: see beat_log "no engine here"). Until a real
    #    conversation turn or artifact exists, cap both at 30. The cap LIFTS itself the moment the
    #    engines answer and rooms advance, so the score can only rise on real evidence. ──
    real_turns = 0
    for cf in (ROOT / "data" / "excava" / "chats").glob("**/*.jsonl"):
        try:
            for ln in cf.read_text(encoding="utf-8").splitlines():
                if ln.strip() and '"agent": "system"' not in ln:
                    real_turns += 1
        except Exception:
            pass
    rooms_ = _load("excava/rooms.json", {})
    real_artifacts = sum(1 for r in rooms_.get("rooms", []) if r.get("artifact"))
    # Graduated honesty ladder (owner order 2026-07-06): the score rises only on real evidence.
    #   0 turns → 30 (dead) · turns but 0 artifacts → 50 (deliberates, doesn't produce) ·
    #   1-2 artifacts → 65 (PROVEN but early) · 3+ artifacts → uncapped (produces work routinely).
    if real_artifacts < 3:
        cap = 30 if real_turns == 0 else (50 if real_artifacts == 0 else 65)
        note = ("no real agent conversation yet (engines not answering)" if real_turns == 0
                else f"{real_turns} real turns but 0 artifacts — deliberates, doesn't execute" if real_artifacts == 0
                else f"{real_artifacts} real artifact(s) produced — PROVEN but early (need 3+ to uncap)")
        for gid in ("G4", "G9"):
            s0, gap0 = sig.get(gid, (cap, ""))
            sig[gid] = (min(s0, cap), gap0 + f" — CAPPED {cap}: {note}")

    out = []
    for g in ns:
        score, gap = sig.get(g["id"], (50, ""))
        out.append({"id": g["id"], "name": g["name"], "concept": g["concept"],
                    "score": int(score), "status": band(score), "gap": gap})

    OUT.write_text(json.dumps({"generated_at": NOW, "overall": round(sum(o["score"] for o in out) / max(len(out), 1)),
                               "goals": out}, ensure_ascii=False, indent=2), encoding="utf-8")

    # queue unmet/at-risk goals so the system self-corrects toward them
    tj = _load("improvement_tasks.json", {"tasks": []}) or {"tasks": []}
    tasks = tj.get("tasks", [])
    have = {t.get("goal_key") for t in tasks}
    added = 0
    for o in out:
        if o["status"] != "met":
            k = f"goal:{o['id']}:{o['status']}"
            if k not in have:
                tasks.append({"goal_key": k, "kind": "goal", "goal": o["id"],
                              "question": f"[goal {o['id']} {o['name']}] {o['status']} ({o['score']}/100)",
                              "fix": f"Advance goal {o['id']}: {o['gap']}.", "status": "open", "created_at": NOW})
                added += 1
    if added:
        TASKS.write_text(json.dumps({"updated_at": NOW, "tasks": tasks}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"goals_check: overall {round(sum(o['score'] for o in out)/max(len(out),1))}/100; "
          + ", ".join(f"{o['id']}={o['score']}({o['status']})" for o in out) + f"; queued {added}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
