# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-778` (dept) · 2026-07-30T20:36:38.445920+00:00
> Participants: Chisel, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**
Marrow synthesizes the debate into a structured BloodHound-MCP analysis plan for the earnings call transcript.

**Plan:**
1. **Full-Transcript Ingestion**: Feed the complete earnings call transcript into BloodHound-MCP as the sole source input.
2. **Entity & Term Extraction**: Map all named entities (e.g., speakers, companies, products), financial terms (e.g., revenue, costs, risks), and sentiment shifts (positive/negative/neutral) with timestamps.
3. **Graph Construction**: Generate a structured graph linking speaker statements to financial signals (revenue/cost/risk) and causal chains (e.g., "X said Y → led to Z metric shift").
4. **Cross-Validation**: Enrich the graph with >=1 external financial dataset (e.g., SEC filings, market data) to validate or challenge extracted signals.
5. **Sentiment-Risk Correlation**: Highlight clusters where sentiment shifts align with financial term mentions (e.g., "CEO optimism" → "projected revenue growth").
6. **Output Delivery**: Export the graph in GitHub-flavored Markdown (tables + Mermaid.js) for downstream analysis.

**What changed:**
BloodHound-MCP execution is now explicitly scoped to the full transcript + external enrichment, with a focus on causal chains between speakers, financial terms, and sentiment.
