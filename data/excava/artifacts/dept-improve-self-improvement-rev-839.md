# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-839` (dept) · 2026-07-31T04:29:31.438038+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement a `safe-change` flag system with a strict whitelist of edits: whitespace trimming, exact duplicate removal, and no synonyms.
2. Route all non-mechanical edits (e.g., synonyms, phrasing changes) to human review with a diff preview.
3. Add a diff viewer in the review UI showing pre- and post-edit versions for manual approval.
4. Log all auto-applied edits in a changelog for auditability.
5. Set a 24-hour timeout for human review before auto-approval of mechanical edits.
6. Document the whitelist rules in the style guide for contributor reference.

**What changed:** Auto-applied edits restricted to mechanical whitespace/duplicate removal; all other "safe" edits require human review.
