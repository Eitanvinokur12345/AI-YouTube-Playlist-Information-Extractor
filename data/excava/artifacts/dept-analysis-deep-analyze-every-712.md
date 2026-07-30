# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-712` (dept) · 2026-07-30T21:13:13.970333+00:00
> Participants: Chisel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. **Extract full transcript** from the earnings call repository (or API source) and preprocess into a clean, machine-readable format (e.g., JSON/CSV with speaker turns, timestamps, and raw text).
2. **Run BloodHound-MCP** against the preprocessed transcript to auto-detect entities (people, orgs, financial terms, risks) and their relationships, outputting a structured graph (e.g., Neo4j-compatible or JSON-LD).
3. **Enrich the graph** with external context (e.g., SEC filings, news archives, or domain-specific ontologies) to validate entities and add missing relationships (e.g., "Person X → Board Member → Org Y").
4. **Query the graph** for high-value insights (e.g., "Show all risks mentioned by Person Z" or "Map financial terms to their sentiment scores").
5. **Generate a synthesis report** (Markdown) with:
   - Top 10 most connected entities.
   - Key relationship clusters (e.g., "Regulatory Risk → Compliance Team").
   - Anomalies (e.g., entities mentioned only once but linked to high-impact terms).
6. **Store outputs** in a dedicated repo branch (`/analysis/earnings-call-{date}`) with versioned snapshots of the graph and report.

**What changed:** Transcript analysis shifted from manual keyword extraction to an automated, queryable knowledge graph with external enrichment.
