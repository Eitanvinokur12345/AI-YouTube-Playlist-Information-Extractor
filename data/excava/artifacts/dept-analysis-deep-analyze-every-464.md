# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-464` (dept) · 2026-07-30T17:31:59.961299+00:00
> Participants: Chisel, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**
Run BloodHound-MCP on the full earnings call transcript to generate a strict human-only "Speaker Attribution Map" live doc.

**Plan:**
1. Execute BloodHound-MCP on the full earnings call transcript to extract raw speaker attributions with timestamps.
2. Filter results to isolate direct quotes vs. paraphrased interpretations using confidence thresholds (e.g., >90% for direct quotes).
3. Cross-validate attributions against the original transcript for accuracy, flagging discrepancies for review.
4. Compile verified attributions into a GitHub markdown live doc with speaker names, timestamps, and confidence scores.
5. Enrich the doc with contextual metadata (e.g., speaker roles, sentiment cues) from >=1 external source (e.g., earnings call metadata or prior analysis).
6. Publish the doc as the final "Speaker Attribution Map" and archive raw BloodHound outputs for reproducibility.

**What changed:**
Marrow adopted Chisel’s BloodHound-MCP action verbatim, replacing the original vague plan with a concrete, multi-step execution.
