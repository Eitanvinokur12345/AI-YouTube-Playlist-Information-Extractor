"""
src/resolve_links.py — THE ACCESS protocol: give every tool/skill/connector REAL, working links.

FAST rewrite (F1). The old resolver did ONE LLM call per item + a serial HTTP verify + a slow grounded
search for everything — ~30s/item, so runs timed out and coverage crawled. The bottleneck was never
"power", it was MANAGEMENT. This version:
  1. BATCHES ~25 items into a single call (25× fewer round-trips).
  2. Routes FAST engines first (Cerebras / Groq know most canonical URLs instantly); slow grounded
     Gemini search is used ONLY for the residue the batch couldn't resolve, with a small budget.
  3. VERIFIES every candidate URL in PARALLEL (thread pool) instead of one-at-a-time.
Every stored URL is still HTTP-verified (no hallucinated/dead links). Un-resolved items retry up to
MAX_TRIES on later runs (so coverage never gets permanently stuck). Free, no paid search API.

Run:  python -m src.resolve_links --limit 300
"""
from __future__ import annotations

import argparse
import itertools
import json
import os
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor
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
SETS = [("tools.json", "tools", "name"), ("connectors.json", "connectors", "name"),
        ("skills.json", "skills", "skill_name")]
BATCH = 25            # items resolved per LLM call
MAX_TRIES = 6         # retry a hard item up to this many runs (more attempts → more eventually resolve)
GROUND_CAP = 200      # grounded-search calls per run (the residue) — parallel across keys; push coverage +5%/day
FAST = ("cerebras", "groq", "sambanova")   # providers to try first (very high tok/s)


def _load(p, default):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return default


def _save(p, obj):
    Path(p).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def _pool() -> list:
    cfg = _load(CONFIG, {})
    bc = cfg.get("bulk_analyze", {}) or {}
    eng = []
    for e in (bc.get("engines") or []):
        k = os.environ.get(e.get("secret_name", ""), "").strip()
        if k:
            eng.append({"provider": e.get("provider", "gemini"), "base_url": e.get("base_url", ""),
                        "model": e.get("model", ""), "key": k})
    # fast engines first — they answer in ~1s and know most canonical URLs
    eng.sort(key=lambda e: 0 if any(f in (e.get("provider") or "").lower() for f in FAST) else 1)
    return eng


def _gemini_keys() -> list:
    ks = []
    for n in ["EXTERNAL_REVIEW_API_KEY", "GEMINI_API_KEY"] + [f"GEMINI_API_KEY_{i}" for i in range(2, 9)]:
        v = (os.environ.get(n) or "").strip()
        if v and v not in ks:
            ks.append(v)
    return ks


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


def verify_many(urls: list, workers: int = 16) -> dict:
    """Verify many URLs in PARALLEL — the old serial HEAD/GET loop was a big part of the slowness."""
    uniq = [u for u in dict.fromkeys(urls) if u]
    if not uniq:
        return {}
    with ThreadPoolExecutor(max_workers=workers) as ex:
        results = list(ex.map(verify, uniq))
    return dict(zip(uniq, results))


def _clean_url(u) -> str:
    u = u.strip().strip('"').strip("'") if isinstance(u, str) else ""
    return u if u.lower().startswith(("http://", "https://")) else ""


def ask_links_batch(batch: list, engines: list, timeout: int = 30) -> dict:
    """Resolve a whole BATCH of items in ONE call. `batch` = [(idx, name, desc)]. Returns
    {idx: {"website":..., "github":...}}. Tries fast engines first, falls back through the pool."""
    lines = "\n".join(f"{i}. {name} :: {(desc or '')[:90]}" for i, name, desc in batch)
    prompt = (
        "For each numbered AI tool/product below, give its REAL official website and GitHub repo.\n"
        f"{lines}\n\n"
        "Reply with STRICT JSON ONLY — an object keyed by the number as a string:\n"
        '{"1":{"website":"https://... or null","github":"https://github.com/owner/repo or null"}, ...}\n'
        "Use ONLY genuine URLs you are confident are the real official links; use null if unsure. "
        "Never invent a URL. If not open-source, github is null."
    )
    for e in engines[:4]:
        try:
            r = extract(e["provider"], e["base_url"], e["key"], e["model"], prompt, timeout)
            if isinstance(r, dict) and r:
                out = {}
                for i, _n, _d in batch:
                    v = r.get(str(i)) or r.get(i)
                    if isinstance(v, dict):
                        out[i] = {"website": _clean_url(v.get("website")), "github": _clean_url(v.get("github"))}
                if out:
                    return out
        except Exception:
            continue
    return {}


def gemini_grounded(name: str, desc: str, keys: list, timeout: int = 14) -> dict:
    """Slow but strong: Gemini WITH Google-Search grounding (runs on Google's servers, works from the
    datacenter IP). Used ONLY for the residue the fast batch couldn't resolve, with a per-run budget."""
    if not keys:
        return {}
    prompt = (f"Search the web for the AI tool/product called \"{name}\" ({desc[:120]}). "
              "Reply with ONLY its real official website URL and GitHub repo URL (if open source), "
              "each on its own line as 'website: <url>' and 'github: <url>'. Use real URLs from the "
              "search results only; if unknown, write null. Never invent a URL.")
    body = {"contents": [{"parts": [{"text": prompt}]}], "tools": [{"google_search": {}}],
            "generationConfig": {"temperature": 0}}
    for key in keys[:2]:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={key}"
        try:
            req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
                                         headers={"Content-Type": "application/json"})
            payload = json.loads(urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "replace"))
            txt = payload["candidates"][0]["content"]["parts"][0]["text"]
            gh = GH_RE.search(txt)
            site = re.search(r"https?://[^\s)\"']+", re.sub(r"github\.com/\S+", "", txt))
            return {"website": site.group(0) if site else "",
                    "github": f"https://github.com/{gh.group(1)}/{gh.group(2)}" if gh else ""}
        except Exception:
            continue
    return {}


def _store(it: dict, site: str, gh: str) -> bool:
    """Store already-VERIFIED links on the item. Returns True if anything was set."""
    got = False
    if gh and "github.com" in gh:
        it["github"] = gh
        it["deploy_url"] = f"https://vercel.com/new/clone?repository-url={gh}"
        it.pop("run_url", None)
        got = True
    if site:
        it["homepage"] = site
        got = True
    if got:
        it["links_verified_at"] = NOW
        it.pop("link_tries", None)
    return got


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=300)
    ap.add_argument("--sleep", type=float, default=0.0, help="(unused; kept for workflow compatibility)")
    args = ap.parse_args()
    engines = _pool()
    if not engines:
        print("resolve_links: no engine key present — skipped (graceful)."); return 0
    gkeys = _gemini_keys()

    # ── gather items needing a link, highest-quality first, across all sets ──
    loaded, todo = {}, []
    for fname, key, nk in SETS:
        d = _load(DATA / fname, {})
        loaded[fname] = d
        items = d.get(key, []) if isinstance(d, dict) else []
        for it in sorted(items, key=lambda x: x.get("quality_score", 0) or 0, reverse=True):
            has_link = it.get("homepage") or it.get("github") or it.get("install_or_source")
            if has_link or (it.get("link_tries") or 0) >= MAX_TRIES:
                continue
            name = str(it.get(nk) or it.get("slug") or "").strip()
            if name:
                todo.append((fname, it, name))
            if len(todo) >= args.limit:
                break
        if len(todo) >= args.limit:
            break

    fixed = 0
    residue = []        # (it, name) the fast batch couldn't resolve → grounded search (budgeted)
    # ── batched fast resolution + parallel verification ──
    for s in range(0, len(todo), BATCH):
        chunk = todo[s:s + BATCH]
        batch = [(i, name, it.get("description") or it.get("what_it_does") or "")
                 for i, (_fn, it, name) in enumerate(chunk)]
        proposed = ask_links_batch(batch, engines)
        cand_urls = []
        for i, (_fn, it, name) in enumerate(chunk):
            p = proposed.get(i) or {}
            cand_urls += [p.get("website"), p.get("github")]
        ok = verify_many(cand_urls)
        for i, (_fn, it, name) in enumerate(chunk):
            p = proposed.get(i) or {}
            site = p.get("website") if ok.get(p.get("website")) else ""
            gh = p.get("github") if ok.get(p.get("github")) else ""
            if _store(it, site, gh):
                fixed += 1
            else:
                residue.append((it, name))

    # ── residue → grounded Google search, PARALLEL across keys. Grounding is the STRONG resolver (it
    #    actually finds the obscure ones); the fast batch made runs cheap, so we can afford many now.
    #    Each job uses its own key (round-robin) to spread load and dodge per-key rate limits.
    grounded = 0
    work = residue[:GROUND_CAP] if gkeys else []
    if work:
        keycycle = itertools.cycle(gkeys)
        jobs = [(it, name, next(keycycle)) for it, name in work]

        def _ground(job):
            it, name, key = job
            wf = gemini_grounded(name, str(it.get("description") or it.get("what_it_does") or ""), [key])
            site = wf.get("website") if verify(wf.get("website", "")) else ""
            gh = wf.get("github") if verify(wf.get("github", "")) else ""
            return it, site, gh

        with ThreadPoolExecutor(max_workers=min(max(len(gkeys), 1) * 2, 12)) as ex:
            for it, site, gh in ex.map(_ground, jobs):
                grounded += 1
                if _store(it, site, gh):
                    fixed += 1
                else:
                    it["link_tries"] = (it.get("link_tries") or 0) + 1

    for fname, key, nk in SETS:
        if fname in loaded:
            _save(DATA / fname, loaded[fname])
    _save(STATE, {"updated_at": NOW, "processed_this_run": len(todo), "grounded": grounded})
    print(f"resolve_links: {len(todo)} items, {fixed} got REAL verified links "
          f"(fast batch + {grounded} grounded). Parallel-verified, fast-engine-first.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
