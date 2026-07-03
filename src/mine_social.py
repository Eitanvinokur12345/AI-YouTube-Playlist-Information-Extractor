"""
src/mine_social.py — PHASE 9 TIER-1: omni-source intake from PUBLIC, FREE endpoints.

Owner directive 2026-07-03: extract capability-knowledge from beyond the playlist. Tier 1 =
no login, no key, no cost: Reddit public JSON · Telegram public channel previews (t.me/s) ·
DuckDuckGo whole-web search · YouTube-beyond-playlist (existing free API key, optional) ·
WhatsApp group exports the owner drops in data/whatsapp_exports/ (tier 2, no API exists).
Locked feeds (Instagram/TikTok/Facebook/LinkedIn) are deliberately ABSENT until D6 opts in.

Everything lands in data/social_intake.json as candidate items — an INTAKE QUEUE, not the
hub: the mining department consumes candidates through the existing verify+security gate
(quality over quantity; nothing untrusted touches the hub directly).

Sources config: data/social_sources.json (owner-editable, see QUESTIONS.md #22).
Free, stdlib-only, graceful: a dead endpoint skips, never breaks the lane.
Run: python -m src.mine_social [--limit-per-source 25]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import urllib.request
from urllib.parse import quote, unquote
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "social_intake.json"
# A plain browser UA: Reddit 403s script-looking UAs and DDG serves a 202 challenge to them.
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _get(url: str, timeout: int = 20) -> str:
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", errors="replace")
    except Exception:
        return ""


def _trust() -> dict:
    try:
        return json.load(open(DATA / "source_trust.json", encoding="utf-8")).get("sources", {})
    except Exception:
        return {}


_TRUST = None


def _item(source: str, title: str, url: str, extra: str = "", via: str = "") -> dict:
    global _TRUST
    if _TRUST is None:
        _TRUST = _trust()
    kind = source.split("/")[0]
    return {"source": source, "title": title.strip()[:220], "url": url,
            "extra": extra.strip()[:300], "via": via, "found_at": _now(),
            "trust": _TRUST.get(kind, 40)}


def reddit(subs: list[str], limit: int) -> list[dict]:
    """Reddit via public RSS — the .json endpoint 403s unauthenticated clients since the
    API lockdown, but hot.rss still serves keyless. Atom entries: title + link."""
    out = []
    for sub in subs:
        raw = _get(f"https://www.reddit.com/r/{sub}/hot.rss")
        for entry in re.findall(r"<entry>(.*?)</entry>", raw, re.S)[:limit]:
            t = re.search(r"<title>(.*?)</title>", entry, re.S)
            u = re.search(r'<link href="([^"]+)"', entry)
            if t and u:
                title = re.sub(r"<[^>]+>", "", t.group(1)).replace("&amp;", "&")
                out.append(_item(f"reddit/r/{sub}", title, u.group(1).replace("&amp;", "&")))
    return out


class _TgParse(HTMLParser):
    """Minimal parser for t.me/s/<channel> public previews (no login needed)."""
    def __init__(self):
        super().__init__()
        self.msgs, self._in, self._buf = [], False, []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "div" and "tgme_widget_message_text" in (a.get("class") or ""):
            self._in, self._buf = True, []
    def handle_endtag(self, tag):
        if self._in and tag == "div":
            self._in = False
            t = re.sub(r"\s+", " ", "".join(self._buf)).strip()
            if len(t) > 30:
                self.msgs.append(t)
    def handle_data(self, data):
        if self._in:
            self._buf.append(data)


def telegram(channels: list[str], limit: int) -> list[dict]:
    out = []
    for ch in channels:
        html = _get(f"https://t.me/s/{ch}")
        if not html:
            continue
        p = _TgParse()
        try:
            p.feed(html)
        except Exception:
            continue
        for msg in p.msgs[-limit:]:
            u = re.search(r"https?://\S+", msg)
            out.append(_item(f"telegram/{ch}", msg[:150], u.group(0).rstrip(").,") if u else
                             f"https://t.me/s/{ch}", msg[150:400]))
    return out


def ddg(queries: list[str], limit: int) -> list[dict]:
    """DuckDuckGo html endpoint — whole-internet search, no key. Best-effort parse."""
    out = []
    for q in queries:
        html = _get("https://html.duckduckgo.com/html/?q=" + quote(q))
        for url, title in re.findall(
                r'class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', html)[:limit]:
            title = re.sub(r"<[^>]+>", "", title)
            if url.startswith("//duckduckgo.com/l/?uddg="):
                url = unquote(url.split("uddg=", 1)[1].split("&", 1)[0])
            out.append(_item("web-search", title, url, via=q))
    return out


def youtube(queries: list[str], limit: int) -> list[dict]:
    """Beyond-playlist discovery on the EXISTING free API key; silently skips without one."""
    key = (os.environ.get("YOUTUBE_API_KEY") or "").strip()
    if not key:
        return []
    out = []
    for q in queries:
        raw = _get("https://www.googleapis.com/youtube/v3/search?part=snippet&type=video"
                   f"&maxResults={min(limit, 25)}&q={quote(q)}&key={key}")
        try:
            for it in json.loads(raw).get("items", []):
                sn, vid = it.get("snippet", {}), (it.get("id") or {}).get("videoId", "")
                if vid:
                    out.append(_item("youtube-beyond", sn.get("title", ""),
                                     f"https://www.youtube.com/watch?v={vid}",
                                     sn.get("channelTitle", ""), q))
        except Exception:
            continue
    return out


def whatsapp_exports(folder: Path, limit: int) -> list[dict]:
    """Tier 2: parse owner-dropped WhatsApp .txt exports for links (the only free path)."""
    out = []
    if not folder.exists():
        return out
    for f in folder.glob("*.txt"):
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for u in re.findall(r"https?://\S+", text)[:limit]:
            out.append(_item(f"whatsapp/{f.stem}", u[:120], u.rstrip(").,")))
    return out


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit-per-source", type=int, default=0)
    args = ap.parse_args()
    try:
        cfg = json.load(open(DATA / "social_sources.json", encoding="utf-8"))
    except Exception:
        cfg = {}
    limit = args.limit_per_source or cfg.get("max_items_per_source", 25)

    items = []
    items += reddit(cfg.get("reddit_subreddits", []), limit)
    items += telegram(cfg.get("telegram_channels", []), limit)
    items += ddg(cfg.get("search_queries", []), limit)
    items += youtube(cfg.get("youtube_queries", []), limit)
    items += whatsapp_exports(ROOT / cfg.get("whatsapp_exports_dir", "data/whatsapp_exports"), limit)

    # merge with the existing queue, dedupe by url, keep newest 800 (bounded)
    try:
        old = json.load(open(OUT, encoding="utf-8")).get("items", [])
    except Exception:
        old = []
    seen, merged = set(), []
    for it in items + old:
        u = it.get("url", "")
        if u and u not in seen:
            seen.add(u)
            merged.append(it)
    merged = merged[:800]
    per = {}
    for it in merged:
        k = it["source"].split("/")[0]
        per[k] = per.get(k, 0) + 1
    OUT.write_text(json.dumps({
        "generated_at": _now(), "total": len(merged), "new_this_run": len(items),
        "per_source": per, "tier": "1 (public, free — owner decision 2026-07-03)",
        "note": "INTAKE QUEUE, not the hub: the mining lane consumes these through the verify+security gate.",
        "items": merged}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"social intake: +{len(items)} this run, {len(merged)} queued total; per source: "
          + ", ".join(f"{k}={v}" for k, v in sorted(per.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
