# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-826` (dept) · 2026-07-27T18:19:22.490152+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Run a 48-hour shadow test at 5% traffic first, then auto-apply only changes that cut error rates by 10% or more.

**Plan:**
1. Fork the core logic of the Claude Self-Improvement Skill Pack into our own repository.
2. Conduct a 48-hour shadow test with 5% of user traffic to compare current prompts against the modified prompts.
3. Monitor and evaluate error rates during the shadow test.
4. If the shadow test shows a reduction in error rates of 10% or more, proceed to auto-apply the changes to all users.
5. If the shadow test does not meet the criteria, discontinue the Skill Pack and continue with manual prompt tuning.

**What changed:** The decision balances the need for innovation with risk mitigation, prioritizing a controlled evaluation before broad implementation.
