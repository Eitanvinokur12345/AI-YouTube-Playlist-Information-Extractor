"""
src/standing_checks.py — ONE command for the start-of-fire ritual (owner law, 2026-07-26).

Fires 6, 7, and 8 (AWAY_LOG.md) each independently hand-diagnosed the same handful of
symptoms at the top of a session: is the locally cached `origin/main` ref actually stale
(risk of a "day of work" scare that a real fetch would clear in one shot), is upstream
tracking configured on this branch, and are the guardrails still green. Fire 8 queued a
dedicated entrypoint for this twice without building it ("next fire should build it instead
of re-diagnosing by hand a third time") — this module is that entrypoint. Run it FIRST,
before any other work, and read the verdict instead of re-deriving it.

Run:  python -m src.standing_checks           # print + write data/standing_checks.json
      python -m src.standing_checks --strict  # exit 1 if anything needs attention
"""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from src import git_safe, guardrails, loop_contract, net_canary

ROOT = Path(__file__).parent.parent
OUT = ROOT / "data" / "standing_checks.json"


def _git(args):
    r = subprocess.run(["git", *args], cwd=str(ROOT), text=True, capture_output=True)
    return (r.stdout or "").strip()


def check_remote() -> dict:
    """Snapshot the cached origin/main ref, force a real fetch, snapshot again. A mismatch
    before/after is the exact "is a day of work actually at risk?" question fire 8 spent time
    ruling out by hand — this answers it in one call instead of a manual rev-parse + fetch +
    rev-parse + eyeball-the-diff each time.

    Fire 83: compares against THIS BRANCH's own upstream, not a hardcoded origin/main. Cloud
    fires ship to a branch + draft PR, so measuring a branch against main reported "disagree"
    forever — a permanent false alarm that makes the whole check worthless.
    """
    branch = _git(["rev-parse", "--abbrev-ref", "HEAD"]) or "main"
    up = _git(["rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"]) or "origin/main"
    track = up.split("/", 1)[1] if "/" in up else "main"
    before = _git(["rev-parse", up])
    fetch = subprocess.run(["git", "fetch", "origin", track, "--quiet"], cwd=str(ROOT),
                            text=True, capture_output=True)
    after = _git(["rev-parse", up])
    head = _git(["rev-parse", "HEAD"])
    return {
        "fetch_ok": fetch.returncode == 0,
        "fetch_error": (fetch.stderr or fetch.stdout).strip() if fetch.returncode != 0 else None,
        "branch": branch,
        "tracking": up,
        "cached_ref_was_stale": bool(before) and before != after,
        "origin_main_before_fetch": before[:9],
        "origin_main_after_fetch": after[:9],
        "head": head[:9],
        "in_sync": bool(head) and head == after,
    }


def check_upstream() -> dict:
    """Delegates to git_safe.ensure_upstream() (fire 8) so there is exactly one place that
    owns "is tracking configured" — this just surfaces whether it had to act."""
    return {"upstream_was_missing": git_safe.ensure_upstream()}


def run() -> dict:
    remote = check_remote()
    upstream = check_upstream()
    gr = guardrails.run()
    # The GO AWAY MODE contract used to be enforced by nothing at all — every rule in it was
    # obeyed only because a fire happened to open the file. Folding its status in here means a
    # drifting fire is VISIBLE at the one point every fire already runs.
    contract = loop_contract.status()
    # Fire 124: surface egress capability up front. Fires 122/123 each spent real time
    # rediscovering by hand that a repo-scoped cloud session can't do the network-verify/
    # mining backlog — this puts the same verdict where every fire already looks first.
    egress = net_canary.describe()

    needs_attention = (
        not remote["fetch_ok"]
        or not remote["in_sync"]
        or gr["critical_failures"] > 0
        or not contract["contract_present"]
    )
    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "ok": not needs_attention,
        "remote": remote,
        "upstream": upstream,
        "guardrails": {"passing": gr["passing"], "total": gr["total"],
                       "critical_failures": gr["critical_failures"]},
        "loop_contract": contract,
        "egress": egress,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    return result



def _open_owner_blockers() -> list:
    """Tasks only Eitan can do that HALT the loop. See data/excava/owner_blockers.json.

    Returns [] when the file is missing or unreadable — a broken blocker file must not
    silently halt the program, and must not silently un-halt it either; the guardrail
    G-X below is what catches the file going missing.
    """
    import json as _json
    p = ROOT / "data" / "excava" / "owner_blockers.json"
    try:
        d = _json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return []
    return [b for b in d.get("blockers", []) if b.get("status") == "open"]


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    strict = "--strict" in sys.argv
    r = run()

    # OWNER BLOCKERS (Eitan's rule, 2026-08-10): "If there is something critical to the project
    # that I absolutely must do — regardless of what I say — do not continue working until I
    # have finished that task." This runs FIRST and prints before anything else, because a loop
    # that reports "clear to work" and then works is exactly what the rule forbids. Encoded here
    # rather than left in a chat message so it binds the away loop too, which never reads chat.
    blockers = _open_owner_blockers()
    if blockers:
        print("=" * 72)
        print("HALTED — OWNER BLOCKER OPEN. Do not advance the milestone this fire.")
        for b in blockers:
            print(f"  [{b['id']}] {b['title']}")
            print(f"    unblocks when: {b.get('what_unblocks_it','')}")
            print(f"    owner effort : {b.get('estimated_owner_effort','?')}")
        print("  Allowed meanwhile: safety fixes, honest reporting, preparing what Eitan needs")
        print("  to decide. NOT allowed: new features, new increments, new departments.")
        print("=" * 72)

    print(f"STANDING CHECKS: {'OK — clear to work' if r['ok'] and not blockers else 'NEEDS ATTENTION'}")

    rem = r["remote"]
    if not rem["fetch_ok"]:
        print(f"  XX fetch failed: {rem['fetch_error']}")
    elif rem["cached_ref_was_stale"] and rem["in_sync"]:
        print(f"  !! local cache of origin/main was stale ({rem['origin_main_before_fetch']} -> "
              f"{rem['origin_main_after_fetch']}) — re-fetched, HEAD matches, nothing lost.")
    elif not rem["in_sync"]:
        print(f"  XX {rem['tracking']} ({rem['origin_main_after_fetch']}) and HEAD ({rem['head']}) "
              f"disagree — investigate before pushing anything.")
    else:
        print(f"  OK {rem['tracking']} unchanged at {rem['origin_main_after_fetch']}, HEAD in sync.")

    if r["upstream"]["upstream_was_missing"]:
        print("  !! upstream tracking was missing/wrong on this branch — repointed to origin/main.")
    else:
        print("  OK upstream tracking already set.")

    g = r["guardrails"]
    print(f"  guardrails: {g['passing']}/{g['total']} passing, {g['critical_failures']} critical failure(s)")

    eg = r["egress"]
    print(f"  {'OK' if eg['open'] else '!!'} egress: {eg['note']}")

    c = r["loop_contract"]
    if not c["contract_present"]:
        print("  XX GO AWAY MODE contract MISSING (data/excava/away_mode.json) — the loop has no rules.")
    else:
        print(f"  OK contract: {'always-on' if c['always_on'] else 'present'}"
              f"{'' if c['acked_recently'] else ' — NOT acknowledged recently (run: python -m src.loop_contract ack)'}")
    if c.get("open_gates"):
        print(f"  !! {len(c['open_gates'])} OPEN P5 GATE(S) — BINDING ON BOTH LOOPS, only Eitan decides:")
        for g in c["open_gates"]:
            print(f"       {g['id']}: {g['blocks'][:74]}")
        print("       (decide: python -m src.loop_contract gate <id> --verdict go|no|changed)")
    inc = c["open_increment"]
    print(f"  -> carry-over: '{inc['title']}' [{inc['kind']}], {inc['fires']} fire(s) in — CONTINUE IT"
          if inc else "  -> carry-over: none open — this fire starts one")
    if c["must_do_product_next"]:
        print(f"  !! {c['consecutive_meta_fires']} consecutive META fires (cap {c['meta_cap']}) — "
              f"THIS FIRE MUST ADVANCE THE PRODUCT, not the loop's own machinery.")
    return 1 if (strict and not r["ok"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
