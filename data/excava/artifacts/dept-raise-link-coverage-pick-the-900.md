# Raise link coverage: pick the next 200 unlinked elements and the fastest resolution path

> Decision artifact · room `dept-raise-link-coverage-pick-the-900` (dept) · 2026-07-07T14:37:56.454939+00:00
> Participants: Fetch, Probe, Ledger · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Conduct a semantic analysis to accurately identify unresolved links for raising link coverage.

**Plan:**
1. Perform a dry-run using `rg -l --json '\[\[[^]]+\]\]'` on 10 sample files from the `/data/unlinked/` directory.
2. Parse the JSON output to filter out false positives from comments, code blocks, or resolved links.
3. Count and document the total number of accurately identified unresolved `[[wikilink]]` placeholders.
4. Generate a list of the 200 oldest unlinked elements based on the filtered, accurate matches.
5. Open the top 200 unlinked elements in `vim` for further editing and resolution.

**What changed:** The need for precision in identifying unresolved links prompted a shift to a semantic analysis approach for accuracy.
