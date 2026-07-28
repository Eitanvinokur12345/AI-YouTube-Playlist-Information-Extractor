# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-751` (dept) · 2026-07-28T23:58:17.399435+00:00
> Participants: Chisel, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run BloodHound-MCP on the full earnings call transcript to extract entities (executives, products, financials, risks) and their relationships.
2. Generate a structured graph output optimized for the weekly exec sync slide (prioritize clarity and executive-level insights).
3. Validate the graph for accuracy by cross-referencing key claims with the transcript’s full source.
4. Enrich the graph with at least one external data source (e.g., SEC filings, analyst notes) to contextualize risks/financials.
5. Format the output as a GitHub markdown file with visual hierarchy (e.g., Mermaid.js for the graph, bullet points for risks).
6. Schedule delivery to the exec sync slide owner with a 24-hour buffer for review.

**What changed:** BloodHound-MCP execution is now explicitly tied to validation and enrichment steps for higher confidence.
