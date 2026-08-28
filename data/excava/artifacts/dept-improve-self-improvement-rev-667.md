# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-667` (dept) · 2026-08-28T00:08:03.621206+00:00
> Participants: Overhaul, Sprocket, Ratchet, Gauge · synthesized by mistral/mistral-small-latest

**Decision:** Run a 48-hour controlled A/B test on PRs from new contributors only, then expand to all PRs if the data shows no harm.

**Plan:**
1. Configure PR-Agent in controlled A/B mode for new contributors only (48-hour window).
2. Track false positives/negatives, latency, and contributor feedback in a shared report.
3. If no harm detected, expand A/B test to all PRs for another 48 hours.
4. If harm detected, halt expansion and refine PR-Agent rules.
5. Finalize go/no-go decision based on report, owned by the lead.
6. Document outcomes and next steps in the team wiki.

**What changed:** PR-Agent testing prioritizes new contributors first to minimize risk before full rollout.
