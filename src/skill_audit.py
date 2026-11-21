"""Scan stored skill records and distributed package files without executing them."""
import json
import subprocess
import tempfile
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def scan(root):
    data = root / "data"
    records = json.loads((data / "skills.json").read_text(encoding="utf-8"))["skills"]
    checks = defaultdict(list)
    packages = defaultdict(list)
    for pattern in ("skills/*", "other-skills/*/*"):
        for folder in root.glob(pattern):
            if folder.is_dir() and not folder.is_symlink():
                packages[folder.name].append(folder)
    with tempfile.TemporaryDirectory() as temp:
        staging = Path(temp)
        owners = {}
        def stage(slug, content):
            path = staging / str(len(owners))
            path.write_bytes(content)
            owners[str(path)] = slug
        for rec in records:
            slug = rec.get("slug") or rec.get("skill_name", "")
            stage(slug, json.dumps(rec, ensure_ascii=False).encode("utf-8"))
        for slug, folders in packages.items():
            for folder in folders:
                for path in folder.rglob("*"):
                    if path.is_symlink():
                        checks[slug].append("unscanned")
                    elif path.is_file():
                        stage(slug, path.read_bytes())
        run = subprocess.run(["clamscan", "--recursive", "--no-summary", "--alert-exceeds-max=yes",
                              "--alert-encrypted=yes", str(staging)], text=True, capture_output=True)
        if run.returncode not in (0, 1):
            raise RuntimeError("ClamAV scan failed: " + run.stderr[-500:])
        results = {}
        for line in run.stdout.splitlines():
            path, _, verdict = line.partition(": ")
            if path in owners:
                results[path] = ("detected" if verdict.endswith(" FOUND") else
                                 "no detection" if verdict == "OK" else "unscanned")
        for path, slug in owners.items():
            checks[slug].append(results.get(path, "unscanned"))
    return {"at": datetime.now(timezone.utc).isoformat(),
            "engine": subprocess.check_output(["clamscan", "--version"], text=True).strip(),
            "skills": {slug: {"result": "detected" if "detected" in items else
                              "unscanned" if "unscanned" in items else "no detection",
                              "package": bool(packages.get(slug))}
                       for slug, items in checks.items()}}


if __name__ == "__main__":
    report = scan(ROOT)
    target = ROOT / "data/skill_scan.json"
    target.write_text(json.dumps(report, ensure_ascii=False), encoding="utf-8")
    from collections import Counter
    print(dict(Counter(row["result"] for row in report["skills"].values())))
