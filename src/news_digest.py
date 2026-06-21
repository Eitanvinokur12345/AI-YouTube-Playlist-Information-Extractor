"""
src/news_digest.py — the system's OWN editorial summary of the AI news (not raw headlines).

news.py collects headlines from ~83 official feeds and uses each source's own blurb verbatim. That
is a list, not a summary. This reads the windowed news files and uses the FREE engine pool to write
a real synthesis: a short "what's actually happening and why it matters" paragraph plus a few THEMES
that GROUP related items across sources — the digest a person would write, for $0 (no Claude tokens).

Graceful: if no free-engine key is present it skips and the dashboard keeps the headline digest.
Run it in a lane that has the engine keys (bulk_analyze). Writes data/news_digest.json.

Usage:  python -m src.news_digest
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

from src.bulk_analyze import extract

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "news_digest.json"
CONFIG = ROOT / "config.json"
WINDOWS = [("daily", "daily_web_news.json", "the last 24 hours"),
           ("weekly", "weekly_web_news.json", "the last 7 days"),
           ("monthly", "monthly_web_news.json", "the last 30 days")]


def _load(p: Path, default):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return default


def _pool() -> list[dict]:
    cfg = _load(CONFIG, {})
    bc = cfg.get("bulk_analyze", {}) or {}
    engines = []
    for e in (bc.get("engines") or []):
        k = os.environ.get(e.get("secret_name", ""), "").strip()
        if k:
            engines.append({"provider": e.get("provider", "gemini"), "base_url": e.get("base_url", ""),
                            "model": e.get("model", ""), "key": k, "name": e.get("name", "engine")})
    if not engines:
        k = os.environ.get("EXTERNAL_REVIEW_API_KEY", "").strip()
        if k:
            engines.append({"provider": "gemini", "base_url": "", "model": "gemini-2.5-flash",
                            "key": k, "name": "gemini-2.5-flash"})
    return engines


def synthesize(entries: list[dict], window_text: str, engines: list[dict], timeout: int = 40) -> dict | None:
    items = entries[:18]
    if not items:
        return None
    lines = [f"- {e.get('title','')} ({e.get('source_name','')})" +
             (f": {e.get('summary','')[:160]}" if e.get("summary") else "") for e in items]
    prompt = (
        f"You are the editor of an AI-news brief. Below are headlines from official sources over "
        f"{window_text}. Write the brief a smart reader wants: synthesize, don't list. STRICT JSON ONLY:\n"
        '{"summary":"3-4 sentences: the through-line of the period — what actually happened and why '
        'it matters. Concrete, no hype, no marketing words.",'
        '"themes":[{"theme":"short label","detail":"1-2 sentences grouping the related items"}]}\n'
        "- 3 to 5 themes. Group related items across sources; never just restate one headline.\n"
        "- No em dashes. If the items are thin, say so briefly.\n\nHEADLINES:\n" + "\n".join(lines)
    )
    for e in engines:
        try:
            res = extract(e["provider"], e["base_url"], e["key"], e["model"], prompt, timeout)
            if isinstance(res, dict) and res.get("summary"):
                res["_engine"] = e["name"]
                return res
        except Exception:
            continue
    return None


def main() -> int:
    engines = _pool()
    if not engines:
        print("news_digest: no free-engine key present — skipped (dashboard keeps the headline digest).")
        return 0
    out = {"generated_at": datetime.now(timezone.utc).isoformat(), "windows": {}}
    made = 0
    for key, fname, wtext in WINDOWS:
        data = _load(DATA / fname, {})
        entries = (data.get("entries") if isinstance(data, dict) else None) or []
        dg = synthesize(entries, wtext, engines)
        if dg:
            out["windows"][key] = {"summary": dg.get("summary", ""), "themes": dg.get("themes", [])[:5],
                                   "n_sources": len(entries), "engine": dg.get("_engine", "")}
            made += 1
    if made:
        OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"news_digest: synthesized {made}/{len(WINDOWS)} windows (free engine, 0 Claude tokens).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
