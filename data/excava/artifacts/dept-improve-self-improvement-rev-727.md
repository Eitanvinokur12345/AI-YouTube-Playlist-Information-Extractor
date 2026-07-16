# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-727` (dept) · 2026-07-16T17:58:21.541669+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement a dual logging system: log *all* prompt changes instantly, with auto-apply gated by a fast semantic diff check (embeddings + human triage for edge cases).
2. Deploy a weekly controlled prompt variant audit as a fallback, logging all changes and flagging semantic shifts with lightweight human review.
3. Run a 1% traffic A/B test for one week comparing the dual system against the weekly audit to measure drift detection and response quality.
4. Sprocket owns the A/B test setup and metrics; Gauge owns the semantic diff check and triage process.
5. After the test, evaluate results and decide whether to standardize on the dual system or iterate further.
6. Document the chosen system and update routing logic to enforce the new policy.

**What changed:** Switched from a weekly audit to a dual system with instant logging, semantic gating, and A/B testing.
