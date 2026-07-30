"""
src/excava_core.py — M2 class overhaul, CLASS 1 of 5: **Element / Package**.

THE PROBLEM THIS FIXES. `data/elements_index.json` is the one normalized view of all ~11k hub
items, but nothing owns *access* to it: 14 separate modules (`relate`, `deep_retrieve`,
`verify_elements`, `power_scan`, `excava_creators`, `discover_promote`, `build_hub_api`,
`github_meta_enrich`, `excava_backlog`, `excava_proof`, `excava_selfimprove`,
`excava_experiments`, `element_model` itself, plus `docs/dashboard.js`) each re-open the file
and re-interpret its fields by hand. Every one of them re-decides what "usable" means, what a
stub is, and how to reach a link. That duplication IS the 97-module fragmentation the END PLAN's
§2/§6 class overhaul exists to collapse — so `Element` is the correct first class: it is the
narrowest, most-depended-on shape in the system, and the other four (Tool, Room, Agent, Router)
all end up holding Elements.

WHAT THIS IS NOT. This is not a rewrite. `element_model.py` remains the sole builder of the
index and the sole write path (`set_field`); this module is a typed, tested *accessor* over its
output. Every existing consumer keeps working untouched — they are migrated one at a time, on
purpose (P5: an overhaul is never silently half-built). `activate.py` is the first migration.

LAW COMPLIANCE. Free + stdlib only, no new dependency (P1). Offline/online parity (P7): the
loader falls back to the public hub exactly like `activate.py` does, so this works outside the
repo. Read-only by default; the single write path delegates to `element_model.set_field`.

Run:
    python -m src.excava_core stats
    python -m src.excava_core find "github mcp" --usable
    python -m src.excava_core show connector:github-mcp
    python -m src.excava_core package my-stack --add tool:n8n --add connector:github-mcp
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
INDEX = DATA / "elements_index.json"
PACKAGES = DATA / "excava" / "packages.json"
REMOTE = "https://eitanvinokur12345.github.io/AI-YouTube-Playlist-Information-Extractor/data"

# Status law (P3, mirrored from element_model): a low rating is NEVER a reason to discard.
# "niche" is a first-class usable status — a 1/10 may be perfect for exactly one task.
USABLE_STATUS = ("verified", "niche")


def _norm(s) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(s or "").lower()).strip()


class Element:
    """One hub item, in the unified shape. Wraps a record from elements_index.json.

    Read-only apart from `set()`, which routes to element_model's single write path.
    """

    __slots__ = ("_d",)

    def __init__(self, d: dict):
        self._d = d or {}

    # --- identity -------------------------------------------------------
    @property
    def id(self) -> str:
        return self._d.get("id", "")

    @property
    def type(self) -> str:
        return self._d.get("type", "")

    @property
    def name(self) -> str:
        return self._d.get("name", "")

    @property
    def what(self) -> str:
        return self._d.get("what", "")

    @property
    def category(self) -> str:
        return self._d.get("category", "")

    @property
    def body(self) -> str:
        """The element's own content (prompts/commands ARE their body)."""
        return self._d.get("body", "")

    @property
    def install(self) -> str:
        return self._d.get("install", "")

    @property
    def quality(self):
        return self._d.get("quality_score")

    @property
    def source_videos(self) -> list:
        return self._d.get("source_videos", []) or []

    @property
    def related_ids(self) -> list:
        return self._d.get("related", []) or []

    # --- links ----------------------------------------------------------
    @property
    def links(self) -> dict:
        return self._d.get("links", {}) or {}

    @property
    def github(self) -> str:
        return self.links.get("github", "")

    @property
    def website(self) -> str:
        return self.links.get("website", "")

    @property
    def best_link(self) -> str:
        """The one link most worth opening for this element."""
        return self.github or self.website or self.links.get("source_url", "")

    # --- status ---------------------------------------------------------
    @property
    def status(self) -> str:
        """verified | niche | unverified | dead (element_model's P3 status law)."""
        return (self._d.get("verified") or {}).get("status", "unverified")

    @property
    def is_stub(self) -> bool:
        return bool(self._d.get("stub"))

    @property
    def is_enriched(self) -> bool:
        return bool(self._d.get("enriched"))

    @property
    def is_dead(self) -> bool:
        return self.status == "dead"

    def is_usable(self) -> bool:
        """Can Eitan actually DO something with this today?

        Usable = it passed its checks (verified or niche) AND there is a real way in: a live
        link, an install line, or its own body. This is the single definition the 14 hand-rolled
        consumers each re-invented; every future class asks this method instead.
        """
        if self.status not in USABLE_STATUS:
            return False
        return bool(self.best_link or self.install or self.body)

    # --- actions --------------------------------------------------------
    def activation(self) -> dict:
        """The paste-ready setup recipe for this element.

        Delegates to `activate.plan()` rather than re-deriving the recipe (Ponytail: reuse the
        proven path). Imported lazily so `activate` can depend on this module without a cycle.
        """
        from src import activate as _activate

        raw = {
            "name": self.name,
            "slug": self.id.partition(":")[2],
            "github": self.github,
            "homepage": self.website,
            "quality_score": self.quality,
            "setup": self._d.get("setup") or ({"command": self.install} if self.install else {}),
        }
        return _activate.plan(raw, self.type)

    def set(self, field: str, value) -> bool:
        """The ONLY write path — delegates to element_model so the owning file stays truth."""
        from src import element_model

        return element_model.set_field(self.id, field, value)

    def related(self) -> list:
        idx = load()
        return [idx[r] for r in self.related_ids if r in idx]

    def to_dict(self) -> dict:
        return dict(self._d)

    def __repr__(self) -> str:
        return f"<Element {self.id} [{self.status}]{' stub' if self.is_stub else ''}>"


class Package:
    """A named bundle of Elements — the plan's 'Element/Package' pair (§2, law P8).

    A Package is what EXCAVA hands over when one element is not enough: 'the stack for
    building an MCP-backed research agent' = a connector + a skill + a prompt. Persisted to
    data/excava/packages.json so a package built in one session survives into the next.
    """

    def __init__(self, name: str, element_ids: list | None = None, note: str = ""):
        self.name = name
        self.element_ids = list(element_ids or [])
        self.note = note

    def add(self, eid: str) -> bool:
        if eid in self.element_ids:
            return False
        self.element_ids.append(eid)
        return True

    def elements(self) -> list:
        idx = load()
        return [idx[e] for e in self.element_ids if e in idx]

    def missing(self) -> list:
        """Ids in the package that no longer resolve — a package can rot; say so honestly."""
        idx = load()
        return [e for e in self.element_ids if e not in idx]

    def to_dict(self) -> dict:
        return {"name": self.name, "elements": self.element_ids, "note": self.note}

    # --- persistence ----------------------------------------------------
    @staticmethod
    def _store() -> dict:
        try:
            return json.loads(PACKAGES.read_text(encoding="utf-8"))
        except Exception:
            return {"packages": []}

    @classmethod
    def load(cls, name: str):
        for p in cls._store().get("packages", []):
            if p.get("name") == name:
                return cls(p["name"], p.get("elements", []), p.get("note", ""))
        return None

    @classmethod
    def all(cls) -> list:
        return [cls(p["name"], p.get("elements", []), p.get("note", ""))
                for p in cls._store().get("packages", [])]

    def save(self) -> None:
        store = self._store()
        pkgs = [p for p in store.get("packages", []) if p.get("name") != self.name]
        pkgs.append(self.to_dict())
        store["packages"] = pkgs
        PACKAGES.parent.mkdir(parents=True, exist_ok=True)
        PACKAGES.write_text(json.dumps(store, ensure_ascii=False, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# Index access (cached; offline/online parity per P7)
# ---------------------------------------------------------------------------
_INDEX_CACHE: dict | None = None
_DUPES: list = []


def _raw_index() -> dict:
    """Local index first; fall back to the public hub so this works outside the repo (P7)."""
    try:
        if INDEX.exists():
            return json.loads(INDEX.read_text(encoding="utf-8"))
    except Exception:
        pass
    try:
        with urllib.request.urlopen(f"{REMOTE}/elements_index.json", timeout=20) as r:
            return json.loads(r.read().decode("utf-8", "replace"))
    except Exception:
        return {}


def load(refresh: bool = False) -> dict:
    """id -> Element for the whole hub. Cached; pass refresh=True after a rebuild.

    An id must be unique — it is how every consumer, override and relation addresses an element.
    The index does not currently guarantee that (see `duplicates()`), so collisions are recorded
    instead of being silently dropped: a swallowed record is invisible work, and the whole point
    of this class is that nothing goes quiet.
    """
    global _INDEX_CACHE, _DUPES
    if _INDEX_CACHE is None or refresh:
        raw = _raw_index()
        _INDEX_CACHE, _DUPES = {}, []
        for e in raw.get("elements", []):
            if not isinstance(e, dict) or not e.get("id"):
                continue
            eid = e["id"]
            if eid in _INDEX_CACHE:
                _DUPES.append(e)
                continue
            _INDEX_CACHE[eid] = Element(e)
    return _INDEX_CACHE


def duplicates() -> list:
    """Records the index emitted under an id that was already taken — they are UNREACHABLE.

    Cause (found 2026-07-30 by this class's first run): `element_model._slug()` truncates to 60
    chars, so distinct long `command` names collapse onto one id. Fixing the slug re-keys
    elements hub-wide and would invalidate `element_overrides.json` / `elements_related.json`
    keys, so it is deliberately a separate, verified increment — not a silent side-effect here.
    """
    load()
    return list(_DUPES)


def get(eid: str):
    return load().get(eid)


def find(query: str, type: str | None = None, usable_only: bool = False,
         limit: int = 10) -> list:
    """Score-ranked search over the hub.

    Scoring mirrors activate.find (exact > substring > all-words > some-words) so the two agree,
    but adds the status awareness activate.py never had: dead elements are excluded outright and
    usable ones outrank unusable ones at equal text score.
    """
    q = _norm(query)
    qs = set(q.split())
    hits = []
    for el in load().values():
        if type and el.type != type:
            continue
        if el.is_dead:
            continue
        if usable_only and not el.is_usable():
            continue
        n = _norm(el.name)
        if not n:
            continue
        words = set(n.split())
        if n == q:
            score = 100
        elif q and q in n:
            score = 70
        elif qs and qs <= words:
            score = 60
        elif qs & words:
            score = 30 + 8 * len(qs & words)
        elif q and q in _norm(el.what):
            score = 20
        else:
            continue
        # directly-installable kinds win ties, then usability, then rating
        score += {"connector": 4, "skill": 3, "prompt": 2, "command": 2}.get(el.type, 0)
        score += 5 if el.is_usable() else 0
        score += (el.quality or 0) / 100.0
        hits.append((score, el))
    hits.sort(key=lambda x: (-x[0], x[1].name))
    return [el for _, el in hits[:limit]]


def stats() -> dict:
    els = list(load().values())
    by_status, by_type = {}, {}
    for e in els:
        by_status[e.status] = by_status.get(e.status, 0) + 1
        by_type[e.type] = by_type.get(e.type, 0) + 1
    return {"total": len(els), "usable": sum(1 for e in els if e.is_usable()),
            "stubs": sum(1 for e in els if e.is_stub), "by_status": by_status,
            "by_type": dict(sorted(by_type.items(), key=lambda kv: -kv[1])),
            "unreachable": len(duplicates())}


# ---------------------------------------------------------------------------
def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="EXCAVA Element/Package class (M2 class 1 of 5)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("stats")
    f = sub.add_parser("find")
    f.add_argument("query")
    f.add_argument("--type")
    f.add_argument("--usable", action="store_true")
    f.add_argument("--limit", type=int, default=10)
    f.add_argument("--json", action="store_true")
    s = sub.add_parser("show")
    s.add_argument("eid")
    s.add_argument("--json", action="store_true")
    p = sub.add_parser("package")
    p.add_argument("name")
    p.add_argument("--add", action="append", default=[])
    p.add_argument("--note", default="")
    a = ap.parse_args()

    if a.cmd == "stats":
        st = stats()
        print(f"hub: {st['total']} elements · {st['usable']} usable · {st['stubs']} stubs")
        print("  by status:", ", ".join(f"{k}={v}" for k, v in st["by_status"].items()))
        print("  by type:  ", ", ".join(f"{k}={v}" for k, v in st["by_type"].items()))
        if st["unreachable"]:
            print(f"  ⚠ {st['unreachable']} record(s) UNREACHABLE — id collisions "
                  f"(element_model._slug truncates at 60 chars):")
            for d in duplicates():
                print(f"      {d['id']}  <- {d.get('name', '')[:60]!r}")
        return 0

    if a.cmd == "find":
        hits = find(a.query, type=a.type, usable_only=a.usable, limit=a.limit)
        if a.json:
            print(json.dumps([h.to_dict() for h in hits], ensure_ascii=False, indent=2))
            return 0
        if not hits:
            print(f'no match for "{a.query}"')
            return 1
        for el in hits:
            mark = "USABLE" if el.is_usable() else el.status.upper()
            print(f"  [{mark:>10}] {el.id:<44} {el.what[:70]}")
        return 0

    if a.cmd == "show":
        el = get(a.eid)
        if not el:
            print(f"no element {a.eid}")
            return 1
        if a.json:
            print(json.dumps(el.to_dict(), ensure_ascii=False, indent=2))
            return 0
        print(f"{el.name}  ({el.type} | {el.status}{' | stub' if el.is_stub else ''})")
        print(f"  {el.what}")
        if el.best_link:
            print(f"  link: {el.best_link}")
        act = el.activation()
        print(f"  ACTIVATE ({act['kind']}{' | needs key' if act['needs_key'] else ''}):")
        for i, step in enumerate(act["steps"], 1):
            print(f"    {i}. {step}")
        if el.related_ids:
            print("  related:", ", ".join(el.related_ids[:6]))
        return 0

    if a.cmd == "package":
        pkg = Package.load(a.name) or Package(a.name, note=a.note)
        if a.note:
            pkg.note = a.note
        added = [e for e in a.add if get(e) and pkg.add(e)]
        unknown = [e for e in a.add if not get(e)]
        pkg.save()
        print(f"package '{pkg.name}': {len(pkg.element_ids)} element(s)"
              + (f" (+{len(added)} added)" if added else ""))
        for el in pkg.elements():
            print(f"  - {el.id:<44} {'usable' if el.is_usable() else el.status}")
        if unknown:
            print("  unknown ids (not added):", ", ".join(unknown))
        if pkg.missing():
            print("  MISSING (no longer in hub):", ", ".join(pkg.missing()))
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
