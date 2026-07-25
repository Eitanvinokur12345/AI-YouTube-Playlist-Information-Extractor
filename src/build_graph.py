"""
src/build_graph.py — emit data/brain_graph.json (nodes + links) for the dashboard's in-page
"knowledge brain" (Brain 1) in the Dev tab.

Plotting all ~1400 items at once collapses the force layout into an unreadable white hairball, so
this emits a READABLE graph: the hubs (Home, categories, tool-hubs, connectors) + the TOP items per
hub by quality, PLUS two things the owner asked to see:
  - STAR anchors  — the highest-quality, most-endorsed skills ("the ones that don't change"),
                    drawn as gold star nodes. Honors data/stars.json if present.
  - COMBINATIONS  — skills/tools that show up together in the same video (a real "combo seen in the
                    wild"), drawn as combo nodes linking their members.
Everything beyond the per-hub cap stays browsable in the tabs; the graph is the map, not the index.

Run:  python -m src.build_graph
"""
from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
# Owner wants a BIG constellation. The grid-based force engine in the dashboard scales to ~1k+
# nodes, so we plot generously while STILL ranking by quality (dedup/quality gate unchanged).
CAP_PER_HUB = 55          # top items shown individually per category (quality-ranked)
CONN_CAP = 80             # top connectors shown
STARS_PER_CAT = 3         # top-quality anchors per category promoted to gold "star" nodes
MAX_COMBOS = 36           # co-occurrence combinations drawn


def _load(name):
    try:
        return json.load(open(DATA / name, encoding="utf-8"))
    except Exception:
        return {}


def _q(x):
    return x.get("quality_score") or 0


def _vid(x):
    v = x.get("endorsement_video_ids") or []
    return (v[0] if v else None) or x.get("source_video_id")


def main() -> None:
    skills = (_load("skills.json") or {}).get("skills", [])
    tools = (_load("tools.json") or {}).get("tools", [])
    prompts = (_load("prompts.json") or {}).get("prompts", [])
    conns = (_load("connectors.json") or {}).get("connectors", [])
    star_cfg = _load("stars.json") or {}
    starred_slugs = set(star_cfg.get("slugs", []) if isinstance(star_cfg, dict) else [])

    nodes: dict = {}
    links: list = []

    def node(nid, label, group, url=None, **extra):
        if nid not in nodes:
            nodes[nid] = {"id": nid, "label": (str(label or nid))[:60], "group": group, **extra}
            if url:
                nodes[nid]["url"] = url
        return nid

    def link(a, b):
        if a != b and a in nodes and b in nodes:
            links.append({"source": a, "target": b})

    def uniq_nid(base: str) -> str:
        """Guarantee a fresh node id for a per-ITEM node. Two distinct skills/tools/prompts/
        connectors can share a slug or name (a real data collision, not a duplicate reference —
        each is only visited once in these loops), and `node()` silently keeps the first writer
        and drops the rest, which is exactly the bug where distinct items overwrote one another
        onto a single graph node. Hub ids (cat:/toolhub:/Home) are intentionally reused across
        items and must NOT go through this — only call it for a new per-item nid."""
        nid, i = base, 2
        while nid in nodes:
            nid = f"{base}#{i}"; i += 1
        return nid

    home = node("Home", "Excavatortron", "home")
    conn_hub = node("hub:connectors", "Connectors", "hub"); link(conn_hub, home)
    cat_ids: dict = {}
    th_ids: dict = {}

    def cat_hub(cat):
        c = str(cat or "other").lower(); cid = "cat:" + c
        if cid not in nodes:
            node(cid, cat or "other", "category"); link(cid, home)
        cat_ids[c] = cid
        return cid

    def tool_hub(tt):
        t = str(tt or "claude").lower(); tid = "toolhub:" + t
        if tid not in nodes:
            node(tid, tt or "claude", "toolhub"); link(tid, home)
        return tid

    included: dict = {}     # item-node-id -> the source record (for combo co-occurrence)

    # group skills + tools by category, keep the top CAP by quality (so the graph is the BEST of each)
    by_cat: dict = defaultdict(list)
    for s in skills:
        by_cat[str(s.get("category") or "other").lower()].append(("skill", s))
    for t in tools:
        by_cat[str(t.get("category") or "other").lower()].append(("tool", t))

    for cat, items in by_cat.items():
        cid = cat_hub(cat)
        items.sort(key=lambda kt: _q(kt[1]), reverse=True)
        for rank, (kind, x) in enumerate(items[:CAP_PER_HUB]):
            slug = str(x.get("slug") or x.get("name") or x.get("skill_name") or rank)
            nid = uniq_nid(f"{kind}:{slug}")
            is_star = (slug in starred_slugs) or (rank < STARS_PER_CAT and _q(x) >= 8)
            node(nid, x.get("name") or x.get("skill_name") or slug,
                 "star" if is_star else kind, x.get("source_url"), q=_q(x))
            link(nid, cid)
            if kind == "skill":
                link(nid, tool_hub(x.get("target_tool") or "claude"))
            included[nid] = x

    for p in prompts:                                   # only 24 prompts — show them all
        nid = uniq_nid("prompt:" + str(p.get("slug") or p.get("title") or len(nodes)))
        node(nid, p.get("title"), "prompt", p.get("source_url")); link(nid, cat_hub(p.get("category")))
    for c in sorted(conns, key=_q, reverse=True)[:CONN_CAP]:
        nid = uniq_nid("conn:" + str(c.get("slug") or c.get("name") or len(nodes)))
        node(nid, c.get("name"), "connector", c.get("url")); link(nid, conn_hub)
        included[nid] = c

    # COMBINATIONS — items that co-occur in the same source video are a real combo "seen together".
    by_vid: dict = defaultdict(list)
    for nid, x in included.items():
        v = _vid(x)
        if v:
            by_vid[v].append(nid)
    combos = sorted((m for m in by_vid.items() if len(m[1]) >= 3), key=lambda m: len(m[1]), reverse=True)
    for i, (vid, members) in enumerate(combos[:MAX_COMBOS]):
        cnode = node(f"combo:{vid}", f"Combo · {len(members)} together", "combo",
                     f"https://www.youtube.com/watch?v={vid}")
        for m in members[:8]:
            link(cnode, m)

    valid = set(nodes)
    links = [ln for ln in links if ln["source"] in valid and ln["target"] in valid]
    n_star = sum(1 for n in nodes.values() if n["group"] == "star")
    out = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "counts": {"skills": len(skills), "tools": len(tools), "prompts": len(prompts),
                   "connectors": len(conns), "nodes": len(nodes), "links": len(links),
                   "stars": n_star, "combos": min(len(combos), MAX_COMBOS)},
        "nodes": list(nodes.values()),
        "links": links,
    }
    (DATA / "brain_graph.json").write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    print(f"brain_graph.json: {len(nodes)} nodes ({n_star} stars, {min(len(combos), MAX_COMBOS)} combos), "
          f"{len(links)} links — capped from {len(skills) + len(tools)} items for readability.")


if __name__ == "__main__":
    main()
