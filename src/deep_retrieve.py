"""
src/deep_retrieve.py — M1.C1: RETRIEVAL DEPTH, the #1 accuracy fix (EXCAVA v2).

The owner's verdict: elements are too thin — things get missed from the playlist or never
found online. This lane walks every STUB element (what < 80 chars / no body) and rebuilds it
from FULL sources:
  1. the element's source videos' FULL transcripts (data/processed/<vid>.json — real
     transcripts recovered by the residential drain),
  2. its GitHub README (raw.githubusercontent, keyless),
  3. its homepage <title>/<meta description> (keyless),
then (in CI, where the free-engine keys live) asks a free LLM to fuse them into an accurate
2-3 sentence description. Keyless enrichment still upgrades stubs when no engine is present
(README/meta text), so the lane always makes progress.

Every enrichment records its SOURCES (video / readme / homepage / llm-fused) — the M1.C3
">=2 independent sources" evidence — into data/element_overrides.json (sidecar; the owner
files get only the improved description text itself).

Run: python -m src.deep_retrieve --limit 40 [--dry-run]
Progress cursor in data/deep_retrieve_state.json; the elements_index rebuild picks results up.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from src import element_model as em

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
STATE = DATA / "deep_retrieve_state.json"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
# which owning field carries the description per type (the real content fix)
DESC_FIELD = {"skill": "description", "tool": "description", "prompt": "notes",
              "command": "description", "connector": "what_it_does", "design": "look",
              "format": "description", "model": "description", "creation": "what"}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _get(url: str, timeout: int = 20) -> str:
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read(400_000).decode("utf-8", errors="replace")
    except Exception:
        return ""


def transcript_excerpt(el: dict, chars: int = 6000) -> str:
    """Full-source pillar 1: the element's source videos' real transcripts."""
    out = []
    for vid in el.get("source_videos", [])[:3]:
        try:
            rec = json.load(open(DATA / "processed" / f"{vid}.json", encoding="utf-8"))
        except Exception:
            continue
        t = rec.get("transcript", "")
        if t and rec.get("transcript_source") == "transcript":
            name = el["name"].lower()
            pos = t.lower().find(name.split()[0][:12])
            start = max(0, pos - 800) if pos > -1 else 0
            out.append(f"[video {vid} · {rec.get('title', '')}]\n{t[start:start + chars // 3]}")
        elif rec.get("description"):
            out.append(f"[video {vid} description]\n{rec['description'][:800]}")
    return "\n\n".join(out)[:chars]


def readme_excerpt(el: dict, chars: int = 3000) -> str:
    """Full-source pillar 2: the repo's own README (keyless)."""
    gh = el.get("links", {}).get("github", "") or (
        el.get("links", {}).get("website", "") if "github.com" in el.get("links", {}).get("website", "") else "")
    m = re.search(r"github\.com/([\w.\-]+)/([\w.\-]+)", gh)
    if not m:
        return ""
    owner, repo = m.group(1), m.group(2).removesuffix(".git")
    for branch in ("HEAD",):
        raw = _get(f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/README.md")
        if raw and not raw.startswith("404"):
            raw = re.sub(r"!\[[^\]]*\]\([^)]*\)|<[^>]+>|\[!\[.*?\)\]", " ", raw)   # strip badges/html
            raw = re.sub(r"\n{3,}", "\n\n", raw).strip()
            return raw[:chars]
    return ""


def homepage_meta(el: dict) -> str:
    """Full-source pillar 3: the homepage's own title + meta description (keyless)."""
    url = el.get("links", {}).get("website", "")
    if not url or "github.com" in url:
        return ""
    html = _get(url, timeout=15)[:60_000]
    title = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
    desc = re.search(r'<meta[^>]+(?:name="description"|property="og:description")[^>]+content="([^"]{20,400})"', html, re.I)
    bits = [x.group(1).strip() for x in (title, desc) if x]
    return re.sub(r"\s+", " ", " · ".join(bits))[:500]


def _llm_fuse(el: dict, sources: dict) -> str:
    """CI-only polish: a free engine fuses the raw sources into 2-3 accurate sentences.
    Skips gracefully with no keys (keyless enrichment already improved the element)."""
    keys = [os.environ.get(k, "").strip() for k in
            ["EXTERNAL_REVIEW_API_KEY", "GEMINI_API_KEY", "GEMINI_API_KEY_2", "GEMINI_API_KEY_3"]]
    keys = [k for k in keys if k]
    groq = os.environ.get("GROQ_API_KEY", "").strip()
    if not keys and not groq:
        return ""
    material = "\n\n".join(f"### {k}\n{v}" for k, v in sources.items() if v)[:9000]
    prompt = (f"You are enriching a catalog entry. Element: {el['name']} (type: {el['type']}).\n"
              f"Current description: {el.get('what', '(none)')}\n\nRaw source material:\n{material}\n\n"
              "Write an ACCURATE, specific 2-3 sentence description of what this is and what it does, "
              "grounded ONLY in the material above. No hype, no invented facts. Reply with the "
              "description text only.")
    try:
        from src.bulk_analyze import call_gemini, call_openai_compatible
        if groq:
            r = call_openai_compatible("https://api.groq.com/openai/v1", groq,
                                       "llama-3.3-70b-versatile", prompt, 40)
        else:
            r = call_gemini(keys[0], "gemini-2.0-flash", prompt, 40)
        text = r if isinstance(r, str) else (r.get("text") or r.get("content") or "")
        text = re.sub(r"\s+", " ", str(text)).strip()
        return text[:600] if 60 < len(text) < 900 else ""
    except Exception:
        return ""


def enrich(el: dict, dry: bool = False) -> dict | None:
    """One element: gather full sources -> best new description -> write back + evidence."""
    sources = {}
    t = transcript_excerpt(el)
    if t:
        sources["full-transcript"] = t
    r = readme_excerpt(el)
    if r:
        sources["github-readme"] = r
    h = homepage_meta(el)
    if h:
        sources["homepage-meta"] = h
    if not sources:
        return None                      # nothing recoverable (yet) — discovery may find more
    fused = _llm_fuse(el, sources)
    if fused:
        new_what, method = fused, "llm-fused"
    else:                                # keyless fallback: best raw source beats a stub
        raw = (r or h or t)
        first = re.split(r"(?<=[.!?])\s+", re.sub(r"[#*`\[\]]", "", raw).strip())
        new_what = " ".join(first[:3])[:500]
        method = "keyless-extract"
    if len(new_what) < 60 or len(new_what) <= len(el.get("what", "")):
        new_what = None                  # don't downgrade an already-decent description
    evidence = {"sources": sorted(sources.keys()), "n_sources": len(sources),
                "method": method, "at": _now()}
    if not dry:
        if new_what:
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
    ap.add_argument("--limit", type=int, default=40)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    idx = em.build()
    todo = sorted((e for e in idx["elements"] if e.get("stub") or not e.get("enriched")),
                  key=lambda e: (not e.get("stub"), e["id"]))   # worst-first: stubs lead
    st = em._load("deep_retrieve_state.json", {"cursor": 0})
    start = st.get("cursor", 0) % max(len(todo), 1)
    batch = todo[start:start + a.limit]
    done = upgraded = 0
    for el in batch:
        r = enrich(el, a.dry_run)
        if r:
            done += 1
            upgraded += r["new"]
    st["cursor"] = start + len(batch)
    st["todo_at_last_run"] = len(todo)
    st["updated_at"] = _now()
    STATE.write_text(json.dumps(st, ensure_ascii=False, indent=2), encoding="utf-8")
    if not a.dry_run:
        idx2 = em.build()
        print(f"deep-retrieve: batch {start}..{start + len(batch)} of {len(todo)} thin elements; "
              f"{done} enriched ({upgraded} descriptions upgraded); stubs now {idx2['stubs']}")
    else:
        print(f"[dry] would process {len(batch)} of {len(todo)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
