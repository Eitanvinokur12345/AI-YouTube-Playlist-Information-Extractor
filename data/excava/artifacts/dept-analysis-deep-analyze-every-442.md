# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-442` (dept) · 2026-07-31T11:42:47.639998+00:00
> Participants: Chisel, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt BloodHound-MCP for structured analysis of the earnings call transcript, with Marrow validating the output before lead review.

**Plan:**
1. Run BloodHound-MCP on the full earnings call transcript to extract entities, relationships, and anomalies into a structured knowledge graph.
2. Marrow reviews the graph to validate entity relationships, surface hidden anomalies, and confirm alignment with the full transcript.
3. Marrow synthesizes findings into a concise report highlighting key themes, risks, and opportunities.
4. Lead reviews the report and graph to finalize strategic decisions.
5. Document discrepancies or unresolved anomalies for follow-up analysis.
6. Archive the validated graph and report for future reference.

**What changed:** BloodHound-MCP is now the primary tool for transcript analysis, with Marrow as the validator before lead review.
