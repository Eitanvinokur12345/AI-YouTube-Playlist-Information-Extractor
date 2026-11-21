"""Standalone Element/Package access. No agents, routing, rooms or OS execution."""
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
EXC = DATA / "excava"
PACKAGES = EXC / "packages.json"
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
    # Fire 95 found a REAL orphan: two package stores existed and the public hub API
    # (build_hub_api.py) only read the legacy one, so any package assembled through this class
    # was invisible outside the repo. Rather than move files (quarantine-never-delete), Package
    # now READS BOTH and is the single accessor; writes go to the class store. LEGACY is the
    # curated/pinned set built by earlier phases; PACKAGES is what this class creates.
    LEGACY = DATA / "packages.json"

    @staticmethod
    def _read(p: Path) -> list:
        try:
            return json.loads(p.read_text(encoding="utf-8")).get("packages", []) or []
        except Exception:
            return []

    @staticmethod
    def _store() -> dict:
        try:
            return json.loads(PACKAGES.read_text(encoding="utf-8"))
        except Exception:
            return {"packages": []}

    @classmethod
    def _from_raw(cls, p: dict) -> "Package":
        pkg = cls(p.get("name", p.get("id", "?")), p.get("elements", []),
                  p.get("note") or p.get("what", ""))
        return pkg

    @classmethod
    def load(cls, name: str):
        for p in cls._read(PACKAGES) + cls._read(cls.LEGACY):
            if p.get("name") == name or p.get("id") == name:
                return cls._from_raw(p)
        return None

    @classmethod
    def all(cls) -> list:
        """Every package from BOTH stores, class-created first, deduped by name."""
        out, seen = [], set()
        for p in cls._read(PACKAGES) + cls._read(cls.LEGACY):
            key = p.get("name") or p.get("id")
            if not key or key in seen:
                continue
            seen.add(key)
            out.append(cls._from_raw(p))
        return out

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

