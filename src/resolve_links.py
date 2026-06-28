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


def verify(url: str, timeout: int = 12) -> bool:
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


def ask_links(name: str, desc: str, engines: list, timeout: int = 30) -> dict:
    prompt = (
        f"Tool/product name: {name}\nWhat it is: {desc[:200]}\n\n"
        "Give ONLY the REAL official links for THIS exact product, as STRICT JSON: "
        '{"website":"https://...","github":"https://github.com/owner/repo"}. '
        "Use null for any you are not confident is the genuine official link. Never guess or invent a "
        "URL. If it is not open-source, github is null."
    )
    for e in engines:
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
    done = set(st.get("done", []))
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
            if ident in done or it.get("homepage") or it.get("links_verified_at"):
                continue
            name = str(it.get(nk) or it.get("slug") or "").strip()
            if not name:
                continue
            checked += 1
            done.add(ident)
            time.sleep(args.sleep)
            res = ask_links(name, str(it.get("description") or it.get("what_it_does") or ""), engines)
            site, gh = (res.get("website") or "").strip(), (res.get("github") or "").strip()
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
            it["links_verified_at"] = NOW
            if got:
                fixed += 1; changed = True
        if changed:
            _save(DATA / fname, d)

    _save(STATE, {"updated_at": NOW, "done": sorted(done)})
    print(f"resolve_links: checked {checked} items, gave {fixed} REAL verified links "
          f"(website/github/codespaces). {len(done)} total resolved so far.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
