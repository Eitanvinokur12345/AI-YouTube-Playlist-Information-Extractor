"""
src/security_scan.py — pipeline SECURITY: secret-leak scan + prompt-injection guard.

Two real risks for a system that ingests external web/video content and exposes a public hub + an
activator that other agents act on:
  1. A secret/API key accidentally committed into the data (it must NEVER leak to the public repo).
  2. Prompt-injection hidden in scraped/transcribed content ("ignore previous instructions...") that
     could hijack the activator or the future OS, since they read hub records.
This scans the data files for both, marks injection-suspect records `injection_risk: true` (so the
activator/OS treat them as DATA, never commands), writes data/security.json, and queues criticals.
Complements safety_check.py (which rates connectors safe/caution/risky). Free, mechanical.

Run:  python -m src.security_scan
"""
from __future__ import annotations

import glob
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "security.json"
TASKS = DATA / "improvement_tasks.json"
NOW = datetime.now(timezone.utc).isoformat()

SECRET_PATS = [
    ("OpenAI", re.compile(r"sk-[A-Za-z0-9]{20,}")),
    ("Google/Gemini", re.compile(r"AIza[0-9A-Za-z_\-]{30,}")),
    ("GitHub", re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}")),
    ("AWS", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("Anthropic", re.compile(r"sk-ant-[A-Za-z0-9\-]{20,}")),
    ("Slack", re.compile(r"xox[baprs]-[A-Za-z0-9\-]{10,}")),
]
INJECT_PATS = [re.compile(p, re.I) for p in [
    r"ignore (all )?(the )?previous instructions", r"disregard (the )?above", r"you are now",
    r"new instructions:", r"system prompt", r"do not follow", r"jailbreak", r"\bDAN mode\b",
    r"pretend you are", r"forget everything", r"reveal your (system )?prompt", r"exfiltrat"]]


def main() -> int:
    files = glob.glob(str(DATA / "*.json"))
    leaks = []
    inj_flagged = 0
    inj_samples = []
    for f in files:
        if Path(f).name in ("security.json",):
            continue
        try:
            raw = open(f, encoding="utf-8").read()
        except Exception:
            continue
        for label, pat in SECRET_PATS:
            for m in pat.findall(raw):
                leaks.append({"file": Path(f).name, "type": label, "sample": m[:6] + "…"})

    # injection scan over record text; mark suspect records so downstream treats them as data
    for fname, key, fields in [("skills.json", "skills", ("description", "use_case", "tips")),
                               ("tools.json", "tools", ("description",)),
                               ("prompts.json", "prompts", ("purpose", "prompt_text")),
                               ("connectors.json", "connectors", ("what_it_does", "description"))]:
        p = DATA / fname
        try:
            d = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        items = d.get(key, []) if isinstance(d, dict) else []
        changed = False
        for it in items:
            text = " ".join(str(it.get(x, "")) for x in fields)
            hit = any(pat.search(text) for pat in INJECT_PATS)
            if hit and not it.get("injection_risk"):
                it["injection_risk"] = True
                inj_flagged += 1
                if len(inj_samples) < 6:
                    inj_samples.append(it.get("name") or it.get("skill_name") or it.get("title"))
                changed = True
            elif not hit and it.get("injection_risk"):
                it.pop("injection_risk", None); changed = True
        if changed:
            json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    OUT.write_text(json.dumps({"generated_at": NOW, "secret_leaks": leaks,
                               "injection_flagged": inj_flagged, "injection_samples": inj_samples,
                               "status": "CRITICAL: secrets in data" if leaks else "clean"},
                              ensure_ascii=False, indent=2), encoding="utf-8")

    if leaks:  # a leaked secret is critical — queue it loudly
        tj = json.load(open(TASKS, encoding="utf-8")) if TASKS.exists() else {"tasks": []}
        tasks = tj.get("tasks", [])
        if not any(t.get("sec_key") == "leak" for t in tasks):
            tasks.append({"sec_key": "leak", "kind": "security",
                          "question": f"[SECURITY] {len(leaks)} secret-like string(s) found IN DATA",
                          "fix": "Remove the secret from the data + git history and rotate the key immediately.",
                          "status": "open", "created_at": NOW})
            TASKS.write_text(json.dumps({"updated_at": NOW, "tasks": tasks}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"security_scan: {len(leaks)} secret leak(s), {inj_flagged} injection-suspect records flagged.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
