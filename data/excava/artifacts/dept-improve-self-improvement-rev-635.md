# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-635` (dept) · 2026-08-26T09:15:44.309331+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in shadow mode on *only* new-contributor PRs for two weeks, then expand to all PRs if noise stays below 15% of total comments.

**Plan:**
1. Configure PR-Agent to run in shadow mode exclusively on PRs from new contributors (defined as <3 merged PRs in the last 3 months).
2. Track noise-to-signal ratio (irrelevant/incorrect comments vs. actionable feedback) for 14 days, logging examples weekly.
3. If noise exceeds 15% of total comments, pause expansion and refine PR-Agent’s rules (e.g., lower sensitivity for new contributors).
4. If noise ≤15%, enable shadow mode on *all* PRs for one week, measuring impact on reviewer workload and PR merge time.
5. After full deployment, auto-apply safe changes (e.g., formatting, dependency updates) via PR-Agent with manual approval for critical changes.
6. Document the process in `CONTRIBUTING.md` with clear opt-out instructions for reviewers.

**What changed:**
Scope narrowed to new-contributor PRs first, with expansion contingent on noise metrics.
