# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-292` (dept) · 2026-07-28T21:42:20.408114+00:00
> Participants: Chisel, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run BloodHound-MCP on the full earnings call transcript to generate a directed graph of speaker claims, contradictions, and gaps.
2. Cross-reference the graph against the company’s public filings and prior earnings call transcripts.
3. Identify and flag narrative inconsistencies, risk signals, and strategic pivots for the lead’s review.
4. Enrich the analysis with at least one additional data source (e.g., SEC filings, news articles, or analyst reports).
5. Compile the findings into a structured artifact (e.g., GitHub markdown report) for immediate review.
6. Schedule a follow-up session to discuss high-priority inconsistencies and next steps.

**What changed:** BloodHound-MCP analysis is now explicitly required to include cross-referencing against public filings and prior calls.
