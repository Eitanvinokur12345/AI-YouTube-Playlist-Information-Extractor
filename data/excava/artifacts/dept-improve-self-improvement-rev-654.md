# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-654` (dept) · 2026-07-30T20:29:32.080771+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Auto-apply *only* formatting tweaks; route dependency bumps and all prompt/engine/routing changes to human review.

**Plan:**
1. Configure PR-Agent to flag formatting-only changes (whitespace, indentation, etc.) for auto-apply.
2. Route all dependency updates (version bumps, lockfile changes) to human review.
3. Route all prompt/engine/routing modifications to human review.
4. Add a post-merge failure tracker for dependency-related issues.
5. Update review guidelines to clarify the split.
6. Assign ownership to the lead for enforcement and adjustments.

**What changed:**
Split auto-apply for formatting only; all else requires human review.
