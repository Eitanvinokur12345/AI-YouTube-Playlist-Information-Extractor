# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-189` (dept) · 2026-07-31T04:50:34.337508+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Restrict auto-apply to *only* mechanical edits where reversibility is trivial.

**Plan:**
1. Audit all prompts/engines/routing/own-code to identify and remove any "safe-change" flags.
2. Implement a whitelist of *mechanical edits* (whitespace normalization, exact duplicate removal, typo fixes).
3. Add runtime validation to reject any auto-apply request outside the whitelist.
4. Update documentation to define "mechanical edits" and exclude semantic changes.
5. Test auto-apply on a subset of prompts to confirm no unintended edits occur.
6. Roll out changes system-wide with a rollback plan.

**What changed:** Auto-apply now *only* performs mechanical edits (whitespace, duplicates, typos).
