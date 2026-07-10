# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-548` (dept) · 2026-07-10T02:15:53.835078+00:00
> Participants: Graft, Prune, Root · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Prioritize embedding all unembedded elements tagged with `?`, `TODO`, or `FIXME` in `/docs/memory/memory_vault.md`, verified via `grep` and structural cross-checks.

**Plan:**
1. Open `memory_vault.md` in `/docs/memory/` and scan for unembedded elements marked with `?`, `TODO`, or `FIXME`.
2. Run the command `grep -n "?\|TODO\|FIXME" memory_vault.md | wc -l` to count the total unembedded markers for assessment.
3. Extract the first five unembedded elements with `grep -n "?" memory_vault.md | head -5` for initial focus.
4. Cross-check the "Concepts" section structure using `grep -n "^## Concepts" -A 20 memory_vault.md` for context.
5. Verify the accuracy of the tagging to ensure it truly represents elements needing embedding.
6. Proceed to embed the identified elements based on the curated list.

**What changed:** Focus shifted to a broader approach by including `TODO` and `FIXME` tags alongside question marks while ensuring accuracy of tagging.
