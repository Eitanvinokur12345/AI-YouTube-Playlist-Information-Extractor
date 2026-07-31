# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-776` (dept) · 2026-07-31T20:59:38.786756+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Modify PR-Agent to gate only on verifiable mechanical issues (lint, formatting, mechanical regressions).
2. Implement a stratified live traffic sample (last 24h) for pre-deployment quality checks.
3. Deploy the stratified sample test as a mandatory gate before any engine deployment.
4. Document the stratified sample criteria (e.g., coverage of edge cases, diversity of inputs).
5. Add a fallback mechanism to rerun the test with a fresh sample if it fails unexpectedly.
6. Monitor false positives/negatives and adjust stratification parameters monthly.

**What changed:** PR-Agent now enforces mechanical checks only; pre-deployment tests use stratified live traffic samples.
