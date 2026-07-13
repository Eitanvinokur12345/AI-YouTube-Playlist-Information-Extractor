"""
src/discover_promote.py — R2 stage 2 (owner: 'more retrieval sources'). The discovery agent
already MINES new sources (HuggingFace, arXiv, GitHub, Product Hunt, Reddit, HN) into
social_intake.json — this turns the structured, high-signal finds into element-shaped
DISCOVERIES the owner can actually see and act on, WITHOUT polluting the canonical hub
(elements_index.json) with unverified intake. A promote-to-hub step waits on an owner answer
(saved in pending_questions.json).

Output: data/discovered_elements.json — recent discoveries, source-labeled, deduped by url,
status 'discovered' (unverified). Surfaced in the Sources tab.
Free, stdlib-only. Run: python -m src.discover_promote
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "discovered_elements.json"

# structured sources whose finds map cleanly to a hub element type (skip vague web/forum chatter)
SRC_TYPE = {"huggingface-model": "model", "huggingface-space": "tool", "arxiv": "paper",
            "gh-new": "tool", "gh-active": "tool", "producthunt": "tool"}


def promote(max_keep: int = 120) -> dict:
    try:
        intake = json.load(open(DATA / "social_intake.json", encoding="utf-8"))
        items = intake.get("items", intake if isinstance(intake, list) else [])
    except Exception:
        items = []
    out, seen = [], set()
    for it in items:
        src = it.get("source", "")
        etype = SRC_TYPE.get(src)
        if not etype:
            continue
        url = (it.get("url") or "").strip()
        if not url or url in seen:
            continue
        seen.add(url)
        title = (it.get("title") or "").strip()
        name = re.split(r"\s+[—-]\s+", title)[0][:80] or url
        out.append({"id": f"discovered:{etype}:{re.sub(r'[^a-z0-9]+', '-', name.lower())[:40].strip('-')}",
                    "type": etype, "name": name, "what": title[:160],
                    "source": src, "url": url, "status": "discovered",
                    "found_at": it.get("found_at", "")})
    # newest first
    out.sort(key=lambda x: x.get("found_at", ""), reverse=True)
    out = out[:max_keep]
    from collections import Counter
    report = {"generated_at": datetime.now(timezone.utc).isoformat(),
              "total": len(out), "by_source": dict(Counter(x["source"] for x in out)),
              "by_type": dict(Counter(x["type"] for x in out)),
              "note": "R2: structured finds from the new retrieval sources (HuggingFace, arXiv, "
                      "GitHub, Product Hunt). Status 'discovered' = mined, not yet verified into "
                      "the canonical hub (that promotion awaits an owner decision).",
              "elements": out}
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    return report


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    r = promote()
    print(f"discover-promote: {r['total']} discoveries staged; by source {r['by_source']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
