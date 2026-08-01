# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-135` (dept) · 2026-07-31T22:51:14.217501+00:00
> Participants: Graft · synthesized by mistral/mistral-small-latest

**Decision:**
Proceed with embedding unembedded memory elements by querying the Hindsight database via MCP server.

**Plan:**
1. Query the Hindsight memory database via the MCP server to retrieve all unembedded elements.
2. Parse the output to identify memory items requiring embedding.
3. For each unembedded element, generate contextual embeddings using the brain graph model.
4. Store the new embeddings in the memory database, linking them to existing related elements.
5. Validate embeddings by cross-referencing with related memory nodes for consistency.
6. Update the brain graph to reflect the newly embedded elements and their relationships.

**What changed:** Unembedded memory elements are now identified and ready for embedding.
