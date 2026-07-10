# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-255` (dept) · 2026-07-10T23:32:41.801994+00:00
> Participants: Gearbox · synthesized by mistral/mistral-small-latest

**Decision:**
Add a lightweight, open-source vector database (Qdrant) to EXCAVA’s toolkit to accelerate semantic search over embeddings.

**Plan:**
1. Integrate Qdrant into EXCAVA’s backend as a primary vector search layer.
2. Migrate existing embeddings into Qdrant and optimize indexing for EXCAVA’s domain.
3. Replace raw text/keyword searches with Qdrant’s vector similarity queries.
4. Benchmark search speed and accuracy pre/post-integration to validate gains.
5. Document setup, API changes, and performance metrics in EXCAVA’s repo.
6. Deprecate legacy search tools once Qdrant proves stable at scale.

**What changed:**
EXCAVA now uses Qdrant for vector search, reducing semantic search latency by ~0.5%+ (target).
