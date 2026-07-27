"""
src/liveliness_scan.py — a real, mechanical scan over EXCAVA's OWN dashboard for the
"visualization" department (data/excava/intent.json -> "visualization"): "Own EXCAVA'S OWN
interface — visibility, liveliness, clarity, enjoyment, speed of OUR screens." HARD BOUNDARY
(owner 2026-07-12): NOT hunting external designs — that belongs to "visual"; this department
only tends the screens EXCAVA itself ships. success_looks_like: "measurable clarity/liveliness
improvement the owner can see." Before this script, "visualization" was staffed with
`right_tool: null` — talk-only, unable to do real work (systemcheck flagged it as the last
department still stuck at talk_only once accessibility got `src.accessibility_scan`).

This checks three concrete, checkable things over docs/*.html + docs/dashboard.js:
  1. Broken local asset refs — a src=/href= pointing at a same-repo file (docs/... or a
     docs-relative path) that does not actually exist on disk. A dead reference is a real,
     visible break (a missing icon, a 404'd stylesheet) — exactly "visibility" the charter names.
  2. Shipped placeholder text — "Lorem ipsum", bare "TODO"/"FIXME", or a leaked JS artifact
     ("undefined", "NaN", "[object Object]") sitting in STATIC markup (outside a ${...} template
     expression, which legitimately renders those tokens as code, not content). Deliberately
     excludes "Coming Soon" — that's a real, intentional tab name (the upcoming-tools view), not
     unfinished-content boilerplate; a naive check flagged it as a false positive on first run.
  3. Data liveliness — every data/*.json file dashboard.js actually fetches must exist, parse,
     and carry a NON-EMPTY payload (a `len() == 0` top-level list/dict is a screen with nothing
     to show, the "liveliness" the charter is about) — flags an empty/tiny/unreadable data
     source that would render a blank or stub tab.
Static regex checks over a JS-templated shell are necessarily approximate (see
accessibility_scan.py's identical caveat), so this errs toward under-reporting: only exact,
checkable breaks are flagged, never a suspected-but-uncertain one. Read-only — it reports, it
does not rewrite HTML/JS or regenerate data; a human/agent applies the fix, then a re-run proves
it closed. Writes data/visualization.json. Free, mechanical, no engine calls.

Run: python -m src.liveliness_scan
"""
from __future__ import annotations

import glob
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"
OUT = DATA / "visualization.json"
NOW = datetime.now(timezone.utc).isoformat()

_TMPL = re.compile(r"\$\{[^{}]*\}")
_PLACEHOLDER_PATTERNS = (
    ("lorem-ipsum", re.compile(r"lorem ipsum", re.I)),
    ("todo-fixme", re.compile(r"\b(TODO|FIXME)\b")),
    ("leaked-js-undefined", re.compile(r">\s*undefined\s*<")),
    ("leaked-js-nan", re.compile(r">\s*NaN\s*<")),
    ("leaked-js-object", re.compile(r"\[object Object\]")),
)


def _scan_broken_assets(name: str, html: str) -> list[dict]:
    """A local (non-http, non-anchor, non-mailto) src=/href= that doesn't resolve to a real file."""
    issues = []
    for m in re.finditer(r'\b(?:src|href)\s*=\s*["\']([^"\']+)["\']', html, re.I):
        ref = m.group(1).strip()
        if not ref or ref.startswith(("http://", "https://", "//", "#", "mailto:", "data:", "javascript:")):
            continue
        target = (DOCS / ref.split("#")[0].split("?")[0]).resolve()
        try:
            target.relative_to(ROOT.resolve())
        except ValueError:
            continue  # escaped the repo root — not ours to judge
        if not target.exists():
            issues.append({"rule": "broken-asset", "file": name, "detail": ref})
    return issues


def _scan_placeholders(name: str, html: str) -> list[dict]:
    issues = []
    # strip template-literal expressions first so `${x || "undefined"}`-style code isn't flagged
    stripped = _TMPL.sub("x", html)
    for rule, pat in _PLACEHOLDER_PATTERNS:
        for m in pat.finditer(stripped):
            issues.append({"rule": rule, "file": name, "detail": stripped[max(0, m.start() - 20):m.end() + 20].strip()})
    return issues


def _referenced_data_files() -> list[str]:
    js = (DOCS / "dashboard.js").read_text(encoding="utf-8", errors="replace") if (DOCS / "dashboard.js").exists() else ""
    return sorted(set(re.findall(r"data/[a-zA-Z0-9_./-]+\.json", js)))


def _scan_data_liveliness() -> list[dict]:
    issues = []
    for rel in _referenced_data_files():
        p = ROOT / rel
        if not p.exists():
            issues.append({"rule": "missing-data-source", "file": rel, "detail": "referenced by dashboard.js, not on disk"})
            continue
        try:
            doc = json.loads(p.read_text(encoding="utf-8", errors="replace"))
        except Exception as e:
            issues.append({"rule": "unreadable-data-source", "file": rel, "detail": type(e).__name__})
            continue
        size = len(doc) if isinstance(doc, (list, dict)) else None
        if size == 0:
            issues.append({"rule": "empty-data-source", "file": rel, "detail": "0 top-level entries — screen would render blank"})
    return issues


def check() -> dict:
    issues: list[dict] = []
    for f in sorted(glob.glob(str(DOCS / "*.html"))):
        name = Path(f).name
        html = Path(f).read_text(encoding="utf-8", errors="replace")
        issues += _scan_broken_assets(name, html)
        issues += _scan_placeholders(name, html)
    issues += _scan_data_liveliness()
    by_rule: dict[str, int] = {}
    for it in issues:
        by_rule[it["rule"]] = by_rule.get(it["rule"], 0) + 1
    return {"generated_at": NOW, "total_issues": len(issues), "by_rule": by_rule,
            "data_sources_checked": _referenced_data_files(),
            "issues": issues[:60], "status": "clean" if not issues else "issues found"}


def main() -> int:
    doc = check()
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"liveliness_scan: {doc['total_issues']} issue(s) — {doc['by_rule'] or 'clean'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
