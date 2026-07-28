"""
src/merge_json_array_conflict.py — generic conflict resolver for JSON-array data files.

During the "pull --rebase, else merge" recovery in every scheduled lane's "Commit results" step,
a same-day double-write on a shared JSON file (e.g. data/designs.json, appended to by both the
mine and visual lanes) triggers a real merge conflict. The existing recovery only auto-resolves
data/data_guard.json (stateless, no unique history) "in our favor" and leaves any other conflict
unresolved on purpose, so the whole commit — and with it every OTHER file this run touched
(skills/tools/models/...) — is dropped and "push skipped" is reported as a success.

This resolves that for JSON files shaped like {"<array_key>": [ {..., "<dedup_key>": ...}, ... ]}:
read both conflicting blobs straight from the git index (stage 2 = ours, stage 3 = theirs — no
working-tree conflict markers to parse), union the array by the dedup key (both sides' unique
entries are kept; on a same-key collision "ours" wins since it's this run's fresher pass), and
write the merged result back so the file can be staged and the commit can proceed. Real content
from both sides survives instead of one side being silently discarded.

Usage: python -m src.merge_json_array_conflict <path> <array_key> <dedup_key>
Exits 0 and rewrites <path> on success. Exits 1 and leaves <path> untouched if it isn't actually
mid-conflict in the expected shape (caller should treat that as "nothing to do here" and fall
back to leaving the conflict unresolved, same as before this script existed).
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def _read_stage(path: str, stage: str):
    try:
        out = subprocess.run(["git", "show", f":{stage}:{path}"], capture_output=True,
                              text=True, timeout=15)
        if out.returncode != 0 or not out.stdout.strip():
            return None
        return json.loads(out.stdout)
    except Exception:
        return None


def main() -> int:
    if len(sys.argv) != 4:
        print("usage: merge_json_array_conflict <path> <array_key> <dedup_key>")
        return 1
    path, array_key, dedup_key = sys.argv[1], sys.argv[2], sys.argv[3]

    ours = _read_stage(path, "2")
    theirs = _read_stage(path, "3")
    if not isinstance(ours, dict) or not isinstance(theirs, dict):
        return 1
    ours_arr, theirs_arr = ours.get(array_key), theirs.get(array_key)
    if not isinstance(ours_arr, list) or not isinstance(theirs_arr, list):
        return 1

    merged = {}
    for item in theirs_arr:
        if isinstance(item, dict) and item.get(dedup_key):
            merged[item[dedup_key]] = item
    for item in ours_arr:  # ours wins on a same-key collision — it's this run's fresher pass
        if isinstance(item, dict) and item.get(dedup_key):
            merged[item[dedup_key]] = item

    out = dict(ours)
    out[array_key] = list(merged.values())
    Path(path).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"merge_json_array_conflict: {path} — {len(theirs_arr)} (theirs) + {len(ours_arr)} "
          f"(ours) -> {len(merged)} unique by '{dedup_key}'")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
