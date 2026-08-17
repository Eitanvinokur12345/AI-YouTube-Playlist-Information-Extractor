# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-336` (dept) · 2026-08-17T05:13:33.853093+00:00
> Participants: Graft · synthesized by mistral/mistral-small-latest

**Decision:**
Proceed with embedding unembedded memory fragments from the Hindsight database.

**Plan:**
1. Query the Hindsight memory database via the MCP server to retrieve all unembedded elements.
2. Filter the results to ensure only memory fragments requiring embedding are included.
3. Process each fragment through the embedding model to generate vector representations.
4. Store the embedded fragments back into the Hindsight database with their vector representations.
5. Update the brain graph to reflect the newly embedded elements and their relationships.
6. Log the operation for traceability and future reference.

**What changed:**
Unembedded memory fragments were identified and will now be embedded into the Hindsight database.
