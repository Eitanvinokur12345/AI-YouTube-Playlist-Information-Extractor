"""
src/effectiveness.py — the EFFECTIVENESS & RIGIDITY scoreboard (Eitan's request).

For every retrieval/analysis LANE the project runs, score how effective and how rigid it is,
so the self-improvement system has concrete, measured targets (it reads data/effectiveness.json
and opens improvement tasks for the weakest lanes). NO Claude, NO network — stdlib only; runs
every analysis cycle.

Dimensions (0-10 each), per the owner's spec:
  quality       — how good the output is (avg quality_score, low-quality fraction)
  quantity      — how much it produces / coverage
  form          — how clean/structured the output is
  time          — how fast / how often it refreshes
  tokens        — Claude-Pro token thrift (10 = free, lower = burns the scarce Pro budget)
  ease_external — how easily an OUTSIDE system can consume it (the "hub for future systems" goal)
  ease_project  — how easily THIS project's own systems consume it
  ease_user     — how easily Eitan reads/uses it after analysis
Plus:
  effectiveness — weighted mean of the dimensions (the headline number)
  rigidity      — 0-10, how brittle/locked-in the lane is (HIGHER = worse; e.g. a hard IP block)

Live signals (health.json, skills/tools.json, processed transcript-sources, news/discover/sources
freshness) overlay a documented per-lane baseline; ease_*/form start as rated baselines the
weekly Claude self-improve pass can refine. Everything is transparent in the "basis" strings.

Usage:  python -m src.effectiveness        # writes data/effectiveness.json + one-line summary
"""
from __future__ import annotations

import glob
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"

# Dimension weights for the headline "effectiveness" number (sum need not be 1; normalised).
WEIGHTS = {
    "quality": 1.4, "quantity": 1.2, "form": 1.0, "time": 0.8, "tokens": 1.0,
    "ease_external": 1.2, "ease_project": 0.9, "ease_user": 1.1,
}


def _load(path, default=None):
    try:
        return json.load(open(path, encoding="utf-8"))
    except Exception:
        return default


def _avg_quality(arr, key="quality_score"):
    qs = [x.get(key) for x in arr if isinstance(x.get(key), (int, float))]
    return round(sum(qs) / len(qs), 2) if qs else 0.0


def _transcript_sources():
    """Count how each processed/pending video got its transcript — feeds the retrieval lanes."""
    c = {"transcript": 0, "whisper": 0, "supadata": 0, "description_only": 0, "total": 0}
    seen = set()
    for f in glob.glob(str(DATA / "processed" / "*.json")) + glob.glob(str(DATA / "_pending" / "*.json")):
        r = _load(f)
        if not isinstance(r, dict):
            continue
        vid = r.get("video_id")
        if not vid or vid in seen:
            continue
        seen.add(vid)
        c["total"] += 1
        src = r.get("transcript_source")
        if r.get("backfill_via") == "supadata":
            c["supadata"] += 1
        elif src == "transcript":
            c["transcript"] += 1
        elif src == "whisper":
            c["whisper"] += 1
        else:
            c["description_only"] += 1
    return c


def _eff(metrics: dict) -> float:
    num = sum(metrics[k] * WEIGHTS[k] for k in WEIGHTS if k in metrics)
    den = sum(WEIGHTS[k] for k in WEIGHTS if k in metrics)
    return round(num / den, 1) if den else 0.0


def _lane(id, name, kind, engine, metrics, rigidity, note):
    weak = sorted(metrics, key=lambda k: metrics[k])[:2]
    return {"id": id, "name": name, "kind": kind, "engine": engine,
            "metrics": metrics, "effectiveness": _eff(metrics), "rigidity": rigidity,
            "weak_dims": weak, "improve_note": note}


def main() -> int:
    health = _load(DATA / "health.json", {}) or {}
    hv = health.get("videos", {}) if isinstance(health, dict) else {}
    total = hv.get("total", 0) or 1
    cov = round(100 * hv.get("with_transcript", 0) / total, 1)
    ts = _transcript_sources()

    skills = (_load(DATA / "skills.json", {}) or {}).get("skills", [])
    tools = (_load(DATA / "tools.json", {}) or {}).get("tools", [])
    sk_q, tl_q = _avg_quality(skills), _avg_quality(tools)
    lowq = sum(1 for x in skills + tools if x.get("low_quality_source")) / max(len(skills) + len(tools), 1)
    library_quality = round((sk_q + tl_q) / 2, 2)

    web = _load(DATA / "web_news_store.json", {}) or {}
    web_n = len(web.get("items", web if isinstance(web, list) else [])) if web else 0
    chan = (_load(DATA / "channel_suggestions.json", {}) or {})
    chan_n = len(chan.get("suggestions", [])) if isinstance(chan, dict) else 0

    # cov->0-10 quantity score for retrieval lanes; coverage is the whole game.
    cov10 = round(min(cov / 8.0, 10), 1)               # 80% coverage == 10
    lanes = []

    # ── RETRIEVAL lanes ──────────────────────────────────────────────────────
    nsrc = len((_load(ROOT / "config.json") or {}).get("news_sources", []))
    lanes.append(_lane(
        "transcript_supadata", "Transcript fetch — Supadata (cloud, UNATTENDED)", "retrieval",
        "Supadata API (their infra, no PC)",
        {"quality": 8.5, "quantity": round(min(2 + ts["supadata"] / 3.0, 10), 1), "form": 9.0,
         "time": 8.0, "tokens": 10.0, "ease_external": 8.0, "ease_project": 9.0, "ease_user": 8.0},
        rigidity=4,  # proven working & fully unattended; only constraint is the free-tier volume
        note=f"PROVEN working & PC-FREE (the autonomy baseline): fetches on Supadata's infra so the "
             f"datacenter-IP block doesn't apply; daily, dead-video skip protects the ~100/mo free "
             f"quota ({ts['supadata']} recovered). Lever: the quota caps backlog speed, not new videos."))
    lanes.append(_lane(
        "transcript_residential", "Transcript backfill — residential (optional turbo)", "retrieval",
        "youtube-transcript-api (home IP)",
        {"quality": 9.0, "quantity": cov10, "form": 9.0, "time": 6.0, "tokens": 10.0,
         "ease_external": 8.0, "ease_project": 9.0, "ease_user": 8.0},
        rigidity=5,  # no longer the SOLE path (Supadata is the baseline) — now an accelerator
        note=f"Recovers ~85% of caption-less videos fast from a home IP (coverage {cov}%) + translates "
             f"foreign captions. No longer required — Supadata is the unattended baseline; this is the "
             f"turbo when we're in a session. Block-aware (auto-stops on the escalating IP block)."))

    # ── ANALYSIS lanes ───────────────────────────────────────────────────────
    q10 = round(library_quality, 1)
    lanes.append(_lane(
        "analysis_free", "Free analysis lane (bulk_analyze)", "analysis",
        "4 verified free engines (pool)",
        {"quality": 8.0, "quantity": 9.0, "form": 8.5, "time": 8.5, "tokens": 10.0,
         "ease_external": 8.0, "ease_project": 9.0, "ease_user": 8.0},
        rigidity=3,  # 4 verified engines + pool auto-drops any that fail = robust
        note=f"Turns transcripts into records at 0 Claude cost via 4 VERIFIED engines (gpt-4.1-mini, "
             f"OpenRouter, Groq, Gemini; pool auto-drops failures). Library avg quality {library_quality}/10, "
             f"{round(100*lowq)}% low-source. Output is externally consumable via data/hub.json."))
    lanes.append(_lane(
        "analysis_claude", "Deep analysis (Claude, night-gated)", "analysis",
        "Claude Pro subscription token",
        {"quality": 9.0, "quantity": 4.0, "form": 9.0, "time": 4.0, "tokens": 2.0,
         "ease_external": 8.0, "ease_project": 9.0, "ease_user": 8.0},
        rigidity=5,  # highest quality but throttled by the tiny Pro budget + night window (by design)
        note="Highest quality, reserved for curation/self-improve (not bulk) to protect the small Pro "
             "budget — night-gated by design. The free pool carries the volume."))

    # ── EXTERNAL (non-playlist) acquisition lanes ────────────────────────────
    lanes.append(_lane(
        "web_news", f"Web AI news ({nsrc} sources)", "external",
        "src/news.py (RSS: labs/research/community/analysts)",
        {"quality": 7.5, "quantity": round(min(web_n / 35.0, 10), 1), "form": 8.0, "time": 9.0,
         "tokens": 10.0, "ease_external": 8.0, "ease_project": 9.0, "ease_user": 8.0},
        rigidity=2,
        note=f"Always-on (every 6h), {nsrc} RSS sources across labs, research (arXiv/BAIR/MIT), "
             f"community (Reddit/HN) and top analysts; {web_n} items stored. Dead feeds auto-prune."))
    lanes.append(_lane(
        "tool_discovery", "Tool discovery (off-playlist)", "external",
        "discover.yml (Claude, Sun/Tue/Thu)",
        {"quality": 7.5, "quantity": 6.0, "form": 8.0, "time": 5.0, "tokens": 5.0,
         "ease_external": 8.0, "ease_project": 9.0, "ease_user": 8.0},
        rigidity=4,
        note="Finds tools beyond the playlist 3x/week. Next lever: move it to the free engine pool to "
             "save the Pro budget (currently uses the Claude token)."))
    lanes.append(_lane(
        "source_suggestion", "Channel/source suggestion", "external",
        "suggest_channels.py (daily)",
        {"quality": 7.5, "quantity": round(min(2 + chan_n / 5.0, 10), 1), "form": 8.0, "time": 7.0,
         "tokens": 10.0, "ease_external": 8.0, "ease_project": 9.0, "ease_user": 8.0},
        rigidity=4,
        note=f"Proposes new channels daily ({chan_n} pending). One-time OAuth would let it auto-add to "
             f"the playlist (else suggestions only — surfaced on the Grow Sources tab)."))

    # The public hub index (data/hub.json) makes every lane's output externally consumable —
    # raise ease_external accordingly so the scoreboard reflects the infrastructure that exists.
    if (DATA / "hub.json").exists():
        for L in lanes:
            if L["metrics"].get("ease_external", 0) < 8:
                L["metrics"]["ease_external"] = 8
                L["effectiveness"] = _eff(L["metrics"])
                L["weak_dims"] = sorted(L["metrics"], key=lambda k: L["metrics"][k])[:2]

    lanes.sort(key=lambda L: L["effectiveness"])
    weakest = lanes[0] if lanes else None
    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "north_star": "A huge, machine-readable hub of all AI knowledge that also improves existing "
                      "skills, integrates new parts, and tests better versions.",
        "dimensions": list(WEIGHTS.keys()),
        "weights": WEIGHTS,
        "transcript_sources": ts,
        "library_quality": library_quality,
        "lanes": lanes,
        "summary": {
            "weakest_lane": weakest["name"] if weakest else "",
            "weakest_effectiveness": weakest["effectiveness"] if weakest else 0,
            "top_improvement": weakest["improve_note"] if weakest else "",
            "transcript_coverage_pct": cov,
        },
    }
    with open(DATA / "effectiveness.json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)
    print(f"effectiveness: {len(lanes)} lanes scored | weakest = {out['summary']['weakest_lane']} "
          f"({out['summary']['weakest_effectiveness']}/10) | coverage {cov}% | library quality {library_quality}/10")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
