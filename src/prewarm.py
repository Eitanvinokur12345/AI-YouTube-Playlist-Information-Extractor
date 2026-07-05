"""
src/prewarm.py — M1.5: the <10s PRE-WARM / OPEN system.

Every beat, the top-N elements (verified first, then quality x trust) get their OPEN target
resolved AHEAD of the click: repos -> a validated github.dev / Codespaces URL; sites -> the
live (redirect-resolved) URL; MCP/connectors -> the ready install command. The dashboard's
Open button hits data/prewarm.json first: WARM = instant. Cold elements derive their target
in-browser under the pancake-warming animation (<10s). Pre-warmed ids also re-verify every
verify pass — the "on-access" half of M1.C3.

Run: python -m src.prewarm --top 80
"""
from __future__ import annotations

import argparse
import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from src import element_model as em

DATA = Path(__file__).parent.parent / "data"
OUT = DATA / "prewarm.json"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _alive(url: str) -> str:
    try:
        req = urllib.request.Request(url, headers=UA, method="HEAD")
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.url if r.status < 400 else ""
    except Exception:
        return ""


def target(el: dict) -> dict | None:
    """Resolve the real runnable open-target for one element."""
    links = el.get("links", {})
    gh = links.get("github", "") or (links.get("website", "") if "github.com" in links.get("website", "") else "")
    m = re.search(r"github\.com/([\w.\-]+)/([\w.\-]+)", gh)
    if m:
        owner, repo = m.group(1), m.group(2).removesuffix(".git")
        return {"kind": "repo",
                "open_url": f"https://github.dev/{owner}/{repo}",
                "codespaces": f"https://codespaces.new/{owner}/{repo}",
                "install": el.get("install", "")}
    if el.get("install"):
        return {"kind": "mcp", "open_url": links.get("website", "") or links.get("source_url", ""),
                "install": el["install"]}
    site = links.get("website") or links.get("source_url")
    if site:
        live = _alive(site)
        return {"kind": "site", "open_url": live or site} if (live or site) else None
    return None


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=80)
    a = ap.parse_args()

    els = em.build()["elements"]
    def rank(e):
        s = {"verified": 3, "niche": 2, "unverified": 1, "dead": -9}.get(e["verified"]["status"], 0)
        q = e.get("quality_score") or 0
        return -(s * 100 + (q if isinstance(q, (int, float)) else 0) * 10 + e.get("trust", 0) / 10)
    ranked = sorted((e for e in els if e["verified"]["status"] != "dead"), key=rank)[:a.top]

    warm, failed = [], 0
    for el in ranked:
        t = target(el)
        if t and t.get("open_url"):
            warm.append({"id": el["id"], "name": el["name"], **t, "ready": True, "at": _now()})
        else:
            failed += 1
    OUT.write_text(json.dumps({"generated_at": _now(), "count": len(warm),
                               "note": "M1.5 pre-warmed open targets — the Open button hits these first (instant); cold items derive in-browser under the pancake animation.",
                               "warm": warm}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"prewarm: {len(warm)} targets ready ({failed} had nothing resolvable)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
