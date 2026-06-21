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
GEN_FOLDERS = ["Skills", "Tools", "Prompts", "Connectors", "Categories", "Tools-hubs", "Vendors", "Project"]
HUB_CAP = 90          # a category bigger than this is split into alphabetical sub-hubs (no hairballs)
SUB_SIZE = 50         # target members per sub-hub


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


def uniq_title(name: str, used: set) -> str:
    """A note title that's UNIQUE across the vault — so distinct items never collide onto one
    note (which used to make the hub links all point at a single 'white' super-node)."""
    base = title(name)
    t, i = base, 2
    while t.lower() in used:
        t = f"{base} ({i})"; i += 1
    used.add(t.lower())
    return t


def sub_hubs(cat: str, members: list[str]) -> dict[str, list[str]]:
    """Split an oversized category's members into alphabetical sub-hubs so no single hub radiates
    hundreds of edges (the 'hairball'). Returns {sub_hub_title: [member_links]}; small categories
    return one hub keyed by the category title itself."""
    uniq = sorted(set(members), key=lambda m: m.lower())
    if len(uniq) <= HUB_CAP:
        return {title(cat): uniq}
    out: dict[str, list[str]] = {}
    for i in range(0, len(uniq), SUB_SIZE):
        chunk = uniq[i:i + SUB_SIZE]
        a = re.sub(r"[^A-Za-z0-9]", "", chunk[0].strip("[]"))[:1].upper() or "#"
        b = re.sub(r"[^A-Za-z0-9]", "", chunk[-1].strip("[]"))[:1].upper() or "#"
        out[title(f"{cat} · {a}–{b}")] = chunk
    return out


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
    # Member lists so the CENTRAL hubs link OUT to every specific item (more edges = specific
    # tools/skills are visible from the centre, not buried as single-edge peripheral dots).
    cat_members: dict[str, list[str]] = {}
    toolhub_members: dict[str, list[str]] = {}
    vendor_members: dict[str, list[str]] = {}
    used: set[str] = set()          # every note title, to guarantee uniqueness (no collisions)
    n = skipped = 0

    def member(d, key, link):
        d.setdefault(key, []).append(link)

    # MAINTENANCE FIX: an item with no real body became a blank 'white' graph node; skip those.
    def has_body(*vals) -> bool:
        return any(str(v or "").strip() for v in vals)

    # PASS 1 — write each item note with a UNIQUE title; collect category membership. Because
    # oversized categories are split into sub-hubs (pass 2), we first record each item's RAW
    # category, then rewrite the per-item Category:: link to its assigned (sub-)hub.
    cat_of: dict[str, str] = {}     # note-title -> raw category, so we can link to the right sub-hub
    pending_cat_link: dict[str, Path] = {}

    for s in skills:
        if not has_body(s.get("description"), s.get("use_case"), s.get("tips")):
            skipped += 1; continue
        name = uniq_title(s.get("skill_name") or s.get("slug") or "skill", used)
        cat = (s.get("category") or "other"); cats.add(cat)
        tt = title(s.get("target_tool") or "claude"); toolhubs.add(tt)
        b = ["---", "tags: [skill]", "---", f"# {name}", "", (s.get("description") or "").strip(), ""]
        if s.get("use_case"):
            b += [f"**Use case:** {s['use_case'].strip()}", ""]
        for t in (s.get("tips") or [])[:5]:
            b.append(f"- {str(t).strip()}")
        b += ["", f"Category:: __CATLINK__", f"Tool:: {wl(tt)}", ""]
        if s.get("source_url"):
            b.append(f"[Source]({s['source_url']})")
        write(vault, f"Skills/{name}.md", "\n".join(b)); n += 1
        cat_of[name] = cat; pending_cat_link[name] = vault / f"Skills/{name}.md"
        member(toolhub_members, tt, f"[[{name}]]")

    for t in tools:
        if not has_body(t.get("description")):
            skipped += 1; continue
        name = uniq_title(t.get("name") or t.get("slug") or "tool", used)
        cat = (t.get("category") or "other"); cats.add(cat)
        b = ["---", "tags: [tool]", "---", f"# {name}", "", (t.get("description") or "").strip(), "",
             "Category:: __CATLINK__"]
        vend = (t.get("company") or "").strip()
        if vend:
            vt = title("Vendor - " + vend)
            b.append(f"Vendor:: {wl(vt)}{' · ' + t['country'] if t.get('country') else ''}")
            member(vendor_members, vt, f"[[{name}]]")   # cluster tools by maker -> a 2nd edge per tool
        if t.get("model_version"):
            b.append(f"Version: {t.get('model_version')}")
        if t.get("release_status") == "upcoming":
            b.append("Status: 🔜 upcoming")
        if t.get("source_url"):
            b += ["", f"[Source]({t['source_url']})"]
        write(vault, f"Tools/{name}.md", "\n".join(b)); n += 1
        cat_of[name] = cat; pending_cat_link[name] = vault / f"Tools/{name}.md"

    for p in prompts:
        if not has_body(p.get("purpose"), p.get("prompt_text")):
            skipped += 1; continue
        name = uniq_title(p.get("title") or "prompt", used)
        cat = (p.get("category") or "other"); cats.add(cat)
        b = ["---", "tags: [prompt]", "---", f"# {name}", "", (p.get("purpose") or "").strip(), "",
             "```", (p.get("prompt_text") or "").strip(), "```", "", "Category:: __CATLINK__"]
        write(vault, f"Prompts/{name}.md", "\n".join(b)); n += 1
        cat_of[name] = cat; pending_cat_link[name] = vault / f"Prompts/{name}.md"

    for c in conns:
        if not has_body(c.get("what_it_does"), c.get("description")):
            skipped += 1; continue
        name = uniq_title(c.get("name") or "connector", used)
        b = ["---", "tags: [connector]", "---", f"# {name}", "",
             (c.get("what_it_does") or c.get("description") or "").strip(), ""]
        if c.get("works_in"):
            b.append(f"Works in: {c.get('works_in')}")
        b.append(f"Type:: {wl('Connectors')}")        # link so a connector is never an orphan
        if c.get("url"):
            b += ["", f"[Link]({c['url']})"]
        write(vault, f"Connectors/{name}.md", "\n".join(b)); n += 1

    # PASS 2 — assign each category's members to a (sub-)hub so no hub is a hairball, then patch
    # every item's Category:: link to point at its assigned (sub-)hub.
    by_cat: dict[str, list[str]] = {}
    for name, cat in cat_of.items():
        by_cat.setdefault(cat, []).append(f"[[{name}]]")
    item_hub: dict[str, str] = {}       # note-title -> the hub it should link to
    cat_to_hubs: dict[str, dict[str, list[str]]] = {}
    for cat, links in by_cat.items():
        hubs = sub_hubs(cat, links)
        cat_to_hubs[cat] = hubs
        for hub_title, links_in in hubs.items():
            for lk in links_in:
                item_hub[lk.strip("[]")] = hub_title
    for name, path in pending_cat_link.items():
        if path.exists():
            hub_title = item_hub.get(name, title(cat_of.get(name, "other")))
            txt = path.read_text(encoding="utf-8").replace("__CATLINK__", f"[[{hub_title}]]")
            path.write_text(txt, encoding="utf-8")

    # PASS 3 — write the hubs. Each hub lists its members (capped) and big categories get a parent
    # hub that links to its alphabetical sub-hubs.
    def hub(folder, key_title, tag, members, blurb):
        body = ["---", f"tags: [{tag}]", "---", f"# {key_title}", "", blurb, ""]
        u = sorted(set(members))
        if u:
            body += [f"## Members ({len(u)})", *[f"- {m}" for m in u[:SUB_SIZE]]]
            if len(u) > SUB_SIZE:
                body.append(f"- …and {len(u) - SUB_SIZE} more")
        write(vault, f"{folder}/{title(key_title)}.md", "\n".join(body) + "\n")

    for cat in sorted(cats):
        hubs = cat_to_hubs.get(cat, {title(cat): []})
        if len(hubs) == 1:
            (only,) = hubs.keys()
            hub("Categories", only, "category", hubs[only],
                f"Category hub — every skill, tool and prompt in **{cat}** links here. Part of [[Home]].")
        else:   # parent hub linking to its sub-hubs; each sub-hub holds ~{SUB_SIZE} members
            sub_links = [f"[[{h}]]" for h in sorted(hubs)]
            hub("Categories", title(cat), "category", sub_links,
                f"Category hub for **{cat}** ({sum(len(v) for v in hubs.values())} items), split into "
                f"alphabetical sub-hubs so the graph stays readable. Part of [[Home]].")
            for h, links_in in hubs.items():
                hub("Categories", h, "category", links_in,
                    f"Sub-hub of [[{title(cat)}]]. Part of [[Home]].")

    for th in sorted(toolhubs):
        hub("Tools-hubs", title(th), "tool-hub", toolhub_members.get(th, []),
            f"Hub — skills that target **{th}** link here. Part of [[Home]].")
    for v in sorted(vendor_members):
        hub("Vendors", v, "vendor", vendor_members.get(v, []),
            f"Vendor hub — tools made by **{v.replace('Vendor - ', '')}** link here. Part of [[Home]].")
    # Connectors hub (so the connectors are linked, not orphans) — also ties to Home.
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
            "- `Categories/`, `Tools-hubs/`, `Vendors/` — the hubs the graph clusters around "
            "(each hub now lists its members, so specific tools are reachable from the centre)",
            "- `Project/` — how Excavatortron itself is built (start at [[Excavatortron Brain]])", "",
            "## Hubs", "- [[Connectors]]", *[f"- {wl(th)}" for th in sorted(toolhubs)], "",
            "## Vendors", *[f"- {wl(v)}" for v in sorted(vendor_members)], "",
            "## Categories", *[f"- {wl(c)}" for c in sorted(cats)]]
    write(vault, "Home.md", "\n".join(home))
    print(f"Brain built at: {vault}")
    print(f"  {n} item notes (+{skipped} empty-body items skipped so they don't show as blank nodes) "
          f"+ {len(cats)} category hubs (oversized ones split into sub-hubs) + {len(toolhubs)} tool "
          f"hubs + project notes + Home.")


if __name__ == "__main__":
    main()
