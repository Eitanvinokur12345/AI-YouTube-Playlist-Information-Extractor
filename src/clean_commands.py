"""
src/clean_commands.py — enforce CLAUDE.md Step 6's slash-command filter on data/commands.json.

data/commands.json had accumulated 914 records, but a mining pipeline (mine_feeds/gemini-video)
had been recording ANY string mentioned near "command" in a video — shell commands (`git clone
...`, `brew install node`), file paths (`./scripts/install.sh`), and full prose sentences — none
of which are actual invocable /commands per CLAUDE.md's own filter ("it starts with `/` and is a
single invocable token... Reject prose or a sentence after the slash, hashtags, URLs / file
paths..."). This left self_check.py's Q13 permanently failing (only 24% of records started with
`/`, threshold is 60%).

This is a one-shot deterministic cleanup, not a new collector:
  - Records whose `command` does not start with "/" are quarantined (not deleted — appended to
    data/commands_quarantine.json with a reason, per the project's quarantine-never-delete rule).
  - Records that start with "/" but carry extra text after the token (e.g. "/improve quick",
    "/ask-the-board <question>") are normalized to the base invocable token ("/improve",
    "/ask-the-board") — the token IS the real command; the trailing text was an example
    argument/usage, not part of the command itself.
  - Records where even the leading token isn't clean (letters/digits/hyphens only, single slash)
    are quarantined too — e.g. "/ for commands" (no token), "/compound-engineering/ce-plan ..."
    (a second internal slash).
  - After normalization, commands are re-deduplicated on the token (case-insensitive), merging
    `also_seen_in`/`source_url` and keeping the richer `description`.

Usage:  python -m src.clean_commands
"""
from __future__ import annotations

import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
COMMANDS_PATH = DATA / "commands.json"
QUARANTINE_PATH = DATA / "commands_quarantine.json"
SNAPSHOT_PATH = ROOT / "backups" / "snapshot" / "commands.json"

TOKEN_RX = re.compile(r"^/[a-zA-Z0-9][a-zA-Z0-9-]*$")


def _cmdstr(c):
    return str(c.get("command", c if isinstance(c, str) else "")).strip()


def main() -> int:
    doc = json.load(open(COMMANDS_PATH, encoding="utf-8"))
    records = doc.get("commands", [])

    quarantine_doc = json.load(open(QUARANTINE_PATH, encoding="utf-8")) if QUARANTINE_PATH.exists() else {"quarantined": []}
    quarantined = quarantine_doc.setdefault("quarantined", [])
    already_quarantined = {json.dumps(q.get("record"), sort_keys=True) for q in quarantined}

    now = datetime.now(timezone.utc).isoformat()
    kept_by_token = {}
    newly_quarantined = 0
    normalized = 0

    for rec in records:
        raw = _cmdstr(rec)
        if not raw.startswith("/"):
            reason = "does not start with / (shell command, file path, or prose)"
            token = None
        else:
            token = raw.split(None, 1)[0]
            if not TOKEN_RX.match(token):
                reason = "leading token is not a clean /command (bad chars or nested slash)"
                token = None
            else:
                reason = None

        if token is None:
            key = json.dumps(rec, sort_keys=True)
            if key not in already_quarantined:
                quarantined.append({"record": rec, "reason": reason, "quarantined_at": now})
                already_quarantined.add(key)
                newly_quarantined += 1
            continue

        if token != raw:
            normalized += 1

        norm_key = token.lower()
        if norm_key not in kept_by_token:
            new_rec = dict(rec)
            new_rec["command"] = token
            kept_by_token[norm_key] = new_rec
        else:
            keeper = kept_by_token[norm_key]
            if len(rec.get("description") or "") > len(keeper.get("description") or ""):
                keeper["description"] = rec.get("description")
            seen = set(keeper.get("also_seen_in") or [])
            for u in [rec.get("source_url")] + (rec.get("also_seen_in") or []):
                if u and u not in seen and u != keeper.get("source_url"):
                    keeper.setdefault("also_seen_in", []).append(u)
                    seen.add(u)

    doc["commands"] = list(kept_by_token.values())
    json.dump(doc, open(COMMANDS_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    json.dump(quarantine_doc, open(QUARANTINE_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    # data_guard.py restores commands.json from backups/snapshot/commands.json whenever the live
    # file drops below 55% of that snapshot's count — a guard against ACCIDENTAL data loss. This
    # cleanup is a deliberate, audited shrink (bad records move to commands_quarantine.json, they
    # are not lost), so re-baseline the snapshot down here too; otherwise the very next data_guard
    # run treats this fix as a collapse and silently restores the pre-cleanup junk (confirmed: it
    # did exactly that ~1h after away-fire 94 first ran this cleanup).
    SNAPSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(COMMANDS_PATH, SNAPSHOT_PATH)

    print(f"commands: {len(records)} -> {len(doc['commands'])} kept "
          f"({normalized} normalized to base token, {newly_quarantined} newly quarantined, "
          f"{len(quarantined) - newly_quarantined} already quarantined before this run); "
          f"data_guard snapshot re-baselined to {len(doc['commands'])} so this cleanup sticks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
