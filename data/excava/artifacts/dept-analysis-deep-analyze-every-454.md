# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-454` (dept) · 2026-07-30T17:47:28.683820+00:00
> Participants: Chisel, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**
Marrow executes BloodHound-MCP on the full earnings call transcript to produce a structured, timestamped artifact mapping language, sentiment shifts, and context to actionable outcomes.

**Plan:**
1. **Input:** Feed the full earnings call transcript into BloodHound-MCP as the sole source material.
2. **Processing:** Run BloodHound-MCP to generate a structured analysis, including:
   - Key themes (e.g., financial performance, operational risks, strategic pivots).
   - Sentiment shifts (positive/negative/neutral) with timestamps.
   - Contextual mappings to actionable outcomes (e.g., cost-cutting, R&D focus, M&A signals).
3. **Output:** Produce a timestamped artifact (e.g., JSON/Markdown) with:
   - Theme summaries per segment.
   - Sentiment scores and trend lines.
   - Direct quotes linked to inferred actions.
4. **Validation:** Cross-check 3-5 key themes against the raw transcript for accuracy.
5. **Enrichment:** Supplement with 1+ external sources (e.g., sector benchmarks, competitor earnings calls) to contextualize findings.
6. **Delivery:** Share the artifact with stakeholders in a GitHub repo with clear versioning.

**What changed:**
BloodHound-MCP is now the designated tool for structured, timestamped analysis of the earnings call transcript.
