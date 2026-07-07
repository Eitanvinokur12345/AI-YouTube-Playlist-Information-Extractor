# Raise link coverage: pick the next 200 unlinked elements and the fastest resolution path

> Decision artifact · room `dept-raise-link-coverage-pick-the-353` (dept) · 2026-07-07T14:41:29.610352+00:00
> Participants: Fetch, Probe, Ledger · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Conduct a comprehensive scan to identify the next 200 unlinked elements and their fastest resolution paths.

**Plan:**
1. Run `mwxml dump` on a sample page to gather all link types present in the content.
2. Use `grep` to extract all applicable links, including `[[...]]`, `{{...}}`, bare URLs, image embeds, and interwiki links.
3. Cross-reference the output against `all_links.txt` to filter out already linked entries.
4. Identify the next 200 unlinked elements based on the comprehensive link scan.
5. Analyze and determine the fastest resolution paths for the unlinked elements identified.
6. Document the findings and prepare the data for implementation.

**What changed:** The approach now includes a broader capture of link types, ensuring no entries are overlooked.
