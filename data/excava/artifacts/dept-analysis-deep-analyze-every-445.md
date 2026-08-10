# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-445` (dept) · 2026-08-10T08:16:27.876664+00:00
> Participants: Chisel, Sift, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**
Marrow will use the local `kimtaeyoon83/mcp-server-youtube-transcript` tool to extract a timestamped, speaker-labeled transcript of the earnings call for deep analysis.

**Plan:**
1. Run `kimtaeyoon83/mcp-server-youtube-transcript` on the full earnings call transcript to generate a clean, timestamped, speaker-labeled artifact.
2. Validate the transcript for accuracy (speaker labels, timestamps, pauses) against the original source.
3. Enrich the transcript with contextual metadata (e.g., speaker roles, call segments) from the full source.
4. Store the validated transcript in a dedicated analysis repo branch (e.g., `analysis/earnings-call-transcript`).
5. Cross-reference the transcript with supplementary materials (e.g., slides, financial tables) from the repo.
6. Generate a consolidated analysis report (markdown) synthesizing all extracted elements.

**What changed:**
Replaced reliance on Luma’s external tool with a local, controllable transcript extraction method.
