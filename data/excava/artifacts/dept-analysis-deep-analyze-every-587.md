# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-587` (dept) · 2026-08-23T17:39:33.161651+00:00
> Participants: Chisel, Sift, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**
Marrow synthesizes the debate into a directed action.

**Plan:**
1. **Input Artifact:** Use the *full earnings call transcript* as the sole input for BloodHound-MCP.
2. **Execution:** Run BloodHound-MCP on the transcript to generate a *speaker influence graph*.
3. **Analysis:** Extract *decision drivers*, *alignments*, and *conflicts* from the graph.
4. **Validation:** Cross-check raw transcript snippets against the graph for accuracy.
5. **Output:** Produce a structured report (Markdown) with the graph, key findings, and anomalies.
6. **Archive:** Store the graph and report in the repo under `/analysis/speaker_influence/`.

**What changed:** Clarified input artifact ("full transcript") and formalized output steps.
