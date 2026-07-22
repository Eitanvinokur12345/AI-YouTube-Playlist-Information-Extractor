# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-815` (dept) · 2026-07-22T17:10:57.125799+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run live A/B tests on prompt variants first—measure real-world impact before any audit or routing tweaks.

**Plan:**
1. Deploy 3-5 prompt variants (including current baseline) to live traffic via A/B testing framework.
2. Log compute usage, latency, and output quality metrics for each variant.
3. Run tests for 72 hours or until statistical significance is achieved (whichever is longer).
4. Analyze results to identify top/bottom performers (waste/misfire indicators).
5. Share findings with team for prompt refinement or routing adjustments.
6. Document test parameters and outcomes in `/docs/ab_tests/prompt_variants_YYYYMMDD.md`.

**What changed:** Prompt variants now validated in production before routing or audit work.
