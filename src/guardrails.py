"""
src/guardrails.py — the INFORMATION-LOSS GUARDRAILS (owner law, 2026-07-06).

The project must never be "toppled" — no committed work lost, no data silently dropped,
no push that only *looked* like it saved, no corruption shipped that breaks the dashboard.
This module enforces 16 named guardrails, each a concrete check. It writes
data/guardrails_status.json (for the cockpit) and APPENDS to data/guardrails_log.jsonl
(never rewritten — a permanent audit trail).

Run:  python -m src.guardrails            # check + print + write status
      python -m src.guardrails --strict   # exit 1 if any CRITICAL guardrail fails (for CI)

Pairs with src/git_safe.py, which implements the safe git operations these guardrails watch.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"
STATUS = DATA / "guardrails_status.json"
LOG = DATA / "guardrails_log.jsonl"
MOJIBAKE = b"\xc3\xa2\xe2\x82\xac"          # 'â€' — the UTF-8-double-encoding fingerprint (cost us v67)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _git(args) -> str:
    try:
        r = subprocess.run(["git", *args], cwd=str(ROOT), text=True, capture_output=True)
        return (r.stdout or "").strip()
    except Exception:
        return ""


def _ok(gid, name, ok, detail, severity="warn"):
    return {"id": gid, "name": name, "ok": bool(ok), "detail": detail, "severity": severity}


# ── the 12 guardrails ──────────────────────────────────────────────────────────
def g_quarantine():
    p = (ROOT / "src" / "git_safe.py")
    has = p.exists() and "QUARANTINE, NEVER DELETE" in p.read_text(encoding="utf-8", errors="replace")
    return _ok("G-A", "Quarantine over delete", has,
               "safe-git moves colliding untracked files to _ATTIC (never `git clean -fd`)." if has
               else "src/git_safe.py missing — blind deletes could lose uncommitted work.", "critical")


def g_msgfile():
    p = (ROOT / "src" / "git_safe.py")
    has = p.exists() and 'commit", "-F"' in p.read_text(encoding="utf-8", errors="replace")
    return _ok("G-B", "Message-file commits", has,
               "commit messages go through a UTF-8 file (`commit -F`) — no shell mangling." if has
               else "no message-file commit path — inline messages can be mangled.", "critical")


def g_backup():
    b = sorted((ROOT / "_ATTIC" / "backups").glob("*.bundle")) if (ROOT / "_ATTIC" / "backups").exists() else []
    fresh = False
    if b:
        newest = max(x.stat().st_mtime for x in b)
        fresh = (datetime.now().timestamp() - newest) < 26 * 3600
    if not b and os.environ.get("GITHUB_ACTIONS") == "true":
        # 2026-07-26 fix: the CI beat (.github/workflows/excava_beat.yml) commits+pushes with raw
        # git directly — it never calls src/git_safe.py, so backup_bundle() never runs there and
        # _ATTIC/backups (gitignored, per-machine only) is permanently empty on every ephemeral
        # runner. That's not a risk (every beat pushes straight to origin, GitHub's own redundancy)
        # — it's this check assuming the local/interactive git_safe path, which CI doesn't take.
        # Flagged as a permanent false "warn" once v128 wired guardrails into the CI beat itself.
        return _ok("G-C", "History backup fresh", True,
                   "n/a in CI — the beat pushes straight to origin each cycle, bypassing git_safe/local bundles by design.", "info")
    return _ok("G-C", "History backup fresh", bool(b) and fresh,
               f"{len(b)} bundle(s); newest within 26h." if fresh else
               "no recent history bundle — run `python -m src.git_safe backup` before risky ops.", "warn")


def g_mojibake():
    bad = []
    for pat in ("docs/*.js", "docs/*.html", "docs/*.css", "docs/**/*.js", "src/*.py", "*.md"):
        for f in ROOT.glob(pat):
            if not f.is_file() or f.name == "guardrails.py":   # the detector holds the pattern as data
                continue
            b = f.read_bytes()
            if MOJIBAKE in b or b"\xc3\xa2\xe2\x80" in b:
                bad.append(str(f.relative_to(ROOT)))
    return _ok("G-D", "No mojibake (UTF-8 intact)", not bad,
               "no double-encoded text found." if not bad else f"CORRUPT: {', '.join(bad[:5])}", "critical")


def g_build_align():
    try:
        js = (DOCS / "dashboard.js").read_text(encoding="utf-8")
        sw = (DOCS / "sw.js").read_text(encoding="utf-8")
        app = re.search(r'APP_BUILD\s*=\s*"([^"]+)"', js)
        shell = re.search(r'SHELL_CACHE\s*=\s*"ai-skills-shell-([^"]+)"', sw)
        a, s = (app.group(1) if app else "?"), (shell.group(1) if shell else "?")
        return _ok("G-E", "Build alignment", a == s,
                   f"APP_BUILD {a} == SHELL_CACHE {s}." if a == s else f"MISMATCH: APP_BUILD {a} vs SHELL_CACHE {s} (stale shell risk).", "warn")
    except Exception as e:
        return _ok("G-E", "Build alignment", False, f"could not read builds: {e}", "warn")


def g_json():
    bad = []
    for d in (DATA, DOCS):
        for f in d.glob("*.json"):
            try:
                json.loads(f.read_text(encoding="utf-8"))
            except Exception:
                bad.append(str(f.relative_to(ROOT)))
    return _ok("G-F", "JSON integrity", not bad,
               "all top-level data/ + docs/ JSON parses." if not bad else f"BROKEN JSON: {', '.join(bad[:5])}", "critical")


def g_remote_sync():
    head, origin = _git(["rev-parse", "HEAD"]), _git(["rev-parse", "origin/main"])
    counts = _git(["rev-list", "--left-right", "--count", "origin/main...HEAD"])
    synced = head and origin and head == origin
    return _ok("G-G", "Remote sync verified", synced,
               "HEAD == origin/main (work is really saved)." if synced else
               f"NOT in sync (behind/ahead: {counts or '?'}) — a push may not have landed.", "warn")


def g_collisions():
    untracked = [f for f in _git(["ls-files", "--others", "--exclude-standard"]).splitlines() if f]
    origin = set(_git(["ls-tree", "-r", "--name-only", "origin/main"]).splitlines())
    coll = [f for f in untracked if f in origin]
    return _ok("G-H", "No rebase-blocking collisions", not coll,
               "no untracked file collides with incoming commits." if not coll else
               f"{len(coll)} untracked file(s) would block a rebase — safe-git will quarantine them.", "warn")


def g_handoff():
    hf = ROOT / "SESSION_HANDOFF.md"
    try:
        txt = hf.read_text(encoding="utf-8")
        js = (DOCS / "dashboard.js").read_text(encoding="utf-8")
        build = re.search(r'APP_BUILD\s*=\s*"([^"]+)"', js)
        b = build.group(1) if build else ""
        fresh = b and b in txt
        return _ok("G-I", "Handoff mentions live build", fresh,
                   f"SESSION_HANDOFF.md references {b}." if fresh else
                   f"handoff does not mention the live build ({b}) — update §0d so no context is lost.", "warn")
    except Exception as e:
        return _ok("G-I", "Handoff mentions live build", False, f"cannot read handoff: {e}", "warn")


def g_memory():
    ep = DATA / "project_memory" / "episodes.jsonl"
    n = len(ep.read_text(encoding="utf-8").splitlines()) if ep.exists() else 0
    return _ok("G-J", "Project-memory contract", n > 0,
               f"{n} memory episodes on record." if n else "no project-memory episodes — the WHY log is empty.", "warn")


def g_auditlog():
    n = len(LOG.read_text(encoding="utf-8").splitlines()) if LOG.exists() else 0
    return _ok("G-K", "Append-only audit log", True,
               f"{n} guardrail runs logged (append-only, never rewritten).", "info")


def g_watchdog():
    untracked = [f for f in _git(["ls-files", "--others", "--exclude-standard"]).splitlines() if f]
    # source-like files that are NOT CI data/backups and NOT ephemeral — real work at risk of being lost
    sus = [f for f in untracked if not f.startswith(("data/", "backups/", "_ATTIC/", "scratch/"))
           and f.rsplit(".", 1)[-1] in ("py", "js", "html", "css", "md", "json", "yml", "yaml")]
    return _ok("G-L", "Uncommitted-work watchdog", not sus,
               "no stray source files uncommitted." if not sus else
               f"{len(sus)} untracked source file(s) not committed — commit or quarantine so nothing is lost: {', '.join(sus[:4])}", "warn")


def g_movement():
    """Owner law 2026-07-06: EACH loop, confirm work is actually MOVING (not all at 0).

    2026-07-26 fix: this used to recount "done" live from bus.json each time, but
    src/excava_bus.py:prune() deliberately ARCHIVES finished tasks out of the bus after
    PRUNE_DAYS — so that live count falls as pruning runs, with no relation to whether work
    is actually happening. Two consecutive away-sessions (2026-07-24, 2026-07-26) flagged the
    resulting "decline" as a mystery regression; it was a metric bug, not a stall. The real
    monotonic total already exists at state.json['usage'][dept]['done'] (bumped once per
    completion, never pruned) — use THAT for the stall check."""
    mv = DATA / "excava" / "movement.json"
    state = _load_json(DATA / "excava" / "state.json", {})
    usage = state.get("usage", {}) or {}
    done = sum(u.get("done", 0) for u in usage.values())
    depts = sum(1 for u in usage.values() if u.get("done", 0) > 0)
    hist = _load_json(mv, {"history": []}).get("history", [])
    hist.append({"at": _now(), "done": done, "depts_moving": depts})
    hist = hist[-30:]
    mv.parent.mkdir(parents=True, exist_ok=True)
    mv.write_text(json.dumps({"history": hist, "done": done, "depts_moving": depts},
                             ensure_ascii=False, indent=1), encoding="utf-8")
    recent = [h["done"] for h in hist[-4:]]
    stalled = len(recent) >= 4 and len(set(recent)) == 1        # 4 checks, zero movement
    return _ok("G-M", "Work is moving (not all at 0)", not stalled,
               f"{done} tasks done, {depts} departments moving" + (" — STALLED (no new completions in the last 4 beats)" if stalled else ""),
               "warn")


def g_disk():
    """Owner-critical 2026-07-17: a 100%-full disk silently broke a ship (`git bundle` → "Out of
    diskspace"), and nothing was watching. Watch free space so the system NOTICES before the next
    ship or beat dies. A ship's history bundle needs ~120 MB, so <250 MB free means the next ship
    will fail — surfaced loudly here, in the panel the owner already trusts."""
    import shutil
    free_mb = shutil.disk_usage(str(ROOT)).free // (1024 * 1024)
    if free_mb < 250:
        return _ok("G-N", "Disk headroom", False,
                   f"CRITICAL: only {free_mb} MB free — a ship WILL fail (bundle needs ~120 MB). "
                   f"Free space now (prune _ATTIC/backups, clear the drive).", "warn")
    if free_mb < 1024:
        return _ok("G-N", "Disk headroom", False,
                   f"LOW: {free_mb} MB free — under the 1 GB comfort line; a big ship could fail.", "warn")
    return _ok("G-N", "Disk headroom", True, f"{free_mb} MB free on the repo drive.", "info")


def g_localfuel():
    """The LOCAL DRAIN's pulse (2026-07-20): unattended enrichment on the owner's machine ships
    data/excava/local_worker.json with every batch, so BOTH sides (CI reads the committed file,
    local reads it live) can see whether the zero-quota brain is actually draining stubs. Stale
    >26h = the scheduled task died (reboot, moved repo, Ollama gone) — say so before the stub
    race is silently lost again."""
    st = _load_json(DATA / "excava" / "local_worker.json", {})
    if not st:
        return _ok("G-O", "Local drain alive", False,
                   "no local_worker.json yet — the unattended drain has never run.", "warn")
    try:
        age_h = (datetime.now(timezone.utc)
                 - datetime.fromisoformat(st["at"])).total_seconds() / 3600
    except Exception:
        return _ok("G-O", "Local drain alive", False, "local_worker.json has no readable timestamp.", "warn")
    detail = (f"last batch {age_h:.1f}h ago on {st.get('host', '?')} ({st.get('model', '?')}): "
              f"{st.get('enriched', 0)} enriched, stubs {st.get('stubs', '?')}")
    if age_h > 26:
        return _ok("G-O", "Local drain alive", False,
                   detail + " — STALE: the hourly task isn't running (PC off, or Ollama gone).", "warn")
    return _ok("G-O", "Local drain alive", bool(st.get("ok")), detail, "warn" if not st.get("ok") else "info")


def g_beat_heartbeat():
    """2026-07-27 (fire 18): G-M's "done" counter is fed by ANY caller of `python -m src.excava`
    (bulk_analyze.yml calls it once per run too), so it can look healthy even when the DEDICATED
    excava_beat.yml heartbeat — which should commit "excava-beat #N: <ts>" every ~5-10 min for its
    whole 5.3h run — is actually wedged. Fire 16/17 diagnosed exactly this by hand (an unbounded
    room-advance loop hanging inside one already-running job, starving the GH Actions concurrency
    queue for 3+ hours while G-M's lagging done-counter still read "moving"). This check reads the
    git history directly (no network) for the last real "excava-beat #N" commit and flags it stale
    — an early, cheap signal the done-counter alone misses.

    Shallow-clone caveat: a fresh checkout (this sandbox, and `actions/checkout@v4`'s own
    fetch-depth=1 default) may not have enough local history to find ANY match even when the
    heartbeat is perfectly healthy — that is a checkout-depth artifact, not evidence of a stall,
    so a shallow repo with zero matches reports "info" (can't tell), never a false "STALE" warn.
    A match IS still meaningfully aged even in a shallow clone (its timestamp is real), so a found
    commit is always evaluated for staleness regardless of clone depth."""
    log = _git(["log", "-1", "--format=%ad", "--date=iso-strict", "--grep=^excava-beat #", "origin/main"])
    if not log:
        log = _git(["log", "-1", "--format=%ad", "--date=iso-strict", "--grep=^excava-beat #"])
    if not log:
        shallow = _git(["rev-parse", "--is-shallow-repository"]) == "true"
        if shallow:
            return _ok("G-P", "Beat heartbeat commit freshness", True,
                       "shallow clone — not enough local history to find an 'excava-beat #N' "
                       "commit either way; not a stall signal, just a checkout-depth limit.", "info")
        return _ok("G-P", "Beat heartbeat commit freshness", False,
                   "no 'excava-beat #N' commit found in (full) history — the dedicated heartbeat "
                   "loop has never landed a per-cycle commit.", "warn")
    try:
        age_h = (datetime.now(timezone.utc) - datetime.fromisoformat(log)).total_seconds() / 3600
    except Exception:
        return _ok("G-P", "Beat heartbeat commit freshness", False,
                   f"could not parse heartbeat commit date: {log!r}", "warn")
    stale = age_h > 6          # normal cadence is ~5-10 min inside a run; 6h is generous slack for
                                # cron queueing/quota-exhaustion cycles without a real per-cycle commit
    return _ok("G-P", "Beat heartbeat commit freshness", not stale,
               f"last 'excava-beat #N' commit {age_h:.1f}h ago" +
               (" — STALE: the dedicated heartbeat loop isn't landing per-cycle commits (check for "
                "a wedged/queued excava_beat.yml run)." if stale else "."), "warn")


def _load_json(p, d):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return d


CHECKS = [g_quarantine, g_msgfile, g_backup, g_mojibake, g_build_align, g_json,
          g_remote_sync, g_collisions, g_handoff, g_memory, g_auditlog, g_watchdog, g_movement,
          g_disk, g_localfuel, g_beat_heartbeat]


def run() -> dict:
    # 2026-07-27 (fire 21): g_remote_sync and g_beat_heartbeat both read the LOCAL cached
    # `origin/main` ref. standing_checks.py fetches before calling here, so it's always fresh —
    # but `python -m src.guardrails` run on its own (as this fire itself just did) reads
    # whatever origin/main happened to be cached at container-start, producing a phantom
    # "50 commits behind" / "38h stale beat" false alarm that four separate diagnoses already
    # traced to this exact cause (fires 16/17/19/20, AWAY_LOG.md). One quiet fetch here removes
    # the whole failure class instead of relying on the caller to remember it.
    subprocess.run(["git", "fetch", "origin", "main", "--quiet"], cwd=str(ROOT), capture_output=True)
    results = [c() for c in CHECKS]
    crit_fail = [r for r in results if not r["ok"] and r["severity"] == "critical"]
    status = {"generated_at": _now(), "total": len(results),
              "passing": sum(1 for r in results if r["ok"]),
              "critical_failures": len(crit_fail), "guardrails": results}
    STATUS.parent.mkdir(parents=True, exist_ok=True)
    STATUS.write_text(json.dumps(status, ensure_ascii=False, indent=1), encoding="utf-8")
    with LOG.open("a", encoding="utf-8") as fh:      # APPEND-only, never truncate
        fh.write(json.dumps({"at": status["generated_at"], "passing": status["passing"],
                             "total": status["total"], "critical_failures": status["critical_failures"],
                             "failed": [r["id"] for r in results if not r["ok"]]}, ensure_ascii=False) + "\n")
    return status


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    strict = "--strict" in sys.argv
    s = run()
    print(f"GUARDRAILS: {s['passing']}/{s['total']} passing · {s['critical_failures']} critical failure(s)")
    for r in s["guardrails"]:
        mark = "OK " if r["ok"] else ("XX " if r["severity"] == "critical" else "!! ")
        print(f"  {mark}{r['id']} {r['name']} — {r['detail']}")
    return 1 if (strict and s["critical_failures"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
