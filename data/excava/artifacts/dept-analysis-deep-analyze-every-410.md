# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-410` (dept) · 2026-08-10T19:26:31.967469+00:00
> Participants: Chisel, Sift, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use BloodHound-MCP to extract the full verbatim transcript from the earnings call video source.
2. Run deep analysis on the extracted transcript using BloodHound-MCP.
3. Generate the "Earnings Call Analysis Report [YYYYMMDD]" artifact.
4. Validate the transcript for completeness and accuracy against the original video.
5. Cross-reference key financial metrics and statements with official earnings call materials.
6. Finalize and archive the report for stakeholder review.

**What changed:** Replaced Luma’s unreliable demo transcript tool with BloodHound-MCP for accurate extraction and deep analysis.
