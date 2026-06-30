"""
src/activate.py — the ACTIVATION engine (F2): turn "set me up with X" into an exact in-project PLAN.

The activator skill / EXCAVA call this to (1) find the best hub item for a request and (2) emit the
precise steps to set it up WITHIN your tools — install the Claude skill, add the MCP connector, or
clone+run the repo — using the machine-readable `setup` recipe already on each item. A link is shown
only for the unavoidable external step (a hosted product's sign-in / an API key).

Reads local data/*.json when present, else fetches the public hub, so it works even outside the repo.
Free, stdlib. Run:  python -m src.activate "n8n"   (add --json for machine output, --top N for choices)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
REMOTE = "https://eitanvinokur12345.github.io/AI-YouTube-Playlist-Information-Extractor/data"
SETS = [("tools.json", "tools", "name", "tool"), ("skills.json", "skills", "skill_name", "skill"),
        ("connectors.json", "connectors", "name", "connector")]


def _load(fname: str) -> dict:
    p = DATA / fname
    if p.exists():
        try:
            return json.load(open(p, encoding="utf-8"))
        except Exception:
            return {}
    try:
        with urllib.request.urlopen(f"{REMOTE}/{fname}", timeout=15) as r:
            return json.loads(r.read().decode("utf-8", "replace"))
    except Exception:
        return {}


def _norm(s) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(s or "").lower()).strip()


def find(query: str, limit: int = 5) -> list:
    q = _norm(query)
    qs = set(q.split())
    hits = []
    for fname, key, nk, typ in SETS:
        for it in _load(fname).get(key, []):
            name = it.get(nk) or it.get("slug") or ""
            n = _norm(name)
            if not n:
                continue
            words = set(n.split())
            if n == q:
                score = 100
            elif q and q in n:
                score = 70
            elif qs and qs <= words:
                score = 60
            elif qs & words:
                score = 30 + 8 * len(qs & words)
            else:
                continue
            # prefer directly-installable kinds (MCP connector / Claude skill) over a raw repo on ties
            tw = {"connector": 4, "skill": 3, "tool": 0}.get(typ, 0)
            hits.append((score + tw + (it.get("quality_score", 0) or 0) / 100.0, typ, it, name))
    hits.sort(key=lambda x: x[0], reverse=True)
    return hits[:limit]


def plan(it: dict, typ: str) -> dict:
    su = it.get("setup") or {}
    name = it.get("name") or it.get("skill_name") or it.get("slug") or "?"
    home = it.get("homepage") or (it.get("url") if not str(it.get("url", "")).find("youtube") >= 0 else "") or ""
    gh = it.get("github") or ""
    kind = su.get("kind") or typ
    cmd = su.get("command")
    needs_key = bool(su.get("needs_key"))
    slug = it.get("slug") or _norm(name).replace(" ", "-")
    if "skill" in kind:
        steps = [f'Create ~/.claude/skills/{slug}/SKILL.md with the "{name}" skill'
                 + (f" (source: {gh or home})" if (gh or home) else " (from the hub)") + ".",
                 "Reload Claude Code so the skill registers.",
                 f"Use it: invoke the {slug} skill."]
    elif "mcp" in kind or typ == "connector":
        steps = [cmd or f"claude mcp add {slug} -- npx -y <package>",
                 "Reload Claude so the MCP connects.",
                 "Confirm: claude mcp list"]
    elif gh:
        repo = gh.rstrip("/").split("/")[-1]
        steps = [f"git clone {gh}", f"cd {repo}", "Install deps + run per its README (npm install / pip install)."]
    elif home:
        steps = [f"Open {home} — hosted product; sign in and use it."]
        needs_key = True
    else:
        steps = [cmd or f'No setup recipe yet for "{name}" — open its source from the hub.']
    return {"name": name, "type": typ, "kind": kind, "needs_key": needs_key,
            "steps": steps, "homepage": home, "github": gh}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--top", type=int, default=1)
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    hits = find(args.query, max(args.top, 4))
    if not hits:
        print(f'activate: no hub match for "{args.query}". Try a different name.'); return 1
    plans = [plan(it, typ) for _, typ, it, _ in hits[: args.top]]
    if args.json:
        print(json.dumps(plans, ensure_ascii=False, indent=2)); return 0
    for p in plans:
        print(f'\n>> ACTIVATE: {p["name"]}  ({p["type"]} | {p["kind"]}{" | needs key" if p["needs_key"] else ""})')
        for i, s in enumerate(p["steps"], 1):
            print(f"  {i}. {s}")
        links = " ".join(x for x in [p["homepage"], p["github"]] if x)
        if links:
            print("  links:", links)
    if len(hits) > args.top:
        print("\nother matches:", ", ".join(f"{n} ({t})" for _, t, _, n in hits[args.top:]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
