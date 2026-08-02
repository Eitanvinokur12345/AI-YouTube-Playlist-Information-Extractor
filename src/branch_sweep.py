"""
src/branch_sweep.py — audits the stray `claude/kind-shannon-*` session branches on origin.

AWAY_LOG.md flags these repeatedly (fires 6, 7, 8, 9, 10, and AWAY_MODE.md §5-6) as "someone
else's problem" — every fire that noticed them had a narrower time budget and moved on. By
fire 100 the count had grown from the original ~13 to 57: every scheduled/cloud session gets a
fresh throwaway branch name, and only a session that explicitly ships via a branch+PR flow (or
that happens to notice and clean up) leaves anything behind other than the orphaned ref itself.

WHAT THIS DOES NOT DO: delete anything. Quarantine-never-delete (AWAY_MODE.md §3, CLAUDE.md §3)
is a branch-content rule, and there is no way to "quarantine" a git branch without a positive
argument that a hard delete is safe. So this module only PROVES safety where proof exists and
reports everything else for a human (or a future fire with an explicit mandate) to act on.

The one thing it CAN prove cheaply: `git rev-list --left-right --count origin/main...<branch>`
gives the count of commits unique to each side. If the branch's unique-commit count is exactly
0, every commit it carries is already reachable from origin/main — deleting it destroys no
history, full stop, no judgment call. Branches with a no-common-ancestor history (fire 7 found
this happens after certain rewrites — confirmed again here: e.g. kind-shannon-00pnba shares NO
merge-base with main) still get an honest unique-commit count from rev-list; it is just not a
"how far behind" number, it is "how much of this branch's own history main doesn't already
contain," which is exactly the number that matters for a safety judgment.

Run:  python -m src.branch_sweep            # print + write data/excava/branch_sweep.json
      python -m src.branch_sweep --fetch    # `git fetch origin` first (do this if unsure the
                                             # local remote-tracking refs are current)
"""
from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUT = ROOT / "data" / "excava" / "branch_sweep.json"
KEEP_PREFIXES = ("origin/main",)


def _git(args: list[str]) -> str:
    r = subprocess.run(["git", *args], cwd=str(ROOT), text=True, capture_output=True)
    return (r.stdout or "").strip()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def remote_branches() -> list[str]:
    out = []
    for line in _git(["for-each-ref", "--format=%(refname:short)", "refs/remotes/origin/"]).splitlines():
        line = line.strip()
        if not line or line == "origin/HEAD" or line in KEEP_PREFIXES:
            continue
        out.append(line)
    return out


def audit_branch(branch: str) -> dict:
    counts = _git(["rev-list", "--left-right", "--count", f"origin/main...{branch}"])
    parts = counts.split()
    behind, unique = (int(parts[0]), int(parts[1])) if len(parts) == 2 else (None, None)
    tip = _git(["log", "-1", "--format=%h|%ci|%s", branch])
    sha, date, subject = (tip.split("|", 2) + ["", "", ""])[:3]
    merge_base = _git(["merge-base", "origin/main", branch])
    verdict = "SAFE-DELETE (0 commits unique to branch, proven no data loss)" if unique == 0 \
        else f"REVIEW ({unique} commit(s) unique to branch, not reachable from main)"
    return {
        "branch": branch,
        "tip_sha": sha,
        "tip_date": date,
        "tip_subject": subject,
        "commits_behind_main": behind,
        "commits_unique_to_branch": unique,
        "shares_merge_base_with_main": bool(merge_base),
        "verdict": verdict,
    }


def sweep(do_fetch: bool = False) -> dict:
    if do_fetch:
        _git(["fetch", "origin"])
    branches = remote_branches()
    audits = [audit_branch(b) for b in branches]
    audits.sort(key=lambda a: (a["commits_unique_to_branch"] if a["commits_unique_to_branch"] is not None else 1 << 30))
    safe = [a for a in audits if a["commits_unique_to_branch"] == 0]
    result = {
        "generated_at": _now(),
        "total_stray_branches": len(audits),
        "safe_delete_count": len(safe),
        "safe_delete_branches": [a["branch"] for a in safe],
        "branches": audits,
        "note": "Report only — nothing deleted (quarantine-never-delete). safe_delete_branches "
                "are mathematically proven to carry zero commits absent from origin/main; "
                "everything else needs a human or a mandated follow-up fire to review before "
                "any deletion.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    return result


def main() -> int:
    ap = argparse.ArgumentParser(description="Audit stray origin branches for safe-to-delete status")
    ap.add_argument("--fetch", action="store_true", help="git fetch origin before auditing")
    args = ap.parse_args()
    result = sweep(do_fetch=args.fetch)
    print(f"branch_sweep: {result['total_stray_branches']} stray branches, "
          f"{result['safe_delete_count']} provably safe to delete (0 unique commits)")
    for b in result["safe_delete_branches"]:
        print(f"  SAFE-DELETE: {b}")
    print(f"wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
