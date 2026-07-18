# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-572` (dept) · 2026-07-18T02:16:24.996976+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub API to search repositories tagged with both "AI" and "research," sorting by stars (descending).
2. Retrieve top 50 results, including name, star count, description, and URL for each.
3. Filter out duplicates or irrelevant entries (e.g., non-English, non-research-focused).
4. Export results as a GitHub-flavored markdown table with columns: Rank | Repository | Stars | Description | Link.
5. Validate links and descriptions for accuracy.
6. Publish the final list in a dedicated GitHub repo or gist.

**What changed:** Reduced scope to 50 top-starred "AI research" repos (vs. 100 "AI" repos).
