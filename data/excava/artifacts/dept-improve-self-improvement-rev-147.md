# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-147` (dept) · 2026-08-04T20:11:49.807557+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in shadow mode on the oldest merged PR first to validate routing stability, then expand to the newest open PR once proven reliable.

**Plan:**
1. Select the oldest merged PR with no recent changes or conflicts.
2. Enable PR-Agent in shadow mode on this PR, logging routing accuracy and false positives.
3. Review shadow mode logs for 24 hours to confirm no false positives or routing flaws.
4. If stable, expand shadow mode to the newest open PR, prioritizing high-risk routing cases.
5. Monitor both PRs for 48 hours, comparing PR-Agent’s routing decisions against manual reviews.
6. Document any discrepancies and adjust PR-Agent’s routing rules as needed.

**What changed:** Shadow mode validation order shifted from newest open PR to oldest merged PR for stability testing.
