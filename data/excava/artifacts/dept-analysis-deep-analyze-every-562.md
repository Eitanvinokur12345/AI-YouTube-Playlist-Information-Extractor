# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-562` (dept) · 2026-07-31T04:29:50.716525+00:00
> Participants: Chisel, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**
BloodHound-MCP will be executed to generate a speaker attribution map for the full earnings call transcript.

**Plan:**
1. Run BloodHound-MCP on the full earnings call transcript to process all segments.
2. Generate a speaker attribution map labeling every segment with its true speaker.
3. Resolve overlaps and ambiguities in speaker attribution.
4. Produce a clean, verifiable artifact showing who spoke, when, and how often.
5. Validate the artifact for accuracy and completeness.
6. Archive the artifact for future reference.

**What changed:** Execution of BloodHound-MCP to produce a speaker attribution map.
