"""
src/decision_audit.py — DECISION AUDIT (owner 2026-07-11, priority 0): "a lot of the decisions
in the departments are actually SELF-IMPROVEMENT for the department… examine the decisions and
see what is really about their goals and what is actually self-improvement."

Method (mechanical, engine-free): every decision artifact (data/excava/artifacts/*.md) is scored
against two vocabularies —
  MISSION  = the department's own charter words (agents.json specialization + intent should_do)
  SELF-IMP = the improve-the-machine vocabulary (interface, prompts, engines, rooms, workflow…)
minus any words that are legitimately the department's charter (visualization's 'interface'
decisions ARE its mission). Higher score wins; ties = 'mixed'.

Output: data/excava/decision_audit.json (per-dept counts + drift pct + worst examples).
The supervisor reads it and flags departments that mostly navel-gaze; SI-type decisions
belong to the improve department's EXTERNAL ARMS (next layer: an SI liaison per dept).
Run: python -m src.decision_audit
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
ART = ROOT / "data" / "excava" / "artifacts"
OUT = ROOT / "data" / "excava" / "decision_audit.json"

SELF_IMP = {"interface", "dashboard", "screen", "panel", "tab", "card", "button", "layout",
            "prompt", "prompts", "agent", "agents", "room", "rooms", "engine", "engines",
            "workflow", "process", "pipeline", "excava", "formation", "debate", "summary",
            "contrast", "focus", "navigation", "changelog", "standardize", "refactor"}


def _dept_vocab() -> dict[str, set]:
    reg = json.load(open(ROOT / "data" / "excava" / "agents.json", encoding="utf-8"))
    intent = json.load(open(ROOT / "data" / "excava" / "intent.json", encoding="utf-8")).get("departments", {})
    vocab = {}
    for d, spec in (reg.get("departments") or {}).items():
        words = set()
        for s in spec.get("specialization", []):
            words |= set(re.findall(r"[a-z]{4,}", s.lower()))
        words |= set(re.findall(r"[a-z]{5,}", (spec.get("purpose", "") + " "
                     + intent.get(d, {}).get("should_do", "")).lower()))
        vocab[d] = words
    return vocab


def audit() -> dict:
    vocab = _dept_vocab()
    rooms = {}
    try:                                          # authoritative room->dept/kind map
        for r in json.load(open(ROOT / "data" / "excava" / "rooms.json",
                                encoding="utf-8")).get("rooms", []):
            rooms[r["id"]] = (r.get("kind", ""), r.get("dept", ""))
    except Exception:
        pass
    per: dict[str, dict] = {}
    for f in sorted(ART.glob("*.md")):
        try:
            txt = f.read_text(encoding="utf-8")
        except Exception:
            continue
        rid = (re.search(r"room `([^`]+)`", txt) or [None, f.stem])[1]
        kind, dept = rooms.get(rid, ("", ""))
        if not dept:
            m = re.match(r"dept-([a-z]+)", f.stem)
            dept = m.group(1) if m and m.group(1) in vocab else \
                ("war-room" if f.stem.startswith("war-") else
                 "group-chat" if f.stem.startswith("group-") else "unattributed")
        if kind == "war":
            dept = "war-room"
        elif kind == "group":
            dept = "group-chat"
        body = txt.lower()
        words = set(re.findall(r"[a-z]{4,}", body))
        mission_words = vocab.get(dept, set())
        si_words = SELF_IMP - mission_words          # charter words never count as navel-gazing
        mi, si = len(words & mission_words), len(words & si_words)
        verdict = "mission" if mi > si else "self-improvement" if si > mi else "mixed"
        p = per.setdefault(dept, {"total": 0, "mission": 0, "self-improvement": 0, "mixed": 0,
                                  "si_examples": []})
        p["total"] += 1
        p[verdict] += 1
        if verdict == "self-improvement" and len(p["si_examples"]) < 2:
            first = next((l.strip() for l in txt.splitlines()
                          if l.strip() and not l.startswith(("#", ">"))), "")[:110]
            p["si_examples"].append({"file": f.name, "gist": first})
    for d, p in per.items():
        p["si_pct"] = round(100 * p["self-improvement"] / max(p["total"], 1))
    total = sum(p["total"] for p in per.values())
    si_total = sum(p["self-improvement"] for p in per.values())
    report = {"generated_at": datetime.now(timezone.utc).isoformat(),
              "decisions_audited": total,
              "self_improvement_pct_overall": round(100 * si_total / max(total, 1)),
              "per_department": per,
              "rule": "SI-type decisions belong to the improve department's external arms; "
                      "departments keep mission decisions (owner law 2026-07-11).",
              "next_layer": "SI liaison agent per department (tier-2.5) routes these."}
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    return report


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    r = audit()
    print(f"decision-audit: {r['decisions_audited']} decisions; "
          f"{r['self_improvement_pct_overall']}% are self-improvement, not mission")
    for d, p in sorted(r["per_department"].items(), key=lambda x: -x[1]["si_pct"]):
        print(f"  {d:<14} {p['si_pct']:>3}% SI  ({p['self-improvement']}/{p['total']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
