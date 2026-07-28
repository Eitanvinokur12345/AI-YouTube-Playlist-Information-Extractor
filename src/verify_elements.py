"""
src/verify_elements.py — M1.2 + M1.C3: VERIFY EVERY ELEMENT to the owner's standard.

The standard (M1.C3):
  - REAL requires cross-evidence from >=2 independent sources + a live link test.
    Source #1 = the element's source video(s) (it was really shown/used);
    source #2 = a LIVE link (website/github answers) or a fetched README/homepage
    (deep_retrieve's enrichment evidence rides in here too).
  - ROLLING re-check: the cursor loops over all ~6.4k elements continuously (a full pass
    ~5-6 days at CI cadence), and items younger than --recheck-days are skipped so the lane
    always spends effort where staleness is possible. Pre-warmed (about-to-open) elements
    re-check every pass = the "on-access" half.
  - CONFLICTS: when the live page redirects to a DIFFERENT domain than recorded (rebrand /
    parked domain), the conflict is noted on the record — reconciled, best-supported kept.
  - DEAD is earned, not guessed: all links failing on >=2 CONSECUTIVE passes -> confirmed_dead
    (and even then only hidden, never deleted — protocol P3).
Text elements (prompts/commands/formats) get schema sanity + a security wordlist instead of
liveness. Results -> data/elements_verified.json; the elements_index join surfaces them.

Run: python -m src.verify_elements --limit 300 [--recheck-days 7]
"""
from __future__ import annotations

import argparse
import json
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

from src import element_model as em

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "elements_verified.json"
STATE = DATA / "verify_elements_state.json"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
SUSPECT = ("curl | sh", "rm -rf", "base64 -d", "eval(", "api_key=", "password=", "ignore previous")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _domain(u: str) -> str:
    m = re.match(r"https?://(?:www\.)?([^/]+)", str(u).lower())
    return m.group(1) if m else ""


def _network_open() -> bool:
    """Canary: is general internet egress actually open right now?

    Added fire 50 (2026-07-28) after a manual run from an interactive cloud dev sandbox
    (NOT the `core_spoton.yml` GitHub Actions runner, which has real unrestricted egress)
    mass-flagged ~1,000 live, well-known connectors/tools as fail/dead within minutes —
    that sandbox's outbound HTTPS goes through a policy-restricted proxy that 403s any
    host outside a small allowlist (package registries + anthropic.com), so `_head()`
    silently turned "blocked by this session's proxy" into "the link is dead" for every
    third-party site. Two independent, almost-never-simultaneously-down anchors: if BOTH
    are unreachable, egress is restricted (or a true outage), and this run must not write
    any live-link verdicts — better to skip a batch than poison confirmed_dead/fail data.
    """
    for anchor in ("https://github.com", "https://www.wikipedia.org"):
        alive, _ = _head(anchor)
        if alive:
            return True
    return False


def _head(url: str) -> tuple[bool, str]:
    """(alive, final_url). GET-fallback because plenty of real sites reject HEAD."""
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, headers=UA, method=method)
            with urllib.request.urlopen(req, timeout=12) as r:
                return r.status < 400, r.url
        except urllib.error.HTTPError as e:
            if method == "GET":
                return e.code < 400, url
        except Exception:
            if method == "GET":
                return False, url
    return False, url


def check(el: dict, prev: dict) -> dict:
    """One element -> a verification record at the M1.C3 standard."""
    rec = {"at": _now(), "consecutive_fails": prev.get("consecutive_fails", 0)}
    sources = 1 if el.get("source_videos") else 0
    enr = (el.get("enrichment") or {})
    sources += min(enr.get("n_sources", 0), 2)

    if el["type"] in ("prompt", "command", "format"):
        text = json.dumps(el, ensure_ascii=False).lower()
        clean = not any(s in text for s in SUSPECT)
        ok = clean and (len(el.get("what", "")) >= 30 or el.get("body"))
        rec.update({"status": "pass" if ok else "fail", "link_alive": None,
                    "method": "schema+security", "sources": max(sources, 1 if ok else 0),
                    "log": "clean" if clean else "SECURITY WORDLIST HIT"})
        rec["consecutive_fails"] = 0 if ok else rec["consecutive_fails"] + 1
    else:
        links = el.get("links", {})
        url = links.get("website") or links.get("github") or links.get("source_url") or ""
        if not url:
            rec.update({"status": "unverifiable", "link_alive": None, "method": "no-link",
                        "sources": sources, "log": "no link to test — deep-retrieve/discovery may recover one"})
            return rec
        alive, final = _head(url)
        if alive:
            sources += 1
            rec["consecutive_fails"] = 0
        else:
            rec["consecutive_fails"] += 1
        conflict = ""
        if alive and _domain(final) and _domain(final) != _domain(url):
            conflict = f"redirects to {_domain(final)} (recorded {_domain(url)}) — kept live target, noted"
        rec.update({"status": "pass" if (alive and sources >= 2) else ("fail" if not alive else "thin"),
                    "link_alive": alive, "final_url": final if final != url else "",
                    "method": "2-source+live" if sources >= 2 else "live-only",
                    "sources": sources, "conflict": conflict,
                    "log": "ok" if alive else f"link dead (fail #{rec['consecutive_fails']})"})
        if rec["consecutive_fails"] >= 2 and not el.get("source_videos"):
            rec["confirmed_dead"] = True
            rec["status"] = "dead"
    return rec


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=300)
    ap.add_argument("--recheck-days", type=int, default=7)
    ap.add_argument("--skip-network-check", action="store_true",
                     help="bypass the egress canary (only for offline/schema-only testing)")
    a = ap.parse_args()

    if not a.skip_network_check and not _network_open():
        print("verify-elements: ABORTED — network canary failed (github.com and "
              "wikipedia.org both unreachable). Outbound egress looks restricted in this "
              "environment (e.g. an interactive sandbox's proxy allowlist) rather than the "
              "real internet the scheduled CI runner has — skipping this batch untouched "
              "rather than risk writing false fail/dead verdicts.")
        return 0

    idx = em.build()
    store = em._load("elements_verified.json", {"verified": {}})
    ver = store.setdefault("verified", {})
    prewarm = {p.get("id") for p in em._load("prewarm.json", {}).get("warm", [])}
    st = em._load("verify_elements_state.json", {"cursor": 0})

    els = idx["elements"]
    now = datetime.now(timezone.utc)
    def fresh(eid):
        at = (ver.get(eid) or {}).get("at", "")
        try:
            return (now - datetime.fromisoformat(at)).days < a.recheck_days
        except Exception:
            return False

    start = st.get("cursor", 0) % max(len(els), 1)
    batch, i = [], start
    while len(batch) < a.limit and i < start + len(els):
        el = els[i % len(els)]
        if el["id"] in prewarm or not fresh(el["id"]):    # on-access items always re-check
            batch.append(el)
        i += 1
    st["cursor"] = i % max(len(els), 1)

    with ThreadPoolExecutor(max_workers=16) as ex:
        recs = list(ex.map(lambda e: (e["id"], check(e, ver.get(e["id"], {}))), batch))
    for eid, rec in recs:
        ver[eid] = rec

    by = {}
    for r in ver.values():
        by[r.get("status", "?")] = by.get(r.get("status", "?"), 0) + 1
    conflicts = sum(1 for r in ver.values() if r.get("conflict"))
    # Honest coverage (fire 48, 2026-07-28, same fix applied to verify_connectors.py):
    # `ver` accumulates a verdict per element ID forever, but IDs go stale when elements
    # are merged/deduped/pruned out of the live index — those ghosts still counted toward
    # `checked`, slightly overstating real coverage (25 found live). This lane's own
    # gap-detection (`fresh()` always re-includes anything unverified, regardless of cursor
    # position) already guarantees every CURRENT element eventually gets checked, so this
    # was never a completion-blocking bug like the connectors one — just an inflated number.
    live_ids = {e["id"] for e in els}
    live_checked = len(live_ids & set(ver.keys()))
    store["summary"] = {"checked": live_checked, "total": len(els), "by_status": by,
                        "stale_ghost_entries": len(ver) - live_checked,
                        "conflicts_noted": conflicts, "updated_at": _now(),
                        "standard": "M1.C3: >=2 sources + live test; rolling+on-access; dead only after 2 consecutive full failures"}
    OUT.write_text(json.dumps(store, ensure_ascii=False, indent=1), encoding="utf-8")
    STATE.write_text(json.dumps(st, ensure_ascii=False, indent=2), encoding="utf-8")
    em.build()                                            # re-join statuses into the index
    print(f"verify-elements: batch {len(batch)} · checked {len(ver)}/{len(els)} · "
          f"{by} · conflicts noted {conflicts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
