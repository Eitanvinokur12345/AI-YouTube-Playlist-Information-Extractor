# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-562` (dept) · 2026-07-30T07:16:22.455840+00:00
> Participants: Chisel, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run BloodHound-MCP on the full earnings call transcript to generate a speaker attribution map, resolving overlaps and ambiguities.
2. Produce a clean, verifiable artifact labeling every segment with its true speaker, including timestamps and frequency counts.
3. Validate the artifact against the original transcript to ensure accuracy and completeness.
4. Enrich the analysis with contextual metadata (e.g., speaker roles, sentiment trends) from the full transcript.
5. Cross-reference with additional sources (e.g., SEC filings, press releases) to corroborate speaker attributions.
6. Publish the final artifact (speaker map + enriched analysis) in the repo with clear documentation.

**What changed:** BloodHound-MCP is now explicitly tasked with producing a timestamped, frequency-annotated speaker attribution map, validated against the full transcript and enriched with contextual metadata.
