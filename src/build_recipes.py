"""
src/build_recipes.py — attach an in-project SETUP RECIPE to every tool / skill / MCP connector.

The owner wants activation + setup to happen WITHIN the project, not via links that send him elsewhere.
A static page can't install software, but the activator/EXCAVA agent CAN — if every item carries a
machine-readable recipe of what to actually run. This derives that recipe mechanically (free, no LLM)
from fields we already store (github, install_or_source, open_source, target_tool, free), so the
dashboard can show a copy-paste setup line now and the future activator can EXECUTE it (no link-out).

Recipe shape stored on each item as `setup`:
  {"kind": "...", "command": "...", "needs_key": bool, "in_project": true, ["github": "..."]}

Pure hosted web tools get NO recipe (there's nothing to install — you just use the site). Run:
  python -m src.build_recipes
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
NOW = datetime.now(timezone.utc).isoformat()
_MCP_HINTS = ("npx", "mcp add", "pip ", "pip3 ", "npm ", "uvx", "uv ", "docker", "pipx")


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")[:80]


def _repo_tail(gh: str) -> str:
    return gh.rstrip("/").split("/")[-1].removesuffix(".git") if gh else ""


def recipe(it: dict, kind: str) -> dict | None:
    src = (it.get("install_or_source") or "").strip()
    gh = (it.get("github") or "").strip()
    name = it.get("name") or it.get("skill_name") or it.get("slug") or ""
    slug = it.get("slug") or _slug(name)
    needs_key = (it.get("free") is False) or bool(it.get("needs_key"))

    if kind == "skills":
        # The in-project way to set up a hub skill IS the activator — that's the no-link path.
        cmd = src if (src and ("/" in src or "claude" in src.lower())) else f'activator: set me up with "{name}"'
        return {"kind": "claude skill", "command": cmd,
                "target": it.get("target_tool") or "claude", "needs_key": False, "in_project": True}

    if kind == "connectors":
        if src and any(h in src.lower() for h in _MCP_HINTS):
            cmd = src
        elif gh:
            cmd = f"claude mcp add {slug} -- npx -y {_repo_tail(gh)}"
        else:
            cmd = f'activator: add the "{name}" MCP connector'
        return {"kind": "mcp connector", "command": cmd, "needs_key": needs_key, "in_project": True}

    # tools
    if it.get("open_source") and gh:
        return {"kind": "open-source", "command": f"git clone {gh}", "github": gh,
                "needs_key": False, "in_project": True}
    if src and any(h in src.lower() for h in _MCP_HINTS + ("git clone", "brew", "curl")):
        return {"kind": "install", "command": src, "needs_key": needs_key, "in_project": True}
    return None        # pure hosted web tool — nothing to install locally


def main() -> int:
    total = 0
    for fname, key, kind in [("tools.json", "tools", "tools"), ("skills.json", "skills", "skills"),
                             ("connectors.json", "connectors", "connectors")]:
        p = DATA / fname
        if not p.exists():
            continue
        d = json.load(open(p, encoding="utf-8"))
        items = d.get(key, []) if isinstance(d, dict) else []
        n = 0
        for it in items:
            r = recipe(it, kind)
            if r and it.get("setup") != r:
                it["setup"] = r
                n += 1
            elif r and "setup" not in it:
                it["setup"] = r
                n += 1
        if n:
            d["recipes_updated_at"] = NOW
            p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
        total += sum(1 for it in items if it.get("setup"))
        print(f"build_recipes: {fname} — {sum(1 for it in items if it.get('setup'))} items have a setup recipe.")
    print(f"build_recipes: {total} total items now carry an in-project setup recipe.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
