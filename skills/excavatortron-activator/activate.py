"""
activate.py — ACTIVATE a chosen item from the Excavatortron hub (not copy-paste).

  python activate.py skill <slug>                 # install SKILL.md into ~/.claude/skills/<slug>/ (live in Claude)
  python activate.py connector <slug>             # print the mcpServers JSON + how to add it
  python activate.py paste skill <slug> [--tool X]  # emit a deploy block for any tool (ChatGPT/Gemini/Cursor/Antigravity/…)
  python activate.py paste tool|prompt|command <slug>

Reads the hub locally (inside the repo) or from the public API. Stdlib only.
"""
from __future__ import annotations

import json
import shutil
import sys
import urllib.request
from pathlib import Path

BASE = "https://eitanvinokur12345.github.io/AI-YouTube-Playlist-Information-Extractor/data/"
RAW = "https://raw.githubusercontent.com/Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor/main/"


def _repo_root() -> Path | None:
    p = Path(__file__).resolve().parent
    for _ in range(6):
        if (p / "data" / "skills.json").exists() and (p / "skills").exists():
            return p
        p = p.parent
    return None


def _load(name: str):
    rr = _repo_root()
    if rr and (rr / "data" / name).exists():
        try:
            return json.load(open(rr / "data" / name, encoding="utf-8"))
        except Exception:
            pass
    try:
        req = urllib.request.Request(BASE + name, headers={"User-Agent": "Mozilla/5.0"})
        return json.loads(urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "replace"))
    except Exception:
        return {}


def _slug(s: str) -> str:
    import re
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")


def _find(name, key, slug):
    want = _slug(slug)
    d = _load(name)
    for x in (d.get(key, []) if isinstance(d, dict) else []):
        if not isinstance(x, dict):
            continue
        cands = {(x.get("slug") or "").lower(), _slug(str(x.get("name", ""))),
                 _slug(str(x.get("skill_name", ""))), _slug(str(x.get("title", "")))}
        if want in cands or slug.lower() in cands:
            return x
    return None


def install_skill(slug: str) -> int:
    slug = _slug(slug)
    rr = _repo_root()
    src = (rr / "skills" / slug / "SKILL.md") if rr else None
    md = None
    if src and src.exists():
        md = src.read_bytes()
    else:
        try:
            md = urllib.request.urlopen(RAW + f"skills/{slug}/SKILL.md", timeout=20).read()
        except Exception as e:
            print(f"Could not find a SKILL.md package for '{slug}': {e}")
            print("  (Tip: pass the exact 'slug' from find.py. Not every catalogued skill has a "
                  "SKILL.md yet — for those, use:  python activate.py paste skill <slug>)")
            return 1
    dest = Path.home() / ".claude" / "skills" / slug
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "SKILL.md").write_bytes(md)
    print(f"OK: installed skill -> {dest / 'SKILL.md'}")
    print("  Claude Code: live now. Claude Desktop: restart to load it.")
    return 0


def show_connector(slug: str) -> int:
    c = _find("connectors.json", "connectors", slug)
    if not c:
        print(f"connector '{slug}' not found in the hub.")
        return 1
    name = c.get("name", slug)
    print(f"# MCP connector: {name}")
    print(f"# {c.get('what_it_does','')}")
    if c.get("install_or_source"):
        print(f"# install/source: {c['install_or_source']}")
    if c.get("url"):
        print(f"# website/repo: {c['url']}")
    print("\n# Claude Desktop — add to claude_desktop_config.json:")
    print(json.dumps({"mcpServers": {slug: {"command": "npx", "args": ["-y", "<package-from-the-repo-above>"]}}}, indent=2))
    print("\n# Claude Code:  claude mcp add " + slug + " -- npx -y <package-from-the-repo-above>")
    print("# Then restart — its tools appear in your session.")
    return 0


def paste(kind: str, slug: str, tool: str) -> int:
    name_key = {"skill": ("skills.json", "skills", "skill_name"), "tool": ("tools.json", "tools", "name"),
                "prompt": ("prompts.json", "prompts", "title"), "command": ("commands.json", "commands", "command")}.get(kind)
    if not name_key:
        print("kind must be skill|tool|prompt|command"); return 2
    x = _find(name_key[0], name_key[1], slug)
    if not x:
        print(f"{kind} '{slug}' not found."); return 1
    t = (tool or x.get("target_tool") or "").lower()
    how = "Paste this into the tool's system prompt or first message — it loads the capability into the session."
    if "chatgpt" in t or "gpt" in t:
        how = "ChatGPT: paste as a Custom GPT's / Project's instructions, or as your first message."
    elif "gemini" in t:
        how = "Gemini: paste as a Gem's instructions, or into the chat."
    elif "cursor" in t or "windsurf" in t:
        how = "Cursor/Windsurf: add to your rules file (.cursor/rules / .windsurfrules), or paste in chat."
    elif "antigravity" in t or "stitch" in t or "gamma" in t or "omni" in t:
        how = f"{tool}: paste into its instruction / brief field (or first prompt)."
    body = [f"# {x.get(name_key[2], slug)}", "", str(x.get("description") or x.get("purpose") or x.get("what_it_does") or "").strip()]
    if x.get("use_case"):
        body += ["", f"When to use: {x['use_case']}"]
    if x.get("prompt_text"):
        body += ["", x["prompt_text"]]
    for tip in (x.get("tips") or [])[:6]:
        body.append(f"- {tip}")
    if x.get("source_url"):
        body += ["", f"Source: {x['source_url']}"]
    print(f"## How to deploy ({tool or x.get('target_tool') or 'any tool'}):\n{how}\n")
    print("## Ready-to-paste block:\n" + "\n".join(body))
    return 0


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")   # Windows console is cp1252 by default
    except Exception:
        pass
    a = sys.argv[1:]
    if not a:
        print(__doc__); return 2
    cmd = a[0]
    tool = ""
    if "--tool" in a:
        i = a.index("--tool"); tool = a[i + 1] if i + 1 < len(a) else ""; a = a[:i] + a[i + 2:]
    if cmd == "skill" and len(a) >= 2:
        return install_skill(a[1])
    if cmd == "connector" and len(a) >= 2:
        return show_connector(a[1])
    if cmd == "paste" and len(a) >= 3:
        return paste(a[1], a[2], tool)
    print(__doc__); return 2


if __name__ == "__main__":
    raise SystemExit(main())
