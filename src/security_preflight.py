"""
src/security_preflight.py — SECURITY GATE before activating any third-party item.

We do NOT know the intentions of every tool/skill/MCP creator, so treat all of them as UNTRUSTED.
Given a GitHub repo (or an install command), this statically scans the code that WOULD run — install
scripts + source — for red flags that could hack or exfiltrate, BEFORE it runs, and returns a verdict
(safe | caution | dangerous | unknown) + the specific reasons. The Activator / EXCAVA must pass this
(and sandbox anything not clearly safe, with no secrets + no network) before executing. Free, stdlib.

Run:  python -m src.security_preflight https://github.com/owner/repo
"""
from __future__ import annotations

import json
import re
import sys
import urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36")

# (pattern, reason, severity) — tuned to catch MALICIOUS behavior, not normal code
DANGER = [
    (r"curl\s+\S+\s*\|\s*(sudo\s+)?(ba)?sh", "curl|bash: pipes a remote script straight into a shell", "dangerous"),
    (r"wget\s+\S+\s*\|\s*(ba)?sh", "wget|sh: pipes a remote script straight into a shell", "dangerous"),
    (r"(\.ssh/|id_rsa|\.aws/credentials|\.npmrc|/etc/passwd|\.config/gcloud)", "reads SSH/AWS/credential files", "dangerous"),
    (r"(atob\(|base64\s*-?-?d(ecode)?|b64decode)[^\n]{0,60}(eval|exec|Function\s*\()", "runs obfuscated / base64-decoded code", "dangerous"),
    (r"(keylog|screencapture|clipboard\.(read|paste)|GetAsyncKeyState)", "captures keystrokes / screen / clipboard", "dangerous"),
    (r"(coinhive|cryptonight|stratum\+tcp|xmrig|miner\.start)", "crypto-mining indicators", "dangerous"),
    (r"(eval\(|child_process\.exec|os\.system|subprocess\.(call|Popen|run)\()", "executes dynamic / shell commands", "caution"),
    (r"(process\.env|os\.environ)[^\n]{0,80}(fetch|axios|requests\.|urllib|http)", "may send environment/secrets over the network", "dangerous"),
]
POSTINSTALL = re.compile(r'"(pre|post)install"\s*:')


def _get(u: str) -> str:
    try:
        return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}),
                                      timeout=15).read().decode("utf-8", "replace")
    except Exception:
        return ""


def scan_repo(gh: str) -> dict:
    m = re.search(r"github\.com/([\w.-]+)/([\w.-]+)", gh or "")
    if not m:
        return {"verdict": "unknown", "reasons": ["No GitHub repo to inspect — treat as untrusted and run it in a sandbox first."], "repo": ""}
    owner, repo = m.group(1), m.group(2).replace(".git", "")
    reasons, sev = set(), "safe"
    for branch in ("main", "master"):
        got = False
        for f in ("package.json", "README.md", "install.sh", "setup.py", "index.js"):
            txt = _get(f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{f}")
            if not txt:
                continue
            got = True
            if f == "package.json" and POSTINSTALL.search(txt):
                reasons.add("Runs a pre/post-install script — code executes just from installing it.")
                sev = "caution" if sev == "safe" else sev
            for pat, why, s in DANGER:
                if re.search(pat, txt, re.I):
                    reasons.add(why)
                    if s == "dangerous":
                        sev = "dangerous"
                    elif sev == "safe":
                        sev = "caution"
        if got:
            break
    return {"verdict": sev, "reasons": sorted(reasons) or ["No obvious red flags found in install scripts / README."],
            "repo": f"{owner}/{repo}",
            "advice": ("Proceed." if sev == "safe" else
                       "Do NOT auto-run. Warn the user with these reasons, get explicit approval, and run it in an ISOLATED sandbox (no secrets, no network to your data). Use throwaway keys only.")}


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: python -m src.security_preflight <github url or repo>"); return 1
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    print(json.dumps(scan_repo(sys.argv[1]), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
