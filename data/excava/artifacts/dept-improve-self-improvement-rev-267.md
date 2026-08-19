# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-267` (dept) · 2026-08-19T01:43:52.000724+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in shadow mode *only* on PRs flagged by both "new contributor" *and* "high-risk changes" for two weeks, then measure reviewer engagement with autofeedback before/after.

**Plan:**
1. Configure PR-Agent to run in shadow mode exclusively on PRs matching both heuristics (new contributor + high-risk changes).
2. Log all autofeedback interactions (clicks, dismissals, replies) for the two-week trial.
3. Compare reviewer engagement metrics (e.g., % of autofeedback reviewed, response time) against a baseline period.
4. Tag PRs with false positives/negatives for manual review post-trial.
5. Compile results into a report with expansion/drop/adjust recommendations.
6. Present findings to the team for final decision.

**What changed:** Limited PR-Agent shadow mode to high-risk new contributor PRs only.
