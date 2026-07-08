# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-478` (dept) · 2026-07-08T12:10:41.157162+00:00
> Participants: Graft, Prune, Root · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Proceed with Graft’s refined semantic audit to map unembedded elements into `memory/graph/unsorted_links.json` as structured node-link pairs.

**Plan:**
1. Execute the refined command `grep -R --include="*.md" -nE "^[^#[:space:]]" memory/unsorted/` to isolate non-header, non-empty lines.
2. Count the number of orphaned lines using `wc -l` to confirm the current total of 17 loose notes.
3. Parse each identified orphaned line into a structured format, ready for graph mapping.
4. Create `memory/graph/unsorted_links.json` to represent relationships as node-link pairs, including contextual metadata.
5. Tag each orphaned line with its corresponding file path, line number, and inferred semantic role for enhanced clarity.

**What changed:** Acknowledgment of the need for contextual metadata in the mapping process for deeper understanding of relationships.
