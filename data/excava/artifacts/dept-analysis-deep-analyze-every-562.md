# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-562` (dept) · 2026-07-30T19:24:54.170342+00:00
> Participants: Chisel, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. **Extract full earnings call transcript** from the repo as the primary source for analysis.
2. **Run BloodHound-MCP** on the transcript to generate a speaker attribution map, resolving overlaps and ambiguities.
3. **Label every segment** with its true speaker, including timestamps and frequency counts.
4. **Verify the artifact** for accuracy and completeness against the source transcript.
5. **Enrich the analysis** with contextual metadata (e.g., speaker roles, sentiment trends) from >=1 external source.
6. **Document the process** in a GitHub markdown file with clear steps and outputs.

**What changed:** Speaker attribution map generated and verified.
