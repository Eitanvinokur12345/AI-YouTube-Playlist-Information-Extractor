"""
src/accessibility_scan.py — REAL executor for the `accessibility` department (owner charter,
data/excava/agents.json: "make EXCAVA usable by EVERYONE — colour contrast, mobile/touch targets,
reduced-motion, keyboard navigation and screen-reader support (WCAG); find and fix accessibility
barriers"). Was talk_only (systemcheck 2026-07-25): every task got an honest but NEVER-executed
plan. This scans EXCAVA's own UI shells for real, cheap, deterministic WCAG-lite issues and writes
data/accessibility.json — the same "REAL_TOOL, honest output" contract as security_scan.py /
power_scan.py. Free, mechanical, bounded — no browser, no network.

Run:  python -m src.accessibility_scan
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "accessibility.json"
NOW = datetime.now(timezone.utc).isoformat()

# EXCAVA's own interface shells (visualization/accessibility's charter — NOT mined external designs).
UI_FILES = ["docs/index.html", "launcher/index.html"]

IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
ALT_RE = re.compile(r"\balt\s*=", re.I)
HTML_TAG_RE = re.compile(r"<html\b[^>]*>", re.I)
LANG_RE = re.compile(r"\blang\s*=", re.I)
VIEWPORT_RE = re.compile(r'<meta[^>]+name=["\']viewport["\']', re.I)
REDUCED_MOTION_RE = re.compile(r"prefers-reduced-motion", re.I)
CLICK_DIV_RE = re.compile(r"<(div|span)\b(?![^>]*\brole\s*=)[^>]*\bonclick\s*=", re.I)


def _scan_file(rel: str) -> dict:
    p = ROOT / rel
    if not p.exists():
        return {"file": rel, "skipped": "not found"}
    text = p.read_text(encoding="utf-8", errors="replace")
    issues = []

    m = HTML_TAG_RE.search(text)
    if not m or not LANG_RE.search(m.group(0)):
        issues.append({"rule": "html-lang", "wcag": "3.1.1", "detail": "<html> has no lang attribute"})

    if not VIEWPORT_RE.search(text):
        issues.append({"rule": "viewport-meta", "wcag": "1.4.10", "detail": "no <meta name=viewport> — mobile reflow at risk"})

    imgs = IMG_RE.findall(text)
    missing_alt = [i for i in imgs if not ALT_RE.search(i)]
    if missing_alt:
        issues.append({"rule": "img-alt", "wcag": "1.1.1",
                       "detail": f"{len(missing_alt)}/{len(imgs)} <img> tag(s) missing an alt attribute"})

    click_divs = CLICK_DIV_RE.findall(text)
    if click_divs:
        issues.append({"rule": "clickable-div-no-role", "wcag": "2.1.1 / 4.1.2",
                       "detail": f"{len(click_divs)} <div>/<span onclick> with no role= — not reachable/announced for keyboard/screen-reader users"})

    if not REDUCED_MOTION_RE.search(text):
        issues.append({"rule": "reduced-motion", "wcag": "2.3.3",
                       "detail": "no @media (prefers-reduced-motion) rule found — animations can't be turned down"})

    return {"file": rel, "img_count": len(imgs), "issues": issues}


def main() -> int:
    results = [r for f in UI_FILES if (r := _scan_file(f)).get("issues") is not None or "skipped" in r]
    total_issues = sum(len(r.get("issues", [])) for r in results)
    by_rule: dict[str, int] = {}
    for r in results:
        for iss in r.get("issues", []):
            by_rule[iss["rule"]] = by_rule.get(iss["rule"], 0) + 1
    top = max(by_rule, key=by_rule.get) if by_rule else None

    OUT.write_text(json.dumps({
        "generated_at": NOW,
        "files_scanned": len([r for r in results if "skipped" not in r]),
        "total_issues": total_issues,
        "by_rule": by_rule,
        "results": results,
        "status": "clean" if total_issues == 0 else f"{total_issues} issue(s) — see by_rule",
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"accessibility_scan: {total_issues} issue(s) across {len(UI_FILES)} UI file(s)"
          + (f", most common: {top} ({by_rule[top]}x)" if top else " — clean"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
