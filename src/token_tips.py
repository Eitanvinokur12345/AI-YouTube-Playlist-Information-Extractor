"""
src/token_tips.py — surface the hub's best TOKEN-EFFICIENCY skills for Claude.

The owner asked Excavatortron to offer skills for using fewer / better tokens in Claude. The library
already catalogues many; this pulls the strongest into data/token_tips.json so the dashboard can
show them in one place (and the activator can offer them). Free, mechanical.

Run:  python -m src.token_tips
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "token_tips.json"
KW = ("token", "context window", "context management", "compact", "prune", "cache", "caching",
      "cheaper", "efficien", "minimal context", "cost optim", "context efficiency", "subagent",
      "context rot", "/compact", "lean")


def _load(name, default):
    try:
        return json.load(open(DATA / name, encoding="utf-8"))
    except Exception:
        return default


def _blob(x):
    return " ".join(str(x.get(k, "")) for k in ("skill_name", "name", "description", "use_case", "category")).lower()


def main() -> int:
    skills = (_load("skills.json", {}) or {}).get("skills", [])
    cmds = (_load("commands.json", {}) or {}).get("commands", [])
    hits = [s for s in skills if any(k in _blob(s) for k in KW)]
    hits.sort(key=lambda s: s.get("quality_score", 0) or 0, reverse=True)
    skill_tips = [{
        "name": s.get("skill_name") or s.get("slug"),
        "slug": s.get("slug"),
        "quality": s.get("quality_score"),
        "why": (str(s.get("use_case") or s.get("description") or "")[:160]),
        "url": s.get("source_url", ""),
    } for s in hits[:10]]
    cmd_tips = [{"command": c.get("command"), "description": (str(c.get("description") or "")[:120])}
                for c in cmds if any(k in (str(c.get("command", "")) + str(c.get("description", ""))).lower()
                                     for k in ("compact", "token", "context", "cost", "clear"))][:6]
    OUT.write_text(json.dumps({
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "count": len(hits),
        "skills": skill_tips,
        "commands": cmd_tips,
        "activator_hint": 'Run the activator: ask it to "set me up to use fewer tokens in Claude" '
                          'and it assembles a token-saving combination (skill + /compact + memory MCP).',
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"token_tips: {len(hits)} token-efficiency skills found; surfaced top {len(skill_tips)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
