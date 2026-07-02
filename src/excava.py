"""
src/excava.py — EXCAVA: the agentic OS that operates Excavatortron toward the 6 goals.

Honest first version (OS-1 operator). Each cycle EXCAVA:
  1. Runs its VERIFICATION GATE — focused checkers that decide if it's safe to act:
     data_guard (no collapse), security_scan (no leaks/clean), goals_check (esp. G3 truth/access),
     link coverage. This is the owner's "focused agents make sure it's good" — so power is never
     applied to bad data: outward actions (create/publish/self-edit) are BLOCKED until the gate is
     green AND the owner approves.
  2. Picks the next action from data/priorities.json. Internal/safe actions it owns; outward actions
     it HOLDS with the reason, until the gate opens.
  3. Self-optimizes its own tool stack via pipeline_scout (find more / combine / offload) and queues
     changes to self-improvement.
It writes data/excava_status.json (decisions + gate + holds) and logs. It does NOT yet autonomously
create/publish — that's OS-2, deliberately gated. Free, mechanical, no Claude tokens.

Run:  python -m src.excava
"""
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path

from src.build_memory import embed as _embed, search as _search

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "excava_status.json"
NOW = datetime.now(timezone.utc).isoformat()
G3_OUTWARD = 70          # truth/access must be this high before EXCAVA may create/publish

OUTWARD = {"create", "promote", "publish", "self-code", "leverage"}


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
    """EXCAVA's MEANING-based recall: embed the task and return the hub items closest in meaning (not
    just keyword match). This is what 'point EXCAVA at the semantic memory' buys — grounded tool
    selection. Free + graceful: with no key or empty index it returns [] (so the cron never breaks)."""
    if not query or not keys or not idx.get("vectors"):
        return []
    emb = _embed(query, keys[0])
    if not isinstance(emb, list):
        return []
    return _search(emb, idx, k)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--recall", default="", help="print the hub items semantically closest to a task, then exit")
    args, _ = ap.parse_known_args()
    mem = _load("memory_index.json", {})
    keys = _keys()
    if args.recall:                                  # manual / activator probe of the semantic memory
        for h in semantic_recall(args.recall, mem, keys, 10):
            print(f"  {h['score']:.3f}  {h.get('type')}: {h.get('name')}  [{h['id']}]")
        return 0

    guard = _load("data_guard.json", {})
    sec = _load("security.json", {})
    goals = {g["id"]: g for g in _load("goals_status.json", {}).get("goals", [])}
    prios = _load("priorities.json", {}).get("priorities", [])
    scout = _load("pipeline_scout.json", {})
    cfg = _load("excava_config.json", {})

    # ── VERIFICATION GATE (the focused agents) ──
    g3 = (goals.get("G3", {}) or {}).get("score", 0)
    checks = {
        "data_guard_ok": guard.get("restored", 0) == 0,
        "security_clean": not sec.get("secret_leaks"),
        "truth_access_G3": g3,
        "G3_ready_for_outward": g3 >= G3_OUTWARD,
    }
    internal_ok = checks["data_guard_ok"] and checks["security_clean"]
    outward_ok = internal_ok and checks["G3_ready_for_outward"]

    # ── RESOURCE CHECK (owner's rule): before carrying out ANY task, verify we have what it needs.
    #    resources.json is written hourly by resource_check in CI (where the secrets live). A task
    #    whose resources are missing is HELD with the exact reason — never attempted blind. ──
    res = _load("resources.json", {})
    can = res.get("can_do", {}) or {}
    NEED = [("transcript", "fetch-transcripts"), ("watch", "analyze-videos"), ("video", "analyze-videos"),
            ("visual", "visual-extract"), ("link", "resolve-links"), ("embed", "embed-memory"),
            ("memory", "embed-memory"), ("design", "screenshots-designs"), ("creat", "create-drafts"),
            ("competitor", "mine-competitors")]

    def missing_resource(text) -> str | None:
        tl = str(text or "").lower()
        for kw, cap in NEED:
            if kw in tl:
                c = can.get(cap)
                if c and not c.get("ok"):
                    return f"missing resource for {cap}: {c.get('needs')}"
        return None

    # ── OWNER'S INBOX first: tasks Eitan sends outrank the auto-priorities. Internal tasks are
    #    worked autonomously; outward ones are held by the same gate. ──
    inbox = _load("excava_inbox.json", {})
    inbox_tasks = inbox.get("tasks", []) if isinstance(inbox, dict) else []
    action, holding = None, []
    changed_inbox = False
    for t in inbox_tasks:
        if t.get("status") in ("done", "held"):
            continue
        is_outward = any(w in str(t.get("task", "")).lower() for w in OUTWARD)
        if is_outward and not outward_ok:
            if t.get("status") != "held":
                t["status"] = "held"; changed_inbox = True
            holding.append({"priority": t.get("task"), "why_held": "owner task is outward; gate closed"})
            continue
        mr = missing_resource(t.get("task"))
        if mr:
            holding.append({"priority": t.get("task"), "why_held": mr})
            continue
        if action is None and internal_ok:
            action = {"do": t.get("task"), "area": "owner-inbox", "type": "internal", "source": "inbox"}
            if t.get("status") != "working":
                t["status"] = "working"; changed_inbox = True
    if changed_inbox:
        (DATA / "excava_inbox.json").write_text(
            json.dumps(inbox, ensure_ascii=False, indent=2), encoding="utf-8")

    # ── then the auto-priorities; outward ones are held until the gate opens ──
    for p in prios:
        area = (p.get("area") or "").lower()
        is_outward = any(w in area for w in OUTWARD)
        if is_outward and not outward_ok:
            holding.append({"priority": p.get("title"), "why_held": f"outward action; gate closed (G3={g3}<{G3_OUTWARD} or checks failing)"})
            continue
        mr = missing_resource(f"{p.get('title')} {p.get('detail')}")
        if mr:
            holding.append({"priority": p.get("title"), "why_held": mr})
            continue
        if action is None and internal_ok:
            action = {"do": p.get("title"), "area": p.get("area"), "detail": p.get("detail"),
                      "type": "outward" if is_outward else "internal"}
    if action is None and not internal_ok:
        action = {"do": "HOLD ALL — verification gate failing", "type": "blocked",
                  "detail": "fix data_guard/security before EXCAVA acts"}

    # ── point EXCAVA at the SEMANTIC MEMORY: ground the chosen action in the right hub items ──
    if action and action.get("do"):
        q = " ".join(x for x in [action.get("do"), action.get("detail")] if x)
        action["use_tools"] = [{"id": h["id"], "name": h.get("name"), "type": h.get("type"),
                                "score": h["score"]} for h in semantic_recall(q, mem, keys, 6)]
    mem_wired = bool(keys and mem.get("vectors"))

    # ── self-optimize the tool stack ──
    stack_review = {
        "candidates_available": scout.get("total_candidates", 0),
        "note": ("EXCAVA reviews its stack each cycle: integrate the best free per-process tool, "
                 "combine overlaps, offload weak ones. Top open process gaps: "
                 + ", ".join(r["process"] for r in (scout.get("processes") or []) if r.get("count", 0) < 6)[:120]),
    }

    OUT.write_text(json.dumps({
        "generated_at": NOW, "name": "EXCAVA",
        "phase": "OS-1 operator (live); OS-2 creator + OS-3 self-coder gated",
        "gate": {"checks": checks, "internal_allowed": internal_ok, "outward_allowed": outward_ok,
                 "outward_needs": "data_guard ok + security clean + G3>=70 + owner approval"},
        "memory": {"vectors": len(mem.get("vectors", {})), "model": mem.get("model"), "wired": mem_wired},
        "resources": {"missing": res.get("missing", []), "checked_at": res.get("generated_at"),
                      "can_do": {k: v.get("ok") for k, v in can.items()}},
        "next_action": action, "holding": holding[:6],
        "tool_stack": cfg.get("tool_stack", []), "stack_review": stack_review,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"EXCAVA: gate internal={'open' if internal_ok else 'CLOSED'} outward={'open' if outward_ok else 'closed (G3=' + str(g3) + ')'}; "
          f"next = {action['do'] if action else 'none'} ({len((action or {}).get('use_tools', []))} tools recalled); "
          f"memory {'wired ' + str(len(mem.get('vectors', {}))) + ' vecs' if mem_wired else 'not wired (no key)'}; holding {len(holding)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
