# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-569` (dept) · 2026-07-30T19:31:38.729663+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Configure PR-Agent to flag *all* style/doc issues (semantic and trivial) with a "needs human review" label.
2. Disable auto-application of *any* style/doc fixes in PR-Agent.
3. Update PR-Agent’s review guidelines to prioritize the "needs human review" label in reviewer workflows.
4. Document the new policy in the team’s PR review standards (e.g., "All style/doc issues require human sign-off").
5. Monitor for 2 weeks to measure reviewer compliance and adjust if needed.
6. Retire the 90% threshold for style/doc fixes in PR-Agent’s config.

**What changed:** PR-Agent now flags all style/doc issues for human review; auto-fixes disabled.
