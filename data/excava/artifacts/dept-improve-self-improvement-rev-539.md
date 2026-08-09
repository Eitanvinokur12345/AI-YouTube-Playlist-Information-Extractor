# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-539` (dept) · 2026-08-09T22:05:23.164920+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in shadow mode on the newest open PR first, then expand to merged PRs only after zero critical routing errors for a full week in open PRs.

**Plan:**
1. Enable PR-Agent shadow mode on the newest open PR immediately.
2. Monitor error rates in open PRs for critical routing errors.
3. If zero critical errors persist for 7 days, enable shadow mode on merged PRs.
4. Track fix cost reduction vs. baseline (target: ≥40% reduction).
5. Pause expansion if critical errors exceed threshold in open PRs.
6. Document routing error patterns weekly for review.

**What changed:**
PR-Agent shadow mode prioritizes open PRs first, delaying merged PR testing until open PRs show zero critical routing errors for a week.
