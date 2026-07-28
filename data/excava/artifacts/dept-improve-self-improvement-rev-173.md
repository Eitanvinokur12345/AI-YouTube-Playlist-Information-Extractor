# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-173` (dept) · 2026-07-28T17:38:36.239459+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Adopt a dual-gate rule for auto-applying edits to ensure safety and accuracy.
**Plan:**
1. Implement a semantic diff test to verify changes don't alter the code's behavior.
2. Introduce a human review gate for the first 100 auto-applied changes.
3. Auto-apply edits that pass both the semantic diff test and human review for the initial 100 changes.
4. Monitor the auto-apply system for 100 clean runs to ensure reliability.
5. Drop the human review gate after 100 successful auto-applied changes.
6. Continuously review and refine the auto-apply system to adapt to new scenarios.
**What changed:** The auto-apply system now uses a dual-gate rule with semantic diff testing and initial human review to ensure safer and more accurate code edits.
