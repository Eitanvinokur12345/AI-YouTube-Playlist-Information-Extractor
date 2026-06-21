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
    ("hub", "data/ hub (the store)", "home", "G1"),
    # ── DISCOVERY: search the internet + GitHub for new material ──
    ("fetch", "Playlist fetch", "connector", "G1"),
    ("news", "Web/news discovery (83 feeds)", "connector", "G1"),
    ("discover", "GitHub/web tool & MCP discovery", "connector", "G1"),
    ("sources", "Channel growth", "connector", "G1"),
    # ── RETRIEVAL: get the actual content ──
    ("supadata", "Supadata transcripts (cloud)", "tool", "G1"),
    ("residential", "Residential backfill", "tool", "G1"),
    ("gemini_video", "Gemini watch (audio+visual)", "tool", "G1"),
    # ── ANALYSIS: turn content into structured knowledge ──
    ("freepool", "Free engine pool (analyze)", "skill", "G1"),
    ("claude", "Claude deep (night)", "skill", "G1"),
    ("mine", "Mine feeds", "skill", "G1"),
    ("resolver", "Comment resolver", "skill", "G1"),
    # ── SELF-IMPROVEMENT (G2): watch, check, maintain, improve ──
    ("selfcheck", "Self-check (50Q)", "toolhub", "G2"),
    ("effectiveness", "Effectiveness scoreboard", "toolhub", "G2"),
    ("review", "3-agent review", "toolhub", "G2"),
    ("safety", "Security/safety gate (rates connectors)", "toolhub", "G2"),
    ("trend", "Trend watch → proposes new tabs/features", "toolhub", "G2"),
    ("maintenance", "Maintenance / integrity sweep", "toolhub", "G2"),
    ("dedup", "Dedup / models / graph", "toolhub", "G4"),
    ("improve", "Self-improve (weekly)", "toolhub", "G2"),
    # ── OUTPUT (G3/G5): the surfaces that USE the knowledge ──
    ("dashboard", "Dashboard (Pages)", "category", "G1"),
    ("hubapi", "Hub API (hub.json)", "category", "G1"),
    ("brain", "Obsidian brain", "category", "G1"),
    ("activator", "Activator skill (find+combine+activate)", "category", "G5"),
]
EDGES = [
    ("sources", "fetch"), ("fetch", "hub"),
    ("supadata", "hub"), ("residential", "hub"), ("gemini_video", "hub"),
    ("hub", "freepool"), ("freepool", "hub"), ("hub", "claude"), ("claude", "hub"),
    ("news", "mine"), ("mine", "hub"), ("discover", "hub"), ("resolver", "hub"), ("news", "hub"),
    ("hub", "selfcheck"), ("selfcheck", "hub"), ("hub", "effectiveness"), ("effectiveness", "hub"),
    ("hub", "review"), ("review", "hub"), ("hub", "safety"), ("safety", "hub"),
    ("hub", "trend"), ("trend", "improve"), ("hub", "maintenance"), ("maintenance", "improve"),
    ("hub", "dedup"), ("dedup", "hub"), ("hub", "improve"), ("improve", "hub"),
    ("hub", "dashboard"), ("hub", "hubapi"), ("hub", "brain"), ("hub", "activator"),
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
                 "G4": "Evaluate/test", "G5": "Activate"}
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
