"""
src/build_pipeline_graph.py — the SECOND brain: the system/protocol orchestration graph.

The knowledge graph (build_graph.py) shows what the project KNOWS. This shows how the project
WORKS — every internal system/protocol as a node, the data-flow dependencies as edges, and the
central data/ hub as the main node everything feeds and reads from (n8n-style). Rendered in the
Dev tab next to the knowledge graph so you can see both "brains" in one place. Stdlib only.

Usage:  python -m src.build_pipeline_graph
"""
from __future__ import annotations

import glob
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
WF = ROOT / ".github" / "workflows"

# group -> reuses an existing GRAPH_COLORS key so the dashboard colours it. store=home(amber, main),
# source=connector(blue), transcript=tool(pink), analysis=skill(green), quality=toolhub(purple),
# output=category(sky).
# group: store=home(amber, main) · DISCOVERY=connector(blue) · RETRIEVAL=tool(pink) ·
# ANALYSIS=skill(green) · SELF-IMPROVEMENT=toolhub(purple) · OUTPUT=category(sky).
# `goal` ties each protocol to one of the 5 main goals (G1 retrieve/analyze, G2 self-improve,
# G3 integrate, G4 evaluate/test, G5 activate) so the graph shows what each part is FOR.
NODES = [
    ("hub", "data/ hub — the shared JSON store", "home", "G1"),
    # ── DISCOVERY: search the internet + GitHub for new material ──
    ("fetch", "Playlist fetch (ingest new videos)", "connector", "G1"),
    ("news", "Web/news discovery (83 official feeds)", "connector", "G1"),
    ("discover", "GitHub/web tool & MCP discovery", "connector", "G1"),
    ("sources", "Channel growth (suggest + add sources)", "connector", "G1"),
    # ── RETRIEVAL: get the actual content ──
    ("supadata", "Supadata transcripts (cloud captions)", "tool", "G1"),
    ("residential", "Residential backfill (home-IP captions)", "tool", "G1"),
    ("gemini_video", "Gemini watch (video audio + on-screen)", "tool", "G1"),
    # ── ANALYSIS: turn content into structured knowledge ──
    ("freepool", "Free engine pool (transcript → skills/tools)", "skill", "G1"),
    ("claude", "Claude deep analysis (night-gated)", "skill", "G1"),
    ("mine", "Mine 83 web feeds → new tools/skills/MCPs", "skill", "G1"),
    ("resolver", "Comment-gated resolver (find the named resource)", "skill", "G1"),
    ("links", "Link resolver + verifier (real site/GitHub/Codespaces)", "skill", "G3"),
    # ── SELF-IMPROVEMENT (G2): watch, check, maintain, improve ──
    ("selfcheck", "Self-check (50-question spec audit)", "toolhub", "G2"),
    ("effectiveness", "Effectiveness scoreboard (per-lane quality)", "toolhub", "G2"),
    ("review", "3-agent review (usability/bullshit/bugs + UI/UX)", "toolhub", "G2"),
    ("safety", "Security/safety gate (rates connectors)", "toolhub", "G2"),
    ("trend", "Trend watch → proposes new tabs/features", "toolhub", "G2"),
    ("maintenance", "Maintenance / integrity sweep", "toolhub", "G2"),
    ("crosstab", "Cross-tab consistency check", "toolhub", "G2"),
    ("requeue", "Requeue shallow videos (deep re-run)", "toolhub", "G2"),
    ("status", "Pipeline heartbeat / live status", "toolhub", "G4"),
    ("backup", "Backup + regression guard", "toolhub", "G2"),
    ("dedup", "Dedup (merge duplicates)", "toolhub", "G4"),
    ("improve", "Self-improve (weekly + UI/UX)", "toolhub", "G2"),
    # ── EVALUATE / RANK (G4): the podium ranking the owner asked for ──
    ("rating", "Tool-rating / podium (quality ranking)", "toolhub", "G4"),
    ("models", "Models ranking (build_models)", "toolhub", "G4"),
    # ── OUTPUT (G1/G3/G5): the surfaces that USE the knowledge ──
    ("digest", "News digest synthesis (themes)", "skill", "G1"),
    ("graph", "Knowledge-graph builder (Brain 1)", "category", "G1"),
    ("devdoc", "Dev-doc builder (auto Dev tab)", "category", "G3"),
    ("dashboard", "Dashboard (Pages)", "category", "G1"),
    ("hubapi", "Hub API (hub.json)", "category", "G1"),
    ("brain", "Obsidian brain", "category", "G1"),
    ("activator", "Activator skill (find+combine+activate)", "category", "G5"),
    ("agentic_os", "Agentic OS — 6th goal (spec; orchestrates all)", "home", "G6"),
]
EDGES = [
    ("sources", "fetch"), ("fetch", "hub"),
    ("supadata", "hub"), ("residential", "hub"), ("gemini_video", "hub"),
    ("hub", "freepool"), ("freepool", "hub"), ("hub", "claude"), ("claude", "hub"),
    ("news", "mine"), ("mine", "hub"), ("discover", "hub"), ("resolver", "hub"), ("news", "hub"),
    ("hub", "links"), ("links", "hub"),
    ("hub", "selfcheck"), ("selfcheck", "hub"), ("hub", "effectiveness"), ("effectiveness", "hub"),
    ("hub", "review"), ("review", "hub"), ("hub", "safety"), ("safety", "hub"),
    ("hub", "trend"), ("trend", "improve"), ("hub", "maintenance"), ("maintenance", "improve"),
    ("hub", "crosstab"), ("crosstab", "hub"), ("hub", "requeue"), ("requeue", "hub"),
    ("hub", "status"), ("status", "dashboard"), ("hub", "backup"), ("backup", "improve"),
    ("hub", "dedup"), ("dedup", "hub"), ("hub", "improve"), ("improve", "hub"),
    ("hub", "rating"), ("rating", "dashboard"), ("hub", "models"), ("models", "rating"),
    ("hub", "digest"), ("digest", "hub"), ("hub", "graph"), ("graph", "brain"),
    ("hub", "devdoc"), ("devdoc", "dashboard"),
    ("hub", "dashboard"), ("hub", "hubapi"), ("hub", "brain"), ("hub", "activator"),
    ("activator", "agentic_os"), ("hub", "agentic_os"), ("improve", "agentic_os"),
]


def main() -> int:
    ids = {n[0] for n in NODES}
    # auto-include any workflow not already represented, so nothing is forgotten
    known = " ".join(n[1].lower() for n in NODES)
    extra = []
    for f in sorted(glob.glob(str(WF / "*.yml"))):
        stem = Path(f).stem
        if stem in ("codeql", "claude", "engine_selftest"):
            continue
        if stem not in ids and stem.replace("_", " ") not in known:
            extra.append((stem, stem.replace("_", " "), "connector"))
    extra = [(i, l, g, "G1") for (i, l, g) in extra]    # auto-found workflows default to G1
    nodes = NODES + extra
    deg = {n[0]: 0 for n in nodes}
    for a, b in EDGES:
        deg[a] = deg.get(a, 0) + 1
        deg[b] = deg.get(b, 0) + 1
    GOAL_TEXT = {"G1": "Retrieve & analyze", "G2": "Self-improve", "G3": "Integrate",
                 "G4": "Evaluate/test", "G5": "Activate", "G6": "Agentic OS"}
    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "main": "hub",
        "goals": GOAL_TEXT,
        "counts": {"nodes": len(nodes), "links": len(EDGES)},
        "nodes": [{"id": i, "label": l, "group": g, "goal": goal, "deg": deg.get(i, 0)}
                  for i, l, g, goal in nodes],
        "links": [{"source": a, "target": b} for a, b in EDGES],
    }
    json.dump(out, open(DATA / "pipeline_graph.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"pipeline graph: {len(nodes)} systems, {len(EDGES)} dependencies; main = data/ hub "
          f"(deg {deg.get('hub')}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
