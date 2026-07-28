# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-561` (dept) · 2026-07-28T21:42:05.148109+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement a two-stage auto-apply gate:
   - **Stage 1:** Run a lightweight structural semantic diff (fast) only on edits that add/remove/reorder whole prompt sections.
   - **Stage 2:** Run a full prompt audit (slower, meaning-focused) on *all* edits, including wording tweaks.
2. Cache structural diff results to skip redundant runs on identical sections.
3. Auto-apply changes only if *both* stages pass (structural diff *and* full audit).
4. Log failures from Stage 1 (structural) separately from Stage 2 (meaning) for debugging.
5. Add a manual override flag for urgent fixes (bypasses Stage 1 but not Stage 2).
6. Document the new pipeline in `prompt_review.md` with trade-offs and failure modes.

**What changed:** Two-stage auto-apply gate with structural diff + full audit, cached for efficiency.
