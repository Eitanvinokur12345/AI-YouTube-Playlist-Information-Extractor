# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-931` (dept) · 2026-07-18T01:52:25.888674+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a GitHub search for repositories tagged with both "AI" and "research."
2. Sort results by stars in descending order.
3. Extract the top 50 repositories with their descriptions, star counts, and links.
4. Format the output as a GitHub-flavored markdown list with headers for each entry.
5. Exclude any repositories that are not directly related to AI research.
6. Validate links and descriptions for accuracy before finalizing.

**What changed:** Reduced scope from top 100 to top 50 and added "research" tag filter.
