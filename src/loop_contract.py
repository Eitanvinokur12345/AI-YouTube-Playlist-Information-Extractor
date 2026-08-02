"""
src/loop_contract.py — makes the GO AWAY MODE contract ENFORCEABLE instead of advisory.

THE PROBLEM. `data/excava/away_mode.json` was read by no code at all (verified 2026-07-30: a grep
for `away_mode` across every .py/.yml/.js returned the file and zero consumers). Every rule in it
was obeyed only because each fire happened to open it. A fire that skipped it broke no check,
tripped no guardrail, and produced no signal. Compliance was unverifiable.

This module closes that. It owns the three mechanisms the 2026-07 run showed were missing:

  1. CONTRACT ACK — a fire records that it read the contract. `standing_checks` reports a fire
     that did not, so drift is visible instead of silent.
  2. CARRY-OVER — `current_increment.json` lets one piece of real work span several fires. Without
     it every fire must start AND finish something inside its own window, which is precisely why
     81 fires produced mostly plumbing: plumbing is what fits in one window.
  3. META-FIRE CAP — counts consecutive fires that touched only the loop's own machinery. After
     the configured limit the next fire MUST advance the product. The previous run diagnosed this
     bias five separate times in its own self-criticism and never once broke it, because nothing
     was counting.

Free, stdlib. Run:
    python -m src.loop_contract status
    python -m src.loop_contract ack --fire 83
    python -m src.loop_contract start "Tool class (class 2 of 5)" --kind product
    python -m src.loop_contract note "wrapped 3 repos as callable adapters"
    python -m src.loop_contract finish
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
EXC = ROOT / "data" / "excava"
CONTRACT = EXC / "away_mode.json"
GATES = EXC / "gates.json"
INCREMENT = EXC / "current_increment.json"
LOOP_STATE = EXC / "loop_state.json"

# A fire is META when it only touches the loop's own machinery; PRODUCT when it advances the
# thing Eitan actually uses. The cap exists because meta work is what fits in one fire window.
KINDS = ("product", "meta")
DEFAULT_META_CAP = 3


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load(p: Path, d):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return d


def _save(p: Path, d) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")


def contract() -> dict:
    return _load(CONTRACT, {})


def state() -> dict:
    return _load(LOOP_STATE, {"acks": [], "recent_kinds": [], "fires": 0})


def gates() -> list:
    """Every P5 pitch-gate. A gate with verdict None is OPEN and BLOCKS the work it names.

    Eitan's decision 2026-08-02: gates bind BOTH loops — this session and the away loop that
    ships to main. Until now a gate was prose in EXCAVA_END_PLAN.md that a session had to
    notice and choose to honour, which is precisely how the Router gate was built straight
    through on 2026-08-01. Prose cannot bind a process that never reads it; a file both loops
    already check at the top of every fire can.
    """
    return _load(GATES, {}).get("gates", [])


def open_gates() -> list:
    return [g for g in gates() if not g.get("verdict")]


def gate_blocks(text: str) -> list:
    """Open gates whose `blocks` description overlaps what a fire is about to do.

    Deliberately a coarse keyword overlap, not a clever matcher: a gate that fails OPEN (warns
    on something harmless) costs a sentence, while one that fails CLOSED lets an overhaul
    through — the exact failure this exists to stop.
    """
    words = set(_norm_words(text))
    hits = []
    for g in open_gates():
        target = _norm_words(f"{g.get('blocks','')} {g.get('question','')}")
        if words & set(target):
            hits.append(g)
    return hits


def _norm_words(s: str) -> list:
    import re as _re
    stop = {"the", "a", "an", "or", "and", "to", "of", "on", "in", "is", "it", "any", "for",
            "with", "that", "this", "not", "no", "be", "are", "as", "at", "by", "from"}
    return [w for w in _re.findall(r"[a-z0-9]+", str(s).lower()) if len(w) > 2 and w not in stop]


def set_gate(gid: str, verdict: str, note: str = "") -> bool:
    d = _load(GATES, {"gates": []})
    for g in d.get("gates", []):
        if g.get("id") == gid:
            g["verdict"] = verdict
            g["note"] = note or g.get("note", "")
            g["decided_at"] = _now()[:10]
            _save(GATES, d)
            return True
    return False


def meta_cap() -> int:
    for r in contract().get("rules", []):
        if "META-FIRE CAP" in r:
            for tok in r.split():
                if tok.isdigit():
                    return int(tok)
    return DEFAULT_META_CAP


# ── 1. contract acknowledgement ────────────────────────────────────────────────
def ack(fire: str | int = "?") -> dict:
    """Record that this fire READ the contract. Without this the contract is advisory."""
    st = state()
    st["fires"] = int(st.get("fires", 0)) + 1
    st["acks"] = ([{"fire": str(fire), "at": _now()}] + st.get("acks", []))[:50]
    st["last_ack"] = _now()
    _save(LOOP_STATE, st)
    return st


def acked_recently(within_hours: float = 6.0) -> bool:
    last = state().get("last_ack")
    if not last:
        return False
    try:
        d = datetime.fromisoformat(last)
        if d.tzinfo is None:
            d = d.replace(tzinfo=timezone.utc)
        return (datetime.now(timezone.utc) - d).total_seconds() <= within_hours * 3600
    except Exception:
        return False


# ── 2. carry-over increment ───────────────────────────────────────────────────
def start(title: str, kind: str = "product", plan: str = "") -> dict:
    """Open an increment that MAY span several fires."""
    inc = {"title": title, "kind": kind if kind in KINDS else "product", "plan": plan,
           "started_at": _now(), "fires": 1, "notes": [], "status": "open"}
    _save(INCREMENT, inc)
    _record_kind(inc["kind"])
    return inc


def current() -> dict | None:
    inc = _load(INCREMENT, None)
    return inc if inc and inc.get("status") == "open" else None


def note(text: str) -> dict | None:
    """Append progress to the open increment and count this fire against it."""
    inc = current()
    if not inc:
        return None
    inc["notes"] = (inc.get("notes", []) + [{"at": _now(), "text": text}])[-20:]
    inc["fires"] = int(inc.get("fires", 1)) + 1
    _save(INCREMENT, inc)
    _record_kind(inc.get("kind", "product"))
    return inc


def finish(outcome: str = "") -> dict | None:
    inc = current()
    if not inc:
        return None
    inc["status"] = "done"
    inc["finished_at"] = _now()
    inc["outcome"] = outcome
    _save(INCREMENT, inc)
    return inc


# ── 3. meta-fire cap ──────────────────────────────────────────────────────────
def _record_kind(kind: str) -> None:
    st = state()
    st["recent_kinds"] = ([kind] + st.get("recent_kinds", []))[:20]
    _save(LOOP_STATE, st)


def consecutive_meta() -> int:
    n = 0
    for k in state().get("recent_kinds", []):
        if k == "meta":
            n += 1
        else:
            break
    return n


def must_do_product() -> bool:
    """True when the cap is hit — the next fire is REQUIRED to advance the product."""
    return consecutive_meta() >= meta_cap()


# ── report ────────────────────────────────────────────────────────────────────
def status() -> dict:
    c = contract()
    inc = current()
    return {
        "contract_present": bool(c),
        "always_on": c.get("mode") == "always_on",
        "away": bool(c.get("away")),
        "acked_recently": acked_recently(),
        "last_ack": state().get("last_ack"),
        "fires_recorded": state().get("fires", 0),
        "open_increment": ({"title": inc["title"], "kind": inc["kind"], "fires": inc["fires"]}
                           if inc else None),
        "consecutive_meta_fires": consecutive_meta(),
        "meta_cap": meta_cap(),
        "must_do_product_next": must_do_product(),
        "open_gates": [{"id": g.get("id"), "blocks": g.get("blocks", "")} for g in open_gates()],
    }


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="GO AWAY MODE contract enforcement")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    g_ = sub.add_parser("gate", help="decide a P5 pitch-gate (Eitan only)")
    g_.add_argument("gate_id"); g_.add_argument("--verdict", required=True,
                                                choices=["go", "no", "changed"])
    g_.add_argument("--note", default="")
    sub.add_parser("gates", help="list every P5 gate and whether it is open")
    a_ = sub.add_parser("ack"); a_.add_argument("--fire", default="?")
    s_ = sub.add_parser("start"); s_.add_argument("title")
    s_.add_argument("--kind", default="product", choices=list(KINDS))
    s_.add_argument("--plan", default="")
    n_ = sub.add_parser("note"); n_.add_argument("text")
    f_ = sub.add_parser("finish"); f_.add_argument("outcome", nargs="?", default="")
    a = ap.parse_args()

    if a.cmd == "status":
        st = status()
        print(f"contract: {'always-on' if st['always_on'] else 'present' if st['contract_present'] else 'MISSING'}"
              f" · away={st['away']} · acked_recently={st['acked_recently']}")
        inc = st["open_increment"]
        print(f"open increment: {inc['title']} ({inc['kind']}, {inc['fires']} fire(s))" if inc
              else "open increment: none — next fire starts one")
        if st["open_gates"]:
            print(f"!! {len(st['open_gates'])} OPEN P5 GATE(S) — binding on BOTH loops, only Eitan decides:")
            for g in st["open_gates"]:
                print(f"     {g['id']}: {g['blocks'][:76]}")
        print(f"consecutive meta fires: {st['consecutive_meta_fires']}/{st['meta_cap']}"
              + ("  ->  NEXT FIRE MUST ADVANCE THE PRODUCT" if st["must_do_product_next"] else ""))
        return 0
    if a.cmd == "gates":
        gs = gates()
        if not gs:
            print("no gates on file"); return 0
        for g in gs:
            v = g.get("verdict")
            print(f"  [{'OPEN — BLOCKING' if not v else v.upper():>15}] {g.get('id')}")
            print(f"        blocks: {g.get('blocks','')[:88]}")
        n = len(open_gates())
        print(f"\n{n} gate(s) OPEN — these bind BOTH loops; only Eitan decides them."
              if n else "\nno open gates — nothing is blocked.")
        return 0
    if a.cmd == "gate":
        ok = set_gate(a.gate_id, a.verdict, a.note)
        print(f"gate {a.gate_id} -> {a.verdict}" if ok else f"no gate {a.gate_id}")
        return 0 if ok else 1
    if a.cmd == "ack":
        ack(a.fire); print(f"contract acknowledged (fire {a.fire})"); return 0
    if a.cmd == "start":
        inc = start(a.title, a.kind, a.plan); print(f"increment OPEN: {inc['title']} [{inc['kind']}]"); return 0
    if a.cmd == "note":
        inc = note(a.text)
        print(f"noted on '{inc['title']}' (fire {inc['fires']})" if inc else "no open increment"); return 0 if inc else 1
    if a.cmd == "finish":
        inc = finish(a.outcome)
        print(f"increment DONE after {inc['fires']} fire(s): {inc['title']}" if inc else "no open increment")
        return 0 if inc else 1
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
