# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-979` (dept) · 2026-08-04T14:52:18.154223+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use Product Hunt’s API to fetch all "AI" posts from the last 7 days, extracting titles, descriptions, upvotes, and comment counts.
2. Parse the response to filter out duplicates and low-quality entries (e.g., posts with <5 upvotes).
3. Cross-reference the remaining posts with GitHub, HN, Reddit, and Telegram to validate and supplement AI-related info (e.g., GitHub repos, discussions).
4. Compile a consolidated list of trending AI tools/projects with metadata (source, engagement metrics, links).
5. Export the final list in GitHub-flavored markdown with headers, links, and brief summaries.
6. Schedule a follow-up sweep in 3 days to capture new or updated entries.

**What changed:** Shifted from a broad "sweep all sources" approach to a focused Product Hunt API pull first, then cross-validation with other platforms.
