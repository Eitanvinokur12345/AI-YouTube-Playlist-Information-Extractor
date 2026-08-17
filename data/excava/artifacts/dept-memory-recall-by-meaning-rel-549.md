# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-549` (dept) · 2026-08-17T01:16:24.924175+00:00
> Participants: Graft · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the Hindsight memory database via the MCP server to extract all unembedded memory elements (raw facts, decisions, insights).
2. Parse the raw list to identify unintegrated elements requiring embedding into the brain graph.
3. Cross-reference new elements with existing graph nodes to detect relationships, contradictions, or gaps.
4. Embed validated elements into the brain graph with contextual links (e.g., "derived from," "contradicts," "supports").
5. Tag unembedded elements for future review if no immediate integration is possible.
6. Log the operation in the Hindsight audit trail with timestamps and embedded element IDs.

**What changed:** Unembedded memory elements are now identified and ready for graph integration.
