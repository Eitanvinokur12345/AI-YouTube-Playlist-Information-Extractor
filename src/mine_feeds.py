"""
src/mine_feeds.py — MINING SYSTEM (separate from self-improvement).

A standalone acquisition lane that turns the EXTERNAL feeds (the 80+ web/research/community RSS
sources collected by news.py) into catalogued **skills / tools / MCP connectors** — so the other
tabs keep growing from non-playlist information, on their OWN schedule (mine.yml), independent of
the weekly self-improve deep pass.

It reuses the FREE engine pool (the same one bulk_analyze uses → ZERO Claude-Pro tokens), reads
unseen news entries, asks an engine to extract any concrete AI tool/technique/MCP server named, and
merges them in (deduped, attributed to the article). State in data/mined_state.json so nothing is
re-mined.

Usage:  python -m src.mine_feeds --limit 60
"""
from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path

from src.bulk_analyze import (CATEGORIES, NOW, extract, load, norm, save, slugify)

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
CONFIG = ROOT / "config.json"
STATE = DATA / "mined_state.json"
FEEDS = ["weekly_web_news.json", "daily_web_news.json", "monthly_web_news.json"]


def build_pool(cfg: dict) -> list[dict]:
    bc = cfg.get("bulk_analyze", {}) or {}
    pool = []
    for e in (bc.get("engines") or []):
        k = os.environ.get(e.get("secret_name", ""), "").strip()
        if k:
            pool.append({"name": e.get("name") or e.get("model", "engine"),
                         "provider": e.get("provider", "gemini"), "base_url": e.get("base_url", ""),
                         "model": e.get("model", ""), "key": k})
    if not pool:
        k = os.environ.get(bc.get("secret_name", "EXTERNAL_REVIEW_API_KEY"), "").strip()
        if k:
            pool.append({"name": bc.get("model", "gemini-2.5-flash"), "provider": bc.get("provider", "gemini"),
                         "base_url": bc.get("base_url", ""), "model": bc.get("model", "gemini-2.5-flash"), "key": k})
    return pool


def news_prompt(entry: dict) -> str:
    return (
        "From this AI news headline + summary, extract any CONCRETE AI tool/product/model, reusable "
        "technique (skill), or MCP connector that is actually named. Return STRICT JSON ONLY:\n"
        '{"relevant":true,'
        '"skills":[{"skill_name":"","slug":"","category":"","description":"","use_case":"","quality_score":1,"target_tool":"claude","tips":[]}],'
        '"tools":[{"name":"","slug":"","category":"","company":"","open_source":false,"description":"","quality_score":1,"model_version":"","release_status":"released","is_mcp":false}],'
        '"connectors":[{"name":"","what_it_does":"","works_in":"both","free":true,"url":""}]}\n'
        f"- category MUST be one of: {', '.join(CATEGORIES)}.\n"
        "- TOOLS = products/models that EXIST; SKILLS = specific techniques. A product is a TOOL, not a skill.\n"
        "- Only extract what is explicitly named; if it's generic news with no named AI tool/technique, "
        'return {"relevant":false}. Empty arrays are fine. Never invent.\n\n'
        f"SOURCE: {entry.get('source_name','')}\nTITLE: {entry.get('title','')}\n"
        f"SUMMARY: {entry.get('summary','')}\nURL: {entry.get('url','')}\n"
    )


def merge(store: dict, key: str, namefield: str, items: list, url: str, src: str) -> int:
    arr = store.setdefault(key, [])
    by = {norm(x.get(namefield, "")): x for x in arr}
    by_slug = {x.get("slug") for x in arr}
    boiler = {"claude", "chatgpt", "gemini", "openai", "anthropic", "make", "mcp", "ai", "gpt"}
    added = 0
    for it in items or []:
        name = (it.get(namefield) or "").strip()
        if not name or norm(name) in boiler:
            continue
        k = norm(name)
        if k in by:
            seen = by[k].setdefault("also_seen_in", [])
            if url and url not in seen:
                seen.append(url)
            continue
        slug = slugify(it.get("slug") or name)
        i = 2
        while slug in by_slug:
            slug = f"{slugify(name)}-{i}"; i += 1
        by_slug.add(slug)
        rec = {**it, "slug": slug, "source_type": "web_news", "source_url": url,
               "discovered_via": f"mine_feeds ({src})", "added_at": NOW}
        if key in ("skills", "tools") and rec.get("category") not in CATEGORIES:
            rec["category"] = "other"
        arr.append(rec); by[k] = rec; added += 1
    return added


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=60, help="max news entries to mine this run")
    ap.add_argument("--sleep", type=float, default=3.0)
    args = ap.parse_args()

    cfg = load(CONFIG, {})
    pool = build_pool(cfg)
    if not pool:
        print("No engine keys present — mining skipped (graceful)."); return 0
    print("mining engine pool:", ", ".join(e["name"] for e in pool))

    seen = set((load(STATE, {}) or {}).get("urls", []))
    entries, by_url = [], set()
    for f in FEEDS:
        for e in (load(DATA / f, {}) or {}).get("entries", []):
            u = e.get("url")
            if u and u not in seen and u not in by_url:
                by_url.add(u); entries.append(e)
    entries.sort(key=lambda e: e.get("publishedAt", ""), reverse=True)
    entries = entries[: max(args.limit, 0)]
    print(f"mining {len(entries)} unseen news entries ({len(seen)} already mined)")

    skills = load(DATA / "skills.json", {"skills": []})
    tools = load(DATA / "tools.json", {"tools": []})
    conns = load(DATA / "connectors.json", {"connectors": []})
    ns = nt = nc = done = 0
    timeout = int(cfg.get("news", {}).get("request_timeout_seconds", 30))
    errs = {e["name"]: 0 for e in pool}
    idx = 0
    for e in entries:
        active = [x for x in pool if errs[x["name"]] < 3]
        if not active:
            print("  all engines rate-limited — stopping; rest stay for next run."); break
        eng = active[idx % len(active)]; idx += 1
        time.sleep(args.sleep)
        try:
            r = extract(eng["provider"], eng["base_url"], eng["key"], eng["model"], news_prompt(e), timeout)
        except Exception:  # noqa: BLE001
            errs[eng["name"]] += 1
            continue
        seen.add(e.get("url"))
        done += 1
        if not isinstance(r, dict) or not r.get("relevant", True):
            continue
        ns += merge(skills, "skills", "skill_name", r.get("skills"), e.get("url", ""), e.get("source_name", ""))
        nt += merge(tools, "tools", "name", r.get("tools"), e.get("url", ""), e.get("source_name", ""))
        nc += merge(conns, "connectors", "name", r.get("connectors"), e.get("url", ""), e.get("source_name", ""))

    if ns:
        save(DATA / "skills.json", skills)
    if nt:
        save(DATA / "tools.json", tools)
    if nc:
        save(DATA / "connectors.json", conns)
    save(STATE, {"updated_at": NOW, "urls": sorted(seen)})
    print(f"mined {done} entries -> +{ns} skills, +{nt} tools, +{nc} connectors. NO Claude-Pro tokens used.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
