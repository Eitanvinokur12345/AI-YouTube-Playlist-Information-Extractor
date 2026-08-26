# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-958` (dept) · 2026-08-26T11:05:22.071357+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in shadow mode on *only* new-contributor PRs for two weeks first.

**Plan:**
1. Configure PR-Agent to run in shadow mode exclusively on PRs from new contributors.
2. Monitor signal-to-noise ratio for two weeks, focusing on reviewer feedback.
3. If signal-to-noise is acceptable, expand to a representative sample of PRs.
4. After validation, scale to all PRs if systemic issues are detected.
5. Document findings in a shared report for team review.
6. Adjust tooling or thresholds based on data before full deployment.

**What changed:** PR-Agent now runs in shadow mode only on new-contributor PRs for two weeks.
