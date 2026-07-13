# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-428` (dept) · 2026-07-13T20:00:42.932986+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement a weekly automated scan for exact-string duplicate prompts before merge.
2. Block merges only if exact duplicates are detected (no delay for near-duplicates).
3. Log near-duplicates in a triage queue for monthly lead review.
4. Generate a weekly scan report for the lead, highlighting duplicates and triage items.
5. Merge the exact-match blocking logic into the existing CI pipeline.
6. Document the process in the team’s prompt management guidelines.

**What changed:** Weekly exact-match scans + triage queue for near-duplicates.
