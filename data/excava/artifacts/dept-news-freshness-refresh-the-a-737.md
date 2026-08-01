# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-737` (dept) · 2026-07-31T15:48:10.652480+00:00
> Participants: Scoop, Wire · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Fetch OpenAI’s latest official blog posts via their RSS feed or `/feed.xml`.
2. Parse the feed to extract the most recent AI-related updates (e.g., model releases, policy changes).
3. Scrape NVIDIA’s latest developer announcements from their official blog or developer portal.
4. Cross-reference both sources to identify overlapping themes (e.g., AI infrastructure, model optimizations).
5. Compile a 1–2 sentence lead summarizing key decisions/updates from both sources.
6. Format the digest in GitHub-flavored markdown with timestamps and source links.

**What changed:** Consolidated AI-news sourcing into a dual-source digest (OpenAI + NVIDIA) for maximum freshness.
