"""
src/or1_rubric_index.py — makes OR-1's finished debate output findable and usable.

THE PROBLEM (found fire 123, 2026-08-08). OR-1 ("Define what makes an element GOOD — per
element type and per package", value 95, top of backlog.json since fire 98) ran its full
phase 1 -> phase 2 -> phase 3 -> phase 4 multi-model debate for all 10 element types back on
2026-08-03 (`python -m src.excava_chat`, verified: 40 clean artifact files, 0 failed drafts,
4 live model families per type — DeepSeek V4, GLM-5.2, Kimi K2.7, GPT-4o-mini). That is the
expensive, hard-to-fake part of OR-1 and it is DONE. But `grep -rl or1-phase4 src/` before this
file existed matched exactly one hit (`or1_phase_test.py`, a regression test that fakes the
engines) — no code and no doc pointed a reader at the 40 real files sitting in
`data/excava/artifacts/`. That is the exact "orphaned, nothing wired" failure this repo's own
CLAUDE.md warns about: real work, zero surface.

WHAT THIS ADDS. A deterministic (no LLM, no network) index over the existing artifacts:
    python -m src.or1_rubric_index summary          # one line per element type, ready to read
    python -m src.or1_rubric_index show tool         # phase 4 (final) guideline, all 4 families
    python -m src.or1_rubric_index show tool --phase 1

WHAT THIS DELIBERATELY DOES NOT DO. Phase 4 holds FOUR competing "final guideline" texts per
element type (one per model family) that never converged into ONE canonical rubric — no fifth
synthesis/vote pass exists. Picking a winner (or merging them) is an editorial call that changes
how ~11k elements get judged; that is Eitan's decision to make with the real text in front of
him, not this script's to guess at. This tool's job stops at "here are the 4 candidate
guidelines, side by side, one command away" — it does not write, merge, or apply a rubric, and
it does not touch `quality_score` on any element.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
ARTIFACTS = ROOT / "data" / "excava" / "artifacts"
INDEX_OUT = ROOT / "data" / "excava" / "or1_rubrics_index.json"

PHASES = {
    1: "independent brainstorm",
    2: "integration discussion",
    3: "adversarial re-review",
    4: "resolution — final guideline",
}
DRAFT_KEY = {1: "drafts", 2: "drafts", 3: "drafts", 4: "final_drafts"}


def _load(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None


def element_types() -> list[str]:
    types = set()
    for f in ARTIFACTS.glob("or1-phase1-*.json"):
        types.add(f.stem.split("or1-phase1-", 1)[1])
    return sorted(types)


def load_phase(element_type: str, phase: int) -> dict | None:
    return _load(ARTIFACTS / f"or1-phase{phase}-{element_type}.json")


def build_index() -> dict:
    """Deterministic catalog: per type, per phase — is it present, who drafted, how long."""
    out = {"generated_by": "src.or1_rubric_index", "types": {}}
    for t in element_types():
        entry = {"phases": {}}
        for phase in (1, 2, 3, 4):
            d = load_phase(t, phase)
            if not d:
                entry["phases"][str(phase)] = {"present": False}
                continue
            drafts = d.get(DRAFT_KEY[phase], [])
            entry["phases"][str(phase)] = {
                "present": True,
                "label": PHASES[phase],
                "families_used": d.get("families_used", []),
                "agents": [dr.get("agent") for dr in drafts],
                "families": [dr.get("family") for dr in drafts],
                "all_ok": all(dr.get("ok", True) and dr.get("text", "").strip() for dr in drafts),
                "chars": sum(len(dr.get("text", "")) for dr in drafts),
            }
        entry["phase4_converged"] = False  # 4 competing finals, never merged into 1 — see module docstring
        out["types"][t] = entry
    return out


def refresh() -> dict:
    idx = build_index()
    INDEX_OUT.write_text(json.dumps(idx, ensure_ascii=False, indent=1), encoding="utf-8")
    return idx


def summary() -> str:
    idx = _load(INDEX_OUT) or build_index()
    lines = [f"OR-1 rubric debate coverage — {len(idx['types'])} element types"]
    for t, entry in sorted(idx["types"].items()):
        p4 = entry["phases"].get("4", {})
        if not p4.get("present"):
            lines.append(f"  {t:<10} NOT STARTED")
            continue
        fams = ", ".join(p4.get("families", []))
        ok = "clean" if p4.get("all_ok") else "HAS FAILED DRAFTS"
        lines.append(f"  {t:<10} phase 4 done ({ok}) — {len(p4.get('agents', []))} guidelines: {fams}")
    lines.append("")
    lines.append("Every type has 4 competing phase-4 'final' guidelines, not yet converged into one —")
    lines.append("run `python -m src.or1_rubric_index show <type>` to read them side by side.")
    return "\n".join(lines)


def show(element_type: str, phase: int = 4) -> str:
    d = load_phase(element_type, phase)
    if not d:
        return f"no phase {phase} artifact for element type {element_type!r}. Known types: {', '.join(element_types())}"
    drafts = d.get(DRAFT_KEY[phase], [])
    lines = [f"OR-1 phase {phase} ({PHASES.get(phase, '?')}) — element type: {element_type}",
             f"families used: {', '.join(d.get('families_used', []))}", ""]
    for dr in drafts:
        lines.append(f"{'=' * 70}")
        lines.append(f"{dr.get('agent')} — {dr.get('family')} ({dr.get('engine')}/{dr.get('model')})")
        lines.append(f"{'=' * 70}")
        lines.append(dr.get("text", "").strip())
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="Index + browse OR-1's finished per-type rubric debates")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("refresh", help="rebuild data/excava/or1_rubrics_index.json from the artifact files")
    sub.add_parser("summary", help="one line per element type")
    s_ = sub.add_parser("show", help="print a phase's full guideline text for one element type")
    s_.add_argument("element_type")
    s_.add_argument("--phase", type=int, default=4, choices=[1, 2, 3, 4])
    a = ap.parse_args()

    if a.cmd == "refresh":
        idx = refresh()
        print(f"wrote {INDEX_OUT} — {len(idx['types'])} element types indexed")
        return 0
    if a.cmd == "summary":
        print(summary())
        return 0
    if a.cmd == "show":
        print(show(a.element_type, a.phase))
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
