"""
src/agent_issue.py — EXTERNAL-ACTION PILOT (owner spec 2026-07-12): an agent files a REPO ISSUE.

The chosen first real external act, heavily gated by design:
  1. EVIDENCE — only from measured data: a cluster of hub elements whose links are dead
     (elements_verified.json: link_alive false, consecutive_fails >= 2). No evidence, no draft.
  2. DRAFT — attributed to the security lead (Bastion), the full issue text visible to the
     owner IN-APP as a pending approval (category 'outward', pitch-v2 fields).
  3. OWNER GATE — nothing is posted until the owner approves in the decide modal. Ever.
  4. EXECUTE — only in CI (GITHUB_TOKEN + issues:write), only after approval; the created
     issue URL is logged to data/excava/agent_issues.jsonl and syscall-traced.

Owner's standing prohibitions honored: no outside-world posting (future step), NEVER a
YouTube comment bot, never keys in output. This posts to HIS OWN repo only.
Free, stdlib-only. Run: python -m src.agent_issue [--execute]
"""
from __future__ import annotations

import json
import os
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
LOG = DATA / "excava" / "agent_issues.jsonl"
REPO = "Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor"
PILOT_ID = "outward-pilot-dead-links"
MIN_CLUSTER = 5


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def gather_evidence() -> list[dict]:
    try:
        rec = json.load(open(DATA / "elements_verified.json", encoding="utf-8"))["verified"]
    except Exception:
        return []
    return [{"id": k, "fails": v.get("consecutive_fails", 0)}
            for k, v in rec.items()
            if v.get("link_alive") is False and v.get("consecutive_fails", 0) >= 2][:25]


def draft_and_file() -> str:
    """Draft the issue from real evidence and place it in the owner's in-app decide queue."""
    ev = gather_evidence()
    if len(ev) < MIN_CLUSTER:
        return f"agent-issue: only {len(ev)} dead-link elements (<{MIN_CLUSTER}) — no draft"
    ap_p = DATA / "excava_approvals.json"
    ap = json.load(open(ap_p, encoding="utf-8"))
    if PILOT_ID in ap.get("granted", []) or PILOT_ID in ap.get("declined", []):
        return "agent-issue: pilot already decided"
    if any(p.get("id") == PILOT_ID for p in ap.get("pending", [])):
        return "agent-issue: draft already awaiting the owner"
    body = ("**Filed by agent Bastion (security lead) — EXCAVA's external-action pilot.**\n\n"
            f"{len(ev)} hub elements have links that failed verification at least twice in a row:\n\n"
            + "\n".join(f"- `{e['id']}` ({e['fails']} consecutive fails)" for e in ev[:15])
            + ("\n- …" if len(ev) > 15 else "")
            + "\n\nProposed: quarantine or re-resolve these via the links lane. "
              "This issue was drafted from measured data and approved by the owner before posting.")
    ap.setdefault("pending", []).append({
        "id": PILOT_ID, "category": "outward",
        "title": f"[PILOT] Bastion wants to file a repo issue: {len(ev)} dead-link elements",
        "why": "external-action pilot (owner spec 2026-07-12): agent files a repo issue, owner-gated",
        "what": "Approve and EXCAVA posts this issue — in YOUR OWN repo, fully reversible (you can "
                "close/delete it). The full text is below; nothing is posted until you say yes.",
        "requested_by": "Bastion (security lead) — from measured dead-link evidence",
        "need": f"{len(ev)} elements point at dead links; an issue makes the cluster visible and trackable.",
        "importance": "Low-risk, high-signal: the pilot that teaches the whole approval chain.",
        "missing": "Only your yes.", "hub_candidates": [],
        "draft_body": body, "since": _now()})
    ap_p.write_text(json.dumps(ap, ensure_ascii=False, indent=2), encoding="utf-8")
    return f"agent-issue: DRAFT filed for owner approval ({len(ev)} dead links cited)"


def execute_if_approved() -> str:
    """Post the issue — ONLY if the owner granted it, ONLY where a token exists (CI)."""
    ap = json.load(open(DATA / "excava_approvals.json", encoding="utf-8"))
    if PILOT_ID not in ap.get("granted", []):
        return "agent-issue: not approved — nothing posted"
    if LOG.exists() and PILOT_ID in LOG.read_text(encoding="utf-8"):
        return "agent-issue: already posted once — never reposting"
    tok = (os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_MODELS_TOKEN") or "").strip()
    if not tok:
        return "agent-issue: approved but no token here (posts from CI)"
    ev = gather_evidence()
    body = json.dumps({
        "title": f"[EXCAVA agent: Bastion] {len(ev)} hub elements have dead links (verified twice)",
        "body": next((p.get("draft_body", "") for p in ap.get("pending", [])
                      if p.get("id") == PILOT_ID), "") or
                f"{len(ev)} elements failed link verification twice (see data/elements_verified.json).",
        "labels": ["excava-agent", "links"]}).encode()
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/issues", data=body, method="POST",
        headers={"Authorization": f"Bearer {tok}", "Accept": "application/vnd.github+json",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        out = json.loads(r.read().decode())
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"at": _now(), "pilot": PILOT_ID, "agent": "security-lead",
                             "issue_url": out.get("html_url", "")}, ensure_ascii=False) + "\n")
    try:
        from src.excava_agents import _syslog
        _syslog("security", "agent_issue", {"id": PILOT_ID}, True, "outward-executed")
    except Exception:
        pass
    return f"agent-issue: POSTED {out.get('html_url', '')}"


def main() -> int:
    import argparse, sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    a = argparse.ArgumentParser()
    a.add_argument("--execute", action="store_true")
    args = a.parse_args()
    print(execute_if_approved() if args.execute else draft_and_file())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
