"""
src/relate.py — M1.7: RELATE — real related-element rows for every element.

Relatedness is evidence, not vibes: (a) appearing in the SAME SOURCE VIDEO (+3 per shared
video — they were literally shown together), (b) shared meaningful name/description words
(+1 each, capped), (c) same category (+1). Top 3-8 land in data/elements_related.json;
the elements_index join carries them to the detail view, the brain graph, and packages.

Inverted-index implementation — the full 6.4k set relates in seconds, no O(n^2).

Fire 55 (2026-07-29): the score>=2 cutoff left every element with ONLY a category match
(score==1) — mostly the ~1,900 zero-provenance stubs (empty source_videos, empty `what`,
so no video/word evidence at all, just a category) — with an EMPTY related[] forever, even
though a same-category candidate is still real, useful evidence for M1.7's "each detail
shows 3-8 real related elements" goal. Elements that still have <3 after the score>=2 pass
now get backfilled from the SAME already-computed score dict at score>=1 (still real
same-category evidence, never invented), up to 3 total — so a stub with nothing but a
category now shows a few same-category neighbors instead of a bare "no related items" panel.
Elements with real evidence (score>=2 from a shared video/word) are completely unaffected.
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
        ranked = sorted(score.items(), key=lambda kv: -kv[1])
        strong = [els[j]["id"] for j, s in ranked if s >= 2][:8]
        # Backfill (never overwrite) with weaker same-category-only evidence (score==1)
        # so a zero-provenance stub still shows a few real neighbors instead of nothing.
        if len(strong) < 3:
            seen = set(strong)
            for j, s in ranked:
                if s < 1:
                    break
                jid = els[j]["id"]
                if jid in seen:
                    continue
                strong.append(jid)
                seen.add(jid)
                if len(strong) >= 3:
                    break
        related[el["id"]] = strong

    OUT.write_text(json.dumps({"generated_at": datetime.now(timezone.utc).isoformat(),
                               "related": related}, ensure_ascii=False), encoding="utf-8")
    with_rel = sum(1 for v in related.values() if len(v) >= 3)
    with_any = sum(1 for v in related.values() if len(v) >= 1)
    print(f"relate: {len(related)} elements mapped; {with_rel} have >=3 related, "
          f"{with_any} have >=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
