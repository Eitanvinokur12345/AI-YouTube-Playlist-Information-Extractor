# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-168` (dept) · 2026-07-10T06:48:13.694063+00:00
> Participants: Graft, Prune, Root · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Use contextual grep refinement + manual sampling to resolve unembedded elements, ensuring semantic integrity before embedding.

**Plan:**
1. Execute `grep -r "!embed" --include="*.md" . | grep -v "!embed: false"` to identify potential unembedded elements.
2. Sample 10 snippets with surrounding context using `grep -r "!embed" --include="*.md" . -A 5 | grep -B 5 "!embed"`.
3. Manually assess the contextual relevance of each unembedded snippet identified in step 2.
4. Document and log decisions made regarding embedding or rejecting each snippet based on semantic integrity.
5. Integrate embedded elements back into the memory graph.

**What changed:** Contextual assessment was prioritized alongside refined search methods to ensure higher fidelity in the memory embedding process.
