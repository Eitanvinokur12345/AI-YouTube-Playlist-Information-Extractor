"""
src/github_meta_enrich.py — deterministic GitHub-metadata enricher (EXCAVA v2, non-brain front).

QUESTIONS.md (away-week, fire 5) flagged the real hub blocker: 3,628+ stub elements, and the
only enricher that fills them (deep_retrieve.py) needs an LLM to fuse its best results — so on
a normal run it only makes real progress via the local drain on EITAN-PC (Ollama), which is
enriching ~13/day because the machine is often off. deep_retrieve's KEYLESS fallback path
(README scrape + homepage <title>/<meta>) already runs brain-free, but for the ~1,600 GitHub-repo
elements there is a faster, more reliable, fully-structured source that needs no scraping and no
LLM at all: the GitHub REST API's own repo metadata (`description`, `topics`, `homepage`).

This lane is intentionally dumb: one API call per repo, no fusion, no invention — the repo's own
description IS the description. Keyless (60 req/hr is plenty for one CI hour's stub batch); uses
GITHUB_TOKEN when the environment provides one (raises the ceiling to 5,000/hr) but never
requires it. Falls back to deep_retrieve's README-first-sentence extractor only when the API
gives nothing usable, so a repo with no `description` field still gets a real answer.

Run: python -m src.github_meta_enrich --limit 60 [--dry-run]
Progress cursor in data/github_meta_enrich_state.json; the elements_index rebuild picks results up.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

from src import element_model as em
from src.deep_retrieve import DESC_FIELD, readme_excerpt

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
STATE = DATA / "github_meta_enrich_state.json"
MIN_LEN = 60
GH_RE = re.compile(r"github\.com/([\w.\-]+)/([\w.\-]+)")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _repo_slug(el: dict) -> tuple[str, str] | None:
    gh = el.get("links", {}).get("github", "") or ""
    m = GH_RE.search(gh)
    if not m:
        return None
    return m.group(1), m.group(2).removesuffix(".git")


def fetch_repo_meta(owner: str, repo: str, timeout: int = 15) -> dict | None:
    """One keyless (or token-boosted) call to the GitHub REST API. None on any failure —
    a bad/renamed/private repo must never crash the batch."""
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "excava-github-meta-enrich"}
    token = os.environ.get("GITHUB_TOKEN", "")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(f"https://api.github.com/repos/{owner}/{repo}", headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            remaining = r.headers.get("X-RateLimit-Remaining")
            data = json.loads(r.read(200_000).decode("utf-8", errors="replace"))
            data["_rate_remaining"] = int(remaining) if remaining and remaining.isdigit() else None
            return data
    except urllib.error.HTTPError as e:
        if e.code == 403:
            return {"_rate_limited": True}
        return None
    except Exception:
        return None


def describe(meta: dict) -> str:
    """Build a factual description from repo metadata alone — no invention beyond what
    GitHub itself reports."""
    desc = (meta.get("description") or "").strip()
    topics = [t for t in (meta.get("topics") or []) if isinstance(t, str)][:6]
    bits = []
    if desc:
        bits.append(desc.rstrip("."))
    if topics:
        bits.append(f"Topics: {', '.join(topics)}")
    lang = meta.get("language")
    if lang and not desc:
        bits.append(f"Primary language: {lang}")
    return (". ".join(bits) + ".") if bits else ""


def enrich(el: dict, dry: bool = False) -> dict | None:
    slug = _repo_slug(el)
    if not slug:
        return None
    owner, repo = slug
    meta = fetch_repo_meta(owner, repo)
    if meta is None:
        return {"id": el["id"], "new": False, "reason": "fetch-failed"}
    if meta.get("_rate_limited"):
        return {"id": el["id"], "new": False, "reason": "rate-limited"}
    new_what = describe(meta)
    method = "github-api"
    if len(new_what) < MIN_LEN:
        # last resort: deep_retrieve's own README-first-sentences extractor (still keyless)
        raw = readme_excerpt(el)
        if raw:
            first = re.split(r"(?<=[.!?])\s+", re.sub(r"[#*`\[\]]", "", raw).strip())
            new_what = " ".join(first[:3])[:500]
            method = "github-api+readme-fallback"
    if len(new_what) < MIN_LEN or len(new_what) <= len(el.get("what", "")):
        new_what = None  # never downgrade an already-decent description
    if not new_what:
        return {"id": el["id"], "new": False, "reason": "no-usable-metadata"}
    evidence = {"sources": ["github-api"], "n_sources": 1, "method": method, "at": _now()}
    if not dry:
        em.set_field(el["id"], DESC_FIELD.get(el["type"], "description"), new_what)
        ov = em._load("element_overrides.json", {"overrides": {}})
        ov.setdefault("overrides", {}).setdefault(el["id"], {}).update(
            {"enriched": True, "enrichment": evidence})
        em.OVERRIDES.write_text(json.dumps(ov, ensure_ascii=False, indent=1), encoding="utf-8")
    return {"id": el["id"], "new": bool(new_what), **evidence}


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=60)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--deadline", type=float, default=float(os.environ.get("GITHUB_META_ENRICH_DEADLINE", "300")))
    a = ap.parse_args()

    idx = em.build()
    todo = [e for e in idx["elements"] if e.get("stub") and _repo_slug(e)]
    st = em._load("github_meta_enrich_state.json", {"attempts": {}})
    todo_ids = {e["id"] for e in todo}
    attempts = {k: v for k, v in st.get("attempts", {}).items() if k in todo_ids}
    cutoff = (datetime.now(timezone.utc) - timedelta(days=3)).isoformat()
    fresh = [e for e in todo if attempts.get(e["id"], "") < cutoff]
    batch = fresh[:a.limit]

    done = upgraded = attempted = 0
    t0 = time.time()
    stopped_early = rate_limited = False
    for el in batch:
        if a.deadline and time.time() - t0 > a.deadline:
            stopped_early = True
            break
        attempted += 1
        if not a.dry_run:
            attempts[el["id"]] = _now()
        r = enrich(el, a.dry_run)
        if r:
            if r.get("reason") == "rate-limited":
                rate_limited = True
                break
            done += 1
            upgraded += r["new"]
        time.sleep(0.2)  # keyless courtesy pacing — well under the 60/hr ceiling regardless

    st["attempts"] = attempts
    st["todo_at_last_run"] = len(todo)
    st["updated_at"] = _now()
    if not a.dry_run:
        STATE.write_text(json.dumps(st, ensure_ascii=False, indent=2), encoding="utf-8")
        idx2 = em.build()
        tag = " — STOPPED (rate-limited)" if rate_limited else (
            f" — stopped at {a.deadline:.0f}s deadline after {attempted}/{len(batch)}" if stopped_early else "")
        print(f"github-meta-enrich: batch of {len(batch)} (fresh pool {len(fresh)}) from {len(todo)} "
              f"github-linked stubs; {done} processed ({upgraded} descriptions upgraded); "
              f"stubs now {idx2['stubs']}{tag}")
    else:
        print(f"[dry] would process {len(batch)} of {len(todo)} github-linked stubs (fresh pool {len(fresh)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
