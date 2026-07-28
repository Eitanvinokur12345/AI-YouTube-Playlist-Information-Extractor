# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-280` (dept) · 2026-07-28T23:19:19.766935+00:00
> Participants: Chisel, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**
Marrow executes BloodHound-MCP on the full earnings call transcript to generate a structured graph of entities, relationships, and temporal connections, producing `EarningsCall_Graph.json`.

**Plan:**
1. **Input Validation:** Verify the full earnings call transcript is complete and properly formatted for BloodHound-MCP ingestion.
2. **Execution:** Run BloodHound-MCP with parameters to extract named entities (e.g., speakers, topics, financial metrics), relationships (e.g., "said", "contradicted"), and temporal markers (e.g., timestamps, sequence).
3. **Artifact Generation:** Output `EarningsCall_Graph.json` with nodes (entities) and edges (relationships), including metadata (speaker, timestamp, sentiment if applicable).
4. **Validation:** Cross-check a sample of the graph against the transcript for accuracy (e.g., 10% random snippets).
5. **Enrichment:** Augment the graph with external financial context (e.g., stock price movements during the call, sector benchmarks) via API or dataset merge.
6. **Documentation:** Add a README to `EarningsCall_Graph.json` detailing schema, extraction rules, and enrichment sources.

**What changed:**
BloodHound-MCP execution is now the authoritative method for structuring the transcript, replacing ad-hoc analysis.
