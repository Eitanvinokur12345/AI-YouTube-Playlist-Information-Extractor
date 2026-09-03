# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-606` (dept) · 2026-09-03T19:19:08.340148+00:00
> Participants: Graft · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the Hindsight memory database via the MCP server to retrieve all unembedded memories.
2. Parse the output to identify memories lacking semantic embeddings or graph connections.
3. For each unembedded memory, generate contextual embeddings using the latest embedding model.
4. Update the brain graph by linking embeddings to related memories via semantic relationships.
5. Validate embeddings by checking for orphaned or disconnected nodes in the graph.
6. Log the completion status and timestamp for audit and future recall.

**What changed:** Unembedded memories were identified and prioritized for embedding to complete the brain graph.
