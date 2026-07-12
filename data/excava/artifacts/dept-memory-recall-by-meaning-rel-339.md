# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-339` (dept) · 2026-07-12T19:41:28.989084+00:00
> Participants: Graft, Prune, Root · synthesized by mistral/mistral-small-latest

**Decision:** Build the single shared memory graph now—unified from day one to keep recall coherent as we scale.

**Plan:**
1. Define a core schema for nodes and relationships (e.g., "idea," "tool," "conversation") and enforce it across all inputs.
2. Implement a tagging system where every new memory is labeled by its semantic meaning (e.g., "memory," "tool," "debate") before integration.
3. Automate cross-linking between related nodes during ingestion (e.g., connect a "debate" node to its "tools" and "outcomes").
4. Establish a review cycle (weekly) to validate relationships and prune outdated or incorrect connections.
5. Use a single, centralized graph database (e.g., Neo4j) to ensure atomic updates and prevent fragmentation.
6. Document the graph’s structure and update rules in a shared README for onboarding and maintenance.

**What changed:** Unified graph adopted over federated/modular alternatives to prioritize coherence and scalability from day one.
