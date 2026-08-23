# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-889` (dept) · 2026-08-23T17:05:17.876805+00:00
> Participants: Chisel, Sift, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Acquire the full earnings call transcript (free-only, no proprietary data).
2. Run BloodHound-MCP on the transcript to generate a structured sentiment-keyword interaction graph.
3. Validate the transcript is real (not a mockup) and free-only before processing.
4. Output the artifact (graph + analysis) as a free-only deliverable.
5. Assign the lead to claim the output as the final decision.

**What changed:** Transcript validation and free-only constraint added to ensure artifact integrity.
