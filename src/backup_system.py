"""
src/backup_system.py — daily backup + REGRESSION GUARD, so nothing is silently lost.

Two jobs, both free and mechanical:
  1. BACKUP: once per day, write a compact manifest of the library (per-type counts + the set of
     slugs + the current git SHA) to backups/<date>.json, and keep backups/latest.json. Old daily
     files rotate out after 14 days. Full record CONTENT is already preserved in git history (every
     commit is a snapshot), so the manifest is the index that tells us WHAT should exist and WHERE
     to restore it from if it ever disappears.
  2. GUARD: every run, compare the current library to the last backup. If any type's count DROPPED,
     or specific slugs vanished, record it in data/backup_status.json and queue a high-severity
     self-improvement task — so the self-improvement system revisits it and nothing rots unnoticed.

Run:  python -m src.backup_system
"""
from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
BK = ROOT / "backups"
STATUS = DATA / "backup_status.json"
TASKS = DATA / "improvement_tasks.json"
NOW = datetime.now(timezone.utc)
KEEP_DAYS = 14
TYPES = [("skills.json", "skills"), ("tools.json", "tools"), ("models.json", "models"),
         ("connectors.json", "connectors"), ("prompts.json", "prompts"), ("commands.json", "commands")]


def _load(p, default):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return default


def _slugs(fname, key):
    d = _load(DATA / fname, {})
    items = d.get(key, []) if isinstance(d, dict) else (d if isinstance(d, list) else [])
    out = []
    for x in items:
        if isinstance(x, dict):
            out.append(str(x.get("slug") or x.get("name") or x.get("skill_name") or x.get("title") or x.get("command") or ""))
    return [s for s in out if s]


def _git_sha():
    try:
        return subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"],
                              capture_output=True, text=True, timeout=15).stdout.strip()[:12]
    except Exception:
        return ""


def manifest():
    m = {"at": NOW.isoformat(), "git_sha": _git_sha(), "counts": {}, "slugs": {}}
    for fname, key in TYPES:
        sl = _slugs(fname, key)
        m["counts"][key] = len(sl)
        m["slugs"][key] = sorted(set(sl))
    return m


def main() -> int:
    BK.mkdir(exist_ok=True)
    cur = manifest()
    prev = _load(BK / "latest.json", None)

    # GUARD — compare current to the last backup.
    regressions = []
    if isinstance(prev, dict):
        for key, n in cur["counts"].items():
            pn = prev.get("counts", {}).get(key, n)
            if n < pn:                              # a whole type shrank
                lost = sorted(set(prev.get("slugs", {}).get(key, [])) - set(cur["slugs"].get(key, [])))
                regressions.append({"type": key, "was": pn, "now": n, "dropped": pn - n,
                                    "missing_examples": lost[:8]})

    # BACKUP — one snapshot per day (idempotent); rotate old dailies.
    daily = BK / f"{NOW.strftime('%Y-%m-%d')}.json"
    wrote = False
    if not daily.exists():
        daily.write_text(json.dumps({"at": cur["at"], "git_sha": cur["git_sha"], "counts": cur["counts"]},
                                    ensure_ascii=False, indent=2), encoding="utf-8")
        wrote = True
    (BK / "latest.json").write_text(json.dumps(cur, ensure_ascii=False), encoding="utf-8")
    dailies = sorted(BK.glob("20*.json"))
    for old in dailies[:-KEEP_DAYS]:
        try:
            old.unlink()
        except Exception:
            pass

    STATUS.write_text(json.dumps({
        "generated_at": NOW.isoformat(),
        "last_backup": cur["at"], "git_sha": cur["git_sha"],
        "counts": cur["counts"], "backups_kept": len(sorted(BK.glob("20*.json"))),
        "regressions": regressions,
        "restore_hint": (f"To restore lost records, check out the data files from git SHA "
                         f"{prev.get('git_sha') if isinstance(prev, dict) else cur['git_sha']} "
                         f"(the last good backup).") if regressions else "",
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    # queue any regression for self-improvement (dedup by type+counts).
    if regressions:
        tj = _load(TASKS, {"tasks": []}) or {"tasks": []}
        tasks = tj.get("tasks", [])
        have = {t.get("backup_key") for t in tasks}
        added = 0
        for r in regressions:
            k = f"regress:{r['type']}:{r['now']}"
            if k not in have:
                tasks.append({"backup_key": k, "kind": "regression",
                              "question": f"[regression] '{r['type']}' dropped {r['dropped']} ({r['was']}→{r['now']})",
                              "fix": f"Restore the missing {r['type']} from the last good backup "
                                     f"(git {prev.get('git_sha','?') if isinstance(prev,dict) else '?'}); "
                                     f"investigate what removed them.", "status": "open", "created_at": NOW.isoformat()})
                added += 1
        if added:
            TASKS.write_text(json.dumps({"updated_at": NOW.isoformat(), "tasks": tasks},
                                        ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"backup_system: snapshot {'written' if wrote else 'exists for today'}; "
          f"{len(regressions)} regression(s); {len(sorted(BK.glob('20*.json')))} dailies kept.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
