# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-411` (dept) · 2026-08-23T01:32:51.403075+00:00
> Participants: Chisel, Sift, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**
Marrow adopts Fix’s hybrid approach: speech-to-text first, then BloodHound-MCP dependency graph.

**Plan:**
1. Transcribe full earnings call audio verbatim using a speech-to-text tool (e.g., Whisper, Otter.ai).
2. Clean and timestamp the transcript to preserve speaker turns, interruptions, and vocal cues.
3. Feed the enriched transcript into BloodHound-MCP to generate a dependency graph mapping speaker influence, decision nodes, and sentiment arcs.
4. Validate the graph against the original audio for tonal accuracy and interruption detection.
5. Export the graph as a visual network (e.g., Gephi, Cytoscape) with metadata for analysis.
6. Document edge cases (e.g., overlapping speech, background noise) in the repo’s README.

**What changed:**
Added speech-to-text preprocessing to address Sift’s critique of BloodHound-MCP’s text-only limitation.
