# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-459` (dept) · 2026-07-28T12:35:54.388602+00:00
> Participants: Chisel · synthesized by mistral/mistral-small-latest

**Decision:**
Execute a real-time, entity-centric analysis of the full earnings call transcript using BloodHound-MCP to generate a dynamic dependency graph for executive review.

**Plan:**
1. **Ingest & Normalize:** Parse the full transcript into a structured JSON/CSV with timestamps, speakers, and raw text.
2. **Entity Extraction:** Run BloodHound-MCP to map named entities (people, orgs, products), financial metrics (revenue, costs, margins), and sentiment shifts (positive/negative/neutral) per speaker.
3. **Graph Construction:** Build a real-time dependency graph linking entities to metrics and sentiment, with directional edges (e.g., "CEO → Revenue Up 5% → Positive").
4. **Risk Flagging:** Flag anomalies (e.g., sudden cost spikes, conflicting sentiment) and tag with confidence scores.
5. **Exec Sync Prep:** Export the graph to a slide-ready format (e.g., Mermaid.js or Neo4j Bloom) with key insights highlighted.
6. **Validation Loop:** Cross-check top 5 metrics against official filings for accuracy before finalization.

**What changed:**
Shifted from static post-call analysis to real-time, graph-based dependency mapping for immediate executive actionability.
