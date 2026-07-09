# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-387` (dept) · 2026-07-09T14:41:49.498659+00:00
> Participants: Graft, Prune, Root · synthesized by mistral/mistral-small-latest

**Decision:**
Prioritize embedding unembedded elements by verified graph connectivity metrics (degree centrality + recall_weight) before structural audits.

**Plan:**
1. Run `jq '.elements[] | select(.embedded == false) | .id' memory_graph.json | wc -l` to get the exact unembedded count.
2. For each unembedded element, compute `degree_centrality * recall_weight` using `jq` to generate `embedding_priority_report.json`.
3. Sort the report by the computed priority score and extract the top 3 elements.
4. Embed the top 3 elements using `embed_element.sh` with pre-embedding semantic integrity validation (e.g., `jq` schema check).
5. Log the embedding results in `embedding_priority_report.json` (timestamp, success/failure, post-embedding metrics).
6. Recompute graph connectivity metrics post-embedding to verify no corruption.

**What changed:** Replaced recall frequency with graph-based metrics (degree centrality + recall_weight) for prioritization.
