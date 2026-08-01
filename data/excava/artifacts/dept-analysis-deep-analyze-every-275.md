# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-275` (dept) · 2026-07-31T23:04:24.537806+00:00
> Participants: Chisel, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**
Chisel’s BloodHound-MCP approach is adopted to generate a structured speaker influence graph and conversation thread map from the full earnings call transcript.

**Plan:**
1. **Preprocess** the full earnings call transcript into a clean, speaker-segmented text file (e.g., JSONL with `speaker`, `timestamp`, and `utterance` fields).
2. **Run BloodHound-MCP** on the preprocessed transcript to generate:
   - A speaker influence graph (nodes = speakers, edges = influence metrics like adjacency, sentiment shifts, or topic dominance).
   - A conversation thread map (threads = sequences of interlinked utterances, annotated with speaker roles and temporal markers).
3. **Validate** the output by spot-checking 5–10% of the graph edges/threads against the raw transcript for accuracy.
4. **Enrich** the graph with external context (e.g., stock price movements during the call, prior earnings call comparisons) to highlight anomalies or outliers.
5. **Export** the final artifacts as GitHub-flavored Markdown (graph visualization via Mermaid, thread summaries as bullet points) and a JSON file for downstream analysis.
6. **Document** limitations (e.g., sarcasm/ambiguity detection gaps) and next-step hypotheses (e.g., "Speaker X’s influence spikes correlate with Q&A sections").

**What changed:**
BloodHound-MCP’s single-pass structured analysis replaces manual thread mapping, ensuring reproducibility and scalability.
