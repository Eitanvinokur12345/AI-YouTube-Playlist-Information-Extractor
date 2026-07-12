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

# GROUNDING v2 (owner 2026-07-12: build an artifact-output-ratio metric — the vocabulary audit
# rated Creators 0% self-improvement while its rooms were debating a FICTIONAL Rust/cargo
# project with zero connection to the real package builder). Two cheap, honest signals:
#  1. FOREIGN-STACK markers this repo never uses (Python/JS/JSON only) — a near-certain
#     hallucination flag when they appear in a decision.
#  2. REAL PATH grounding — does the decision reference a file that actually exists here.
FOREIGN_STACK = re.compile(
    r"\b(cargo|rustc|npm install|pip install|mvn|gradle|go mod|docker build|"
    r"dotnet|composer require|yarn add)\b", re.I)
REAL_PATH = re.compile(r"[\w][\w./-]{2,60}\.(?:json|py|md|jsonl|js)\b")


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
                                  "si_examples": [], "hallucinated": 0, "grounded": 0,
                                  "hallucination_examples": []})
        p["total"] += 1
        p[verdict] += 1
        if verdict == "self-improvement" and len(p["si_examples"]) < 2:
            first = next((l.strip() for l in txt.splitlines()
                          if l.strip() and not l.startswith(("#", ">"))), "")[:110]
            p["si_examples"].append({"file": f.name, "gist": first})
        # GROUNDING v2: foreign-stack mention = near-certain hallucination (this repo is
        # Python/JS/JSON only); a real existing path = grounded in what actually ships.
        foreign = FOREIGN_STACK.search(txt)
        paths = REAL_PATH.findall(txt)
        real_hit = any((ROOT / pth).exists() or (ROOT / "data" / pth).exists()
                       or (ROOT / "src" / pth).exists() for pth in paths)
        if foreign:
            p["hallucinated"] += 1
            if len(p["hallucination_examples"]) < 2:
                p["hallucination_examples"].append({"file": f.name,
                    "flag": foreign.group(0), "gist": txt.split("**Decision:**")[-1][:120].strip()})
        elif real_hit:
            p["grounded"] += 1
    for d, p in per.items():
        p["si_pct"] = round(100 * p["self-improvement"] / max(p["total"], 1))
        p["grounded_pct"] = round(100 * p["grounded"] / max(p["total"], 1))
        p["hallucinated_pct"] = round(100 * p["hallucinated"] / max(p["total"], 1))
        p["artifact_output_ratio"] = round(p["grounded"] / max(p["total"] - p["hallucinated"], 1), 2)
    total = sum(p["total"] for p in per.values())
    si_total = sum(p["self-improvement"] for p in per.values())
    hall_total = sum(p["hallucinated"] for p in per.values())
    report = {"generated_at": datetime.now(timezone.utc).isoformat(),
              "decisions_audited": total,
              "self_improvement_pct_overall": round(100 * si_total / max(total, 1)),
              "hallucinated_pct_overall": round(100 * hall_total / max(total, 1)),
              "per_department": per,
              "rule": "SI-type decisions belong to the improve department's external arms; "
                      "departments keep mission decisions (owner law 2026-07-11).",
              "metric_v2": "artifact_output_ratio = grounded decisions / (total - hallucinated). "
                           "1.0 = every non-hallucinated decision references something real that "
                           "ships. hallucinated_pct = decisions inventing a foreign tech stack "
                           "(owner caught: Creators debating a fictional Rust/cargo project).",
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
          f"{r['self_improvement_pct_overall']}% self-improvement, "
          f"{r['hallucinated_pct_overall']}% hallucinated (foreign tech stack)")
    for d, p in sorted(r["per_department"].items(), key=lambda x: -x[1]["hallucinated_pct"]):
        print(f"  {d:<14} hallucinated {p['hallucinated_pct']:>3}%  grounded {p['grounded_pct']:>3}%  "
              f"ratio={p['artifact_output_ratio']}  SI {p['si_pct']:>3}%  ({p['total']} decisions)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
