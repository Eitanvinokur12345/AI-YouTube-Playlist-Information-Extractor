# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-176` (dept) · 2026-07-30T20:22:48.898594+00:00
> Participants: Chisel, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run BloodHound-MCP on the full earnings call transcript to extract all speaker claims, sentiment shifts, and factual evidence into a structured graph artifact.
2. Cross-reference extracted claims against >=1 external source (e.g., SEC filings, analyst reports) to validate or flag contradictions.
3. Generate a decision-ready artifact (e.g., JSON/CSV) mapping claims to evidence status (supported/contradicted/missing).
4. Identify key sentiment shifts per speaker and correlate with factual claims for risk assessment.
5. Highlight top 3-5 unresolved contradictions or missing evidence for executive review.
6. Distribute artifact to stakeholders with a 24-hour review window before finalizing.

**What changed:** Structured evidence mapping replaces unstructured analysis, enabling actionable validation.
