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

from src import git_safe, guardrails

ROOT = Path(__file__).parent.parent
OUT = ROOT / "data" / "standing_checks.json"


def _git(args):
    r = subprocess.run(["git", *args], cwd=str(ROOT), text=True, capture_output=True)
    return (r.stdout or "").strip()


def check_remote() -> dict:
    """Snapshot the cached origin/main ref, force a real fetch, snapshot again. A mismatch
    before/after is the exact "is a day of work actually at risk?" question fire 8 spent time
    ruling out by hand — this answers it in one call instead of a manual rev-parse + fetch +
    rev-parse + eyeball-the-diff each time."""
    before = _git(["rev-parse", "origin/main"])
    fetch = subprocess.run(["git", "fetch", "origin", "main", "--quiet"], cwd=str(ROOT),
                            text=True, capture_output=True)
    after = _git(["rev-parse", "origin/main"])
    head = _git(["rev-parse", "HEAD"])
    return {
        "fetch_ok": fetch.returncode == 0,
        "fetch_error": (fetch.stderr or fetch.stdout).strip() if fetch.returncode != 0 else None,
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

    needs_attention = (
        not remote["fetch_ok"]
        or not remote["in_sync"]
        or gr["critical_failures"] > 0
    )
    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "ok": not needs_attention,
        "remote": remote,
        "upstream": upstream,
        "guardrails": {"passing": gr["passing"], "total": gr["total"],
                       "critical_failures": gr["critical_failures"]},
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    return result


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    strict = "--strict" in sys.argv
    r = run()
    print(f"STANDING CHECKS: {'OK — clear to work' if r['ok'] else 'NEEDS ATTENTION'}")

    rem = r["remote"]
    if not rem["fetch_ok"]:
        print(f"  XX fetch failed: {rem['fetch_error']}")
    elif rem["cached_ref_was_stale"] and rem["in_sync"]:
        print(f"  !! local cache of origin/main was stale ({rem['origin_main_before_fetch']} -> "
              f"{rem['origin_main_after_fetch']}) — re-fetched, HEAD matches, nothing lost.")
    elif not rem["in_sync"]:
        print(f"  XX origin/main ({rem['origin_main_after_fetch']}) and HEAD ({rem['head']}) "
              f"disagree — investigate before pushing anything.")
    else:
        print(f"  OK origin/main unchanged at {rem['origin_main_after_fetch']}, HEAD in sync.")

    if r["upstream"]["upstream_was_missing"]:
        print("  !! upstream tracking was missing on this branch — set to origin/main.")
    else:
        print("  OK upstream tracking already set.")

    g = r["guardrails"]
    print(f"  guardrails: {g['passing']}/{g['total']} passing, {g['critical_failures']} critical failure(s)")
    return 1 if (strict and not r["ok"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
