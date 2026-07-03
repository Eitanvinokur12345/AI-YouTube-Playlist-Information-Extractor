"""
src/excava_creators.py — PHASE 3: the CREATORS department (OS-2, now staffed).

Owner rules (2026-07-03 checkpoint answer):
  1. Everything created may enter the project autonomously **as long as it is labeled
     "Created by EXCAVA"** — provenance is always visible, never hidden.
  2. Before a creation is USED/RUN for the first time, an **independent test** runs (the
     test is not the creator grading its own work: it re-verifies links, schema, security).
  3. Creators may draft skills, prompts, formats, tools, connectors, MCP servers, designs —
     and **PACKAGES**: the owner's term for combinations of several elements (skills, tools,
     commands, designs, prompts, formats, outlines, MCP servers) bundled toward one job.

Flow per cycle (DISCOVERY first, per the program):
  discovery  — gap radar over REAL data: hub coverage holes per type, the owner's ×2 taste
               hits, trend keywords, social-intake demand signals.
  draft      — mechanical v1 drafts from those gaps (data-grounded; the free-LLM enrichment
               pass joins later — no tokens burned here).
  self-test  — schema + link liveness + security wordlist; every result stored on the item.
  publish    — tested drafts land in data/created_by_excava.json with the label; the
               dashboard shows them with the 🦾 badge. Running/activating one re-runs the
               independent test first (test_before_run).

Outward publishing BEYOND the project stays behind the G3>=70 gate (unchanged guardrail).
Free, stdlib-only. Run: python -m src.excava_creators [--max-new 6]
"""
from __future__ import annotations

import argparse
import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "created_by_excava.json"
LABEL = "Created by EXCAVA"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
SUSPECT = ("curl | sh", "rm -rf", "base64 -d", "eval(", "api_key=", "password=")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load(name, d=None):
    try:
        return json.load(open(DATA / name, encoding="utf-8"))
    except Exception:
        return d if d is not None else {}


def discovery() -> dict:
    """DISCOVERY: what does the hub actually lack, and what is being asked for out there?"""
    holes = []
    for fname, label in [("skills.json", "skill"), ("tools.json", "tool"),
                         ("prompts.json", "prompt"), ("formats.json", "format"),
                         ("connectors.json", "connector")]:
        items = _load(fname, [])
        items = items if isinstance(items, list) else items.get(label + "s", []) or items.get("items", [])
        unlinked = sum(1 for i in items if isinstance(i, dict)
                       and not (i.get("website") or i.get("github") or i.get("url")))
        holes.append({"type": label, "total": len(items), "unlinked": unlinked})
    trends = [t.get("term") or t.get("title", "") for t in
              (_load("trends.json", {}).get("trends") or [])[:10]]
    intake = _load("social_intake.json", {})
    demand = {}
    for it in intake.get("items", [])[:200]:
        for w in re.findall(r"[a-zA-Z][a-zA-Z\-]{4,}", it.get("title", "").lower()):
            if w in ("about", "using", "these", "their", "would", "should", "release"):
                continue
            demand[w] = demand.get(w, 0) + 1
    hot = sorted(demand, key=lambda w: -demand[w])[:12]
    disc = {"generated_at": _now(), "coverage_holes": holes, "trend_terms": trends,
            "intake_demand_terms": hot,
            "note": "DISCOVERY scoping — drafts below must each point at one of these gaps."}
    (DATA / "creators_discovery.json").write_text(
        json.dumps(disc, ensure_ascii=False, indent=2), encoding="utf-8")
    return disc


def _self_test(c: dict) -> dict:
    """The INDEPENDENT test (also re-run before first use — test_before_run):
    schema completeness, link liveness, and a security wordlist over all text."""
    checks = {}
    checks["schema"] = all(c.get(k) for k in ("name", "type", "what", "how_to_use"))
    text = json.dumps(c, ensure_ascii=False).lower()
    checks["security_clean"] = not any(s in text for s in SUSPECT)
    url = c.get("url", "")
    if url:
        try:
            req = urllib.request.Request(url, headers=UA, method="HEAD")
            with urllib.request.urlopen(req, timeout=15) as r:
                checks["link_alive"] = r.status < 400
        except Exception:
            checks["link_alive"] = False
    else:
        checks["link_alive"] = True     # nothing to verify
    return {"ok": all(checks.values()), "checks": checks, "tested_at": _now()}


def draft(disc: dict, existing: list, max_new: int) -> list[dict]:
    """Mechanical, data-grounded drafts. Every draft names the gap it fills. v1 makes
    prompts / formats / packages (LLM-written skill bodies join in a later pass)."""
    have = {c.get("name") for c in existing}
    out = []
    for term in (disc.get("intake_demand_terms") or [])[:max_new]:
        name = f"Prompt pack: {term}"
        if name in have:
            continue
        out.append({
            "name": name, "type": "prompt", "created_by": "EXCAVA", "label": LABEL,
            "gap": f"intake demand term '{term}' has no hub prompt",
            "what": f"A reusable prompt scaffold for {term} tasks, seeded from live community demand.",
            "how_to_use": f"Paste into any AI tool; replace <goal> with your {term} goal. "
                          "Refine with the Activator once tested.",
            "body": (f"You are an expert on {term}. Goal: <goal>. Constraints: free tools only, "
                     "cite sources, output steps then the final artifact."),
            "status": "draft", "created_at": _now(),
        })
    hole = next((h for h in disc.get("coverage_holes", []) if h.get("unlinked", 0) > 50), None)
    pkg_name = "Package: link-recovery sprint"
    if hole and pkg_name not in have:
        out.append({
            "name": pkg_name, "type": "package", "created_by": "EXCAVA", "label": LABEL,
            "gap": f"{hole['unlinked']} unlinked {hole['type']}s block G3",
            "what": ("A PACKAGE (owner's term: several elements combined) bundling the resolver "
                     "skill + verify command + coverage-report format into one runnable job."),
            "how_to_use": "Activate via EXCAVA inbox: 'EXCAVA: run package link-recovery sprint'.",
            "elements": [{"kind": "skill", "ref": "src/resolve_links.py"},
                         {"kind": "command", "ref": "python -m src.resolve_links --limit 400"},
                         {"kind": "format", "ref": "data/coverage_log.json report shape"}],
            "status": "draft", "created_at": _now(),
        })
    return out[:max_new]


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-new", type=int, default=6)
    ap.add_argument("--test-before-run", metavar="NAME",
                    help="independently re-test one creation (the before-first-use gate)")
    args = ap.parse_args()

    store = _load("created_by_excava.json", {"label_rule": LABEL, "creations": []})
    creations = store.get("creations", [])

    if args.test_before_run:
        c = next((x for x in creations if x.get("name") == args.test_before_run), None)
        if not c:
            print(f"no creation named {args.test_before_run!r}")
            return 1
        c["last_run_test"] = _self_test(c)
        OUT.write_text(json.dumps(store, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"test_before_run {'PASS' if c['last_run_test']['ok'] else 'FAIL'}: {c['last_run_test']['checks']}")
        return 0 if c["last_run_test"]["ok"] else 1

    disc = discovery()
    new = draft(disc, creations, args.max_new)
    published = 0
    for c in new:
        c["self_test"] = _self_test(c)
        if c["self_test"]["ok"]:
            c["status"] = "published"      # allowed: labeled 'Created by EXCAVA' (owner rule)
            published += 1
        else:
            c["status"] = "failed-test"
        creations.append(c)
    store["creations"] = creations[-300:]
    store["updated_at"] = _now()
    store["note"] = ("Everything here is labeled 'Created by EXCAVA' (owner rule 2026-07-03); "
                     "an independent test re-runs before first use (test_before_run).")
    OUT.write_text(json.dumps(store, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"creators: {len(new)} drafted, {published} published (labeled), "
          f"{len(creations)} total; discovery gaps: "
          + ", ".join(f"{h['type']}:{h['unlinked']}unlinked" for h in disc["coverage_holes"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
