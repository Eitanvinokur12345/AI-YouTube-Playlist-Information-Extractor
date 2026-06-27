"""
src/export_graphml.py — export the WHOLE brain as GraphML for Graphify / Gephi / Neo4j / yEd.

The in-page dashboard graph is capped (~850 nodes) so it stays readable in a browser canvas. But
the owner wants a bigger, more significant brain by combining Obsidian + Graphify (graphify.net),
which imports GraphML. So this emits data/brain.graphml — EVERY skill/tool/model/connector/prompt
plus the category and tool hubs, with the full link structure. Load it into Graphify (or Gephi /
Neo4j / yEd) for the huge graph; the Obsidian vault (src/build_brain.py) covers the note side.
Stdlib only, free.

Run:  python -m src.export_graphml
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape

_CTRL = re.compile(r"[\x00-\x08\x0B\x0C\x0E-\x1F]")   # control chars XML 1.0 forbids


def esc(s) -> str:
    return escape(_CTRL.sub("", str(s)), {'"': "&quot;", "'": "&apos;"})

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "brain.graphml"


def _items(name, key):
    try:
        d = json.load(open(DATA / name, encoding="utf-8"))
        return d.get(key, []) if isinstance(d, dict) else []
    except Exception:
        return []


def main() -> int:
    skills = _items("skills.json", "skills"); tools = _items("tools.json", "tools")
    conns = _items("connectors.json", "connectors"); prompts = _items("prompts.json", "prompts")
    models = _items("models.json", "models")

    nodes: dict[str, dict] = {}
    edges: list[tuple[str, str]] = []

    def node(nid, label, typ, category="", quality=0, url=""):
        if nid not in nodes:
            nodes[nid] = {"label": str(label or nid)[:120], "type": typ,
                          "category": category or "", "quality": quality or 0, "url": url or ""}
        return nid

    def cat(c):
        cid = "cat:" + str(c or "other").lower()
        node(cid, c or "other", "category"); return cid

    def thub(t):
        tid = "tool:" + str(t or "claude").lower()
        node(tid, t or "claude", "toolhub"); return tid

    node("ROOT", "Excavatortron", "root")
    for s in skills:
        nid = "skill:" + str(s.get("slug") or s.get("skill_name"))
        node(nid, s.get("skill_name") or s.get("slug"), "skill", s.get("category"),
             s.get("quality_score"), s.get("homepage") or s.get("github") or s.get("source_url"))
        edges += [(nid, cat(s.get("category"))), (nid, thub(s.get("target_tool") or "claude"))]
    for t in tools:
        nid = "tool:" + str(t.get("slug") or t.get("name"))
        node(nid, t.get("name") or t.get("slug"), "tool", t.get("category"),
             t.get("quality_score"), t.get("homepage") or t.get("github") or t.get("url"))
        edges.append((nid, cat(t.get("category"))))
    for m in models:
        nid = "model:" + str(m.get("slug") or m.get("name"))
        node(nid, m.get("name") or m.get("slug"), "model", m.get("category"), m.get("quality_score"))
        edges.append((nid, cat(m.get("category"))))
    for p in prompts:
        nid = "prompt:" + str(p.get("slug") or p.get("title"))
        node(nid, p.get("title"), "prompt", p.get("category")); edges.append((nid, cat(p.get("category"))))
    for c in conns:
        nid = "conn:" + str(c.get("slug") or c.get("name"))
        node(nid, c.get("name"), "connector", "", c.get("quality_score"),
             c.get("homepage") or c.get("url")); edges.append((nid, "ROOT"))
    for nid in list(nodes):
        if nid.startswith(("cat:", "tool:")) and nodes[nid]["type"] in ("category", "toolhub"):
            edges.append((nid, "ROOT"))

    valid = set(nodes)
    edges = [(a, b) for a, b in edges if a in valid and b in valid and a != b]

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<graphml xmlns="http://graphml.graphdrawing.org/xmlns">',
             '<key id="label" for="node" attr.name="label" attr.type="string"/>',
             '<key id="type" for="node" attr.name="type" attr.type="string"/>',
             '<key id="category" for="node" attr.name="category" attr.type="string"/>',
             '<key id="quality" for="node" attr.name="quality" attr.type="double"/>',
             '<key id="url" for="node" attr.name="url" attr.type="string"/>',
             '<graph edgedefault="undirected">']
    for nid, a in nodes.items():
        lines.append(
            f'<node id="{esc(nid)}">'
            f'<data key="label">{esc(a["label"])}</data>'
            f'<data key="type">{esc(a["type"])}</data>'
            f'<data key="category">{esc(a["category"])}</data>'
            f'<data key="quality">{float(a["quality"] or 0)}</data>'
            f'<data key="url">{esc(a["url"])}</data></node>')
    for i, (a, b) in enumerate(edges):
        lines.append(f'<edge id="e{i}" source="{esc(a)}" target="{esc(b)}"/>')
    lines += ['</graph>', '</graphml>']
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"export_graphml: {len(nodes)} nodes, {len(edges)} edges -> data/brain.graphml "
          f"(load into Graphify / Gephi / Neo4j / yEd). Generated {datetime.now(timezone.utc).isoformat()}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
