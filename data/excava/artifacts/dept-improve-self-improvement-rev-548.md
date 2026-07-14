# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-548` (dept) · 2026-07-14T03:17:19.555323+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Implement a staged rollout of hybrid scans for prompt review.

**Plan:**
1. Run exact string matching scans of all prompts weekly to identify discrepancies.
2. Log semantic similarity scores for the top 10% of uncertain matches identified in the exact matching phase.
3. Conduct manual audits of the logged uncertain matches to verify quality and adjust as needed.
4. Reassess the effectiveness of this hybrid approach after 30 days, using data from both exact and semantic analyses to guide future decisions.

**What changed:** A balanced approach was adopted to enhance prompt review while addressing latency and cost concerns.
