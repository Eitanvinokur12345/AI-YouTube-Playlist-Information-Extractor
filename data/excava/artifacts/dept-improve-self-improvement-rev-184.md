# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-184` (dept) · 2026-08-08T21:02:26.566814+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Start PR-Agent in shadow mode on the newest open PR to catch issues before they ship, then expand to merged PRs after validation.

**Plan:**
1. Select the newest open PR in the target repo.
2. Enable PR-Agent in shadow mode for this PR only, logging feedback without applying changes.
3. Monitor error rates and feedback relevance for 24 hours.
4. If error rate <5% and feedback is actionable, scale shadow mode to all open PRs.
5. After 1 week of stable performance on open PRs, enable shadow mode on merged PRs for post-merge validation.
6. Adjust PR-Agent rules based on collected metrics before full automation.

**What changed:** Shadow mode prioritized on open PRs first, then merged PRs, reducing post-mortem fixes.
