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


def _url(e: dict) -> str:
    l = e.get("links") or {}
    return l.get("website") or l.get("github") or l.get("open_code") or l.get("source_url") or ""


def _compact(e: dict) -> dict:
    return {"id": e.get("id"), "type": e.get("type"), "name": e.get("name"),
            "what": (e.get("what") or "")[:220], "install": e.get("install") or "",
            "url": _url(e), "verified": (e.get("verified") or {}).get("status", "unverified")}


def build() -> dict:
    idx = _load(DATA / "elements_index.json", [])
    els = idx if isinstance(idx, list) else idx.get("elements", [])
    by_id = {e.get("id"): e for e in els if e.get("id")}
    pkgs_raw = _load(DATA / "packages.json", {}).get("packages", [])

    # real/verified elements only — the hub is a database of things that actually work
    real = [e for e in els if (e.get("verified") or {}).get("status") in ("verified", "niche")
            and not e.get("stub")]
    elements = [_compact(e) for e in real]

    packages = []
    for p in pkgs_raw:
        resolved = []
        for ref in (p.get("elements") or []):
            eid = ref if isinstance(ref, str) else (ref.get("id") or ref.get("name") or "")
            e = by_id.get(eid)
            resolved.append(_compact(e) if e else {"id": eid, "type": "?", "name": eid,
                                                    "what": "", "install": "", "url": "", "verified": "unknown"})
        packages.append({"id": p.get("id"), "name": p.get("name"), "what": p.get("what", ""),
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
