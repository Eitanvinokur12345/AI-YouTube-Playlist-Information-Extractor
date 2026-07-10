# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-206` (dept) · 2026-07-10T03:56:32.300797+00:00
> Participants: Graft, Prune, Root · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Scan `brain_graph/` for unembedded elements, verify coherence manually before embedding.

**Plan:**
1. Execute the command `grep -LE '## Meaning:|->|\[\[.*\]\]' brain_graph/ | wc -l` to identify unembedded files.
2. Create a list of candidate files that are raw or unlinked.
3. Review each candidate file for contextual relevance and coherence.
4. Embed meaning in selected files based on the findings from the review.
5. Update the brain graph with the newly embedded information.

**What changed:** Added a step to manually verify coherence of the identified candidate files.
