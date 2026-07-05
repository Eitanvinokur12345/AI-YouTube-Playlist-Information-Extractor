"""
src/relate.py — M1.7: RELATE — real related-element rows for every element.

Relatedness is evidence, not vibes: (a) appearing in the SAME SOURCE VIDEO (+3 per shared
video — they were literally shown together), (b) shared meaningful name/description words
(+1 each, capped), (c) same category (+1). Top 3-8 land in data/elements_related.json;
the elements_index join carries them to the detail view, the brain graph, and packages.

Inverted-index implementation — the full 6.4k set relates in seconds, no O(n^2).
Run: python -m src.relate
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from src import element_model as em

DATA = Path(__file__).parent.parent / "data"
OUT = DATA / "elements_related.json"
STOP = {"the", "and", "for", "with", "your", "that", "from", "into", "tool", "tools",
        "using", "based", "open", "source", "free", "claude", "code"}


def _words(el: dict) -> set:
    text = f"{el['name']} {el.get('what', '')[:120]}"
    return {w for w in re.findall(r"[a-z][a-z\-]{3,}", text.lower()) if w not in STOP}


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    els = em.build()["elements"]
    by_video, by_word, by_cat = defaultdict(list), defaultdict(list), defaultdict(list)
    words_of = {}
    for i, el in enumerate(els):
        for v in el.get("source_videos", []):
            by_video[v].append(i)
        w = _words(el)
        words_of[el["id"]] = w
        for word in w:
            if len(by_word[word]) < 400:            # ignore ubiquitous words
                by_word[word].append(i)
        if el.get("category"):
            by_cat[el["category"]].append(i)

    related = {}
    for i, el in enumerate(els):
        score = defaultdict(int)
        for v in el.get("source_videos", []):
            for j in by_video[v]:
                score[j] += 3
        for word in words_of[el["id"]]:
            bucket = by_word[word]
            if len(bucket) <= 60:                   # informative words only
                for j in bucket:
                    score[j] += 1
        for j in by_cat.get(el.get("category", ""), [])[:200]:
            score[j] += 1
        score.pop(i, None)
        top = sorted(score.items(), key=lambda kv: -kv[1])[:8]
        related[el["id"]] = [els[j]["id"] for j, s in top if s >= 2][:8]

    OUT.write_text(json.dumps({"generated_at": datetime.now(timezone.utc).isoformat(),
                               "related": related}, ensure_ascii=False), encoding="utf-8")
    with_rel = sum(1 for v in related.values() if len(v) >= 3)
    print(f"relate: {len(related)} elements mapped; {with_rel} have >=3 related")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
