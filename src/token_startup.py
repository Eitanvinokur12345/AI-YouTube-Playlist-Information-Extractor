"""
src/token_startup.py — the TOKEN-REDUCTION protocol: run ALL token reducers on every startup.

The owner wanted the "Token savers" panel turned into a protocol that, every time the system runs,
activates every token-reduction technique the project knows — so the Claude-using lanes (deep
analyze, the 2x/week review) spend as few Claude-Pro tokens as possible. This compiles the catalogued
token-saver skills (data/token_tips.json) PLUS the project's own hard rules into one ACTIVE directive
at data/token_active.json. CLAUDE.md and REVIEW.md tell the Claude lanes to obey that directive, so
the reducers are genuinely applied on every run, not just listed. Free, mechanical, runs first.

Run:  python -m src.token_startup
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "token_active.json"
NOW = datetime.now(timezone.utc).isoformat()

# The hard reducers the project always applies (concrete, enforceable techniques).
CORE_REDUCERS = [
    ("Lean tool output", "Run scripts with their --lean/quiet flags; never paste raw JSON or full file dumps into context."),
    ("Read only what's needed", "Read specific line ranges, not whole files; don't re-read a file already in context."),
    ("Compact often", "Summarize and drop stale context (/compact-style) before it bloats; keep only the working set."),
    ("Batch independent work", "Do independent reads/edits in one pass; avoid back-and-forth round-trips."),
    ("Prefer mechanical over Claude", "Use the free Python protocols + free engine pool for anything that doesn't need Claude; reserve Claude for judgement."),
    ("Terse writing", "No restated headings, no filler, no marketing words; every sentence earns its place."),
    ("Cache & reuse", "Reuse prior results and the hub data instead of re-deriving; don't recompute what's stored."),
    ("Delegate huge context", "For large-context jobs, dispatch a focused sub-agent with only the slice it needs, not the whole history."),
]


def _load(name):
    try:
        return json.load(open(DATA / name, encoding="utf-8"))
    except Exception:
        return {}


def main() -> int:
    tips = (_load("token_tips.json") or {}).get("skills", [])
    catalogued = [{"name": s.get("name"), "why": s.get("why", "")} for s in tips[:8] if s.get("name")]
    directive = ("TOKEN BUDGET MODE (always on). Spend the fewest Claude tokens possible:\n"
                 + "\n".join(f"- {n}: {t}" for n, t in CORE_REDUCERS)
                 + ("\nAlso apply the techniques from these catalogued token-saver skills: "
                    + ", ".join(c["name"] for c in catalogued) + "." if catalogued else ""))
    OUT.write_text(json.dumps({
        "generated_at": NOW,
        "status": "active",
        "count": len(CORE_REDUCERS) + len(catalogued),
        "core_reducers": [{"name": n, "technique": t} for n, t in CORE_REDUCERS],
        "catalogued_skills": catalogued,
        "directive": directive,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"token_startup: token-reduction ACTIVE — {len(CORE_REDUCERS)} core + {len(catalogued)} "
          f"catalogued reducers compiled into data/token_active.json.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
