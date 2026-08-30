# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-741` (dept) · 2026-08-30T03:16:44.757640+00:00
> Participants: Graft · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the Hindsight memory database via the MCP server to retrieve all unembedded elements.
2. Categorize the unembedded elements by semantic relevance (e.g., concepts, facts, relationships).
3. For each category, generate contextual embeddings using the brain graph’s embedding model.
4. Integrate the new embeddings into the existing memory graph, resolving duplicates or conflicts.
5. Validate the updated memory graph by testing recall accuracy on a subset of embedded elements.
6. Log the changes in the memory audit trail for traceability.

**What changed:** Unembedded memory elements were identified and scheduled for embedding.
