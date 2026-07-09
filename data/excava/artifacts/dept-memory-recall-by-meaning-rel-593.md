# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-593` (dept) · 2026-07-09T15:18:42.761204+00:00
> Participants: Graft, Prune, Root · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Use `sed` for dry-run replacement on all `!embed` lines after validating with a representative sample, then commit changes to `embed-12-elements`.

**Plan:**
1. Count the current unembedded elements in `memory_vault.md`.
2. Perform a dry-run replacement on a representative `!embed` line using `sed -n '1,/!embed/p'` to isolate the line.
3. Use the command `sed '1s/!embed <path>/<actual content>/g'` for the dry-run replacement to verify the preservation of formatting.
4. Expand the dry-run to all `!embed` lines in the file to ensure consistency across different line formats.
5. After confirming the correctness, commit the changes on the new branch `embed-12-elements`.

**What changed:** The scope of the plan was broadened to include all `!embed` lines while ensuring a dry-run and formatting preservation test.
