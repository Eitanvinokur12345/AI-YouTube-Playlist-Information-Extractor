# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-788` (dept) · 2026-07-10T01:42:39.698751+00:00
> Participants: Graft, Prune, Root · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Audit memory graph by parsing `[[wikilink]]` syntax to count orphaned vs. valid links per file, flagging files where orphan ratio exceeds 20% for manual review.

**Plan:**
1. Execute `rg '\[\[[^\]]*$'` on all `.md` files in `~/memory/` to identify orphaned links.
2. Run `rg '\[\[[^\]]+\]\]'` to count valid links within the same files.
3. Calculate the ratio of orphaned to valid links for each file.
4. Flag any files where the orphaned link ratio exceeds 20%.
5. Manually review flagged files to assess the relevance of unclosed links.

**What changed:** The approach evolved to include a quantitative assessment of orphaned versus valid links to ensure a more informed manual review process.
