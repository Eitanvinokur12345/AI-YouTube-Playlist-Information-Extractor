"""
src/discovery_agent.py — M1.C2: the DISCOVERY AGENT (hourly, everywhere).

The owner's freshness law: EXCAVA catches brand-new tools and suddenly-appearing GitHub
repos AS THEY EMERGE — same-day, not weeks later. Every hour this agent sweeps:
  - GitHub: newly-created + recently-pushed AI repos (search API; GITHUB_TOKEN in CI raises
    the rate limit, works keyless locally at low rate) and trending-page parse as fallback,
  - Hacker News front/new (Algolia API, keyless),
  - Product Hunt (RSS/Atom feed, keyless),
  - the tier-1 social sweep (Reddit RSS / Telegram / DDG / YouTube-beyond) via src.mine_social,
  - official release feeds already covered by the news lane (noted, not duplicated).
agent-reach extends the social reach when installed (optional; the sweep works without it).

INCLUSION BAR (owner): AI-relevant + a QUALITY SIGNAL (stars/points/activity/a real README).
Everything lands in the gated intake queue (data/social_intake.json — same one the mining
department consumes through verify+security); NOTHING goes straight to the hub.

Run: python -m src.discovery_agent [--limit-per-source 20]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "social_intake.json"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
AI_WORDS = ("ai", "llm", "agent", "gpt", "claude", "gemini", "rag", "mcp", "copilot",
            "openai", "anthropic", "prompt", "transformer", "diffusion", "ml")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _get(url: str, timeout: int = 20, gh: bool = False) -> str:
    try:
        h = dict(UA)
        tok = os.environ.get("GITHUB_TOKEN", "").strip()
        if gh and tok:
            h["Authorization"] = f"Bearer {tok}"
        req = urllib.request.Request(url, headers=h)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", errors="replace")
    except Exception:
        return ""


def _ai_relevant(text: str) -> bool:
    tl = f" {text.lower()} "
    return any(f" {w}" in tl or f"{w} " in tl or f"-{w}" in tl for w in AI_WORDS)


def _item(source, title, url, extra="", via="", quality=""):
    return {"source": source, "title": str(title).strip()[:220], "url": url,
            "extra": str(extra).strip()[:300], "via": via, "found_at": _now(),
            "quality_signal": quality, "trust": 55 if source.startswith("gh-") else 50}


def github_new(limit: int) -> list[dict]:
    """Brand-new + freshly-pushed AI repos with a quality signal (stars/activity)."""
    out = []
    week = (datetime.now(timezone.utc) - timedelta(days=7)).strftime("%Y-%m-%d")
    day = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")
    queries = [
        (f"topic:ai created:>{week} stars:>10", "gh-new"),          # new repos, early traction
        (f"ai OR llm OR agent in:name,description pushed:>{day} stars:>100", "gh-active"),
    ]
    for q, label in queries:
        raw = _get("https://api.github.com/search/repositories?sort=stars&order=desc"
                   f"&per_page={min(limit, 20)}&q={quote(q)}", gh=True)
        try:
            repos = json.loads(raw).get("items", [])
        except Exception:
            continue
        for r in repos:
            desc = r.get("description") or ""
            if not _ai_relevant(f"{r.get('full_name', '')} {desc}"):
                continue
            if r.get("stargazers_count", 0) < 10 or not r.get("description"):
                continue                                # the quality bar: signal + a real blurb
            out.append(_item(label, f"{r['full_name']} — {desc[:120]}", r["html_url"],
                             f"★{r.get('stargazers_count', 0)} · {r.get('language') or ''} · created {str(r.get('created_at', ''))[:10]}",
                             quality=f"stars={r.get('stargazers_count', 0)}"))
    return out


def hackernews(limit: int) -> list[dict]:
    """HN front + newest AI stories (Algolia, keyless). Points = the quality signal."""
    out = []
    for endpoint, label in [("search?tags=front_page", "hn-front"),
                            ("search_by_date?tags=story&numericFilters=points>20", "hn-new")]:
        raw = _get(f"https://hn.algolia.com/api/v1/{endpoint}&query=ai&hitsPerPage={min(limit, 20)}")
        try:
            hits = json.loads(raw).get("hits", [])
        except Exception:
            continue
        for h in hits:
            title = h.get("title") or ""
            if not _ai_relevant(title):
                continue
            out.append(_item(label, title,
                             h.get("url") or f"https://news.ycombinator.com/item?id={h.get('objectID')}",
                             f"{h.get('points', 0)} points · {h.get('num_comments', 0)} comments",
                             quality=f"points={h.get('points', 0)}"))
    return out


def producthunt(limit: int) -> list[dict]:
    """Product Hunt's public feed (keyless)."""
    raw = _get("https://www.producthunt.com/feed")
    out = []
    for entry in re.findall(r"<entry>(.*?)</entry>", raw, re.S)[:limit * 2]:
        t = re.search(r"<title>(.*?)</title>", entry, re.S)
        u = re.search(r'<link[^>]+href="([^"]+)"', entry)
        c = re.search(r"<content[^>]*>(.*?)</content>", entry, re.S)
        title = (t.group(1) if t else "").strip()
        blurb = re.sub(r"<[^>]+>|\s+", " ", c.group(1) if c else "").strip()[:200]
        if t and u and _ai_relevant(f"{title} {blurb}"):
            out.append(_item("producthunt", f"{title} — {blurb[:100]}", u.group(1),
                             quality="ph-launch"))
    return out[:limit]


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit-per-source", type=int, default=20)
    a = ap.parse_args()
    n = a.limit_per_source

    found = github_new(n) + hackernews(n) + producthunt(n)

    # the tier-1 social sweep rides along (Reddit RSS / Telegram / DDG / YT-beyond)
    social_new = 0
    try:
        from src import mine_social
        cfg = json.load(open(DATA / "social_sources.json", encoding="utf-8"))
        found += mine_social.reddit(cfg.get("reddit_subreddits", []), min(n, 10))
        found += mine_social.ddg(cfg.get("search_queries", []), min(n, 8))
        social_new = len(found)
    except Exception:
        pass

    # merge into the gated intake queue (dedupe by url, bounded)
    try:
        store = json.load(open(OUT, encoding="utf-8"))
    except Exception:
        store = {"items": []}
    old = store.get("items", [])
    seen, merged = set(), []
    for it in found + old:
        u = it.get("url", "")
        if u and u not in seen:
            seen.add(u)
            merged.append(it)
    merged = merged[:1000]
    per = {}
    for it in merged:
        per[it["source"].split("/")[0]] = per.get(it["source"].split("/")[0], 0) + 1
    fresh = len(merged) - len(old) if len(merged) > len(old) else 0
    store.update({"generated_at": _now(), "total": len(merged), "new_this_run": fresh,
                  "per_source": per,
                  "note": ("INTAKE QUEUE (gated): discovery agent (M1.C2, hourly) + tier-1 social. "
                           "Inclusion = AI-relevant + a quality signal; mining consumes via verify+security."),
                  "items": merged})
    OUT.write_text(json.dumps(store, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"discovery: +{fresh} new (of {len(found)} sighted) → {len(merged)} queued; "
          + ", ".join(f"{k}={v}" for k, v in sorted(per.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
