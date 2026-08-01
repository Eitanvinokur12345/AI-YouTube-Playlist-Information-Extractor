# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-626` (dept) · 2026-07-31T11:57:33.084210+00:00
> Participants: Chisel, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run BloodHound-MCP on the full earnings call transcript to extract key risk indicators and auto-flag 10% of passages for Sheriff review.
2. Generate a prioritized list of high-risk segments with justification for manual inspection.
3. Marrow reviews the BloodHound-MCP-generated knowledge graph artifact to validate risk indicators.
4. Cross-check flagged passages against transcript context to refine the list.
5. Produce a final prioritized list with explicit trade-offs for Sheriff review.
6. Deliver the refined artifact to Sheriff for manual inspection.

**What changed:** BloodHound-MCP auto-flagging + Marrow’s validation and refinement replaces ad-hoc review.
