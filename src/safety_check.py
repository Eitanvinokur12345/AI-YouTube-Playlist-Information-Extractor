"""
src/safety_check.py — mechanical SAFETY rating for connectors (and a light pass on skills).

MCP connectors actually RUN in your environment, so "which one is safe" matters. This scores every
connector safe / caution / risky from deterministic heuristics (no Claude), with reasons, into
data/safety.json. The activator's gate (owner's Q20) uses it: safe -> auto-activate, caution ->
warn, risky -> block until you confirm. Stdlib only; refreshes every analysis cycle.

Usage:  python -m src.safety_check
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"

# Phrases that mean broad / dangerous capability in the user's machine.
BROAD = re.compile(r"\b(shell|terminal|execute|exec\b|arbitrary code|run code|run commands?|"
                   r"file ?system|filesystem|delete files?|rm -rf|sudo|root access|full access|"
                   r"system access|control your computer|desktop control|browser control)\b", re.I)
SECRETS = re.compile(r"\b(api[- ]?key|access[- ]?token|secret|oauth|credentials?|password|private key)\b", re.I)
TRUSTED = ("anthropic", "openai", "google", "github", "microsoft", "notion", "linear", "stripe",
           "cloudflare", "supabase", "perplexity", "brave", "slack", "atlassian", "hugging face")


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")


def _load(name, default):
    try:
        return json.load(open(DATA / name, encoding="utf-8"))
    except Exception:
        return default


def rate_connector(c: dict) -> tuple[str, list[str]]:
    text = " ".join(str(c.get(k, "")) for k in ("name", "what_it_does", "install_or_source", "category"))
    name = (c.get("name") or "").lower()
    url = c.get("url") or c.get("source_url") or ""
    official = c.get("official") is True or any(t in name for t in TRUSTED)
    open_src = "github.com" in str(url).lower()
    has_source = bool(url) or official
    reasons = []

    risky = False
    if BROAD.search(text):
        reasons.append("requests broad system/shell/file access"); risky = True
    if not has_source:
        reasons.append("unknown/unverified source (no repo or official vendor)"); risky = True

    caution = False
    if SECRETS.search(text):
        reasons.append("needs an API key / secret"); caution = True
    if not official:
        reasons.append("third-party (not an official vendor connector)"); caution = True

    if risky:
        rating = "risky"
    elif official and has_source and not caution:
        rating = "safe"; reasons = ["official vendor"] + (["open source"] if open_src else [])
    elif caution:
        rating = "caution"
    else:
        rating = "caution"; reasons = reasons or ["MCP server runs in your environment — review before use"]
    if open_src and rating != "risky" and "open source" not in reasons:
        reasons.append("open source")
    return rating, reasons[:4]


def main() -> int:
    conns = _load("connectors.json", {}).get("connectors", [])
    out_conn, summary = {}, {"safe": 0, "caution": 0, "risky": 0}
    for c in conns:
        rating, reasons = rate_connector(c)
        key = c.get("slug") or _slug(c.get("name", ""))
        if not key:
            continue
        out_conn[key] = {"name": c.get("name"), "rating": rating, "reasons": reasons}
        summary[rating] = summary.get(rating, 0) + 1

    # light pass on skills: flag ones whose text tells you to run risky operations
    skills = _load("skills.json", {}).get("skills", [])
    out_skill = {}
    for s in skills:
        blob = " ".join(str(s.get(k, "")) for k in ("description", "use_case", "output", "tips"))
        if BROAD.search(blob):
            out_skill[s.get("slug") or _slug(s.get("skill_name", ""))] = {
                "name": s.get("skill_name"), "rating": "caution",
                "reasons": ["the technique runs system/shell/file operations — review what it executes"]}

    out = {"generated_at": datetime.now(timezone.utc).isoformat(),
           "policy": "activator gate: safe = auto-activate, caution = warn, risky = block until confirmed",
           "summary": summary, "connectors": out_conn, "skills_flagged": out_skill}
    json.dump(out, open(DATA / "safety.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"safety: {summary['safe']} safe, {summary['caution']} caution, {summary['risky']} risky "
          f"(of {len(conns)} connectors); {len(out_skill)} skills flagged.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
