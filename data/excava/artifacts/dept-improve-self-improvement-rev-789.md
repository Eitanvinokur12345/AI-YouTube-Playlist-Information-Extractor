# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-789` (dept) · 2026-08-17T00:59:07.561284+00:00
> Participants: Overhaul, Sprocket, Ratchet, Gauge · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run PR-Agent in shadow mode *only on merged PRs* for two weeks.
2. Compare review quality metrics (review depth, time-to-merge) against a control team not using it.
3. If metrics improve, expand to high-risk PRs flagged by the lightweight system (70% noise reduction).
4. If no improvement, reassess and iterate.
5. Document findings in a post-pilot report for team review.
6. Auto-apply safe changes only after validation.

**What changed:** PR-Agent now runs in shadow mode exclusively on merged PRs for two weeks to measure impact on review quality.
