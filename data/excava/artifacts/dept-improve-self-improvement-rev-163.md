# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-163` (dept) · 2026-09-03T19:30:31.303562+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run a controlled A/B test on new contributors’ PRs only—half get PR-Agent, half get human review—for two weeks, then measure false positives *and* false negatives against a human baseline.

**Plan:**
1. Configure PR-Agent to run in shadow mode for the A/B test, logging all outputs without applying changes.
2. Randomly assign new contributors’ PRs to either PR-Agent or human review, ensuring balanced distribution.
3. Track false positives (incorrect PR-Agent suggestions) and false negatives (missed issues) for both groups.
4. Use a human baseline (experienced reviewers) to validate accuracy of PR-Agent’s outputs.
5. After two weeks, compile metrics and analyze trade-offs (e.g., contributor feedback, review time).
6. Present findings to the team for a final decision on full deployment or adjustments.

**What changed:**
A/B test limited to new contributors’ PRs to isolate PR-Agent’s false negatives while minimizing disruption.
