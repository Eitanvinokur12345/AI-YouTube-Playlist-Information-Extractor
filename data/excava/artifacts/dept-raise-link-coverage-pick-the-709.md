# Raise link coverage: pick the next 200 unlinked elements and the fastest resolution path

> Decision artifact · room `dept-raise-link-coverage-pick-the-709` (dept) · 2026-07-07T12:46:14.428261+00:00
> Participants: Fetch, Probe, Ledger · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Conduct a comprehensive scan of unlinked elements and prioritize by resolution speed and contextual importance.

**Plan:**
1. Run a `ripgrep` command to scan the entire `docs/` directory for all unlinked elements, including `[[wikilink]]`, `#anchor`, and bare URLs.
2. Output the results in a sortable format that includes the filename, element type, and line numbers for better decision-making.
3. Analyze the context of each unlinked element to assess resolution speed and importance.
4. Rank the 200 unlinked elements based on the analysis and contextual importance.
5. Create a clear strategy for linking the top-priority elements based on the rankings.

**What changed:** Shifted focus from a limited search to a comprehensive analysis of all potential unlinked elements for improved decision-making.
