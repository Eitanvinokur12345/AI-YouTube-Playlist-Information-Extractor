"""
src/graph_expand.py — GRAPH EXPANSION (owner 2026-07-13: the brain graph is nice but 'not ALL
the information is in it'). The brain graph holds only hub ELEMENTS; this adds the OWNER LAYER —
what you said, what EXCAVA asked, what you answered, and the problems fixed — as nodes woven in,
so the graph is the whole project's memory, not just its catalogue.

Idempotent: strips any prior owner-layer nodes ('owner:' id prefix) and re-adds the current set,
so a hub rebuild can't silently drop it. Beat-wired after the memory/brain step.
Output: rewrites data/brain_graph.json (adds owner nodes + links + a central hub node).
Free, stdlib-only. Run: python -m src.graph_expand
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
GRAPH = DATA / "brain_graph.json"
KEEP = 120           # cap owner items so the graph stays renderable


def _jsonl(p: Path):
    if not p.exists():
        return []
    out = []
    for ln in p.read_text(encoding="utf-8").splitlines():
        try:
            out.append(json.loads(ln))
        except Exception:
            pass
    return out


def expand() -> dict:
    try:
        g = json.load(open(GRAPH, encoding="utf-8"))
    except Exception:
        g = {"nodes": [], "links": []}
    # strip prior owner layer (idempotent)
    g["nodes"] = [n for n in g.get("nodes", []) if not str(n.get("id", "")).startswith("owner:")]
    g["links"] = [l for l in g.get("links", [])
                  if not (str(l.get("source", "")).startswith("owner:")
                          or str(l.get("target", "")).startswith("owner:"))]
    HUB = "owner:__history__"
    nodes = [{"id": HUB, "label": "🧑 OWNER HISTORY", "group": "owner-hub"}]
    links = []
    n = 0
    # owner messages, questions, answers from the ingested history
    for r in _jsonl(DATA / "excava" / "history.jsonl")[-KEEP:]:
        kind = r.get("kind", "")
        grp = {"owner_msg": "you-said", "question": "excava-asked",
               "answer": "you-answered"}.get(kind)
        if not grp:
            continue
        txt = (r.get("text") or r.get("question") or r.get("q") or "").strip()
        if len(txt) < 12:
            continue
        nid = f"owner:{kind}:{n}"
        nodes.append({"id": nid, "label": txt[:70], "group": grp})
        links.append({"source": HUB, "target": nid})
        n += 1
    # problems fixed / changes from the improvement log
    for r in _jsonl(DATA / "excava" / "improvements.jsonl")[-40:]:
        nid = f"owner:fix:{n}"
        nodes.append({"id": nid, "label": (r.get("what") or r.get("kind") or "change")[:70],
                      "group": "problem-fixed"})
        links.append({"source": HUB, "target": nid})
        n += 1
    g["nodes"] = g.get("nodes", []) + nodes
    g["links"] = g.get("links", []) + links
    g["counts"] = g.get("counts", {})
    g["counts"]["owner_layer"] = len(nodes)
    g["owner_layer_generated_at"] = datetime.now(timezone.utc).isoformat()
    GRAPH.write_text(json.dumps(g, ensure_ascii=False), encoding="utf-8")
    return {"owner_nodes": len(nodes), "total_nodes": len(g["nodes"]),
            "total_links": len(g["links"])}


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    r = expand()
    print(f"graph-expand: +{r['owner_nodes']} owner nodes (you-said / excava-asked / you-answered "
          f"/ problem-fixed); graph now {r['total_nodes']} nodes, {r['total_links']} links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
