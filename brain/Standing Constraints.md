---
tags: [reference, constraints, rules]
aliases: [Standing Constraints, Constraints, Rules]
---

# Standing Constraints

The non-negotiables. Every change must honour these.

## The prime directive
> **No owner intervention, and no new cost.** Free = public-repo GitHub Actions + the Claude
> Pro/Max **subscription** token (not paid API billing) + free external API tiers that
> **skip gracefully** when absent. No babysitting.

## Hard rules
- **Never commit secrets.** API keys/tokens live only in GitHub Actions secrets / local env
  vars — never printed, never committed.
- **Never modify a [[Stars and Freezing|frozen]] record** (in `stars.json`, or
  `starred`/`locked: true`). Max 10 stars.
- **Push automatically** without asking.
- **Output is English only**; **never edit/translate the source transcript** — use YouTube's
  text exactly as-is.
- **No external browser connector (e.g. Playwright) for offline work.**
- **Never commit:** `make_icon.py` (repo root), `.claude/`, and temp files
  (`C:\Users\eitan\_tmp_*.py`, `_transcript_tmp.jsonl`, `_refspec_raw.txt`, `_batch_digest.json`).
  Stage **specific paths**, never `git add -A`.

## Build-time
- Clarifying questions at build time are welcome, but the [[Locked Decisions]] are settled.

See [[Operations and Setup]] for the practical side (tokens, secrets, running it).
