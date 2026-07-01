"""
src/mine_competitors.py — ingest WHOLE CATALOGS from competitor / curated AI directories into the hub.

The big AI-tool and MCP directories are the competitors; their public "awesome" catalogs (curated
markdown on GitHub) are structured lists of tools and MCP servers. This pulls those lists, parses each
entry (name + link + description), classifies tool vs MCP connector, and merges into the hub — deduped
against what's already there. A huge, FREE source (raw GitHub markdown, no scraping). Stdlib only.

Run:  python -m src.mine_competitors
"""
from __future__ import annotations

import re
import urllib.request
from pathlib import Path

from src.bulk_analyze import load, save
from src.mine_feeds import merge

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36")

# (raw markdown URL, kind, source tag) — competitor-curated catalogs of MCP servers + AI tools/agents
LISTS = [
    ("https://raw.githubusercontent.com/modelcontextprotocol/servers/main/README.md", "connectors", "mcp-official"),
    ("https://raw.githubusercontent.com/punkpeye/awesome-mcp-servers/main/README.md", "connectors", "awesome-mcp"),
    ("https://raw.githubusercontent.com/wong2/awesome-mcp-servers/main/README.md", "connectors", "awesome-mcp-wong2"),
    ("https://raw.githubusercontent.com/appcypher/awesome-mcp-servers/main/README.md", "connectors", "awesome-mcp-appcypher"),
    ("https://raw.githubusercontent.com/e2b-dev/awesome-ai-agents/main/README.md", "tools", "awesome-ai-agents"),
    ("https://raw.githubusercontent.com/mahseema/awesome-ai-tools/main/README.md", "tools", "awesome-ai-tools"),
    ("https://raw.githubusercontent.com/steven2358/awesome-generative-ai/master/README.md", "tools", "awesome-genai"),
]
LINK = re.compile(r"[-*]\s*\[([^\]]{2,80})\]\((https?://[^)\s]+)\)\s*[-—:|]*\s*(.*)")
SKIP = {"home", "docs", "doc", "github", "link", "website", "demo", "video", "readme", "license",
        "contributing", "back to top", "table of contents", "twitter", "discord"}


def fetch(u: str) -> str:
    try:
        req = urllib.request.Request(u, headers={"User-Agent": UA})
        return urllib.request.urlopen(req, timeout=25).read().decode("utf-8", "replace")
    except Exception:
        return ""


def main() -> int:
    conns = load(DATA / "connectors.json", {"connectors": []})
    tools = load(DATA / "tools.json", {"tools": []})
    nc = nt = 0
    for url, kind, tag in LISTS:
        md = fetch(url)
        if not md:
            print(f"  {tag}: fetch failed / empty — skipped.")
            continue
        items, seen = [], set()
        for m in LINK.finditer(md):
            name = m.group(1).strip()
            link = m.group(2).strip()
            desc = (m.group(3) or "").strip()[:200]
            low = name.lower()
            if low in SKIP or low in seen or not link.startswith("http"):
                continue
            if "shields.io" in link or "/badge" in link or link.endswith((".png", ".svg", ".gif")):
                continue
            seen.add(low)
            if len(items) >= 400:
                break
            gh = link if "github.com" in link else ""
            if kind == "connectors":
                items.append({"name": name, "what_it_does": desc or name, "url": link, "works_in": "both",
                              "free": True, "github": gh, "quality_score": 3})
            else:
                items.append({"name": name, "description": desc or name, "quality_score": 3,
                              "homepage": (link if not gh else ""), "github": gh})
        if kind == "connectors":
            nc += merge(conns, "connectors", "name", items, url, "competitor:" + tag)
        else:
            nt += merge(tools, "tools", "name", items, url, "competitor:" + tag)
        print(f"  {tag}: parsed {len(items)} entries.")
    if nc:
        save(DATA / "connectors.json", conns)
    if nt:
        save(DATA / "tools.json", tools)
    print(f"mine_competitors: +{nc} connectors, +{nt} tools from competitor catalogs (deduped into the hub).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
