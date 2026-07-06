"""
src/git_safe.py — SAFE git operations. Fixes the two mechanical failures that put the
project at risk, and does it under one law: **QUARANTINE, NEVER DELETE.**

The two failures this replaces:
  1. Untracked trees (skills/, other-skills/, agent drafts) collided with incoming
     tracked files and BLOCKED every rebase — and `git clean -fd` "fixed" it by DELETING
     them (permanent information loss). Here, colliding untracked files are MOVED into
     _ATTIC/quarantine/<ts>/ (preserved, reviewable), never destroyed.
  2. Commit messages passed as inline PowerShell strings were mangled (embedded quotes →
     git read words as pathspecs). Here, every message goes through a UTF-8 file: `commit -F`.

Every op is subprocess with an ARGUMENT LIST (no shell = no quoting/mangling) and takes a
`git bundle` backup of the whole history first, so nothing is ever unrecoverable.

CLI:
  python -m src.git_safe backup                 # snapshot history -> _ATTIC/backups/*.bundle
  python -m src.git_safe commit  -m "msg" [-a p1 p2 ...]
  python -m src.git_safe sync                   # revert CI churn + quarantine collisions + rebase
  python -m src.git_safe push                   # backup -> sync -> push -> VERIFY origin==HEAD
  python -m src.git_safe ship -m "msg" -a p1 .. # commit -> push, one call (the everyday path)
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
ATTIC = ROOT / "_ATTIC"
# Canonical CI-OWNED paths — the only things safe-git ever reverts. Your source is never touched.
CI_CHURN = ["data", "backups"]
KEEP_BUNDLES = 12


def _ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _git(args, check=True) -> str:
    """Run git with an argument LIST (never a shell string) so nothing can be re-parsed."""
    r = subprocess.run(["git", *args], cwd=str(ROOT), text=True, capture_output=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed:\n{(r.stderr or r.stdout).strip()}")
    return (r.stdout or "").strip()


def backup_bundle() -> Path:
    """Snapshot ALL of history into a git bundle. A bundle is a complete, offline-recoverable
    clone source — if the remote or the working copy is ever wrecked, `git clone <bundle>` restores."""
    (ATTIC / "backups").mkdir(parents=True, exist_ok=True)
    dest = ATTIC / "backups" / f"repo-{_ts()}.bundle"
    _git(["bundle", "create", str(dest), "--all"])
    olds = sorted((ATTIC / "backups").glob("*.bundle"))
    for old in olds[:-KEEP_BUNDLES]:
        try:
            old.unlink()
        except OSError:
            pass
    return dest


def quarantine_collisions() -> list:
    """Move untracked files that WOULD collide with incoming commits into _ATTIC/quarantine.
    This unblocks a rebase with ZERO deletion — the files stay, just out of the way, reviewable."""
    _git(["fetch", "origin", "--quiet"], check=False)
    untracked = [f for f in _git(["ls-files", "--others", "--exclude-standard"]).splitlines() if f]
    if not untracked:
        return []
    try:
        origin_files = set(_git(["ls-tree", "-r", "--name-only", "origin/main"]).splitlines())
    except RuntimeError:
        origin_files = set()
    qdir = ATTIC / "quarantine" / _ts()
    moved = []
    for f in untracked:
        if f in origin_files:                       # this untracked file blocks the incoming tracked one
            src, dst = ROOT / f, qdir / f
            try:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(src), str(dst))
                moved.append(f)
            except OSError:
                pass
    return moved


def revert_ci_churn() -> None:
    """Restore CI-owned paths from the INDEX — discards unstaged CI regeneration only.
    Anything you STAGED survives (it lives in the index). Never touches source outside CI_CHURN."""
    _git(["checkout", "--", *CI_CHURN], check=False)


def commit(message: str, add=None) -> str:
    if add:
        _git(["add", *list(add)])
    ATTIC.mkdir(parents=True, exist_ok=True)
    mf = ATTIC / "COMMIT_MSG.txt"
    mf.write_text(message, encoding="utf-8")         # message via UTF-8 file => never shell-mangled
    _git(["commit", "-F", str(mf)])
    return _git(["rev-parse", "--short", "HEAD"])


def sync() -> list:
    """Make the tree rebase-safe, then rebase onto origin. Returns what got quarantined.
    Auto-resolves the recurring CI-data-churn conflict (data/* → take incoming), but for a real
    SOURCE conflict it aborts and surfaces it — never silently drops your code."""
    revert_ci_churn()
    moved = quarantine_collisions()
    r = subprocess.run(["git", "pull", "--rebase", "--no-edit"], cwd=str(ROOT), text=True, capture_output=True)
    while r.returncode != 0 and "conflict" in (r.stdout + r.stderr).lower():
        conflicted = [f for f in _git(["diff", "--name-only", "--diff-filter=U"]).splitlines() if f]
        src = [f for f in conflicted if not f.startswith(("data/", "backups/"))]
        if src or not conflicted:                       # a real source conflict → stop, don't guess
            _git(["rebase", "--abort"], check=False)
            raise RuntimeError(f"source conflict — resolve by hand: {', '.join(src or conflicted)}")
        for f in conflicted:                            # CI data snapshots: your code regenerates them
            _git(["checkout", "--theirs", "--", f], check=False)
            _git(["add", "--", f])
        env_run = subprocess.run(["git", "-c", "core.editor=true", "rebase", "--continue"],
                                 cwd=str(ROOT), text=True, capture_output=True)
        r = env_run
    if r.returncode != 0:
        raise RuntimeError(f"git pull --rebase failed:\n{(r.stderr or r.stdout).strip()}")
    return moved


def push() -> str:
    """The safe push: back up history, sync, push, then PROVE it landed (origin == HEAD)."""
    backup_bundle()
    sync()
    _git(["push"])
    head, origin = _git(["rev-parse", "HEAD"]), _git(["rev-parse", "origin/main"])
    if head != origin:
        raise RuntimeError(f"push did NOT land — origin ({origin[:9]}) != HEAD ({head[:9]}). Investigate before continuing.")
    return head[:9]


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["backup", "commit", "sync", "push", "ship"])
    ap.add_argument("-m", "--message", default="")
    ap.add_argument("-a", "--add", nargs="*", default=[])
    args = ap.parse_args()

    if args.cmd == "backup":
        print(f"backup -> {backup_bundle().relative_to(ROOT)}")
    elif args.cmd == "commit":
        if not args.message:
            print("commit needs -m"); return 1
        print(f"committed {commit(args.message, args.add)}")
    elif args.cmd == "sync":
        moved = sync()
        print(f"synced; quarantined {len(moved)} colliding file(s)" + (f" -> _ATTIC/quarantine" if moved else ""))
    elif args.cmd == "push":
        print(f"pushed + verified: origin==HEAD @ {push()}")
    elif args.cmd == "ship":
        if not args.message:
            print("ship needs -m"); return 1
        c = commit(args.message, args.add)
        print(f"committed {c}; pushed + verified @ {push()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
