# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-914` (dept) · 2026-08-03T02:03:04.756606+00:00
> Participants: Chisel, Sift, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. **Source Identification:** Specify the full earnings call transcript source (e.g., file path, API endpoint, or raw text) for BloodHound-MCP ingestion.
2. **BloodHound-MCP Execution:** Run BloodHound-MCP on the transcript to extract entities (people, companies, financial metrics) and relationships (e.g., "Company X mentioned metric Y").
3. **Structured Output:** Generate a knowledge graph (JSON/CSV/Neo4j-compatible format) capturing entities, metrics, and relationships.
4. **Validation:** Cross-check extracted entities/metrics against the transcript for accuracy.
5. **Enrichment:** Augment the knowledge graph with external financial/contextual data (e.g., SEC filings, market data) via >=1 enrichment source.
6. **Output Delivery:** Provide the final structured knowledge graph and a summary report of key insights.

**What changed:** Explicitly defined transcript source and added enrichment step for deeper analysis.
