"""
src/element_model.py — M1.0: the UNIFIED ELEMENT MODEL (EXCAVA v2).

Every hub item — skill, tool, prompt, command, connector, design, format, model, creation —
normalizes into ONE Element shape (data/schema/element.json) and lands in the read-only
data/elements_index.json that the dashboard, verification, relate, prewarm and the activator
all consume. The per-type files stay the source of truth; the index is derived, never edited
by hand. Writing back goes ONLY through set_field(), which locates the owning file.

Status law (M1.3, protocol P3): verified | unverified | niche | dead.
  - DEAD only when every objective check failed (link dead + sandbox fail where applicable)
    — never for a low rating. Niche elements are kept forever; a "1" may be perfect for one task.
  - Below the M1.C3 minimum enrichment+verification bar -> "unverified", never shown as real.

Free, stdlib-only. Run:
    python -m src.element_model            # rebuild the index
    python -m src.element_model --count    # rebuild + per-type totals + one sample
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
INDEX = DATA / "elements_index.json"
OVERRIDES = DATA / "element_overrides.json"   # sidecar for fields whose owner file is CI-hot
STUB_CHARS = 80                                # M1.C1: a 'what' shorter than this = stub

# type -> (file, list key, field mapping). get() everywhere: files evolve.
TYPES: dict = {
    "skill":     ("skills.json", "skills",
                  {"name": ["skill_name", "name"], "what": ["description"], "slug": ["slug"],
                   "website": ["homepage", "website"], "github": ["github"],
                   "videos": ["endorsement_video_ids", "source_videos"], "cat": ["category"],
                   "q": ["quality_score"]}),
    "tool":      ("tools.json", "tools",
                  {"name": ["name"], "what": ["description"], "slug": ["slug"],
                   "website": ["homepage"], "github": ["github"],
                   "videos": ["endorsement_video_ids"], "cat": ["category"], "q": ["quality_score"]}),
    "prompt":    ("prompts.json", "prompts",
                  {"name": ["title"], "what": ["purpose", "notes"], "slug": [],
                   "body": ["prompt_text"], "videos": ["source_videos"], "cat": ["category"], "q": []}),
    "command":   ("commands.json", "commands",
                  {"name": ["command"], "what": ["description"], "slug": [],
                   "videos": ["source_video"], "cat": ["tool"], "q": []}),
    "connector": ("connectors.json", "connectors",
                  {"name": ["name"], "what": ["what_it_does"], "slug": [],
                   "website": ["url"], "source_url": ["source_url"],
                   "install": ["install_or_source"], "videos": ["source_video", "source_videos"],
                   "cat": ["category"], "q": ["quality_score"]}),
    "design":    ("designs.json", "designs",
                  {"name": ["name"], "what": ["look"], "slug": ["slug"],
                   "github": ["github"], "source_url": ["source_url"], "videos": [],
                   "cat": ["origin"], "q": []}),
    "format":    ("formats.json", "formats",
                  {"name": ["name"], "what": ["description"], "slug": ["slug"],
                   "source_url": ["source_url"], "videos": [], "cat": ["kind"], "q": []}),
    "model":     ("models.json", "models",
                  {"name": ["name"], "what": ["description"], "slug": ["slug"],
                   "source_url": ["source_url"], "videos": ["source_videos", "source_video_id"],
                   "cat": ["category"], "q": ["quality_score"]}),
    "creation":  ("created_by_excava.json", "creations",
                  {"name": ["name"], "what": ["what"], "slug": [],
                   "website": ["url"], "videos": [], "cat": ["type"], "q": []}),
}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load(name, d=None):
    try:
        return json.load(open(DATA / name, encoding="utf-8"))
    except Exception:
        return d if d is not None else {}


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")[:60] or "x"


def _get(item: dict, keys: list, default=""):
    for k in keys:
        v = item.get(k)
        if v:
            return v
    return default


def _as_list(v) -> list:
    if not v:
        return []
    return v if isinstance(v, list) else [v]


def _video_id(v) -> str:
    """Fire 32: a source_videos entry is normally a bare video-id string, but some discovery
    pipelines (mine_feeds/gemini-video) store a full {id, url, title} dict instead. The old
    code did a blind str(v) on every entry, which turned those dicts into an unusable Python
    repr string (e.g. "{'id': 'abc123', 'url': ...}") — silently corrupting the id for 3,371
    elements (736 of them stubs) and permanently hiding their already-downloaded local
    transcript file (data/processed/<id>.json) from deep_retrieve.py's transcript pillar,
    since it looks up that path by the literal string. Extract the real id when the entry is
    a dict; fall back to the plain-string case unchanged."""
    if isinstance(v, dict):
        return str(v.get("id") or v.get("video_id") or v.get("url") or "").strip()
    return str(v).strip()


def _min_bar(el: dict) -> bool:
    """M1.C3 minimum enrichment+verification bar: real info + a real anchor.
    LINK-based elements (tool/skill/connector/model/design) anchor on a live link or a source
    video. TEXT elements (prompt/command/format) ARE their content — a system prompt has no
    website; its substantial body IS the anchor, and M1.C3 verifies text by schema+security,
    not liveness. Requiring an external link on text types silently discarded 424 already-
    PASSED prompts (all shown 'unverified' in the hub) — the content is the anchor here."""
    has_info = len(el.get("what", "")) >= STUB_CHARS or bool(el.get("body"))
    if el.get("type") in ("prompt", "command", "format"):
        return has_info
    anchored = bool(el.get("links", {}).get("website") or el.get("links", {}).get("github")
                    or el.get("source_videos") or el.get("links", {}).get("source_url"))
    return has_info and anchored


def _status(el: dict, ver: dict | None) -> tuple[str, dict]:
    """M1.3: verified | unverified | niche | dead. Dead ONLY on all-checks-failed."""
    v = ver or {}
    checks_failed = v.get("status") in ("dead", "fail") or (
        v.get("link_alive") is False and v.get("sandbox") in ("fail", None)
        and v.get("sources", 0) == 0)
    if v.get("status") == "dead" or (checks_failed and v.get("confirmed_dead")):
        return "dead", v
    passed = v.get("status") in ("pass", "verified") or v.get("link_alive") is True
    if passed and _min_bar(el):
        q = el.get("quality_score")
        return ("niche" if isinstance(q, (int, float)) and q <= 3 else "verified"), v
    return "unverified", v


def _content_provenance(raw: dict, el: dict) -> dict:
    """Did anything actually READ this element's source text?

    Deliberately separate from `verified`, which answers a narrower question — does the link
    resolve, did the package install in a sandbox. Neither of those checks the description,
    use-case or tips, and for almost the whole hub nothing does: src/analyze_batch.py
    regex-matches 89 hardcoded tool names (so it cannot see any tool nobody typed into that
    dict), then keeps any sentence containing the name, 20-180 chars, with one of ~11 verbs.
    That heuristic cannot separate a recommendation from a criticism — "Claude can't reliably
    do X" matches on "claude" and "can".

    Conflating the two is what let 668 elements wear a green "verified" badge over text that
    nothing had ever read. Source: src/content_provenance.py, which now only reports.
    """
    if raw.get("model_version"):
        return {"method": "model-read", "why": f"analyzed by {raw['model_version']}"}
    if raw.get("created_by") == "EXCAVA" or el.get("created_by") == "EXCAVA":
        return {"method": "authored", "why": "generated by EXCAVA with a model in the loop"}
    st = raw.get("source_type") or ""
    if st in ("web_news", "youtube", "linked_resource"):
        p = {"method": "pattern-matched",
             "why": f"{st}: keyword extraction (89-name dict + sentence heuristic), "
                    "no model read the source"}
        if (el.get("verified") or {}).get("status") == "verified":
            p["conflict"] = ("link/sandbox verified, but the description and tips were "
                             "pattern-matched — the green badge refers to the link, not this text")
        return p
    return {"method": "unknown", "why": "no provenance recorded by the miner that created it"}


def build() -> dict:
    """Normalize every per-type file into the unified index (read-only derivative)."""
    trust_map = _load("source_trust.json", {}).get("sources", {})
    conn_ver = _load("connectors_verified.json", {}).get("verified", {})
    el_ver = _load("elements_verified.json", {}).get("verified", {})
    overrides = _load("element_overrides.json", {}).get("overrides", {})
    related_map = _load("elements_related.json", {}).get("related", {})
    out, counts = [], {}
    for etype, (fname, key, m) in TYPES.items():
        items = _load(fname, {}).get(key, []) or []
        for it in items:
            if not isinstance(it, dict):
                continue
            name = str(_get(it, m["name"], "")).strip()
            if not name:
                continue
            slug = _get(it, m.get("slug", []), "") or _slug(name)
            eid = f"{etype}:{slug}"
            el = {
                "id": eid, "type": etype, "name": name,
                "what": str(_get(it, m.get("what", []), ""))[:600],
                "category": str(_get(it, m.get("cat", []), ""))[:60],
                "source_videos": [vid for vid in
                                  (_video_id(v) for v in _as_list(_get(it, m.get("videos", []), [])))
                                  if vid][:12],
                "links": {k: v for k, v in {
                    "website": _get(it, m.get("website", []), ""),
                    "github": _get(it, m.get("github", []), ""),
                    "source_url": _get(it, m.get("source_url", []), ""),
                }.items() if v},
                "install": str(_get(it, m.get("install", []), ""))[:200],
                "quality_score": _get(it, m.get("q", []), None) or it.get("quality_score"),
                "trust": trust_map.get("playlist", 95) if _as_list(_get(it, m.get("videos", []), []))
                         else trust_map.get("awesome-lists", 75),
                "created_by": "EXCAVA" if etype == "creation" else it.get("created_by", ""),
            }
            if _get(it, m.get("body", []), ""):
                el["body"] = str(_get(it, m.get("body", []), ""))[:1200]
            el.update(overrides.get(eid, {}))
            # join verification: connectors have their own sandbox store; everything else
            # joins elements_verified.json (built by src/verify_elements.py, M1.2)
            ver = conn_ver.get(name) if etype == "connector" else el_ver.get(eid)
            if etype == "connector" and ver:
                ver = {"status": "pass" if ver.get("status") == "pass" else
                       ("dead" if ver.get("status") == "fail" and ver.get("confirmed_dead") else ver.get("status")),
                       "link_alive": None, "at": ver.get("at"), "log": str(ver.get("log", ""))[:120],
                       "method": "sandbox", "sources": 1}
            status, v = _status(el, ver)
            el["verified"] = {"status": status, "method": (v or {}).get("method", ""),
                              "sources": (v or {}).get("sources", 0), "at": (v or {}).get("at", "")}
            el["stub"] = len(el.get("what", "")) < STUB_CHARS and not el.get("body")
            el["enriched"] = bool(el.get("enriched")) or (not el["stub"] and (v or {}).get("sources", 0) >= 2)
            el["related"] = related_map.get(eid, [])[:8]
            # CONTENT PROVENANCE (2026-08-10) — derived here, on purpose. The first version of
            # this shipped as a one-shot script that mutated elements_index.json directly, and
            # the away loop's next core-spoton rebuild wiped all 11,278 fields within the hour.
            # This file's own docstring says the index is derived and never edited by hand; I
            # ignored that and produced an orphaned increment, which is precisely what the plan
            # forbids. Deriving it inside build() is the only way it survives a rebuild.
            el["content_provenance"] = _content_provenance(it, el)
            out.append(el)
        counts[etype] = counts.get(etype, 0) + len([e for e in out if e["type"] == etype])
    idx = {"generated_at": _now(), "total": len(out), "counts": counts,
           "stubs": sum(1 for e in out if e["stub"]),
           "by_status": {s: sum(1 for e in out if e["verified"]["status"] == s)
                         for s in ("verified", "niche", "unverified", "dead")},
           "note": "READ-ONLY derivative. Sources of truth = the per-type files; write via element_model.set_field only.",
           "elements": out}
    INDEX.write_text(json.dumps(idx, ensure_ascii=False, indent=1), encoding="utf-8")
    return idx


def set_field(eid: str, field: str, value) -> bool:
    """The ONLY write path. Finds the owning per-type file and sets the field on the item;
    falls back to the overrides sidecar when the element has no natural slot (or its owner
    is regenerated by a CI lane). Rebuild the index afterwards to see the change."""
    etype, _, slug = eid.partition(":")
    spec = TYPES.get(etype)
    if spec:
        fname, key, m = spec
        d = _load(fname, {})
        items = d.get(key, []) or []
        for it in items:
            name = str(_get(it, m["name"], "")).strip()
            it_slug = _get(it, m.get("slug", []), "") or _slug(name)
            if it_slug == slug:
                it[field] = value
                (DATA / fname).write_text(json.dumps(d, ensure_ascii=False, indent=2),
                                          encoding="utf-8")
                return True
    ov = _load("element_overrides.json", {"overrides": {}})
    ov.setdefault("overrides", {}).setdefault(eid, {})[field] = value
    OVERRIDES.write_text(json.dumps(ov, ensure_ascii=False, indent=2), encoding="utf-8")
    return True


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", action="store_true")
    a = ap.parse_args()
    idx = build()
    print(f"elements_index: {idx['total']} elements; stubs {idx['stubs']}; by status {idx['by_status']}")
    if a.count:
        print("per type:", ", ".join(f"{k}={v}" for k, v in idx["counts"].items()))
        sample = next(e for e in idx["elements"] if e["type"] == "tool")
        print("sample:", json.dumps(sample, ensure_ascii=False)[:400])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
