"""
src/git_merge_resolve.py — shared, tested merge-conflict resolver for scheduled push lanes.

Every CI workflow that commits + pushes on a schedule (19 lanes as of 2026-08-02) can hit the
same class of conflict: another lane already pushed since this job's checkout, `git pull
--rebase` fails, the fallback `git pull --no-rebase` also conflicts. Each lane's workflow YAML
originally hand-rolled ~10 lines of inline bash for this: `git checkout --ours` a short list of
fully-regenerated JSON readouts, then `git commit`. Anything else fell through to "leave it
unresolved" — the run's real work stayed local and unpushed, reported only as a swallowed
"push skipped"/"leaving for manual recovery" with no further signal.

`excava_beat.yml` hit this class of bug hardest (fires 88-101, see AWAY_LOG.md 2026-08-01/02)
and hardened its OWN inline copy over five fires: widened the "ours" whitelist to 18
fully-regenerated files (verified each is `.write_text()`/`json.dump()`'d whole every run, never
appended-to), added a UNION merge for `*.jsonl` append-logs (taking "ours" would silently drop
the other lane's real rows — these are line-independent records, so the safe merge is the union,
deduped only on byte-identical lines), and a UNION merge for `data/designs.json` specifically (a
real, growing dataset keyed by `slug`, not a regenerable readout — same reasoning as the jsonl
case, just for a JSON list).

Fire 102 (2026-08-02) found the other 18 push-capable lanes still carry the ORIGINAL narrow
7-file whitelist with none of this hardening — confirmed live, not theoretical, via
`bulk_analyze.yml`'s own job logs (run 30731719512, 2026-08-02T04:04-04:08Z): it hit a conflict
on `data/excava/traces/...`, `data/excava_approvals.json` and ~90 other files outside the
whitelist, fell through to "leave it unresolved", and silently discarded that run's real
bulk-analyze results (the step still exited 0, so nothing downstream noticed).

This module is the fix: ONE tested implementation of the resolve logic, callable via
`python -m src.git_merge_resolve` from any workflow's merge-conflict fallback, in place of
copy-pasting inline bash into each lane's YAML (and re-introducing the narrow-whitelist bug in
a 19th place next time someone adds a lane).

Contract: run this ONLY after `git pull --no-rebase --no-edit origin main` has already failed
and left the repo mid-merge (`MERGE_HEAD` present, conflicted files with markers on disk). It
resolves every conflicted file it recognizes (whitelist / *.jsonl / data/designs.json) and
`git commit`s. Files not on the whitelist that are also not the case in the code above are LEFT
CONFLICTED and the commit will fail — a real, unresolved conflict outside the maintained trust
list. Exit code 0 means the merge committed cleanly; exit code 1 means it didn't (caller should
treat that the same as today's "push skipped").

CLI:
  python -m src.git_merge_resolve          # resolve + commit; exit 0 on success, 1 otherwise
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

# Fully regenerated whole, every run, by the module named in the comment — verified none of
# these are appended-to, so taking "ours" (this run's own fresh copy) loses nothing the next
# cycle doesn't immediately regenerate anyway. Exact list ported from excava_beat.yml's own
# hardened whitelist (fires 89/99).
OURS_WHITELIST = [
    "data/data_guard.json",
    "data/health.json",
    "data/effectiveness.json",
    "data/hub.json",
    "data/self_check.json",
    "data/safety.json",
    "data/guardrails_status.json",
    "data/excava/state.json",
    # data/excava/bus.json was HERE until 2026-08-16 and did not belong: it is not a regenerated
    # readout, it is a read-modify-write ACCUMULATING store, so "take ours" silently discarded
    # every task the other lane had enqueued or completed since the checkout. Caught live while
    # merging main into a feature branch — "ours" would have dropped 15 real tasks. Now handled by
    # resolve_bus_union() below, on the same reasoning as the designs/jsonl cases.
    "data/excava/rooms.json",
    "data/excava/leases.json",
    "data/excava/pulse.json",
    "data/excava/recent_events.json",
    "data/excava/backlog.json",
    "PULSE.md",
    "PROOF.md",
    "docs/hub_api.json",
    "docs/hub_api_packages.json",
]


def _git(args) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=str(ROOT), text=True, capture_output=True)


def conflicted_files() -> list:
    r = _git(["diff", "--name-only", "--diff-filter=U"])
    return [f for f in (r.stdout or "").splitlines() if f.strip()]


def resolve_whitelist(conflicts: list) -> list:
    """`git checkout --ours` + `git add` any conflicted file on OURS_WHITELIST. Returns the
    subset actually resolved this way."""
    hit = [f for f in conflicts if f in OURS_WHITELIST]
    if hit:
        _git(["checkout", "--ours", "--", *hit])
        _git(["add", *hit])
    return hit


def resolve_jsonl_union(conflicts: list) -> list:
    """Union-merge (ours-then-theirs, deduped on exact-duplicate lines) any conflicted *.jsonl
    append-log — line-independent records, so keeping both sides' lines is always safe: it can
    add a harmless exact-duplicate at worst, never discards a real entry either side wrote."""
    hit = [f for f in conflicts if f.endswith(".jsonl")]
    resolved = []
    for f in hit:
        ours = _git(["show", f":2:{f}"]).stdout
        theirs = _git(["show", f":3:{f}"]).stdout
        seen = set()
        merged_lines = []
        for line in (ours + theirs).splitlines():
            if line not in seen:
                seen.add(line)
                merged_lines.append(line)
        path = ROOT / f
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(merged_lines) + ("\n" if merged_lines else ""), encoding="utf-8")
        _git(["add", f])
        resolved.append(f)
    return resolved


def _load_designs_blob(rev_stage: str) -> dict:
    try:
        return json.loads(_git(["show", rev_stage]).stdout)
    except Exception:
        return {"designs": [], "updated_at": ""}


def resolve_designs_union(conflicts: list) -> list:
    """Union-merge data/designs.json specifically: a real, growing dataset of scraped design
    records (keyed by slug, falling back to source_url/name), not a regenerable readout — taking
    "ours" would silently drop every record the other lane just scraped. A record on only one
    side survives; a record both sides scraped independently collapses to one copy."""
    target = "data/designs.json"
    if target not in conflicts:
        return []
    ours = _load_designs_blob(f":2:{target}")
    theirs = _load_designs_blob(f":3:{target}")
    seen = set()
    merged = []
    for side in (ours.get("designs") or [], theirs.get("designs") or []):
        for d in side:
            key = d.get("slug") or d.get("source_url") or d.get("name")
            if key is not None:
                if key in seen:
                    continue
                seen.add(key)
            merged.append(d)
    out = {
        "designs": merged,
        "updated_at": max(ours.get("updated_at") or "", theirs.get("updated_at") or ""),
    }
    (ROOT / target).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    _git(["add", target])
    return [target]


def resolve_bus_union(conflicts: list) -> list:
    """Union-merge data/excava/bus.json by task id — the task bus is the system's work record, and
    losing a row here loses real work.

    Every lane does read-modify-write on the WHOLE file, so two lanes that overlap already race at
    the file level; resolving the resulting conflict with "take ours" turned that race into
    guaranteed loss of the other lane's rows. Union by id keeps both sides' tasks. Where the same
    id exists on both sides, the row with the newer `updated_at` wins, EXCEPT that a terminal
    'blocked' is never overwritten by a stale 'queued'/'working' — a block records a considered
    judgement that some department cannot do this work, and silently un-blocking it would put the
    task back into the loop that produced it.
    """
    target = "data/excava/bus.json"
    if target not in conflicts:
        return []

    def _side(stage):
        try:
            return json.loads(_git(["show", f":{stage}:{target}"]).stdout)
        except Exception:
            return {"tasks": []}

    ours, theirs = _side(2), _side(3)
    merged: dict = {}
    for side in (theirs.get("tasks") or [], ours.get("tasks") or []):
        for t in side:
            tid = t.get("id")
            if tid is None:
                continue
            cur = merged.get(tid)
            if cur is None:
                merged[tid] = t
                continue
            if cur.get("status") == "blocked" and t.get("status") != "blocked":
                continue                                   # never un-block from a stale row
            if t.get("status") == "blocked" or str(t.get("updated_at", "")) > str(cur.get("updated_at", "")):
                merged[tid] = t
    out = dict(theirs)
    out["tasks"] = sorted(merged.values(), key=lambda t: str(t.get("created_at", "")))
    seen_ids = {m.get("id") for m in (theirs.get("migrations") or [])}
    out["migrations"] = (theirs.get("migrations") or []) + [
        m for m in (ours.get("migrations") or []) if m.get("id") not in seen_ids]
    (ROOT / target).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    _git(["add", target])
    return [target]


def resolve() -> bool:
    """Resolve every conflicted file this module recognizes, then attempt the merge commit.
    Returns True if the commit succeeded (merge fully resolved), False otherwise (real conflict
    remains outside the maintained trust list — caller should treat as "push skipped", same as
    before this module existed)."""
    conflicts = conflicted_files()
    if not conflicts:
        # Nothing conflicted (or already resolved) — still try to commit in case a merge is
        # mid-flight (MERGE_HEAD present) with nothing left to resolve.
        pass
    else:
        handled = set()
        handled.update(resolve_whitelist(conflicts))
        handled.update(resolve_jsonl_union(conflicts))
        handled.update(resolve_designs_union(conflicts))
        handled.update(resolve_bus_union(conflicts))
        remaining = [f for f in conflicts if f not in handled]
        if remaining:
            print(f"unresolved conflict outside the maintained trust list: {remaining}", file=sys.stderr)
    r = _git(["commit", "--no-edit"])
    if r.returncode != 0:
        print((r.stderr or r.stdout).strip(), file=sys.stderr)
        return False
    return True


def main() -> int:
    return 0 if resolve() else 1


if __name__ == "__main__":
    raise SystemExit(main())
