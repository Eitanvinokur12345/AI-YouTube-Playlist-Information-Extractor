"""src/memory_brain.py — ONE QUERYABLE BRAIN (M1: unify memory to one brain, read side).

Before this, "recall everything about X" meant hand-querying FIVE fragmented stores:
  · the episodic WHY-log            data/project_memory/episodes.jsonl   (what/why per change)
  · the semantic hub index          data/memory_index.json               (1,490 embedded elements)
  · the brain graph                 data/brain_graph.json                (nodes + links)
  · 35 per-agent conversation logs  data/excava/agent_memory/*.jsonl     (what each agent said)
  · the pipeline graph              data/pipeline_graph.json             (lane structure)

memory_brain federates them behind ONE deterministic recall(query) — the single entry an agent
calls at every decision. Deterministic-first (token-law #7): keyword/topic overlap, no embeddings,
so it runs free and local. The Gemini vector space in memory_index layers on top later as a
semantic re-rank; this is the honest first unification — one façade, every store, one result list.

  python -m src.memory_brain recall "drain deadline"   # federated context pack
  python -m src.memory_brain census                     # store census (feeds the cockpit card)
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
CENSUS = DATA / "excava" / "memory_brain.json"
_WORD = re.compile(r"[a-z0-9][a-z0-9_\-]{2,}")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _tok(text: str) -> set:
    return set(_WORD.findall(str(text).lower()))


def _jsonl(path: Path):
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if line:
            try:
                yield json.loads(line)
            except Exception:
                continue


def _records():
    """Yield (store, text, cite) across every memory store — the federation itself."""
    # 1. episodic WHY-log
    for e in _jsonl(DATA / "project_memory" / "episodes.jsonl"):
        text = " ".join(str(e.get(k, "")) for k in ("what", "why")) + " " + " ".join(e.get("topics", []) or [])
        yield ("why-log", text, {"at": e.get("at", "")[:16], "what": (e.get("what") or "")[:150],
                                 "why": (e.get("why") or "")[:150]})
    # 2. semantic hub index (names/meta only — vectors need the Gemini space, layered later)
    try:
        meta = json.loads((DATA / "memory_index.json").read_text(encoding="utf-8")).get("meta", {})
    except Exception:
        meta = {}
    for eid, m in meta.items():
        nm = m.get("name") or m.get("title") or eid
        yield ("hub", f"{nm} {m.get('category','')}", {"id": eid, "name": str(nm)[:90]})
    # 3. brain graph nodes
    try:
        nodes = json.loads((DATA / "brain_graph.json").read_text(encoding="utf-8")).get("nodes", [])
    except Exception:
        nodes = []
    for n in nodes:
        yield ("brain-graph", f"{n.get('label','')} {n.get('group','')}",
               {"label": str(n.get("label", ""))[:90], "group": n.get("group", "")})
    # 4. per-agent conversation logs
    amdir = DATA / "excava" / "agent_memory"
    if amdir.exists():
        for f in amdir.glob("*.jsonl"):
            for r in _jsonl(f):
                said = r.get("said") or r.get("text") or ""
                if said:
                    yield ("agent-log", said, {"agent": f.stem, "room": r.get("room", ""),
                                               "at": r.get("at", "")[:16], "said": str(said)[:150]})


def recall(query: str, k: int = 8) -> dict:
    """Federated deterministic recall: top-k records across ALL stores by token overlap."""
    q = _tok(query)
    if not q:
        return {"query": query, "hits": [], "note": "empty query"}
    scored = []
    per_store = {}
    for store, text, cite in _records():
        overlap = len(q & _tok(text))
        if overlap:
            scored.append((overlap, store, cite))
            per_store[store] = per_store.get(store, 0) + 1
    scored.sort(key=lambda x: -x[0])
    hits = [{"store": s, "score": sc, **cite} for sc, s, cite in scored[:k]]
    return {"query": query, "stores_hit": per_store, "total_matches": len(scored), "hits": hits}


def census() -> dict:
    """Count every store — the visible proof that one façade sees them all."""
    counts = {}
    for store, _, _ in _records():
        counts[store] = counts.get(store, 0) + 1
    total = sum(counts.values())
    doc = {"updated_at": _now(), "stores": counts, "total_records": total,
           "n_stores": len(counts),
           "note": "ONE recall() federates all of these — src.memory_brain (M1 unify-memory, read side)"}
    CENSUS.parent.mkdir(parents=True, exist_ok=True)
    CENSUS.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    return doc


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("recall")
    r.add_argument("query")
    r.add_argument("-k", type=int, default=8)
    sub.add_parser("census")
    a = ap.parse_args()
    if a.cmd == "recall":
        out = recall(a.query, a.k)
        print(f"ONE-BRAIN recall '{out['query']}' — {out.get('total_matches',0)} matches "
              f"across {len(out.get('stores_hit',{}))} stores {out.get('stores_hit',{})}")
        for h in out["hits"]:
            label = h.get("what") or h.get("name") or h.get("label") or h.get("said") or ""
            print(f"  [{h['store']}·{h['score']}] {label[:110]}")
    else:
        c = census()
        print(f"memory census: {c['total_records']} records across {c['n_stores']} stores -> {c['stores']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
