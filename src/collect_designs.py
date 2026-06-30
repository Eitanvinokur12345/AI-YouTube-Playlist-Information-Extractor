"""
src/collect_designs.py — DESIGNS-ONLY collector for the Designs tab.

The owner: the Designs tab must hold DESIGNS, not tools/skills — real visual looks from AI websites
and from videos, shown as a full-page capture so he can react to every part. This builds a clean
designs.json from:
  1. MIGRATE the old file: keep only entries that are an actual viewable design (have a live URL or a
     described look); DROP repo/tool entries (the "tools in the designs tab" problem).
  2. AI-PRODUCT homepages already resolved in the hub (tools/connectors/models) — the design of a real
     AI website. Deduped by domain, top-quality first.
  3. A curated SEED list of real AI-builder galleries + exemplar AI product sites + design galleries.
  4. SCREEN URLs surfaced by the visual protocol (data/screen_urls.json) — sites SHOWN in the videos.

No GitHub-repo-as-tool entries, no deploy-as-tool. Each entry carries a live `source_url` the dashboard
screenshots full-page (free mShots). Style is left for the Arena to learn when unknown. Free, stdlib.

Run:  python -m src.collect_designs
"""
from __future__ import annotations

import json
import os
import re
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")


def verify(url: str, timeout: int = 5) -> bool:
    """True only if the URL really resolves — so dead demo homepages (the 404 preview tiles) are dropped."""
    if not url or not url.startswith(("http://", "https://")):
        return False
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                if 200 <= r.status < 400:
                    return True
        except Exception:
            continue
    return False


# domain parkers (JungleTrade etc. land on these) + for-sale text → these are NOT designs, drop them
PARKER_HOSTS = ("hugedomains.com", "sedo.com", "sedoparking.com", "parkingcrew.net", "afternic.com",
                "domainmarket.com", "dan.com", "bodis.com", "above.com", "godaddy.com")
PARKED_TEXT = ("buy this domain", "this domain is for sale", "domain is for sale", "domain for sale",
               "the domain you're looking for", "this domain has expired", "is parked free",
               "checkout the full domain details", "domain may be for sale")


def check_url(url: str, timeout: int = 6) -> dict:
    """Persisted liveness check: returns {status: ok|dead|parked, no_embed}. Parked = a for-sale/parking
    page (resolves 200 but is junk). no_embed = the site blocks being shown in an iframe (X-Frame-Options
    / CSP frame-ancestors) so the dashboard shows its screenshot instead of a blank frame."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            if not (200 <= r.status < 400):
                return {"status": "dead", "no_embed": False}
            final = (r.geturl() or "").lower()
            xfo = (r.headers.get("X-Frame-Options") or "").lower()
            csp = (r.headers.get("Content-Security-Policy") or "").lower()
            no_embed = bool(xfo) or ("frame-ancestors" in csp)
            host = urllib.parse.urlparse(final).netloc.lower()
            if any(p in host for p in PARKER_HOSTS):
                return {"status": "parked", "no_embed": no_embed}
            body = r.read(45000).decode("utf-8", "replace").lower()
        if any(t in body for t in PARKED_TEXT):
            return {"status": "parked", "no_embed": no_embed}
        return {"status": "ok", "no_embed": no_embed}
    except Exception:
        return {"status": "dead", "no_embed": False}


ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "designs.json"
SCREEN = DATA / "screen_urls.json"
NOW = datetime.now(timezone.utc).isoformat()

STYLE_ALLOWED = {"bold", "colorful", "playful", "brutalist", "minimal", "retro", "glassy", "dark", "gradient"}

# NOT AI website designs: physical/hardware/robots, dev IDEs/compilers, default builder template pages.
NON_DESIGN_RE = re.compile(
    r"\b(robot|robots|robotic|humanoid|quadruped|drone|compiler|ide|firmware|microcontroller|"
    r"arduino|raspberry pi|cnc|3d printer|soldering|servo|actuator|lidar)\b")
JUNK_HOSTS = ("sites.google.com", "default-domain", "example.com")

# Curated, real, public sources — exemplar AI sites/builders that screenshot as actual designs,
# plus a few gallery hubs to browse more. (name, url, style_tags, source_type)
SEEDS = [
    # AI builders (their own UIs are bold reference designs)
    ("v0 by Vercel", "https://v0.dev", ["bold", "dark", "minimal"], "ai-builder"),
    ("Lovable", "https://lovable.dev", ["bold", "gradient"], "ai-builder"),
    ("Bolt.new", "https://bolt.new", ["bold", "dark"], "ai-builder"),
    ("Replit", "https://replit.com", ["bold", "colorful"], "ai-builder"),
    ("Framer", "https://www.framer.com", ["bold", "playful"], "ai-builder"),
    ("Readdy", "https://readdy.ai", ["colorful", "gradient"], "ai-builder"),
    ("Create.xyz", "https://www.create.xyz", ["bold", "playful"], "ai-builder"),
    # AI product homepages (real, polished designs)
    ("Midjourney", "https://www.midjourney.com", ["dark", "bold"], "ai-product"),
    ("ElevenLabs", "https://elevenlabs.io", ["bold", "gradient"], "ai-product"),
    ("Perplexity", "https://www.perplexity.ai", ["minimal", "dark"], "ai-product"),
    ("Linear", "https://linear.app", ["minimal", "dark", "glassy"], "ai-product"),
    ("Cursor", "https://www.cursor.com", ["dark", "bold"], "ai-product"),
    ("Runway", "https://runwayml.com", ["bold", "dark"], "ai-product"),
    ("Suno", "https://suno.com", ["bold", "colorful"], "ai-product"),
    ("Krea", "https://www.krea.ai", ["colorful", "playful"], "ai-product"),
    ("Pika", "https://pika.art", ["playful", "colorful"], "ai-product"),
    ("Vercel", "https://vercel.com", ["minimal", "bold", "dark"], "ai-product"),
    # Design galleries (browse many more)
    ("Awwwards", "https://www.awwwards.com/websites/", ["bold"], "gallery"),
    ("Godly", "https://godly.website", ["bold", "brutalist"], "gallery"),
    ("Land-book", "https://land-book.com", ["bold", "minimal"], "gallery"),
    ("Lapa Ninja", "https://www.lapa.ninja", ["bold"], "gallery"),
    ("httpster", "https://httpster.net", ["brutalist", "bold"], "gallery"),
    ("SiteInspire", "https://www.siteinspire.com", ["minimal", "bold"], "gallery"),
    ("One Page Love", "https://onepagelove.com", ["bold"], "gallery"),
    ("Brutalist Websites", "https://brutalistwebsites.com", ["brutalist"], "gallery"),
    # Designer concepts
    ("Dribbble — Web Design", "https://dribbble.com/shots/popular/web-design", ["colorful", "playful"], "dribbble"),
    ("Behance — UI/UX", "https://www.behance.net/galleries/ui-ux", ["bold", "colorful"], "dribbble"),
]


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")[:80] or "design"


def _domain(u: str) -> str:
    try:
        n = urllib.parse.urlparse(u).netloc.lower()
        return n[4:] if n.startswith("www.") else n
    except Exception:
        return u.lower()


def _norm(u: str) -> str:
    u = (u or "").strip()
    if not u:
        return ""
    u = re.sub(r"#.*$", "", u).rstrip("/")
    return u.lower()


def _is_design_url(u: str) -> bool:
    u = (u or "").lower()
    return u.startswith(("http://", "https://")) and not any(
        b in u for b in ("youtube.com", "youtu.be", "github.com", "google.com/search", "/login", "/signup",
                         "sites.google.com"))


def _entry(name, url, styles, source_type, look="", origin="", github=""):
    styles = [s for s in (styles or []) if s in STYLE_ALLOWED]
    e = {"name": name or _domain(url), "slug": _slug(github or url or name),
         "source_url": url, "source_type": source_type, "style_tags": styles,
         "look": look or "", "origin": origin or "", "added_at": NOW}
    if github:
        e["github"] = github
    return e


def main() -> int:
    d = json.load(open(OUT, encoding="utf-8")) if OUT.exists() else {"designs": []}
    old = d.get("designs", []) if isinstance(d, dict) else []
    out, seen_url, seen_dom = [], set(), set()

    def add(e):
        live = e.get("source_url") or ""
        key = _norm(live)
        if key:
            if key in seen_url:
                return False
            seen_url.add(key)
        elif not e.get("look"):
            return False                      # nothing to show (no url, no described look)
        # one entry per domain for product/gallery sources (avoid 5 pages of the same site)
        if live and e.get("source_type") in ("ai-product", "ai-builder", "gallery", "dribbble"):
            dom = _domain(live)
            if dom in seen_dom:
                return False
            seen_dom.add(dom)
        out.append(e)
        return True

    # 1) MIGRATE old designs — keep real designs, drop repo/tool entries
    kept = dropped = 0
    for x in old:
        live = x.get("source_url") or x.get("homepage") or ""
        if not _is_design_url(live):
            live = ""
        is_repo_only = (not live) and (x.get("github") or x.get("source_type") == "github-designs")
        if is_repo_only:
            dropped += 1
            continue
        styles = [s for s in (x.get("style_tags") or []) if s in STYLE_ALLOWED]
        st = x.get("source_type")
        if st == "github-designs":
            st = "oss"
        if not st:
            src = str(x.get("source") or "")
            if src.startswith(("gemini", "visual")):
                st = "video"
            elif x.get("github") or live:
                st = "oss"
            else:
                st = "video"        # no url + no repo → it was described from a video
        # legacy OSS/demo homepages often 404 (the "preview unavailable" / yellow-404 tiles) — verify + drop dead ones
        if st == "oss" and live and not verify(live):
            dropped += 1
            continue
        e = _entry(x.get("name"), live, styles, st, look=x.get("look") or "",
                   origin=x.get("origin") or "", github=x.get("github") if live else "")
        if add(e):
            kept += 1

    # 2) AI-PRODUCT homepages already in the hub = the design of real AI websites
    prod = 0
    desc_by_dom = {}        # domain -> source description, so the junk filter can judge URL-only designs
    for fname, key, nk in [("tools.json", "tools", "name"), ("connectors.json", "connectors", "name"),
                           ("models.json", "models", "name")]:
        p = DATA / fname
        if not p.exists():
            continue
        items = (json.load(open(p, encoding="utf-8")) or {}).get(key, [])
        items = sorted(items, key=lambda z: z.get("quality_score", 0) or 0, reverse=True)
        for it in items:
            home = it.get("homepage") or ""
            if home:
                desc_by_dom.setdefault(_domain(home), (it.get("description") or "")[:200])
            if prod >= 160 or not _is_design_url(home):
                continue
            if NON_DESIGN_RE.search((str(it.get(nk) or "") + " " + str(it.get("description") or "")).lower()):
                continue                                  # skip robots / IDEs / hardware at intake
            if add(_entry(it.get(nk), home, [], "ai-product",
                          look=(it.get("description") or "")[:160], origin=fname)):
                prod += 1

    # 3) curated seeds
    for name, url, styles, st in SEEDS:
        add(_entry(name, url, styles, st, origin="seed"))

    # 4) URLs SHOWN in videos (from the visual protocol)
    scr = 0
    if SCREEN.exists():
        for u in (json.load(open(SCREEN, encoding="utf-8")) or {}).get("urls", []):
            url = u.get("url") if isinstance(u, dict) else u
            if _is_design_url(url) and add(_entry(
                    (u.get("name") if isinstance(u, dict) else "") or _domain(url), url,
                    (u.get("style_tags") if isinstance(u, dict) else []) or [], "video",
                    look=(u.get("look") if isinstance(u, dict) else "") or "",
                    origin=(u.get("from_video") if isinstance(u, dict) else "") or "")):
                scr += 1

    # 4b) FILTER non-AI-design junk (robots, IDEs, default builder pages) — these aren't website designs.
    nj, keep = 0, []
    for e in out:
        host = _domain(e.get("source_url") or "")
        blob = (str(e.get("name") or "") + " " + str(e.get("look") or "") + " " + desc_by_dom.get(host, "")).lower()
        # uninformative = a scraped homepage we know NOTHING about (no description, no style) — low-value junk
        # like the misfiled "CODEBLOCK". Curated seeds are always kept.
        uninformative = (e.get("source_type") in ("ai-product", "video", "oss")
                         and not str(e.get("look") or "").strip() and not e.get("style_tags"))
        if NON_DESIGN_RE.search(blob) or any(h in host for h in JUNK_HOSTS) or uninformative:
            nj += 1
        else:
            keep.append(e)
    out = keep

    # 5) LIVENESS + PARKED check (persisted + cached): drop dead/parked URLs, flag embed-blocked ones.
    cache = {}
    for x in old:
        u = _norm(x.get("source_url") or x.get("homepage") or "")
        if u and x.get("url_status"):
            cache[u] = (x.get("url_status"), bool(x.get("no_embed")), x.get("url_checked_at"))
    need = []
    for e in out:
        u = _norm(e.get("source_url") or "")
        if not u:
            continue
        if u in cache:
            e["url_status"], e["no_embed"], e["url_checked_at"] = cache[u]
        else:
            need.append(e)
    checked = 0
    if need:
        batch = need[:400]                                   # cap per run; the rest get checked next cycle
        with ThreadPoolExecutor(max_workers=24) as ex:
            results = list(ex.map(lambda e: check_url(e["source_url"]), batch))
        for e, r in zip(batch, results):
            e["url_status"], e["no_embed"], e["url_checked_at"] = r["status"], r["no_embed"], NOW
        checked = len(batch)
    bad = [e for e in out if e.get("url_status") in ("dead", "parked")]
    out = [e for e in out if e.get("url_status") not in ("dead", "parked")]

    d["designs"] = out
    d["updated_at"] = NOW
    OUT.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"collect_designs: {len(out)} designs (kept {kept} / dropped {dropped} repo-only + {len(bad)} dead/parked "
          f"+ {nj} non-design; +{prod} AI-product, +{len(SEEDS)} seeds, +{scr} shown-in-video; url-checked {checked}). designs-only.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
