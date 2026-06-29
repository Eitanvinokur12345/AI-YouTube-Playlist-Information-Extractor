"""
src/build_memory.py — EXCAVA's semantic MEMORY: embed the hub so it recalls by MEANING.

The owner's "link the processors + improve memory + effectiveness" layer. Embeds each item
(name + description) with Google's FREE embedding model and stores a compact vector index at
data/memory_index.json. EXCAVA + the activator can then match a task to the right tools by meaning,
not just keywords — and every process shares one memory. Incremental + budgeted (resumes via state),
top-quality first, output dim 256 to keep the index small. Uses the Gemini keys already set. Free.

Run:  python -m src.build_memory --limit 250
"""
from __future__ import annotations

import argparse
import json
import math
import os
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "memory_index.json"
NOW = datetime.now(timezone.utc).isoformat()
MODEL = "text-embedding-004"
DIM = 256
CAP = 1400          # embed the top-quality items; keeps the index small + relevant


def _keys() -> list[str]:
    ks = []
    for n in ["EXTERNAL_REVIEW_API_KEY", "GEMINI_API_KEY"] + [f"GEMINI_API_KEY_{i}" for i in range(2, 9)]:
        v = (os.environ.get(n) or "").strip()
        if v and v not in ks:
            ks.append(v)
    return ks


def embed(text: str, key: str, timeout: int = 30) -> list | None:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:embedContent?key={key}"
    body = {"model": f"models/{MODEL}", "content": {"parts": [{"text": text[:2000]}]},
            "outputDimensionality": DIM}
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            v = json.loads(r.read().decode("utf-8", "replace"))["embedding"]["values"]
        return [round(float(x), 4) for x in v]
    except Exception as e:
        return {"_err": f"{type(e).__name__}:{str(e)[:80]}"}  # type: ignore


def _items():
    out = []
    for fname, key, nk in [("tools.json", "tools", "name"), ("skills.json", "skills", "skill_name"),
                           ("connectors.json", "connectors", "name"), ("models.json", "models", "name")]:
        d = json.load(open(DATA / fname, encoding="utf-8")) if (DATA / fname).exists() else {}
        for x in (d.get(key, []) if isinstance(d, dict) else []):
            slug = x.get("slug") or x.get(nk)
            if slug:
                out.append((f"{key}:{slug}", x.get(nk) or slug, key,
                            x.get("quality_score") or 0,
                            f"{x.get(nk) or ''}. {x.get('description') or x.get('what_it_does') or ''}"))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--limit", type=int, default=250)
    ap.add_argument("--sleep", type=float, default=0.4); args = ap.parse_args()
    keys = _keys()
    if not keys:
        print("build_memory: no Gemini key — skipped (graceful)."); return 0

    idx = json.load(open(OUT, encoding="utf-8")) if OUT.exists() else {"dim": DIM, "model": MODEL, "vectors": {}, "meta": {}}
    vecs, meta = idx.get("vectors", {}), idx.get("meta", {})
    items = sorted(_items(), key=lambda t: t[3], reverse=True)[:CAP]
    ki = done = err = 0
    for ident, name, typ, q, text in items:
        if done >= args.limit:
            break
        if ident in vecs:
            continue
        ki = (ki + 1) % len(keys); time.sleep(args.sleep)
        v = embed(text, keys[ki])
        if isinstance(v, list):
            vecs[ident] = v; meta[ident] = {"name": name, "type": typ}; done += 1
        else:
            err += 1
            if err >= 8:
                print("  many embed errors — stopping (quota?)."); break
    idx.update({"dim": DIM, "model": MODEL, "vectors": vecs, "meta": meta, "updated_at": NOW})
    OUT.write_text(json.dumps(idx, ensure_ascii=False), encoding="utf-8")
    print(f"build_memory: +{done} embeddings ({err} errors); index now {len(vecs)}/{len(items)} items.")
    return 0


def search(query_vec: list, idx: dict, k: int = 8) -> list:
    """Cosine top-k over the index — for EXCAVA/activator semantic recall (query embedded by caller)."""
    def cos(a, b):
        s = sum(x * y for x, y in zip(a, b)); na = math.sqrt(sum(x * x for x in a)) or 1
        nb = math.sqrt(sum(y * y for y in b)) or 1
        return s / (na * nb)
    scored = [(cos(query_vec, v), ident) for ident, v in idx.get("vectors", {}).items()]
    scored.sort(reverse=True)
    return [{"id": i, **idx.get("meta", {}).get(i, {}), "score": round(s, 3)} for s, i in scored[:k]]


if __name__ == "__main__":
    raise SystemExit(main())
