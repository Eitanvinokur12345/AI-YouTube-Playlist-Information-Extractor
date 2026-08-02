"""
src/git_merge_resolve_test.py — proves `git_merge_resolve.resolve()` against a REAL git
conflict, not a hand-simulated one. Builds a throwaway bare origin + two clones in a temp dir,
diverges them on a whitelisted file, a *.jsonl append-log, and data/designs.json all at once,
then runs the actual module functions against the real conflicted worktree.

Run: python -m src.git_merge_resolve_test
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import src.git_merge_resolve as gmr


def _run(args, cwd):
    r = subprocess.run(["git", *args], cwd=str(cwd), text=True, capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed in {cwd}:\n{r.stderr or r.stdout}")
    return r.stdout


def build_conflict(tmp: Path):
    origin = tmp / "origin.git"
    a = tmp / "clone_a"
    b = tmp / "clone_b"
    _run(["init", "--bare", str(origin)], tmp)
    _run(["clone", str(origin), str(a)], tmp)
    for repo in (a,):
        _run(["config", "user.email", "t@t.com"], repo)
        _run(["config", "user.name", "t"], repo)

    (a / "data").mkdir(parents=True, exist_ok=True)
    (a / "data" / "data_guard.json").write_text('{"v": 0}', encoding="utf-8")
    (a / "data" / "history.jsonl").write_text('{"e": "base"}\n', encoding="utf-8")
    (a / "data" / "designs.json").write_text(
        json.dumps({"designs": [{"slug": "base-design"}], "updated_at": "2026-01-01T00:00Z"}),
        encoding="utf-8")
    (a / "data" / "unrelated_source.py").write_text("x = 1\n", encoding="utf-8")
    _run(["add", "."], a)
    _run(["commit", "-m", "base"], a)
    _run(["push", "origin", "HEAD:main"], a)

    _run(["clone", "-b", "main", str(origin), str(b)], tmp)
    for repo in (b,):
        _run(["config", "user.email", "t@t.com"], repo)
        _run(["config", "user.name", "t"], repo)

    # clone A pushes first: whitelisted file changes + a new jsonl row + a new design.
    (a / "data" / "data_guard.json").write_text('{"v": 1}', encoding="utf-8")
    (a / "data" / "history.jsonl").write_text('{"e": "base"}\n{"e": "from_a"}\n', encoding="utf-8")
    (a / "data" / "designs.json").write_text(
        json.dumps({"designs": [{"slug": "base-design"}, {"slug": "a-design"}],
                    "updated_at": "2026-08-02T01:00Z"}), encoding="utf-8")
    _run(["add", "."], a)
    _run(["commit", "-m", "from A"], a)
    _run(["push", "origin", "HEAD:main"], a)

    # clone B diverges locally on the SAME files before syncing.
    (b / "data" / "data_guard.json").write_text('{"v": 2}', encoding="utf-8")
    (b / "data" / "history.jsonl").write_text('{"e": "base"}\n{"e": "from_b"}\n', encoding="utf-8")
    (b / "data" / "designs.json").write_text(
        json.dumps({"designs": [{"slug": "base-design"}, {"slug": "b-design"}],
                    "updated_at": "2026-08-02T02:00Z"}), encoding="utf-8")
    _run(["add", "."], b)
    _run(["commit", "-m", "from B"], b)

    # B's pull now conflicts on all three files.
    r = subprocess.run(["git", "pull", "--no-rebase", "--no-edit", "origin", "main"],
                        cwd=str(b), text=True, capture_output=True)
    assert r.returncode != 0, "expected the pull to conflict — test setup is wrong"
    return b


def run() -> dict:
    checks = []
    tmp = Path(tempfile.mkdtemp(prefix="gmr_test_"))
    try:
        b = build_conflict(tmp)

        # Point the module at this throwaway repo instead of the real one.
        real_root = gmr.ROOT
        gmr.ROOT = b
        try:
            conflicts = gmr.conflicted_files()
            checks.append(("conflict_detected_all_three",
                            set(conflicts) >= {"data/data_guard.json", "data/history.jsonl", "data/designs.json"}))

            ok = gmr.resolve()
            checks.append(("commit_succeeded", ok is True))

            merged_guard = json.loads((b / "data" / "data_guard.json").read_text())
            checks.append(("whitelist_took_ours", merged_guard == {"v": 2}))

            hist_lines = (b / "data" / "history.jsonl").read_text().splitlines()
            checks.append(("jsonl_union_kept_both",
                            "{\"e\": \"from_a\"}" in hist_lines and "{\"e\": \"from_b\"}" in hist_lines))

            designs = json.loads((b / "data" / "designs.json").read_text())
            slugs = {d["slug"] for d in designs["designs"]}
            checks.append(("designs_union_kept_both",
                            slugs == {"base-design", "a-design", "b-design"}))
            checks.append(("designs_updated_at_took_newer", designs["updated_at"] == "2026-08-02T02:00Z"))

            log = _run(["log", "--oneline", "-1"], b)
            checks.append(("no_conflict_markers_committed",
                            "<<<<<<<" not in (b / "data" / "history.jsonl").read_text()
                            and "<<<<<<<" not in (b / "data" / "designs.json").read_text()))
        finally:
            gmr.ROOT = real_root
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    passed = sum(1 for _, ok in checks if ok)
    return {"passed": passed, "total": len(checks), "checks": checks}


def main() -> int:
    result = run()
    for name, ok in result["checks"]:
        print(("OK " if ok else "!! ") + name)
    print(f"{result['passed']}/{result['total']} checks passed")
    return 0 if result["passed"] == result["total"] else 1


if __name__ == "__main__":
    sys.exit(main())
