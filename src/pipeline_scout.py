"""
src/pipeline_scout.py — 5 role-based scouts that find tools to improve OUR OWN pipeline.

The owner: have 5 agents with different company roles search the catalogue for tools/commands/
connectors/MCP servers that could help the PROCESS itself (he named Playwright MCP + Firecrawl).
Find them, propose, and only integrate after he approves. This searches the hub from 5 role lenses
and writes ranked PROPOSALS to data/pipeline_scout.json (shown in the Dev tab). It does NOT integrate
anything — it's a proposal list the owner approves. Free, mechanical.

Run:  python -m src.pipeline_scout
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "pipeline_scout.json"
NOW = datetime.now(timezone.utc).isoformat()

ROLES = [
    ("Researcher — web retrieval", ["firecrawl", "tavily", "serpapi", " exa ", "web search",
     "scrape", "crawl", "brave search", "perplexity api"],
     "find real tool/site links the LLM doesn't know (helps G3 link resolution)"),
    ("Automation Engineer — browser", ["playwright", "puppeteer", "browser use", "computer use",
     "selenium", "browser automation", "stagehand"],
     "fetch pages/transcripts blocked from datacenter IPs; verify links live"),
    ("Data Engineer — transcripts/extract", ["transcript", "whisper", "yt-dlp", "caption",
     "speech to text", "subtitle", "supadata", "deepgram", "assemblyai"],
     "recover the captions YouTube blocks (helps G1 coverage)"),
    ("Integrations Scout — MCP", ["mcp server", "model context protocol", " mcp ", "mcp registry"],
     "wire useful capabilities straight into Claude/the activator"),
    ("QA — validation", ["link checker", "validate", "url validator", "test runner", "schema validation"],
     "keep links + data correct (helps G3 truth)"),
]


def _items(name, key):
    try:
        d = json.load(open(DATA / name, encoding="utf-8"))
        return d.get(key, []) if isinstance(d, dict) else []
    except Exception:
        return []


def main() -> int:
    pool = [("tool", t) for t in _items("tools.json", "tools")] \
        + [("connector", c) for c in _items("connectors.json", "connectors")]

    out = []
    for role, kws, why in ROLES:
        finds = []
        for kind, x in pool:
            blob = f" {x.get('name','')} {x.get('description','') or x.get('what_it_does','')} ".lower()
            if any(k in blob for k in kws):
                finds.append({"name": x.get("name"), "kind": kind,
                              "quality": x.get("quality_score") or 0,
                              "link": x.get("homepage") or x.get("github") or x.get("url") or "",
                              "desc": (str(x.get("description") or x.get("what_it_does") or ""))[:120]})
        finds.sort(key=lambda f: f["quality"], reverse=True)
        # de-dup by name
        seen, uniq = set(), []
        for f in finds:
            n = (f["name"] or "").lower()
            if n and n not in seen:
                seen.add(n); uniq.append(f)
        out.append({"role": role, "why_this_role_helps": why,
                    "recommended": uniq[0]["name"] if uniq else None, "finds": uniq[:4]})

    total = sum(len(r["finds"]) for r in out)
    OUT.write_text(json.dumps({"generated_at": NOW, "status": "proposals — approve to integrate",
                               "roles": out}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"pipeline_scout: {total} process-helper candidates across {len(ROLES)} roles "
          f"(top picks: {', '.join(r['recommended'] for r in out if r['recommended'])[:120]}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
