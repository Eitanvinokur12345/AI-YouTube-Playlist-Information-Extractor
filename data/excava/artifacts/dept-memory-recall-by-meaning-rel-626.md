# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-626` (dept) · 2026-07-10T07:22:02.750761+00:00
> Participants: Graft, Prune, Root · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Prioritize resolving the top 3 most recent and context-rich unembedded elements by cross-referencing `./memory/unembedded.md` with `./brain-graph.js`, ensuring each embeds meaningfully into the graph.

**Plan:**
1. Run `grep -R -n "TODO\|FIXME\|UNEMBEDDED" ./memory/ --include="*.md"` to locate all unembedded elements.
2. Sort the results by recency using `sort -r` to identify the most recent items.
3. Review the top 3 entries in the context of current priorities and relevance to our goals.
4. Cross-reference these entries against `./memory/unembedded.md` for context-rich details.
5. Integrate them into the brain graph using `./brain-graph.js`, ensuring meaningful connections are established.

**What changed:** The decision now emphasizes both recency and context relevance to prioritize embedding efforts.
