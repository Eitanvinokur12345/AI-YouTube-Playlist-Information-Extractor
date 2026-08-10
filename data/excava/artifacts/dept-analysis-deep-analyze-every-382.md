# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-382` (dept) · 2026-08-10T20:48:13.099036+00:00
> Participants: Chisel, Sift, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use BloodHound-MCP to extract the full earnings call transcript directly.
2. Validate the verbatim transcript for completeness and accuracy.
3. Deep-analyze the transcript using the full source text.
4. Enrich the analysis with at least one additional source.
5. Synthesize findings into a structured report.
6. Output the final analysis in GitHub markdown format.

**What changed:** Shifted from Luma’s native tool to BloodHound-MCP for transcript extraction.
