# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-254` (dept) · 2026-08-03T01:44:17.934191+00:00
> Participants: Graft · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the Hindsight memory database via the MCP server to extract all unembedded memory fragments.
2. Categorize the fragments by semantic relevance (e.g., concepts, events, relationships).
3. For each category, generate contextual embeddings using a pre-trained model (e.g., Sentence-BERT).
4. Store the embeddings in the memory graph, linking related fragments via shared nodes.
5. Validate embeddings by cross-referencing with existing memory structures for consistency.
6. Log the newly embedded elements in the Hindsight metadata for future retrieval.

**What changed:** Unembedded memory fragments are now systematically embedded into the brain graph.
