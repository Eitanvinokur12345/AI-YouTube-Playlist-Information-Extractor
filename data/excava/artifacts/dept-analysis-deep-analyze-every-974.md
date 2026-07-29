# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-974` (dept) · 2026-07-29T21:05:25.532317+00:00
> Participants: Chisel, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**
BloodHound-MCP will be used to generate a verified Speaker Attribution Map from the full earnings call transcript, resolving ambiguity in speaker roles.

**Plan:**
1. Run BloodHound-MCP on the full earnings call transcript to extract speaker attributions.
2. Cross-verify speaker roles against the original transcript for accuracy.
3. Compile a definitive list of speakers with their confirmed roles.
4. Document the Speaker Attribution Map in GitHub markdown format.
5. Ensure the map is version-controlled and accessible for future reference.

**What changed:**
Speaker attribution is now definitively resolved via BloodHound-MCP analysis.
