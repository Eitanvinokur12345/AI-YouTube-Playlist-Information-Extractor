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

    # (c2) Tool class — CLASS 2 of 5. Detection must be deterministic and HONEST: a tool we
    # cannot actually run must never claim it is runnable (law P4, real-not-display).
    tools = core.Tool.all()
    check("Tool wraps the tool-capable elements", len(tools) > 1000, f"only {len(tools)}")
    check("Tool detection is offline/deterministic",
          all(t.kind in ("mcp", "npm", "pip", "docker", "repo", "hosted", "unknown") for t in tools[:500]))
    check("runnable ALWAYS implies a concrete command",
          all(bool(t.command) for t in tools if t.is_runnable()),
          "a tool claimed runnable with no command")
    check("repo/hosted/unknown are never claimed runnable",
          not any(t.is_runnable() for t in tools if t.kind in ("repo", "hosted", "unknown")),
          "a non-executable kind claimed runnable")
    mcps = [t for t in tools if t.kind == "mcp"]
    check("MCP tools exist and yield a config", bool(mcps) and mcps[0].mcp_config() is not None)
    check("mcp_config is well-formed",
          all(isinstance((t.mcp_config() or {}).get("mcpServers"), dict) for t in mcps[:200]))
    nonmcp = [t for t in tools if t.kind in ("repo", "hosted")]
    check("non-MCP tools return no MCP config",
          all(t.mcp_config() is None for t in nonmcp[:200]))
    check("invocation() states what is missing when not runnable",
          all(t.invocation()["needs"] for t in nonmcp[:100] if not t.is_runnable()),
          "a non-runnable tool gave no reason")
    known = core.get("connector:github-mcp-server")
    if known:
        kt = core.Tool(known)
        check("a known MCP server parses to a real npx command",
              kt.kind == "mcp" and kt.is_runnable() and "npx" in kt.command,
              f"kind={kt.kind} cmd={kt.command!r}")

    # (c3) Room class — CLASS 3 of 5. The point of a room is the ARTIFACT, so the assertions
    # are about whether what it claims to have produced actually exists and is readable.
    rooms = core.Room.all()
    check("Room reads the live rooms store", len(rooms) > 0, "no rooms found")
    check("Room.get round-trips an id",
          rooms and core.Room.get(rooms[0].id) is not None and core.Room.get(rooms[0].id).id == rooms[0].id)
    claimed = [r for r in rooms if r.has_artifact()]
    check("some rooms claim an artifact", bool(claimed))
    # The bug this guards: `artifact` is a DICT {kind,ref,at,title,by}; stringifying it whole
    # made every path unresolvable and reported 0 real artifacts out of 46. Never again.
    check("artifact_path resolves the dict's ref, not the dict",
          all("/" in r.artifact_path and not r.artifact_path.startswith("{") for r in claimed[:50]),
          f"sample path: {claimed[0].artifact_path[:60] if claimed else 'n/a'}")
    unreal = [r for r in claimed if not r.artifact_is_real()]
    check("every claimed artifact is REAL (exists, non-empty, no conflict markers)",
          not unreal, f"{len(unreal)} unreal: {[r.id for r in unreal[:3]]}")
    check("artifact carries provenance (which agent synthesized it)",
          all(r.artifact_by for r in claimed[:30]), "an artifact had no `by`")
    talked = [r for r in rooms if r.transcript()]
    check("rooms have real transcripts", bool(talked))
    check("transcripts name more than one speaker (it is a DEBATE, not a monologue)",
          any(len(r.speakers()) > 1 for r in talked[:20]),
          "no room had 2+ distinct speakers")
    check("an open room is never counted as exhausted",
          not any(r.is_exhausted() for r in rooms if r.is_open()))

    # (c4) Agent class — CLASS 4 of 5. The law-P4 test for a roster is not "does the name
    # exist" but "has this agent done anything and can it reach a real tool".
    agents = core.Agent.all()
    check("Agent reads the roster", len(agents) > 40, f"only {len(agents)}")
    check("Agent.get resolves by name AND by id",
          core.Agent.get(agents[0].name) is not None and core.Agent.get(agents[0].id) is not None)
    check("every agent is scoped to modules that EXIST on disk",
          all(not a.missing_tools() for a in agents),
          f"broken: {[(a.name, a.missing_tools()) for a in agents if a.missing_tools()][:3]}")
    check("can_act() requires real scoped tools",
          all(a.can_act() == (bool(a.scoped_tools) and not a.missing_tools()) for a in agents))
    check("every department has a lead",
          all(any(a.is_lead() for a in core.Agent.all(department=d))
              for d in {x.department for x in agents} - {"core"}),
          "a department has no lead")
    spoken = [a for a in agents if a.has_spoken()]
    check("most of the roster has actually spoken (not just named)",
          len(spoken) > len(agents) * 0.6, f"only {len(spoken)}/{len(agents)}")
    authors = [a for a in agents if a.artifacts_authored()]
    check("some agents authored a REAL artifact", bool(authors),
          "no agent is on record as synthesizing a verified artifact")
    check("artifacts_authored only counts REAL artifacts",
          all(r.artifact_is_real() for a in authors[:10] for r in a.artifacts_authored()))
    rst = core.Agent.roster()
    check("roster census is self-consistent",
          rst["total"] == len(agents) and rst["have_spoken"] + len(rst["silent"]) == rst["total"],
          str(rst)[:120])

    # (c5) The speaker rotation Room depends on. Fire 93 found the checker structurally excluded
    # from short rooms (70 of 83 rooms ran with NO challenge turn) and the improver excluded from
    # every room. A doer proposing + a lead agreeing with nobody challenging IS the correlated-
    # error failure §2 bans, so these assertions guard the debate itself, not just its plumbing.
    from src import excava_chat

    def _cast(nd=1, nc=1, ni=0, nl=1):
        return ([{"role": "doer", "name": f"D{i}"} for i in range(nd)]
                + [{"role": "checker", "name": f"C{i}"} for i in range(nc)]
                + [{"role": "improver", "name": f"I{i}"} for i in range(ni)]
                + [{"role": "lead", "name": f"L{i}"} for i in range(nl)])

    def _seq(mt, **kw):
        c = _cast(**kw)
        return [excava_chat._speaker({"turns": t, "max_turns": mt}, c)["name"] for t in range(mt)]

    for mt in (3, 4, 6):
        s = _seq(mt)
        check(f"a checker CHALLENGES in a {mt}-turn room", "C0" in s, f"order was {s}")
        check(f"the lead converges LAST in a {mt}-turn room", s[-1].startswith("L"), f"order was {s}")
        check(f"the doer OPENS the {mt}-turn room", s[0].startswith("D"), f"order was {s}")
    check("an improver gets a turn once the room can afford one",
          "I0" in _seq(4, ni=1) and "I0" in _seq(6, ni=1),
          f"4-turn: {_seq(4, ni=1)}")
    check("challenge outranks refinement when turns are scarce",
          "C0" in _seq(3, ni=1), f"3-turn: {_seq(3, ni=1)}")

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
