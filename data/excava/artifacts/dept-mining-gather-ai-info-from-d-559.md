# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-559` (dept) · 2026-07-17T21:23:56.527251+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub’s advanced search to query repositories tagged with both "AI" and "research."
2. Sort results by stars (descending) and limit to the top 100.
3. Extract repository names, descriptions, and star counts for each entry.
4. Format the output as a GitHub-flavored markdown list with bolded names and star counts.
5. Validate that all entries are research-focused (e.g., exclude non-research AI projects like apps or tutorials).
6. Output the final list in the specified format.

**What changed:** Expanded scope to include "research" tag for higher-quality AI repositories.
