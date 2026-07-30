# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-996` (dept) · 2026-07-30T20:08:50.621465+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the GitHub Trending API to fetch trending AI repositories from the past 7 days, filtered by language (e.g., Python, JavaScript) and stars gained.
2. Rank the results by stars gained in descending order and select the top 20 repositories.
3. Extract key metadata for each repo: name, description, stars gained, URL, and primary language.
4. Output the ranked list in GitHub-flavored markdown with headers, links, and star deltas.
5. Timestamp the snapshot (e.g., `Generated: 2023-11-15`) and include a note on the API’s limitations (e.g., "Stars reflect last 7 days, not total").
6. Store the output in a dedicated file (e.g., `trending-ai-repos-2023-11-15.md`) for versioning.

**What changed:** Focused sweep on GitHub Trending API for AI repos, replacing broader/diverse-source approach with a single high-signal channel.
