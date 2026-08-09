# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-867` (dept) · 2026-08-03T15:27:24.380302+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in shadow mode on open PRs with known issues for 48 hours to validate catch-rate vs. noise.

**Plan:**
1. Select 5–10 open PRs with documented issues (e.g., routing/prompt failures).
2. Deploy PR-Agent in shadow mode on these PRs for 48 hours.
3. Log all feedback: actionable fixes, false positives, and noise.
4. Calculate false positive rate (target: <10%).
5. If criteria met, promote to default setup; otherwise, revisit.
6. Document trial results in a GitHub issue for team review.

**What changed:**
PR-Agent now runs in shadow mode on open PRs with known issues for 48-hour validation.
