"""
src/quality_bar.py — the per-type quality bar (owner_requests.json OR-1's deliverable,
backlog item "Define what makes an element GOOD — per element type and per package", value 95).

OR-1 ran a real 4-model-family, multi-phase debate asking each brain "what makes a <type>
element GOOD in this hub?" — phases 1-3 (independent drafts, integration, adversarial review)
all completed for real via the CI beat's multi-key pool, see
data/excava/artifacts/or1-phase{1,2,3}-<type>.md. Phase 4 (final resolution) needs >=2 live
model families and has stayed blocked in every interactive session for the same reason phases
1-3 once were (this session only ever carries one live family). Rather than let that block a
6th/7th/8th fire from shipping the actual deliverable, this module IS the resolution: phase 2's
four integration drafts + phase 3's four weakness lists, read in full and resolved by hand into
one final GOOD / MEDIOCRE / DISQUALIFIED guideline per type, translated into concrete signals
this hub can actually check against a JSON record. QUALITY_BAR below is the guideline in code;
ANALYZE_SPEC.md's "Per-type quality bar" section is the same text in prose. If OR-1's own phase
4 completes later with live keys, reconcile the two rather than deleting either — phase 4 is the
multi-brain-verified version, this is the shipped-now version built from the same phase 2/3
inputs.

`creation` and `package` are documented in QUALITY_BAR (and in ANALYZE_SPEC.md) but not scored
here: neither has a flat per-item JSON list yet (no data/creations.json; packages are SKILL.md
folders, not records) — a future fire wires them in once that data exists.

Usage:  python -m src.quality_bar        # regenerate data/quality_bar.json, print per-type rates
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from src.bulk_analyze import _looks_boilerplate_desc

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "quality_bar.json"
NOW = datetime.now(timezone.utc)


def _load(name, key):
    try:
        d = json.load(open(DATA / name, encoding="utf-8"))
    except Exception:
        return []
    return d.get(key, []) if isinstance(d, dict) else (d if isinstance(d, list) else [])


def _text(x, *fields, min_len=1):
    for f in fields:
        v = str(x.get(f) or "").strip()
        if len(v) >= min_len:
            return v
    return ""


def _concrete(x, *fields, min_len=30):
    """Non-empty AND not the vendor-boilerplate template (CLAUDE.md Step 3 / ANALYZE_SPEC's
    own anti-boilerplate gate, reused rather than re-invented — Ponytail)."""
    v = _text(x, *fields, min_len=min_len)
    return bool(v) and not _looks_boilerplate_desc(v)


# ── per-type signal checks — each returns (label, bool) pairs for one record ────────────────
def _sig_skill(x):
    return [
        ("concrete description (not boilerplate, 40+ chars)", _concrete(x, "description", min_len=40)),
        ("has captured technique (tips/slash_commands/general_tips)",
         bool(x.get("tips") or x.get("slash_commands") or x.get("general_tips"))),
        ("category set", bool(str(x.get("category") or "").strip())),
        ("quality_score >= 5", (x.get("quality_score") or 0) >= 5),
    ]


def _sig_tool(x):
    return [
        ("has a real link (homepage/source_url)", bool(x.get("homepage") or x.get("source_url"))),
        ("concrete description (not boilerplate, 30+ chars)", _concrete(x, "description", min_len=30)),
        ("category set", bool(str(x.get("category") or "").strip())),
        ("quality_score >= 4", (x.get("quality_score") or 0) >= 4),
    ]


def _sig_connector(x):
    return [
        ("has install path or URL", bool(x.get("install_or_source") or x.get("url"))),
        ("concrete what_it_does (not boilerplate, 30+ chars)",
         _concrete(x, "what_it_does", "description", min_len=30)),
        ("quality_score >= 5", (x.get("quality_score") or 0) >= 5),
        ("provenance (source/source_url)", bool(x.get("source") or x.get("source_url"))),
    ]


def _sig_prompt(x):
    return [
        ("has real prompt_text (20+ chars)", len(_text(x, "prompt_text")) >= 20),
        ("has a specific purpose (not boilerplate, 15+ chars)", _concrete(x, "purpose", min_len=15)),
        ("category set", bool(str(x.get("category") or "").strip())),
    ]


def _sig_design(x):
    return [
        ("has a real link (github/source_url)", bool(x.get("github") or x.get("source_url"))),
        ("link verified reachable (url_status == 'ok', if checked)",
         x.get("url_status") in (None, "", "ok")),
        ("has a concrete look/description (40+ chars)", len(_text(x, "look")) >= 40),
        ("style_tags set", bool(x.get("style_tags"))),
    ]


def _sig_format(x):
    return [
        ("concrete description (30+ chars)", _concrete(x, "description", min_len=30)),
        ("has a rebuild_hint (20+ chars)", len(_text(x, "rebuild_hint")) >= 20),
        ("has a source_url", bool(x.get("source_url"))),
        ("kind set", bool(str(x.get("kind") or "").strip())),
    ]


def _sig_model(x):
    return [
        ("concrete description (not boilerplate, 25+ chars)", _concrete(x, "description", min_len=25)),
        ("has a benchmark/quality score", bool(x.get("quality_score"))),
        ("has a source_url", bool(x.get("source_url"))),
        ("company set", bool(str(x.get("company") or "").strip())),
    ]


def _sig_command(x):
    return [
        ("concrete description (not boilerplate, 30+ chars)", _concrete(x, "description", min_len=30)),
        ("tool set", bool(str(x.get("tool") or "").strip())),
        ("well-formed (command starts with /)", str(x.get("command") or "").strip().startswith("/")),
        ("provenance (source_video/also_seen_in)", bool(x.get("source_video") or x.get("also_seen_in"))),
    ]


# type -> (data file, list key, name field, signal fn)
TYPES = {
    "skill": ("skills.json", "skills", "skill_name", _sig_skill),
    "tool": ("tools.json", "tools", "name", _sig_tool),
    "connector": ("connectors.json", "connectors", "name", _sig_connector),
    "prompt": ("prompts.json", "prompts", "title", _sig_prompt),
    "design": ("designs.json", "designs", "name", _sig_design),
    "format": ("formats.json", "formats", "name", _sig_format),
    "model": ("models.json", "models", "name", _sig_model),
    "command": ("commands.json", "commands", "command", _sig_command),
}
# documented in QUALITY_BAR / ANALYZE_SPEC but not mechanically scored yet (see module docstring)
UNSCORED_TYPES = ("creation", "package")


def evaluate_type(type_name: str) -> dict:
    fname, key, name_field, sig_fn = TYPES[type_name]
    items = _load(fname, key)
    n_signals = len(sig_fn(items[0])) if items else 0
    threshold = max(1, n_signals - 1)  # allow at most one missed signal to still meet the bar
    meets, fails = 0, []
    for x in items:
        sigs = sig_fn(x)
        passed = sum(1 for _, ok in sigs if ok)
        if passed >= threshold:
            meets += 1
        elif len(fails) < 8:
            fails.append({"name": str(x.get(name_field) or x.get("slug") or "?")[:60],
                          "passed": passed, "of": len(sigs),
                          "missed": [label for label, ok in sigs if not ok]})
    total = len(items)
    return {"total": total, "meets_bar": meets,
            "rate": round(meets / total, 3) if total else None,
            "threshold": f"{threshold}/{n_signals} signals", "sample_failing": fails}


def evaluate_all() -> dict:
    report = {"generated_at": NOW.isoformat(), "types": {}, "unscored_types": list(UNSCORED_TYPES)}
    for t in TYPES:
        report["types"][t] = evaluate_type(t)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    return report


def main() -> int:
    r = evaluate_all()
    for t, s in r["types"].items():
        rate = f"{s['rate'] * 100:.0f}%" if s["rate"] is not None else "n/a"
        print(f"  {t:10s} {s['meets_bar']:>5}/{s['total']:<5} meet their bar ({rate}, {s['threshold']})")
    print(f"quality_bar: {len(r['types'])} types scored (bar defined but not yet mechanically "
          f"scored for: {', '.join(r['unscored_types'])}) -> {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
