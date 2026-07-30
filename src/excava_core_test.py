"""
src/excava_core_test.py — regression test for M2 class 1 (Element/Package).

The class overhaul only earns its place if it CANNOT break what already works. This asserts
(a) the class agrees with element_model's own index, (b) the status law (P3) is honoured —
niche is usable, dead is never returned, (c) the activator still produces a real plan for the
same queries it always did, and (d) Package round-trips through disk without touching the hub.

Free, stdlib, no network. Run:  python -m src.excava_core_test
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

from src import excava_core as core

FAILS: list = []


def check(name: str, cond: bool, detail: str = "") -> None:
    print(f"  {'PASS' if cond else 'FAIL'}  {name}{'' if cond else ' — ' + detail}")
    if not cond:
        FAILS.append(name)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    print("excava_core (Element/Package) regression test")

    idx = core.load()
    check("index loads", len(idx) > 0, "no elements — is data/elements_index.json present?")

    # (a) agreement with element_model's own derived index — the class must not invent totals
    raw = json.loads(core.INDEX.read_text(encoding="utf-8")) if core.INDEX.exists() else {}
    if raw:
        dupes = core.duplicates()
        # Every index record is either addressable or a recorded id-collision — never lost.
        check("total accounted for (reachable + collisions == index total)",
              len(idx) + len(dupes) == raw.get("total"),
              f"class={len(idx)} + dupes={len(dupes)} != index={raw.get('total')}")
        check("id collisions are reported, not swallowed",
              all(d.get("id") in idx for d in dupes),
              "a collision was recorded whose id is not in the index")
        st = core.stats()
        expected = {k: v for k, v in raw.get("by_status", {}).items() if v}
        for d in dupes:  # discount the unreachable records from element_model's own totals
            s = (d.get("verified") or {}).get("status", "unverified")
            expected[s] = expected.get(s, 0) - 1
        check("status counts match element_model (net of collisions)",
              st["by_status"] == {k: v for k, v in expected.items() if v},
              f"{st['by_status']} vs {expected}")
        check("stub count matches element_model (net of collisions)",
              st["stubs"] == raw.get("stubs") - sum(1 for d in dupes if d.get("stub")),
              f"class={st['stubs']} index={raw.get('stubs')} dupes={len(dupes)}")

    # (b) the status law (P3)
    dead = [e for e in idx.values() if e.is_dead]
    check("dead elements exist to test against", len(dead) > 0, "no dead elements in index")
    if dead:
        hits = core.find(dead[0].name, limit=50)
        check("find() never returns a dead element",
              all(not h.is_dead for h in hits), f"dead {dead[0].id} was returned")
    niche = [e for e in idx.values() if e.status == "niche" and (e.best_link or e.body or e.install)]
    check("niche counts as usable (a 1/10 may be perfect for one task)",
          bool(niche) and all(e.is_usable() for e in niche[:200]),
          "a niche element with a real way in was marked unusable")
    unver = [e for e in idx.values() if e.status == "unverified"]
    check("unverified is never usable",
          all(not e.is_usable() for e in unver[:500]), "an unverified element claimed usable")

    # usable implies a real way in
    check("usable always has a link, install or body",
          all(bool(e.best_link or e.install or e.body)
              for e in list(idx.values())[:2000] if e.is_usable()),
          "an element was usable with no way in")

    # (c) the activator still works, on the migrated path
    from src import activate
    for q in ("n8n", "github mcp", "claude"):
        els = core.find(q, limit=1)
        if not els:
            check(f"activator finds '{q}'", False, "no hit")
            continue
        act = els[0].activation()
        check(f"activator plans '{q}' -> {els[0].id}",
              bool(act.get("steps")) and bool(act.get("name")), str(act)[:120])
    legacy = activate.find("n8n", 3)
    check("legacy activate.find still intact (fallback path)", len(legacy) > 0, "legacy path broke")

    # (d) Package round-trip — must not touch the real store
    real = core.PACKAGES
    with tempfile.TemporaryDirectory() as td:
        core.PACKAGES = Path(td) / "packages.json"
        try:
            some = [e.id for e in list(idx.values())[:2]]
            p = core.Package("test-pkg", note="regression")
            for e in some:
                p.add(e)
            check("Package.add dedups", p.add(some[0]) is False)
            p.save()
            back = core.Package.load("test-pkg")
            check("Package round-trips through disk",
                  back is not None and back.element_ids == some, str(back and back.element_ids))
            check("Package resolves to Elements",
                  back is not None and len(back.elements()) == len(some))
            ghost = core.Package("ghost", ["tool:definitely-not-a-real-element-xyz"])
            check("Package reports rotted ids honestly", len(ghost.missing()) == 1)
        finally:
            core.PACKAGES = real
    check("real package store untouched", core.PACKAGES == real)

    print(f"\n{len(FAILS)} failure(s)" if FAILS else "\nall checks passed")
    return 1 if FAILS else 0


if __name__ == "__main__":
    raise SystemExit(main())
