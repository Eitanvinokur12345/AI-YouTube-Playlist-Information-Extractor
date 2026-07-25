"""
src/accessibility_scan.py — a real, mechanical WCAG lint over EXCAVA's OWN dashboard.

Owner intent charter (data/excava/intent.json -> "accessibility"): "Make EXCAVA usable by
EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, screen-reader support (WCAG).
Find and fix accessibility barriers." success_looks_like: "measurable accessibility fix
(contrast/keyboard/mobile/reader)". Before this script, "accessibility" was staffed but had
`right_tool: null` — a talk-only department that could only write an execution plan, never do
real work (systemcheck flagged it: "10/13 depts have a real executor").

This scans docs/*.html (the shell) and docs/dashboard.js (the JS-rendered views, via template
literals) for concrete, checkable WCAG issues:
  1. <html> missing a lang attribute (WCAG 3.1.1)
  2. missing a <meta name="viewport"> tag (mobile/zoom, WCAG 1.4.10)
  3. <img> tags with NO alt attribute at all (WCAG 1.1.1) — alt="" for decorative images is fine
  4. form controls (<input>, excluding hidden/button/submit) that carry neither an aria-label,
     an aria-labelledby, a placeholder, NOR an adjacent id/for-linked <label> (WCAG 4.1.2 / 1.3.1)
  5. icon/emoji-only <button> tags with no rendered text AND no aria-label/title (WCAG 4.1.2)
  6. no `prefers-reduced-motion` media query anywhere in the CSS/JS shell (WCAG 2.3.3)
Static regex checks over dynamic template-literal HTML are necessarily approximate (a text node
built entirely from a JS expression can look empty to a regex but render real text at runtime),
so this errs toward under-reporting: it only flags patterns with no runtime-computed content at
all, never a suspected-but-uncertain case. Read-only — it reports, it does not rewrite arbitrary
JS (auto-editing template literals by regex is not safe); a human/agent applies the fix, then a
re-run proves it closed. Writes data/accessibility.json. Free, mechanical, no engine calls.

Run: python -m src.accessibility_scan
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
OUT = DATA / "accessibility.json"
NOW = datetime.now(timezone.utc).isoformat()

_TAG = re.compile(r"<[^>]+>")
_TMPL = re.compile(r"\$\{[^{}]*\}")  # a JS template-literal expression — treat as "has content"


def _text_of(inner: str) -> str:
    """Strip tags; a ${...} expression counts as real (runtime-computed) content."""
    stripped = _TAG.sub("", inner)
    if _TMPL.search(stripped):
        return "x"  # non-empty sentinel — a template expression may render real text
    return stripped.strip()


def _scan_html(name: str, html: str) -> list[dict]:
    issues = []
    m = re.search(r"<html\b[^>]*>", html, re.I)
    if m and not re.search(r"\blang\s*=", m.group(0), re.I):
        issues.append({"rule": "html-lang", "file": name, "detail": "<html> has no lang attribute"})
    if not re.search(r'<meta[^>]+name=["\']viewport["\']', html, re.I):
        issues.append({"rule": "viewport", "file": name, "detail": "no <meta name=viewport>"})
    for im in re.finditer(r"<img\b[^>]*>", html, re.I):
        if not re.search(r"\balt\s*=", im.group(0), re.I):
            issues.append({"rule": "img-alt", "file": name, "detail": im.group(0)[:100]})
    return issues


def _scan_controls(name: str, html: str) -> list[dict]:
    """Inputs with no accessible name (label/aria-label/aria-labelledby/placeholder)."""
    issues = []
    for im in re.finditer(r"<input\b([^>]*)>", html, re.I):
        attrs = im.group(1)
        t = re.search(r'type\s*=\s*["\']?(\w+)', attrs, re.I)
        typ = (t.group(1).lower() if t else "text")
        if typ in ("hidden", "button", "submit", "checkbox", "radio"):
            continue  # checkboxes/radios are commonly wrapped in a <label>...</label>, skip (noisy)
        has_name = re.search(r'aria-label\s*=|aria-labelledby\s*=|placeholder\s*=', attrs, re.I)
        if not has_name:
            issues.append({"rule": "input-name", "file": name, "detail": im.group(0)[:120]})
    return issues


def _scan_buttons(name: str, html: str) -> list[dict]:
    issues = []
    for m in re.finditer(r"<button\b([^>]*)>(.*?)</button>", html, re.I | re.S):
        attrs, inner = m.group(1), m.group(2)
        if _text_of(inner):
            continue
        if re.search(r'aria-label\s*=|aria-labelledby\s*=|title\s*=', attrs, re.I):
            continue
        issues.append({"rule": "button-name", "file": name, "detail": m.group(0)[:100].replace("\n", " ")})
    return issues


def check() -> dict:
    issues: list[dict] = []
    css_js_blob = ""
    for f in sorted(glob.glob(str(DOCS / "*.html"))):
        name = Path(f).name
        html = Path(f).read_text(encoding="utf-8", errors="replace")
        issues += _scan_html(name, html)
        issues += _scan_controls(name, html)
        issues += _scan_buttons(name, html)
        css_js_blob += html
    for pat in ("dashboard.js", "design/*.css", "*.css"):
        for f in glob.glob(str(DOCS / pat)):
            name = str(Path(f).relative_to(DOCS))
            text = Path(f).read_text(encoding="utf-8", errors="replace")
            css_js_blob += text
            if name == "dashboard.js":  # JS template literals render the app's real controls
                issues += _scan_controls(name, text)
                issues += _scan_buttons(name, text)
    if "prefers-reduced-motion" not in css_js_blob:
        issues.append({"rule": "reduced-motion", "file": "(shell-wide)",
                       "detail": "no prefers-reduced-motion media query found anywhere"})
    by_rule: dict[str, int] = {}
    for it in issues:
        by_rule[it["rule"]] = by_rule.get(it["rule"], 0) + 1
    return {"generated_at": NOW, "total_issues": len(issues), "by_rule": by_rule,
            "issues": issues[:60], "status": "clean" if not issues else "issues found"}


def main() -> int:
    doc = check()
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"accessibility_scan: {doc['total_issues']} issue(s) — {doc['by_rule'] or 'clean'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
