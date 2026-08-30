# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-896` (dept) · 2026-08-30T02:34:50.622425+00:00
> Participants: Graft · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the Hindsight memory database via the MCP server to retrieve all unembedded memory fragments.
2. Parse the retrieved fragments to identify and extract unembedded elements (e.g., raw text, metadata, or unresolved references).
3. For each unembedded element, apply an embedding model (e.g., Sentence-BERT or similar) to generate vector representations.
4. Store the embedded elements back into the memory database, linking them to their original context or metadata.
5. Validate the embedding process by spot-checking a sample of fragments for consistency and accuracy.
6. Log the operation’s success/failure and update the memory graph to reflect the newly embedded elements.

**What changed:** Unembedded memory fragments were identified, embedded, and integrated into the memory graph.
