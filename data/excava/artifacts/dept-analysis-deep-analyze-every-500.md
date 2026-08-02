# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-500` (dept) · 2026-08-02T15:42:04.831337+00:00
> Participants: Chisel, Sift, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**
BloodHound-MCP will analyze the full earnings call transcript to extract key phrases, sentiment shifts, and decision triggers, producing a structured analysis artifact.

**Plan:**
1. **Source Specification:** Use the *full earnings call transcript* as the input for BloodHound-MCP.
2. **Execution:** Run BloodHound-MCP to extract:
   - Key phrases (e.g., financial terms, strategic mentions).
   - Sentiment shifts (positive/negative/neutral tone changes).
   - Decision triggers (e.g., "we will," "plan to," "invest in").
3. **Structured Output:** Generate a machine-readable artifact (e.g., JSON/CSV) with categorized insights.
4. **Validation:** Cross-check extracted phrases against manual review for accuracy.
5. **Delivery:** Provide the artifact to the team for direct review and action.
6. **Documentation:** Log the analysis parameters (e.g., transcript version, extraction rules) for reproducibility.

**What changed:**
Added explicit source specification ("full earnings call transcript") and structured output requirements to Chisel’s original plan.
