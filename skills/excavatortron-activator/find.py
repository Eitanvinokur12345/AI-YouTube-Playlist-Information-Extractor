"""
find.py — search the Excavatortron hub for the best skill/tool/connector/prompt/command for a task.

Works two ways automatically:
  - inside the Excavatortron repo: reads the local data/*.json
  - anywhere else: fetches the public hub API (CORS-open, no key)

Usage:  python find.py "build me a memory + MCP retrieval setup for claude code"
Output: JSON {skills,tools,connectors,prompts,commands: [ {name,slug,score,quality,target_tool,url,desc} ]}
"""
from __future__ import annotations

import json
import re
import sys
import urllib.request
from pathlib import Path

BASE = "https://eitanvinokur12345.github.io/AI-YouTube-Playlist-Information-Extractor/data/"
STOP = {"the", "and", "for", "with", "you", "your", "are", "can", "how", "what", "best", "use",
        "using", "want", "need", "make", "set", "give", "into", "this", "that", "from", "get"}


def _repo_data() -> Path | None:
    p = Path(__file__).resolve().parent
    for _ in range(6):
        if (p / "data" / "skills.json").exists():
            return p / "data"
        p = p.parent
    return None


def _load(name: str):
    d = _repo_data()
    if d and (d / name).exists():
        try:
            return json.load(open(d / name, encoding="utf-8"))
        except Exception:
            return {}
    try:
        req = urllib.request.Request(BASE + name, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read().decode("utf-8", "replace"))
    except Exception:
        return {}


def _items(name, key):
    d = _load(name)
    return d.get(key, []) if isinstance(d, dict) else (d if isinstance(d, list) else [])


def _slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (name or "").lower()).strip("-")


def _score(blob: str, terms: list[str]) -> int:
    t = blob.lower()
    return sum(3 if t.count(w) and len(w) > 5 else t.count(w) for w in terms)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")   # Windows console is cp1252 by default
    except Exception:
        pass
    query = " ".join(sys.argv[1:]).strip()
    if not query:
        print('usage: python find.py "<task description>"')
        return 2
    terms = [w for w in re.findall(r"[a-z0-9][a-z0-9\-]+", query.lower()) if len(w) > 2 and w not in STOP]
    out = {}
    specs = [
        ("skills.json", "skills", "skill_name", ["use_case", "category", "target_tool"], "description"),
        ("tools.json", "tools", "name", ["category", "company"], "description"),
        ("connectors.json", "connectors", "name", ["works_in", "category"], "what_it_does"),
        ("prompts.json", "prompts", "title", ["category"], "purpose"),
        ("commands.json", "commands", "command", ["description"], "description"),
    ]
    for name, key, nk, extra, descf in specs:
        scored = []
        for x in _items(name, key):
            if not isinstance(x, dict):
                continue
            blob = " ".join([str(x.get(nk, "")), str(x.get(descf, ""))] + [str(x.get(e, "")) for e in extra])
            s = _score(blob, terms)
            if s:
                scored.append((s, x))
        scored.sort(key=lambda z: (z[0], z[1].get("quality_score", 0) or 0), reverse=True)
        out[key] = [{
            "name": x.get(nk), "slug": x.get("slug") or _slug(str(x.get(nk, ""))), "score": s,
            "quality": x.get("quality_score"), "target_tool": x.get("target_tool", ""),
            "url": x.get("url") or x.get("source_url", ""),
            "desc": (str(x.get(descf, "")) or "")[:160],
        } for s, x in scored[:4]]
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
