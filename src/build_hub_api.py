"""
src/build_hub_api.py — M4.5 HUB-AS-DATABASE.

Publishes a compact, PUBLIC read endpoint at docs/hub_api.json (served by GitHub Pages,
so any project can fetch it) plus docs/hub_api_packages.json. It lets Budoaris / FreeDup /
any tool pull real elements + assembled packages out of Excavatortron — either directly by
URL or carried by the activator (M4.1).

Shape (docs/hub_api.json):
  { version, generated_at, endpoint, counts,
    packages: [ {id, name, what, elements:[{id,type,name,what,install,url}]} ],
    elements: [ {id, type, name, install, url, verified} ]  # verified/real only, compact
  }

Run: python -m src.build_hub_api   (also safe to call every beat).
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"
ENDPOINT = "https://eitanvinokur12345.github.io/AI-YouTube-Playlist-Information-Extractor/docs/hub_api.json"


def _load(p, default):
    try:
        return json.loads(Path(p).read_text(encoding="utf-8"))
    except Exception:
        return default


def _slug(s: str) -> str:
    import re
    return "pkg-" + re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")[:40]


def _url(e: dict) -> str:
    """Kept for the compact shape, but the precedence now MATCHES Element.best_link
    (github first) instead of the website-first order this module used alone."""
    l = e.get("links") or {}
    return l.get("github") or l.get("website") or l.get("source_url") or l.get("open_code") or ""


def _compact(e: dict) -> dict:
    return {"id": e.get("id"), "type": e.get("type"), "name": e.get("name"),
            "what": (e.get("what") or "")[:220], "install": e.get("install") or "",
            "url": _url(e), "verified": (e.get("verified") or {}).get("status", "unverified")}


def build() -> dict:
    """Migrated onto the Element/Package classes (fire 95) — the 2nd of 14 index consumers.

    This fixed a REAL orphan, not just style: packages lived in TWO stores
    (`data/packages.json`, curated by earlier phases, and `data/excava/packages.json`, written
    by the Package class) and this module only ever read the first. Anything assembled through
    the class was therefore invisible to the public hub API — the exact "nothing orphaned"
    failure the collapse exists to end. `Package.all()` now reads both, so one accessor sees
    every package and this module cannot drift from it again.

    Also drops two hand-rolled definitions in favour of the shared ones: "is this real enough to
    publish" is now `Element.is_usable()` (which additionally requires a real way IN, so a
    verified element with no link/install/body is correctly no longer published as usable), and
    the link is `Element.best_link`.
    """
    from src import excava_core as core

    idx = _load(DATA / "elements_index.json", [])
    els = idx if isinstance(idx, list) else idx.get("elements", [])
    by_id = core.load()

    elements = [_compact(e.to_dict()) for e in by_id.values() if e.is_usable()]

    packages = []
    for p in core.Package.all():
        resolved = []
        for eid in p.element_ids:
            e = by_id.get(eid)
            resolved.append(_compact(e.to_dict()) if e else
                            {"id": eid, "type": "?", "name": eid, "what": "",
                             "install": "", "url": "", "verified": "unknown"})
        packages.append({"id": _slug(p.name), "name": p.name, "what": p.note,
                         "elements": resolved})

    api = {
        "version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "endpoint": ENDPOINT,
        "usage": "GET this file. Find a package in .packages[], or an element in .elements[] "
                 "(by id/type/name). Each element carries install + url so a client can set it up. "
                 "The activator (SKILL.md) can also carry this offline.",
        "counts": {"packages": len(packages), "elements": len(elements), "elements_total": len(els)},
        "packages": packages,
        "elements": elements,
    }
    return api


def main() -> int:
    DOCS.mkdir(parents=True, exist_ok=True)
    api = build()
    (DOCS / "hub_api.json").write_text(json.dumps(api, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    # a smaller packages-only file for cheap package pulls
    (DOCS / "hub_api_packages.json").write_text(
        json.dumps({"generated_at": api["generated_at"], "endpoint": ENDPOINT, "packages": api["packages"]},
                   ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"hub_api: {api['counts']['packages']} packages, {api['counts']['elements']} real elements "
          f"(of {api['counts']['elements_total']}) -> docs/hub_api.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
