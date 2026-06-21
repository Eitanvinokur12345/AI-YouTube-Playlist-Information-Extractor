"""
activate.py — ACTIVATE a chosen item from the Excavatortron hub (not copy-paste).

  python activate.py skill <slug>                      # install SKILL.md into ~/.claude/skills/<slug>/ (live in Claude)
  python activate.py connector <slug>                  # print the mcpServers JSON + how to add it
  python activate.py deploy skill <slug> --tool "X"    # WRITE a native artifact for ANY tool (Cursor .mdc / Copilot /
                                                       #   ChatGPT / Gemini / Antigravity / Stitch / Gamma / Omni / Midjourney / …)
  python activate.py deploy tool|prompt|command <slug> --tool "X"
  python activate.py combo skill:<slug> connector:<slug> tool:<slug> --tool "X"   # activate a whole recommended COMBINATION at once
  python activate.py paste skill|tool|prompt|command <slug>                       # print the portable capability block to stdout
  python activate.py manifest                          # list everything you've activated (so you can swap/uninstall)

Reads the hub locally (inside the repo) or from the public API. Stdlib only.
"""
from __future__ import annotations

import json
import re
import shutil
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

MANIFEST = Path.home() / ".claude" / "excavatortron-activated.json"

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


_KINDS = {"skill": ("skills.json", "skills", "skill_name"), "tool": ("tools.json", "tools", "name"),
          "prompt": ("prompts.json", "prompts", "title"), "command": ("commands.json", "commands", "command")}


def _block(kind: str, x: dict) -> tuple[str, str]:
    """(title, instruction-block text) — the portable capability, ready for any tool."""
    nk = _KINDS[kind][2]
    title = str(x.get(nk) or x.get("slug") or kind)
    body = [f"# {title}", "", str(x.get("description") or x.get("purpose") or x.get("what_it_does") or "").strip()]
    if x.get("use_case"):
        body += ["", f"When to use: {x['use_case']}"]
    if x.get("output"):
        body += ["", f"What it produces: {x['output']}"]
    if x.get("prompt_text"):
        body += ["", x["prompt_text"]]
    tips = (x.get("tips") or []) + (x.get("general_tips") or [])
    if tips:
        body += ["", "Guidance:"] + [f"- {t}" for t in tips[:8]]
    if x.get("slash_commands"):
        body += ["", "Commands: " + " ".join(x["slash_commands"])]
    if x.get("source_url"):
        body += ["", f"Source: {x['source_url']}"]
    return title, "\n".join(body)


# Known NATIVE formats. For everything else (any current/future tool) we still write a portable
# instructions file — so the activator works for EVERY tool, not a fixed list.
_NATIVE = {
    "cursor": (".cursor/rules/{slug}.mdc", "Cursor rule — move into your project's .cursor/rules/."),
    "windsurf": (".windsurf/rules/{slug}.md", "Windsurf rule — move into .windsurf/rules/."),
    "copilot": (".github/copilot-instructions.md", "GitHub Copilot — repo-level instructions."),
    "chatgpt": ("chatgpt/{slug}.instructions.md", "ChatGPT — paste as a Custom GPT's / Project's instructions."),
    "gpt": ("chatgpt/{slug}.instructions.md", "ChatGPT — paste as a Custom GPT's / Project's instructions."),
    "gemini": ("gemini/{slug}.gem.md", "Gemini — paste as a Gem's instructions."),
}


def _native_for(tool: str):
    t = (tool or "").lower().strip()
    for k, v in _NATIVE.items():
        if k in t:
            return v
    safe = re.sub(r"[^a-z0-9]+", "-", t).strip("-") or "any-tool"
    return (safe + "/{slug}.instructions.md",
            f"{tool or 'This tool'} — paste this into its instruction / system-prompt / brief field "
            f"(its equivalent of a 'skill' loaded into the environment).")


def _manifest_add(entry: dict) -> None:
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
    except Exception:
        data = {}
    data.setdefault("activated", [])
    entry["at"] = datetime.now(timezone.utc).isoformat()
    data["activated"].append(entry)
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def deploy(kind: str, slug: str, tool: str) -> int:
    if kind not in _KINDS:
        print("kind must be skill|tool|prompt|command"); return 2
    x = _find(_KINDS[kind][0], _KINDS[kind][1], slug)
    if not x:
        print(f"{kind} '{slug}' not found in the hub."); return 1
    title, content = _block(kind, x)
    pathtpl, header = _native_for(tool)
    rel = pathtpl.format(slug=_slug(slug))
    dest = Path.cwd() / "excavatortron-deploy" / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(f"<!-- {header} -->\n\n{content}\n", encoding="utf-8")
    print(f"OK: wrote a native '{tool or 'portable'}' artifact -> {dest}")
    print(f"   {header}")
    _manifest_add({"type": kind, "slug": _slug(slug), "tool": tool or "portable", "artifact": str(dest)})
    return 0


def paste(kind: str, slug: str) -> int:
    """Print the portable capability block to stdout — for a skill with no packaged SKILL.md,
    or any item you want to drop straight into a tool's instruction field."""
    if kind not in _KINDS:
        print("kind must be skill|tool|prompt|command"); return 2
    x = _find(_KINDS[kind][0], _KINDS[kind][1], slug)
    if not x:
        print(f"{kind} '{slug}' not found in the hub."); return 1
    _title, content = _block(kind, x)
    print(content)
    return 0


def combo(specs: list[str], tool: str) -> int:
    """Activate a whole recommended COMBINATION at once.
    specs look like:  skill:<slug>  connector:<slug>  tool:<slug>  prompt:<slug>  command:<slug>
    (exactly what find.py's recipe.activate_all emits). Each is activated by its kind."""
    if not specs:
        print("usage: activate.py combo skill:<slug> connector:<slug> tool:<slug> [...] --tool \"X\"")
        return 2
    rc = 0
    for spec in specs:
        kind, _, slug = spec.partition(":")
        if not slug:
            print(f"  skip malformed '{spec}'"); continue
        print(f"\n=== {kind}: {slug} ===")
        if kind == "skill":
            r = install_skill(slug)
            if r == 0:
                _manifest_add({"type": "skill", "slug": _slug(slug), "tool": "claude",
                               "artifact": str(Path.home() / ".claude" / "skills" / _slug(slug) / "SKILL.md")})
        elif kind == "connector":
            r = show_connector(slug)
        elif kind in _KINDS:
            r = deploy(kind, slug, tool or "claude")
        else:
            print(f"  unknown kind '{kind}'"); r = 1
        rc = rc or r
    print("\nCombination activated. Run 'python activate.py manifest' to see everything active.")
    return rc


def show_manifest() -> int:
    if not MANIFEST.exists():
        print("Nothing activated yet."); return 0
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for e in data.get("activated", []):
        print(f"  [{e.get('at','')[:19]}] {e.get('type')} {e.get('slug')} -> {e.get('tool')}  {e.get('artifact','')}")
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
        rc = install_skill(a[1])
        if rc == 0:
            _manifest_add({"type": "skill", "slug": _slug(a[1]), "tool": "claude",
                           "artifact": str(Path.home() / ".claude" / "skills" / _slug(a[1]) / "SKILL.md")})
        return rc
    if cmd == "connector" and len(a) >= 2:
        return show_connector(a[1])
    if cmd == "deploy" and len(a) >= 3:
        return deploy(a[1], a[2], tool)
    if cmd == "paste" and len(a) >= 3:
        return paste(a[1], a[2])
    if cmd == "combo" and len(a) >= 2:
        return combo(a[1:], tool)
    if cmd in ("manifest", "list"):
        return show_manifest()
    print(__doc__); return 2


if __name__ == "__main__":
    raise SystemExit(main())
