"""
src/build_graph.py — emit data/brain_graph.json (nodes + links) so the dashboard can render an
in-page "Obsidian graph view" inside the Dev Construction tab. Stdlib only (runs in CI). The link
structure mirrors src/build_brain.py's Obsidian vault, so the web graph matches the desktop graph:
every skill/tool/prompt/connector links to its category hub (+ tool hub for skills), and every hub
links to Home — one fully-connected web that clusters by category and tool.

Run:  python -m src.build_graph
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"


def _load(name):
    try:
        return json.load(open(DATA / name, encoding="utf-8"))
    except Exception:
        return {}


def main() -> None:
    skills = (_load("skills.json") or {}).get("skills", [])
    tools = (_load("tools.json") or {}).get("tools", [])
    prompts = (_load("prompts.json") or {}).get("prompts", [])
    conns = (_load("connectors.json") or {}).get("connectors", [])

    nodes: dict = {}
    links: list = []

    def node(nid, label, group, url=None):
        if nid not in nodes:
            nodes[nid] = {"id": nid, "label": (str(label or nid))[:60], "group": group}
            if url:
                nodes[nid]["url"] = url
        return nid

    def link(a, b):
        if a != b:
            links.append({"source": a, "target": b})

    home = node("Home", "Excavatortron", "home")
    conn_hub = node("hub:connectors", "Connectors", "hub")
    link(conn_hub, home)

    def cat_hub(cat):
        cid = "cat:" + str(cat or "other").lower()
        if cid not in nodes:
            node(cid, cat or "other", "category")
            link(cid, home)
        return cid

    def tool_hub(tt):
        tid = "toolhub:" + str(tt or "claude").lower()
        if tid not in nodes:
            node(tid, tt or "claude", "toolhub")
            link(tid, home)
        return tid

    for i, s in enumerate(skills):
        nid = node("skill:" + str(s.get("slug") or s.get("skill_name") or i),
                   s.get("skill_name") or s.get("slug"), "skill", s.get("source_url"))
        link(nid, cat_hub(s.get("category")))
        link(nid, tool_hub(s.get("target_tool") or "claude"))
    for i, t in enumerate(tools):
        nid = node("tool:" + str(t.get("slug") or t.get("name") or i),
                   t.get("name") or t.get("slug"), "tool", t.get("source_url"))
        link(nid, cat_hub(t.get("category")))
    for i, p in enumerate(prompts):
        nid = node("prompt:" + str(p.get("slug") or p.get("title") or i),
                   p.get("title"), "prompt", p.get("source_url"))
        link(nid, cat_hub(p.get("category")))
    for i, c in enumerate(conns):
        nid = node("conn:" + str(c.get("slug") or c.get("name") or i),
                   c.get("name"), "connector", c.get("url"))
        link(nid, conn_hub)

    valid = set(nodes)
    links = [ln for ln in links if ln["source"] in valid and ln["target"] in valid]
    out = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "counts": {"skills": len(skills), "tools": len(tools), "prompts": len(prompts),
                   "connectors": len(conns), "nodes": len(nodes), "links": len(links)},
        "nodes": list(nodes.values()),
        "links": links,
    }
    (DATA / "brain_graph.json").write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    print(f"brain_graph.json: {len(nodes)} nodes, {len(links)} links "
          f"({len(skills)} skills, {len(tools)} tools, {len(prompts)} prompts, {len(conns)} connectors)")


if __name__ == "__main__":
    main()
