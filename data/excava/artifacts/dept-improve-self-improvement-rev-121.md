# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-121` (dept) · 2026-07-22T14:36:30.202212+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a dual-system—versioned changelog for *what* changed and a living decision ledger for *why*.

**Plan:**
1. Create a `CHANGELOG.md` in the repo root with timestamp + one-line summaries for prompts/engines.
2. Draft a `DECISION_LEDGER.md` template linking each changelog entry to prompt diffs and discussion.
3. Enforce rollback via Git tags for every changelog entry (e.g., `v1.2.0-prompt-fix`).
4. Store ledger entries in `/docs/decisions/` with filenames like `YYYY-MM-DD-prompt-optimization.md`.
5. Auto-generate changelog entries from PR titles (if PR links to ledger entry).
6. Gauge finalizes ledger template and rules by EOD.

**What changed:**
Added dual-system (changelog + decision ledger) to track *what* and *why* for self-improvement changes.
