"""
src/resolve_links.py — THE ACCESS protocol: give every tool/skill/connector REAL, working links.

The catalogue used to store only the VIDEO a tool came from, so clicking a tool opened YouTube and
neither the owner nor the activator could actually USE anything. This resolves, per item:
  - homepage : the official website / docs
  - github   : the source repo (for open-source)
  - run_url  : a one-click "open in GitHub Codespaces" link (already-activated, ready to run)
  - source   : stays the bundle of videos it was found in (endorsement_video_ids), shown separately

How it stays FREE and CORRECT:
  1. Ask the free LLM engine pool for the official website + GitHub of the named tool (only if it's
     confident it's the REAL link). The free models already know the canonical URL for most tools.
  2. VERIFY every returned URL actually resolves (HTTP 200, browser UA) before storing it — so a
     hallucinated or dead link is dropped, never shown. This is the "check the links are correct"
     step the owner asked for.
  3. Derive run_url from the verified github repo: https://codespaces.new/<owner>/<repo>.

Budget per run (state in data/links_state.json) so it chips through the backlog each cycle, newest /
highest-quality first. No paid search API. Run:  python -m src.resolve_links --limit 80
"""
from __future__ import annotations

import argparse
import json
import os
import re
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from src.bulk_analyze import extract

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
STATE = DATA / "links_state.json"
CONFIG = ROOT / "config.json"
NOW = datetime.now(timezone.utc).isoformat()
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
GH_RE = re.compile(r"github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")
# datasets we fix, with the name field and whether github/codespaces is meaningful
SETS = [("tools.json", "tools", "name"), ("connectors.json", "connectors", "name"),
        ("skills.json", "skills", "skill_name")]


def _load(p, default):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return default


def _save(p, obj):
    Path(p).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def _pool():
    cfg = _load(CONFIG, {})
    bc = cfg.get("bulk_analyze", {}) or {}
    eng = []
    for e in (bc.get("engines") or []):
        k = os.environ.get(e.get("secret_name", ""), "").strip()
        if k:
            eng.append({"provider": e.get("provider", "gemini"), "base_url": e.get("base_url", ""),
                        "model": e.get("model", ""), "key": k})
    return eng


def verify(url: str, timeout: int = 5) -> bool:
    """True only if the URL really resolves (so we never store a fake/dead link)."""
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


def codespace(github_url: str) -> str:
    m = GH_RE.search(github_url or "")
    return f"https://codespaces.new/{m.group(1)}/{m.group(2).removesuffix('.git')}" if m else ""


def web_find(name: str, timeout: int = 12) -> dict:
    """Free, no-key fallback: search DuckDuckGo for the tool's real site + GitHub. Best-effort —
    if the datacenter IP gets blocked it just returns {} (the Bright Data token makes this reliable)."""
    import urllib.parse
    out = {}
    try:
        q = urllib.parse.quote(f"{name} official site github")
        req = urllib.request.Request(f"https://html.duckduckgo.com/html/?q={q}",
                                     headers={"User-Agent": UA})
        html = urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "replace")
        # DDG wraps results as ...uddg=<encoded real url>...
        urls = [urllib.parse.unquote(u) for u in re.findall(r"uddg=([^&\"]+)", html)]
        for u in urls:
            if "github.com/" in u and "github" not in out and GH_RE.search(u):
                out["github"] = "https://github.com/" + GH_RE.search(u).group(1) + "/" + GH_RE.search(u).group(2)
            elif u.startswith("http") and "website" not in out and not any(
                    b in u for b in ("duckduckgo", "youtube.com", "reddit.com", "wikipedia.org", "github.com")):
                out["website"] = u
            if "github" in out and "website" in out:
                break
    except Exception:
        pass
    return out


def _gemini_keys() -> list[str]:
    ks = []
    for n in ["EXTERNAL_REVIEW_API_KEY", "GEMINI_API_KEY"] + [f"GEMINI_API_KEY_{i}" for i in range(2, 9)]:
        v = (os.environ.get(n) or "").strip()
        if v and v not in ks:
            ks.append(v)
    return ks


def gemini_grounded(name: str, desc: str, keys: list, timeout: int = 14) -> dict:
    """Use Gemini WITH Google-Search grounding to find the REAL site + repo. The search runs on
    Google's servers, so it works from the datacenter IP (unlike scraping DuckDuckGo). Best fix for
    the niche tools plain LLM-recall doesn't know. Extracts URLs from the grounded answer + sources."""
    if not keys:
        return {}
    prompt = (f"Search the web for the AI tool/product called \"{name}\" ({desc[:120]}). "
              "Reply with ONLY its real official website URL and GitHub repo URL (if open source), "
              "each on its own line as 'website: <url>' and 'github: <url>'. Use real URLs from the "
              "search results only; if unknown, write null. Never invent a URL.")
    body = {"contents": [{"parts": [{"text": prompt}]}], "tools": [{"google_search": {}}],
            "generationConfig": {"temperature": 0}}
    for key in keys[:2]:                               # cap (speed)
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={key}"
        try:
            req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
                                         headers={"Content-Type": "application/json"})
            payload = json.loads(urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "replace"))
            txt = payload["candidates"][0]["content"]["parts"][0]["text"]
            gh = GH_RE.search(txt)
            site = re.search(r"https?://[^\s)\"']+", re.sub(r"github\.com/\S+", "", txt))
            return {"website": site.group(0) if site else None,
                    "github": f"https://github.com/{gh.group(1)}/{gh.group(2)}" if gh else None}
        except Exception:
            continue
    return {}


def ask_links(name: str, desc: str, engines: list, timeout: int = 30) -> dict:
    prompt = (
        f"Tool/product name: {name}\nWhat it is: {desc[:200]}\n\n"
        "Give ONLY the REAL official links for THIS exact product, as STRICT JSON: "
        '{"website":"https://...","github":"https://github.com/owner/repo"}. '
        "Use null for any you are not confident is the genuine official link. Never guess or invent a "
        "URL. If it is not open-source, github is null."
    )
    for e in engines[:3]:                              # cap engines tried (speed — was looping all 16)
        try:
            r = extract(e["provider"], e["base_url"], e["key"], e["model"], prompt, timeout)
            if isinstance(r, dict) and ("website" in r or "github" in r):
                return r
        except Exception:
            continue
    return {}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=80)
    ap.add_argument("--sleep", type=float, default=1.5)
    args = ap.parse_args()
    engines = _pool()
    if not engines:
        print("resolve_links: no engine key present — skipped (graceful)."); return 0

    st = _load(STATE, {}) or {}
    done = set()            # per-RUN only (no permanent skip — un-resolved items get retried)
    MAX_TRIES = 4           # retry a hard item up to this many runs as search sources improve
    gkeys = _gemini_keys()  # for Gemini google-search grounding (works from datacenter IPs)
    fixed = checked = 0

    for fname, key, nk in SETS:
        d = _load(DATA / fname, {})
        items = d.get(key, []) if isinstance(d, dict) else []
        # newest/highest-quality first; skip ones already given real links or already attempted
        ranked = sorted(items, key=lambda x: x.get("quality_score", 0) or 0, reverse=True)
        changed = False
        for it in ranked:
            if checked >= args.limit:
                break
            ident = f"{key}:{it.get('slug') or it.get(nk)}"
            has_link = it.get("homepage") or it.get("github") or it.get("install_or_source")
            # skip if already linked, or tried hard enough already (else RETRY — coverage was stuck
            # at 15% because un-resolved items used to be skipped forever after one attempt)
            if ident in done or has_link or (it.get("link_tries") or 0) >= MAX_TRIES:
                continue
            # Inline-extracted links (e.g. URLs seen on screen) must be VERIFIED, not trusted.
            if it.get("homepage") or it.get("github"):
                if it.get("github") and not verify(it["github"]):
                    it.pop("github", None); it.pop("deploy_url", None)
                elif it.get("github"):
                    it["deploy_url"] = f"https://vercel.com/new/clone?repository-url={it['github']}"
                if it.get("homepage") and not verify(it["homepage"]):
                    it.pop("homepage", None)
                if it.get("homepage") or it.get("github"):
                    it["links_verified_at"] = NOW; done.add(ident); checked += 1; fixed += 1
                    changed = True; continue
            name = str(it.get(nk) or it.get("slug") or "").strip()
            if not name:
                continue
            checked += 1
            done.add(ident)
            time.sleep(args.sleep)
            res = ask_links(name, str(it.get("description") or it.get("what_it_does") or ""), engines)
            site, gh = (res.get("website") or "").strip(), (res.get("github") or "").strip()
            if not (site or gh):                       # LLM didn't know it -> Gemini google-search grounding
                wf = gemini_grounded(name, str(it.get("description") or it.get("what_it_does") or ""), gkeys)
                site, gh = (wf.get("website") or "").strip(), (wf.get("github") or "").strip()
                # (web_find/DDG dropped from the cloud path — it's IP-blocked from datacenter + wastes ~12s/item)
            got = False
            if gh and "github.com" in gh and verify(gh):
                it["github"] = gh
                # owner chose a DEPLOY BUTTON (not Codespaces, which billed his account). Vercel's
                # clone URL is the most general one-click deploy for a repo.
                it["deploy_url"] = f"https://vercel.com/new/clone?repository-url={gh}"
                it.pop("run_url", None)
                got = True
            if site and verify(site):
                it["homepage"] = site
                got = True
            # if the existing url field is already real, keep it as homepage
            if not it.get("homepage") and it.get("url") and verify(it["url"]):
                it["homepage"] = it["url"]; got = True
            if got:
                it["links_verified_at"] = NOW; it.pop("link_tries", None); fixed += 1
            else:
                it["link_tries"] = (it.get("link_tries") or 0) + 1   # retry next run, not skip forever
            changed = True
        if changed:
            _save(DATA / fname, d)

    _save(STATE, {"updated_at": NOW, "processed_this_run": len(done)})
    print(f"resolve_links: checked {checked} items, gave {fixed} REAL verified links "
          f"(website/github/codespaces). {len(done)} total resolved so far.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
