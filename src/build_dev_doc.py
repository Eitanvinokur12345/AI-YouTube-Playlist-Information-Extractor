"""
src/build_dev_doc.py — keep the dashboard's Dev Construction tab TECHNICAL and CURRENT.

The owner wants the Dev tab to show "the real technical stuff of how it all happens." Hand-written
sections go stale; this generates accurate REFERENCE sections straight from the repo — the actual
workflow schedules, the Python modules, and the data-file schemas — and merges them with the
curated narrative sections (the numbered ones) already in data/dev_construction.json.

Auto sections are titled "A./B./C. … (auto)" and are fully regenerated each run; curated sections
(titles starting with a digit) are preserved. Stdlib only; wire into a workflow to self-refresh.

Usage:  python -m src.build_dev_doc
"""
from __future__ import annotations

import glob
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
WF = ROOT / ".github" / "workflows"
SRC = ROOT / "src"
OUT = DATA / "dev_construction.json"


def workflows_section() -> str:
    rows = []
    for f in sorted(glob.glob(str(WF / "*.yml"))):
        txt = Path(f).read_text(encoding="utf-8", errors="replace")
        name = (re.search(r'^name:\s*(.+)$', txt, re.M) or [None, Path(f).stem])[1].strip().strip('"')
        crons = re.findall(r'cron:\s*"([^"]+)"', txt)
        triggers = [t for t in ("schedule", "workflow_dispatch", "push", "issue_comment",
                                "pull_request", "issues") if re.search(rf'^\s*{t}:', txt, re.M)]
        when = ("; ".join(crons) if crons else "—")
        rows.append(f"- **{name}** (`{Path(f).name}`) — triggers: {', '.join(triggers) or '—'}; cron: {when}")
    return ("The cloud pipeline = these GitHub Actions workflows (all free on the public repo). "
            "Schedules are UTC.\n\n" + "\n".join(rows))


def modules_section() -> str:
    rows = []
    for f in sorted(glob.glob(str(SRC / "*.py"))):
        n = Path(f).name
        if n == "__init__.py":
            continue
        txt = Path(f).read_text(encoding="utf-8", errors="replace")
        m = re.search(r'"""(.*?)"""', txt, re.S)
        first = ""
        if m:
            for line in m.group(1).strip().splitlines():
                line = line.strip()
                if line:
                    first = line
                    break
        rows.append(f"- `src/{n}` — {first or '(no docstring)'}")
    return "Every Python module in `src/` and its one-line purpose:\n\n" + "\n".join(rows)


def data_schema_section() -> str:
    rows = []
    for f in sorted(glob.glob(str(DATA / "*.json"))):
        n = Path(f).name
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        if isinstance(d, dict):
            # find the main array key, if any
            arr = [(k, len(v)) for k, v in d.items() if isinstance(v, list)]
            if arr:
                k, c = max(arr, key=lambda x: x[1])
                fields = list(d[k][0].keys())[:10] if d[k] and isinstance(d[k][0], dict) else []
                rows.append(f"- `data/{n}` — `{{{k}: [{c}]}}`" + (f"; item fields: {', '.join(fields)}" if fields else ""))
            else:
                rows.append(f"- `data/{n}` — object, keys: {', '.join(list(d.keys())[:8])}")
        elif isinstance(d, list):
            rows.append(f"- `data/{n}` — array of {len(d)}")
    return ("The committed JSON the dashboard + external systems read (see HUB_API.md for the public "
            "manifest):\n\n" + "\n".join(rows))


def main() -> int:
    doc = {}
    if OUT.exists():
        try:
            doc = json.load(open(OUT, encoding="utf-8"))
        except Exception:
            doc = {}
    # keep curated narrative sections (titles that start with a digit), drop old auto ones
    curated = [s for s in doc.get("sections", [])
               if re.match(r'^\s*\d', str(s.get("title", "")))]
    auto = [
        {"title": "A. Workflows & schedules (auto)", "body": workflows_section()},
        {"title": "B. Python modules (auto)", "body": modules_section()},
        {"title": "C. Data files & schemas (auto)", "body": data_schema_section()},
    ]
    doc["title"] = doc.get("title", "Developer Construction — how Excavatortron is built")
    doc["intro"] = doc.get("intro", "A precise, current description of every part of Excavatortron "
                           "and exactly how it works.")
    doc["updated_at"] = datetime.now(timezone.utc).isoformat()
    doc["sections"] = curated + auto
    json.dump(doc, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"dev doc: {len(curated)} curated + {len(auto)} auto sections -> {OUT.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
