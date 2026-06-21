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


def _norm(n: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (n or "").lower())


def build_recipe(out: dict) -> dict:
    """Assemble the per-type hits into ONE coherent combination for the task.

    This is the heart of the activator: not "here are 4 lists" but "for THIS task, use
    skill X + MCP connector Y + tool Z together — and here's the exact activation plan."
    """
    seen: set[str] = set()
    comps: list[dict] = []
    plan: list[dict] = []

    def take(kind: str, item: dict, role: str, why: str, cmd: str | None, floor: int = 0):
        n = _norm(item.get("name", ""))
        if not item.get("name") or n in seen:
            return False
        if (item.get("score") or 0) < floor:      # too weakly related to belong in the combination
            return False
        seen.add(n)
        comps.append({"role": role, "type": kind, "name": item["name"], "slug": item.get("slug"),
                      "quality": item.get("quality"), "url": item.get("url", ""), "why": why,
                      "desc": item.get("desc", "")})
        if cmd:
            plan.append({"step": len(plan) + 1, "cmd": cmd, "for": item["name"]})
        return True

    # 1) PRIMARY capability — prefer a skill (a technique you DO); fall back to the top tool.
    primary_kind = None
    if out.get("skills"):
        s = out["skills"][0]
        if take("skill", s, "primary", "the core technique for the task", f'python activate.py skill {s.get("slug")}'):
            primary_kind = "skill"
    if primary_kind is None and out.get("tools"):
        t = out["tools"][0]
        take("tool", t, "primary", "the main product to do the task",
             f'python activate.py deploy tool {t.get("slug")} --tool "claude"')

    # 2) MCP CONNECTOR — the live data/capability the task needs wired in (must be on-topic).
    for c in out.get("connectors", []):
        if take("connector", c, "connector", "wires the needed data/capability into the tool via MCP",
                f'python activate.py connector {c.get("slug")}', floor=2):
            break

    # 3) SUPPORTING TOOL(S) — up to two on-topic ones, skipping anything already taken.
    sup = 0
    for t in out.get("tools", []):
        if sup >= 2:
            break
        if take("tool", t, "supporting", "complements the primary capability",
                f'python activate.py deploy tool {t.get("slug")} --tool "claude"', floor=2):
            sup += 1

    # 3b) MODEL — the best-fit model to run it on (recommended, not "installed").
    for m in out.get("models", []):
        if take("model", m, "model", "the recommended model to run this on", None, floor=2):
            break

    # 4) COMMAND + PROMPT — only if they're clearly on-topic for this task.
    for cmd_item in out.get("commands", []):
        if take("command", cmd_item, "command", "a ready slash-command for the workflow", None, floor=2):
            break
    for p in out.get("prompts", []):
        if take("prompt", p, "prompt", "a vetted prompt to drive it",
                f'python activate.py deploy prompt {p.get("slug")} --tool "claude"', floor=2):
            break

    names = [f'{c["name"]} ({c["role"]})' for c in comps]
    why = ("For this task, combine: " + " + ".join(names) + "." if names
           else "No strong match — broaden the task description.")
    return {"why": why, "components": comps, "activation_plan": plan,
            "activate_all": "python activate.py combo " + " ".join(
                f'{c["type"]}:{c["slug"]}' for c in comps if c.get("slug")) + ' --tool "claude"'}


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
    out, rel = {}, {}
    # Search EVERY tab of the hub, not a fixed subset — skills, tools, models, connectors,
    # prompts, commands — so the activator can answer with anything the project knows.
    specs = [
        ("skills.json", "skills", "skill_name", ["use_case", "category", "target_tool"], "description"),
        ("tools.json", "tools", "name", ["category", "company"], "description"),
        ("models.json", "models", "name", ["model_version", "category", "company"], "description"),
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
        # Rank = QUALITY-dominant, then installable (has a SKILL.md slug), then keyword fit.
        def _rank(z):
            s, x = z
            q = x.get("quality_score", 0) or 0
            installable = 2 if (key == "skills" and (x.get("slug") or x.get("skill_name"))) else 0
            return q * 2 + installable + min(s, 6)
        def _fmt(pairs):
            return [{
                "name": x.get(nk), "slug": x.get("slug") or _slug(str(x.get(nk, ""))), "score": s,
                "quality": x.get("quality_score"), "target_tool": x.get("target_tool", ""),
                "url": x.get("url") or x.get("source_url", ""),
                "desc": (str(x.get(descf, "")) or "")[:160],
            } for s, x in pairs]
        # Browse lists: QUALITY-dominant (good for exploring the catalogue).
        scored.sort(key=_rank, reverse=True)
        out[key] = _fmt(scored[:4])
        # Recipe source: RELEVANCE-first (score), quality only as a tiebreaker — so a combination
        # never pulls in a high-quality-but-off-topic item (e.g. Canva for a memory setup).
        rel[key] = _fmt(sorted(scored, key=lambda z: (z[0], z[1].get("quality_score", 0) or 0),
                               reverse=True)[:6])
    out["recipe"] = build_recipe(rel)      # the assembled combination + one-shot activation plan
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
