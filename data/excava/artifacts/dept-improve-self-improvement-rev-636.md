# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-636` (dept) · 2026-08-03T18:24:42.788878+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in shadow mode on the oldest merged PR first to catch routing/prompt drift, then expand to newest open PR once stable—result: a tested, safe rollout plan with documented behavior; owner: Overhaul.

**Plan:**
1. Identify the oldest merged PR with known routing/prompt issues.
2. Run PR-Agent in shadow mode on that PR, logging all outputs and drift detection.
3. Analyze results for edge cases, prompt version compatibility, and routing stability.
4. If stable, expand shadow mode to the newest open PR with a known issue.
5. Document behavior changes and any required prompt/routing adjustments.
6. Gradually expand to parallel runs on newer PRs after confirming stability.

**What changed:**
Prioritized oldest merged PR for initial shadow testing to expose routing/prompt drift before newer PRs.
