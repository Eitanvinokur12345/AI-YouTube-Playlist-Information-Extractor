"""
src/news.py  —  Daily AI news from official web sources (RSS/Atom).
Run with:  python -m src.news

WHY THIS EXISTS
---------------
The video playlist only produces "news" on days new videos appear. To keep the
dashboard's News tab fresh EVERY day (including quiet days), this script pulls
headlines from ~50 official AI sources listed in config.json -> news_sources.

COST / PRIVACY
--------------
- $0: public RSS/Atom feeds, no API keys, no tokens, no paid services.
- Summaries are the SOURCE'S OWN blurb, used VERBATIM (HTML stripped, truncated).
  We never call a model here, so this stage spends no tokens.

OUTPUT (kept SEPARATE from the video news so fetch.py never clobbers it)
------------------------------------------------------------------------
- data/web_news_store.json                     master rolling store (dedup, pruned)
- data/daily_web_news.json  / weekly / monthly  windowed views the dashboard reads

Each windowed file mirrors fetch.py's shape exactly:
  { "header": {run_time, window, covered_from, covered_to}, "entries": [ ... ] }
A web entry: { url, title, source_name, publishedAt, summary, source_type:"web" }
The dashboard merges these with the video news at render time, so the daily feed
always shows BOTH video news and official-site news.

STDLIB ONLY (+ pytz/dateutil already in requirements). No new dependencies.
"""
from __future__ import annotations

import html
import json
import logging
import re
import urllib.error
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path
from xml.etree import ElementTree as ET

import pytz
from dateutil import parser as dateutil_parser

# ── logging ──────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)
log = logging.getLogger(__name__)

# ── paths ──────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent.parent
CONFIG_PATH = ROOT / "config.json"
DATA_DIR = ROOT / "data"
WEB_STORE_JSON = DATA_DIR / "web_news_store.json"
DAILY_WEB_JSON = DATA_DIR / "daily_web_news.json"
WEEKLY_WEB_JSON = DATA_DIR / "weekly_web_news.json"
MONTHLY_WEB_JSON = DATA_DIR / "monthly_web_news.json"

EASTERN = pytz.timezone("America/New_York")
USER_AGENT = "AI-Skills-Tracker/1.0 (+github actions; RSS reader)"

# Illegal XML 1.0 control characters (everything in C0 except TAB, LF, CR).
_ILLEGAL_XML = re.compile(r"[\x00-\x08\x0B\x0C\x0E-\x1F]")
# A bare '&' that is NOT the start of a valid entity (named, decimal, or hex).
_BARE_AMP = re.compile(r"&(?!#\d+;|#x[0-9A-Fa-f]+;|[A-Za-z][\w.-]*;)")


# ── small helpers ────────────────────────────────────────────────────────────
def load_config() -> dict:
    with open(CONFIG_PATH, encoding="utf-8") as fh:
        return json.load(fh)


def save_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)


def load_json(path: Path, default: object) -> object:
    if path.exists():
        try:
            with open(path, encoding="utf-8") as fh:
                return json.load(fh)
        except Exception:
            return default
    return default


def _local(tag: str) -> str:
    """Return an XML tag's local name, lower-cased ('{ns}entry' -> 'entry')."""
    return tag.split("}")[-1].lower()


def strip_html(raw: str, max_chars: int) -> str:
    """Turn an HTML/escaped blurb into clean plain text, truncated. Verbatim text."""
    if not raw:
        return ""
    text = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", raw)  # drop script/style
    text = re.sub(r"<[^>]+>", " ", text)                            # strip tags
    text = html.unescape(text)                                      # &amp; -> &
    text = re.sub(r"\s+", " ", text).strip()                        # collapse whitespace
    if max_chars and len(text) > max_chars:
        text = text[: max_chars - 1].rstrip() + "…"            # add an ellipsis
    return text


def to_iso(date_str: str) -> str:
    """Parse an RFC822 / ISO date to a UTC ISO-8601 string; '' if unparseable."""
    if not date_str:
        return ""
    try:
        dt = dateutil_parser.parse(date_str)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc).isoformat()
    except Exception:
        return ""


# ── feed fetching + parsing ────────────────────────────────────────────────────
def fetch_feed(url: str, timeout: float) -> bytes | None:
    """GET a feed URL. Returns raw bytes, or None on any error (logged, non-fatal)."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except urllib.error.HTTPError as exc:
        log.warning("Feed HTTP %s for %s", exc.code, url)
    except Exception as exc:
        log.warning("Feed error for %s: %s", url, exc)
    return None


def _decode(raw: bytes) -> str:
    """Decode feed bytes, honoring an XML encoding declaration if present."""
    head = raw[:200].decode("ascii", "replace").lower()
    match = re.search(r"encoding=[\"']([\w-]+)[\"']", head)
    enc = match.group(1) if match else "utf-8"
    try:
        return raw.decode(enc, "replace")
    except LookupError:
        return raw.decode("utf-8", "replace")


def _sanitize_xml(raw: bytes) -> bytes:
    """Best-effort repair of feeds that aren't well-formed: strip illegal XML
    control characters and escape bare '&'. The XML declaration is removed so
    ElementTree parses the returned utf-8 bytes without an encoding conflict."""
    text = _decode(raw)
    text = re.sub(r"^\s*<\?xml[^>]*\?>", "", text, count=1)  # drop xml decl
    text = _ILLEGAL_XML.sub("", text)                        # strip control chars
    text = _BARE_AMP.sub("&amp;", text)                      # escape bare '&'
    return text.encode("utf-8")


def _pick_link(item: ET.Element) -> str:
    """Extract the article URL from an RSS <link>text</link> or Atom <link href>."""
    text_link = ""
    href_alt = ""
    href_any = ""
    for child in item:
        if _local(child.tag) != "link":
            continue
        href = child.attrib.get("href", "")
        rel = child.attrib.get("rel", "")
        if href:
            if rel in ("", "alternate") and not href_alt:
                href_alt = href
            if not href_any:
                href_any = href
        elif child.text and child.text.strip() and not text_link:
            text_link = child.text.strip()
    return href_alt or text_link or href_any


def _pick_text(item: ET.Element, names: tuple[str, ...]) -> str:
    """First non-empty text among child elements whose local-name is in `names`."""
    for child in item:
        if _local(child.tag) in names and child.text and child.text.strip():
            return child.text
    return ""


def parse_feed(raw: bytes, source_name: str, max_items: int, max_chars: int) -> list[dict]:
    """Parse RSS or Atom bytes into a list of normalized web-news entries."""
    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        try:                                  # retry once on a sanitized copy
            root = ET.fromstring(_sanitize_xml(raw))
        except ET.ParseError as exc:
            log.warning("Parse error for %s: %s", source_name, exc)
            return []

    # RSS items live at .//item; Atom entries at .//entry. Match by local-name.
    nodes = [el for el in root.iter() if _local(el.tag) in ("item", "entry")]
    entries: list[dict] = []
    for node in nodes[: max_items if max_items else None]:
        title = strip_html(_pick_text(node, ("title",)), 300)
        url = _pick_link(node).strip()
        if not title or not url:
            continue
        date_raw = _pick_text(node, ("pubdate", "published", "updated", "date"))
        blurb = _pick_text(node, ("description", "summary", "content", "encoded"))
        entries.append({
            "url": url,
            "title": title,
            "source_name": source_name,
            "publishedAt": to_iso(date_raw),
            "summary": strip_html(blurb, max_chars),
            "source_type": "web",
        })
    return entries


# ── store maintenance + windowing ────────────────────────────────────────────
def prune_store(items: list[dict], store_days: int, now_utc: datetime) -> list[dict]:
    """Drop entries older than store_days (by publishedAt, else first_seen)."""
    cutoff = now_utc - timedelta(days=store_days)
    kept: list[dict] = []
    for it in items:
        stamp = it.get("publishedAt") or it.get("first_seen") or ""
        try:
            dt = dateutil_parser.isoparse(stamp) if stamp else now_utc
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
        except Exception:
            dt = now_utc
        if dt >= cutoff:
            kept.append(it)
    return kept


def window_entries(items: list[dict], now_utc: datetime) -> tuple[list, list, list]:
    """Split store items into (daily<=24h, weekly<=7d, monthly<=30d), newest first."""
    run_eastern = now_utc.astimezone(EASTERN)
    daily, weekly, monthly = [], [], []
    for it in items:
        stamp = it.get("publishedAt") or it.get("first_seen") or ""
        try:
            dt = dateutil_parser.isoparse(stamp)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
        except Exception:
            continue
        age_hours = (run_eastern - dt.astimezone(EASTERN)).total_seconds() / 3600.0
        entry = {
            "url": it["url"],
            "title": it["title"],
            "source_name": it.get("source_name", ""),
            "publishedAt": it.get("publishedAt", ""),
            "summary": it.get("summary", ""),
            "source_type": "web",
        }
        key = dt
        if age_hours <= 24:
            daily.append((key, entry))
        elif age_hours <= 7 * 24:
            weekly.append((key, entry))
        elif age_hours <= 30 * 24:
            monthly.append((key, entry))

    def order(pairs: list[tuple]) -> list[dict]:
        return [e for _, e in sorted(pairs, key=lambda x: x[0], reverse=True)]

    return order(daily), order(weekly), order(monthly)


def build_web_news_file(now_utc: datetime, entries: list[dict], window_label: str) -> dict:
    """Mirror fetch.py.build_news_file so the dashboard reads one consistent shape."""
    run_eastern = now_utc.astimezone(EASTERN)
    if entries:
        covered_to = entries[0]["publishedAt"]
        covered_from = entries[-1]["publishedAt"]
    else:
        covered_to = covered_from = ""
    return {
        "header": {
            "run_time": run_eastern.isoformat(),
            "window": window_label,
            "covered_from": covered_from,
            "covered_to": covered_to,
        },
        "entries": entries,
    }


# ── main ────────────────────────────────────────────────────────────────────────
def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    cfg = load_config()
    news_cfg = cfg.get("news", {}) or {}
    if not news_cfg.get("enabled", True):
        log.info("news.enabled is false — nothing to do.")
        return

    sources = cfg.get("news_sources", []) or []
    max_items = int(news_cfg.get("max_items_per_source", 8))
    max_chars = int(news_cfg.get("summary_max_chars", 400))
    store_days = int(news_cfg.get("store_days", 30))
    timeout = float(news_cfg.get("request_timeout_seconds", 15))

    now_utc = datetime.now(timezone.utc)
    now_iso = now_utc.isoformat()

    # 1) Load the rolling master store, keyed by URL.
    store = load_json(WEB_STORE_JSON, {"items": []})
    by_url: dict[str, dict] = {it["url"]: it for it in store.get("items", []) if it.get("url")}

    # 2) Fetch every source (each failure is non-fatal).
    fetched = 0
    added = 0
    ok_sources = 0
    for src in sources:
        name = src.get("name", "")
        url = src.get("url", "")
        if not url:
            continue
        raw = fetch_feed(url, timeout)
        if raw is None:
            continue
        ok_sources += 1
        for entry in parse_feed(raw, name, max_items, max_chars):
            fetched += 1
            existing = by_url.get(entry["url"])
            if existing:
                # refresh fields but keep the first time we saw it
                entry["first_seen"] = existing.get("first_seen", now_iso)
                by_url[entry["url"]] = entry
            else:
                entry["first_seen"] = now_iso
                by_url[entry["url"]] = entry
                added += 1

    # 3) Prune anything older than store_days; persist the master store.
    items = prune_store(list(by_url.values()), store_days, now_utc)
    save_json(WEB_STORE_JSON, {"generated_at": now_iso, "items": items})

    # 4) Build the three windowed views the dashboard reads.
    daily, weekly, monthly = window_entries(items, now_utc)
    save_json(DAILY_WEB_JSON, build_web_news_file(now_utc, daily, "last 24 hours"))
    save_json(WEEKLY_WEB_JSON, build_web_news_file(now_utc, weekly, "last 7 days"))
    save_json(MONTHLY_WEB_JSON, build_web_news_file(now_utc, monthly, "last 30 days"))

    log.info(
        "Web news: %d/%d sources ok, %d items parsed, %d new, store=%d  "
        "(daily=%d weekly=%d monthly=%d)",
        ok_sources, len(sources), fetched, added, len(items),
        len(daily), len(weekly), len(monthly),
    )


if __name__ == "__main__":
    main()
