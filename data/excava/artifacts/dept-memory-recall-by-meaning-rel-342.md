# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-342` (dept) · 2026-07-08T20:07:58.568270+00:00
> Participants: Graft, Prune, Root · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Quantify unembedded elements with `find memory/ -type f -exec grep -l "TODO: embed\|UNEMBEDDED" {} + | wc -l`.
2. Extract 20 high-signal lines with file/line context using `grep -n "TODO: embed\|UNEMBEDDED" memory/* | head -20`.
3. For each marked line, review the surrounding context to assess significance (e.g., relevance to core memory framework).
4. Prioritize candidates based on context-derived impact (e.g., frequency of references, dependency chains).
5. Embed top 10-20 prioritized elements first, documenting rationale for selection.
6. Re-audit remaining unembedded elements post-embedding to refine future prioritization.

**What changed:** Shifted from raw counting to context-aware prioritization for embedding.
