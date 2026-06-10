"""
src/external_review.py  —  External "second opinion" for the review stage.
Run with:  python -m src.external_review

WHY THIS EXISTS
---------------
The review stage (REVIEW.md) has Claude review the system first across three
dimensions (usability, cut-the-bullshit, deep code bugs) and write
data/review_findings.json. This script then asks a DIFFERENT engine to verify
those findings and add anything Claude missed — a genuine second pair of eyes,
as the project owner asked ("first Claude checks, then external").

COST / PRIVACY  (the #1 rule: no human babysitting, no new paid cost)
---------------------------------------------------------------------
- Uses the free tier of the configured engine (default: Google Gemini).
- The API key is read ONLY from the environment variable named by
  config.review.external_engine.secret_name (default EXTERNAL_REVIEW_API_KEY),
  which is injected from a GitHub Actions secret. It is NEVER printed or written.
- GRACEFUL SKIP: if the key is absent, or the call fails for any reason (network,
  HTTP, quota, malformed JSON), this script writes a "skipped"/"error" marker
  into review_findings.json and exits 0. It must NEVER fail the workflow or block
  the (free, subscription-token) Claude review that already ran.

STDLIB ONLY. No new dependencies.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# Make sure we can print unicode on the cp1252 Windows runner without crashing.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config.json"
DEFAULT_FINDINGS = ROOT / "data" / "review_findings.json"

# Files we let the external engine look at (truncated) for context. Code + UI +
# the engine specs + a compact data snapshot. NEVER include secrets or .env.
CONTEXT_FILES = [
    "docs/index.html",
    "docs/dashboard.js",
    "src/fetch.py",
    "src/news.py",
    "CLAUDE.md",
    "IMPROVE.md",
    "data/index.json",
]
PER_FILE_CHARS = 6000          # keep the payload small enough for the free tier
NOW = datetime.now(timezone.utc).isoformat()


def load_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def stable_id(*parts: str) -> str:
    return hashlib.sha1("|".join(p or "" for p in parts).encode("utf-8")).hexdigest()[:10]


def write_findings(findings: dict) -> None:
    DEFAULT_FINDINGS.parent.mkdir(parents=True, exist_ok=True)
    DEFAULT_FINDINGS.write_text(
        json.dumps(findings, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def mark_external(findings: dict, status: str, reason: str = "", extra: dict | None = None) -> None:
    """Stamp the external reviewer status and persist. Always safe."""
    rev = findings.setdefault("reviewers", {})
    ext = rev.setdefault("external", {})
    ext.update({"status": status, "reason": reason, "ran_at": NOW})
    if extra:
        ext.update(extra)
    write_findings(findings)


def gather_context() -> str:
    chunks = []
    for rel in CONTEXT_FILES:
        p = ROOT / rel
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")[:PER_FILE_CHARS]
        except Exception:
            continue
        chunks.append(f"\n===== FILE: {rel} (first {PER_FILE_CHARS} chars) =====\n{txt}")
    return "".join(chunks)


def build_prompt(claude_findings: dict, context: str) -> str:
    claude_json = json.dumps(
        {
            "scores": claude_findings.get("scores", {}),
            "findings": claude_findings.get("findings", []),
            "benchmark": claude_findings.get("benchmark", {}),
        },
        ensure_ascii=False,
    )[:18000]
    return (
        "You are an independent senior reviewer giving a SECOND OPINION on an "
        "automated AI-skills dashboard project. Another reviewer (Claude) already "
        "reviewed it across three dimensions: usability (vs competitors Future "
        "Tools / There's An AI For That / Toolify / Product Hunt AI), "
        "'cut_the_bullshit' (vague/padded/hype content), and deep_code_bugs.\n\n"
        "Here are Claude's findings and scores:\n" + claude_json + "\n\n"
        "Here is project context (truncated source/UI/specs/data):\n" + context + "\n\n"
        "Return STRICT JSON ONLY, no prose, with this exact shape:\n"
        "{\n"
        '  "verified": [ {"id": "<claude finding id>", "agree": true, "note": "<short>"} ],\n'
        '  "added":    [ {"dimension":"usability|cut_the_bullshit|deep_code_bugs",'
        '"severity":"high|med|low","area":"dashboard|engine|data|workflow|security",'
        '"where":"<file:line or slug/tab>","detail":"<concrete>","suggestion":"<minimal fix>"} ],\n'
        '  "scores":   {"usability":0,"cut_the_bullshit":0,"deep_code_bugs":0},\n'
        '  "summary":  "<one short paragraph>"\n'
        "}\n"
        "Only include 'added' items that are REAL and that Claude missed. Be terse."
    )


def call_gemini(api_key: str, model: str, prompt: str, timeout: int) -> dict:
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
        f"?key={api_key}"
    )
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.3, "responseMimeType": "application/json"},
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    # Extract the model's text (which is itself JSON because of responseMimeType).
    text = payload["candidates"][0]["content"]["parts"][0]["text"]
    return json.loads(text)


def merge_external(findings: dict, model: str, result: dict) -> None:
    # 1) record verification notes back onto Claude's findings (by id)
    verdicts = {v.get("id"): v for v in result.get("verified", []) if isinstance(v, dict)}
    for f in findings.get("findings", []):
        v = verdicts.get(f.get("id"))
        if v:
            f["external_agree"] = bool(v.get("agree", True))
            f["external_note"] = (v.get("note") or "")[:300]
    # 2) append NEW findings the external engine raised (dedup by stable id)
    have = {f.get("id") for f in findings.get("findings", [])}
    added = 0
    for a in result.get("added", []):
        if not isinstance(a, dict):
            continue
        fid = stable_id(a.get("dimension", ""), a.get("where", ""), a.get("detail", ""))
        if fid in have:
            continue
        findings.setdefault("findings", []).append(
            {
                "id": fid,
                "dimension": a.get("dimension", "usability"),
                "severity": a.get("severity", "low"),
                "area": a.get("area", "dashboard"),
                "where": a.get("where", ""),
                "detail": (a.get("detail") or "")[:600],
                "suggestion": (a.get("suggestion") or "")[:400],
                "status": "open",
                "source": "external",
            }
        )
        have.add(fid)
        added += 1
    # 3) stamp the external reviewer block + its own scores
    rev = findings.setdefault("reviewers", {})
    rev["external"] = {
        "provider": "gemini",
        "model": model,
        "status": "ok",
        "ran_at": NOW,
        "added_findings": added,
        "scores": result.get("scores", {}),
        "summary": (result.get("summary") or "")[:800],
    }


def main() -> int:
    cfg = load_json(CONFIG, {})
    review = cfg.get("review", {}) or {}
    if not review.get("enabled", True):
        print("review disabled in config; nothing to do.")
        return 0

    eng = review.get("external_engine", {}) or {}
    secret_name = eng.get("secret_name", "EXTERNAL_REVIEW_API_KEY")
    model = eng.get("model", "gemini-2.0-flash")
    timeout = int(cfg.get("news", {}).get("request_timeout_seconds", 20))
    graceful = bool(eng.get("graceful_skip_if_absent", True))

    findings = load_json(
        DEFAULT_FINDINGS,
        {"generated_at": NOW, "mode": "weekly", "reviewers": {}, "findings": [], "history": []},
    )

    if not eng.get("enabled", True):
        mark_external(findings, "skipped", "external_engine.enabled is false")
        print("external engine disabled; skipped.")
        return 0

    api_key = os.environ.get(secret_name, "").strip()
    if not api_key:
        mark_external(findings, "skipped", f"no {secret_name} secret present")
        # Static message — do NOT interpolate the secret-named variable into a log sink
        # (CodeQL clear-text-logging). It carries the env-var NAME, never the key value.
        print("external review skipped: API key not set; Claude's review kept.")
        return 0  # graceful: never fail the workflow

    try:
        prompt = build_prompt(findings, gather_context())
        result = call_gemini(api_key, model, prompt, timeout)
        merge_external(findings, model, result)
        write_findings(findings)
        print(f"external review ({model}) ok: added {findings['reviewers']['external']['added_findings']} findings.")
        return 0
    except urllib.error.HTTPError as e:
        reason = f"HTTP {e.code} (quota/auth?)"
    except urllib.error.URLError as e:
        reason = f"network error: {e.reason}"
    except Exception as e:  # malformed JSON, unexpected shape, etc.
        reason = f"{type(e).__name__}: {e}"

    mark_external(findings, "error", reason)
    print(f"external review failed: {reason}. Skipped gracefully.")
    return 0 if graceful else 1


if __name__ == "__main__":
    raise SystemExit(main())
