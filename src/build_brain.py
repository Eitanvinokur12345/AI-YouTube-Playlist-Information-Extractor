"""
src/build_brain.py — generate a rich Obsidian "brain" of the WHOLE project from the data, so
you can browse it and see the graph in the desktop Obsidian app.

It writes a note per skill / tool / prompt / connector, each wikilinked to its CATEGORY hub and
(for skills) its TOOL hub — so Obsidian's graph view clusters everything by category and tool.
It also copies the 25 structural notes (how the project is built) into a Project/ folder, and a
Home note. Re-runnable: it overwrites the generated folders, leaving your own notes alone.

Usage:
    python -m src.build_brain "C:/Users/eitan/OneDrive/Documents/Excavatortron obsidian brain/Excavatortorn"
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
BRAIN = ROOT / "brain"
DEFAULT_VAULT = r"C:/Users/eitan/OneDrive/Documents/Excavatortron obsidian brain/Excavatortorn"
GEN_FOLDERS = ["Skills", "Tools", "Prompts", "Connectors", "Categories", "Tools-hubs", "Project"]


def load(name: str):
    try:
        return json.load(open(DATA / name, encoding="utf-8"))
    except Exception:
        return {}


def title(s: str) -> str:
    # Obsidian note title: drop characters illegal in filenames/wikilinks, keep it readable.
    t = re.sub(r'[\\/:*?"<>|#^\[\]]+', " ", str(s or "")).strip()
    t = re.sub(r"\s+", " ", t)
    return t[:90] or "item"


def wl(s: str) -> str:
    return f"[[{title(s)}]]"


def write(vault: Path, rel: str, text: str) -> None:
    p = vault / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def main() -> None:
    vault = Path(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_VAULT)
    vault.mkdir(parents=True, exist_ok=True)
    # clear previously-generated folders so re-runs stay clean (leave the user's own notes)
    import shutil
    for g in GEN_FOLDERS:
        d = vault / g
        if d.exists():
            shutil.rmtree(d, ignore_errors=True)

    skills = (load("skills.json") or {}).get("skills", [])
    tools = (load("tools.json") or {}).get("tools", [])
    prompts = (load("prompts.json") or {}).get("prompts", [])
    conns = (load("connectors.json") or {}).get("connectors", [])
    cats: set[str] = set()
    toolhubs: set[str] = set()
    n = 0

    for s in skills:
        name = title(s.get("skill_name") or s.get("slug") or "skill")
        cat = (s.get("category") or "other"); cats.add(cat)
        tt = title(s.get("target_tool") or "claude"); toolhubs.add(tt)
        b = [f"---", "tags: [skill]", "---", f"# {name}", "", (s.get("description") or "").strip(), ""]
        if s.get("use_case"):
            b += [f"**Use case:** {s['use_case'].strip()}", ""]
        for t in (s.get("tips") or [])[:5]:
            b.append(f"- {str(t).strip()}")
        b += ["", f"Category:: {wl(cat)}", f"Tool:: {wl(tt)}", ""]
        if s.get("source_url"):
            b.append(f"[Source]({s['source_url']})")
        write(vault, f"Skills/{name}.md", "\n".join(b)); n += 1

    for t in tools:
        name = title(t.get("name") or t.get("slug") or "tool")
        cat = (t.get("category") or "other"); cats.add(cat)
        b = ["---", "tags: [tool]", "---", f"# {name}", "", (t.get("description") or "").strip(), "",
             f"Category:: {wl(cat)}"]
        if t.get("company"):
            b.append(f"Company: {t.get('company')}{' · ' + t['country'] if t.get('country') else ''}")
        if t.get("release_status") == "upcoming":
            b.append("Status: 🔜 upcoming")
        if t.get("source_url"):
            b += ["", f"[Source]({t['source_url']})"]
        write(vault, f"Tools/{name}.md", "\n".join(b)); n += 1

    for p in prompts:
        name = title(p.get("title") or "prompt")
        cat = (p.get("category") or "other"); cats.add(cat)
        b = ["---", "tags: [prompt]", "---", f"# {name}", "", (p.get("purpose") or "").strip(), "",
             "```", (p.get("prompt_text") or "").strip(), "```", "", f"Category:: {wl(cat)}"]
        write(vault, f"Prompts/{name}.md", "\n".join(b)); n += 1

    for c in conns:
        name = title(c.get("name") or "connector")
        b = ["---", "tags: [connector]", "---", f"# {name}", "", (c.get("what_it_does") or "").strip(), ""]
        if c.get("works_in"):
            b.append(f"Works in: {c.get('works_in')}")
        b.append(f"Type:: {wl('Connectors')}")        # link so a connector is never an orphan
        if c.get("url"):
            b += ["", f"[Link]({c['url']})"]
        write(vault, f"Connectors/{name}.md", "\n".join(b)); n += 1

    for c in sorted(cats):
        write(vault, f"Categories/{title(c)}.md",
              f"---\ntags: [category]\n---\n# {title(c)}\n\nCategory hub — skills, tools and prompts in **{c}** link here. Part of [[Home]].\n")
    for th in sorted(toolhubs):
        write(vault, f"Tools-hubs/{title(th)}.md",
              f"---\ntags: [tool-hub]\n---\n# {title(th)}\n\nHub — skills that target **{th}** link here. Part of [[Home]].\n")
    # Connectors hub (so the 42 connectors are linked, not orphans) — also ties to Home.
    write(vault, "Categories/Connectors.md",
          "---\ntags: [hub]\n---\n# Connectors\n\nHub — every MCP server / connector links here. Part of [[Home]].\n")

    # structural notes (how the project is built)
    if BRAIN.exists():
        for f in BRAIN.glob("*.md"):
            write(vault, f"Project/{f.name}", f.read_text(encoding="utf-8", errors="replace"))

    home = ["---", "tags: [home]", "---", "# Excavatortron Brain", "",
            f"The whole project as a knowledge graph: **{len(skills)} skills · {len(tools)} tools · "
            f"{len(prompts)} prompts · {len(conns)} connectors**.", "",
            "Open the **graph view** (the circle-of-dots icon, top-right) to explore — everything "
            "clusters around its category and tool.", "",
            "## Browse", "- `Skills/`, `Tools/`, `Prompts/`, `Connectors/` — the knowledge base",
            "- `Categories/`, `Tools-hubs/` — the hubs the graph clusters around",
            "- `Project/` — how Excavatortron itself is built (start at [[Excavatortron Brain]])", "",
            "## Hubs", "- [[Connectors]]", *[f"- {wl(th)}" for th in sorted(toolhubs)], "",
            "## Categories", *[f"- {wl(c)}" for c in sorted(cats)]]
    write(vault, "Home.md", "\n".join(home))
    print(f"Brain built at: {vault}")
    print(f"  {n} item notes + {len(cats)} category hubs + {len(toolhubs)} tool hubs + project notes + Home.")


if __name__ == "__main__":
    main()
