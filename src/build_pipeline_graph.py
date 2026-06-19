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
NODES = [
    ("hub", "data/ hub (the store)", "home"),
    ("fetch", "Playlist fetch", "connector"),
    ("news", "Web news (83 feeds)", "connector"),
    ("discover", "Tool discovery", "connector"),
    ("sources", "Channel growth", "connector"),
    ("supadata", "Supadata transcripts (cloud)", "tool"),
    ("residential", "Residential backfill", "tool"),
    ("freepool", "Free engine pool (analyze)", "skill"),
    ("claude", "Claude deep (night)", "skill"),
    ("mine", "Mine feeds", "skill"),
    ("resolver", "Comment resolver", "skill"),
    ("selfcheck", "Self-check (50Q)", "toolhub"),
    ("effectiveness", "Effectiveness scoreboard", "toolhub"),
    ("review", "3-agent review", "toolhub"),
    ("safety", "Safety ratings", "toolhub"),
    ("dedup", "Dedup / models / graph", "toolhub"),
    ("improve", "Self-improve (weekly)", "toolhub"),
    ("dashboard", "Dashboard (Pages)", "category"),
    ("hubapi", "Hub API (hub.json)", "category"),
    ("brain", "Obsidian brain", "category"),
    ("activator", "Activator skill", "category"),
]
EDGES = [
    ("sources", "fetch"), ("fetch", "hub"),
    ("supadata", "hub"), ("residential", "hub"),
    ("hub", "freepool"), ("freepool", "hub"), ("hub", "claude"), ("claude", "hub"),
    ("news", "mine"), ("mine", "hub"), ("discover", "hub"), ("resolver", "hub"), ("news", "hub"),
    ("hub", "selfcheck"), ("selfcheck", "hub"), ("hub", "effectiveness"), ("effectiveness", "hub"),
    ("hub", "review"), ("review", "hub"), ("hub", "safety"), ("safety", "hub"),
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
    nodes = NODES + extra
    deg = {n[0]: 0 for n in nodes}
    for a, b in EDGES:
        deg[a] = deg.get(a, 0) + 1
        deg[b] = deg.get(b, 0) + 1
    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "main": "hub",
        "counts": {"nodes": len(nodes), "links": len(EDGES)},
        "nodes": [{"id": i, "label": l, "group": g, "deg": deg.get(i, 0)} for i, l, g in nodes],
        "links": [{"source": a, "target": b} for a, b in EDGES],
    }
    json.dump(out, open(DATA / "pipeline_graph.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"pipeline graph: {len(nodes)} systems, {len(EDGES)} dependencies; main = data/ hub "
          f"(deg {deg.get('hub')}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
