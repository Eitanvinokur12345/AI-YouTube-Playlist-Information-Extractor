# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-221` (dept) · 2026-07-09T23:49:36.198363+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Run a dual-phase audit to improve prompt, engine, and routing code quality.

**Plan:**
1. Execute a static AST analysis to identify and report syntax issues in `./src/prompts/`, `./src/engines/`, and `./src/routing/`.
2. Conduct runtime behavioral tests to detect semantic drift and ensure prompts behave as specified and engines are routing correctly.
3. Auto-patch only the identified syntax-level issues that are deemed safe based on the static analysis report.
4. Flag all semantic issues for manual review to ensure deeper quality and functional adherence.
5. Compile both static analysis and semantic drift reports for transparency and future audits.

**What changed:** The decision incorporates both static and runtime analyses for a comprehensive quality audit.
