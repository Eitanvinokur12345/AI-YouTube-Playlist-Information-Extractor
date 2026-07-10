# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-809` (dept) · 2026-07-10T01:42:34.529587+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Audit all prompt sources (static, dynamic, embedded) and semantic drift via multi-tool sweep + manual review.

**Plan:**
1. Conduct a comprehensive inventory of all prompt locations, including files, configuration settings, database entries, and runtime generation.
2. Execute a multi-faceted static analysis using `ruff` combined with custom checks to identify tone inconsistencies and outdated examples.
3. Perform a semantic drift review by manually examining a representative sample of prompts and templates to ensure alignment with current guidelines and user needs.
4. Implement a reporting mechanism to document findings and propose changes for each prompt identified as needing improvement.
5. Auto-apply safe changes identified during the review process while ensuring a rollback strategy is in place for any risky adjustments.

**What changed:** Decision broadens the scope from static analysis to include dynamic and embedded prompts while incorporating manual review for semantic accuracy.
