# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-419` (dept) · 2026-08-03T23:01:06.714292+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Configure PR-Agent to run in shadow mode on the newest open PR first.
2. Immediately after, run PR-Agent in shadow mode on the oldest merged PR.
3. Collect and review logs from both runs for false positives/negatives.
4. Validate routing stability for both current and historical cases.
5. If logs confirm stability, merge the changes; otherwise, iterate.
6. Document the process and results in the team’s internal wiki.

**What changed:** Shadow mode now validates both current and historical routing paths before full deployment.
