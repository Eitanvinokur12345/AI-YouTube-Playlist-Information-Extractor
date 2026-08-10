# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-565` (dept) · 2026-08-10T13:59:55.750489+00:00
> Participants: Graft · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the Hindsight memory database via the MCP server to retrieve all unembedded elements.
2. Identify memory fragments requiring embedding to complete the brain graph.
3. Process each fragment through the embedding pipeline (e.g., vectorization, relational mapping).
4. Validate embeddings for consistency and completeness against the existing brain graph.
5. Update the brain graph with newly embedded elements and their relationships.
6. Log the changes and trigger downstream memory consolidation if needed.

**What changed:** Unembedded memory fragments are now embedded, completing the brain graph.
