# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-982` (dept) · 2026-08-10T19:26:54.160437+00:00
> Participants: Graft · synthesized by mistral/mistral-small-latest

**Decision:**
Proceed with embedding unembedded memory fragments from the Hindsight database.

**Plan:**
1. Query the Hindsight memory database via the MCP server to retrieve all unembedded elements.
2. Filter and deduplicate the raw list to identify unique memory fragments requiring embedding.
3. For each fragment, generate contextual embeddings using the configured embedding model.
4. Store the embeddings in the memory system with metadata linking to source fragments.
5. Validate embeddings by cross-referencing with existing memory graphs for consistency.
6. Log completion metrics (e.g., fragments embedded, failures, duplicates) for tracking.

**What changed:**
Unembedded memory fragments are now embedded and integrated into the brain graph.
