# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-592` (dept) · 2026-07-17T23:26:52.208275+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub’s advanced search to query repositories tagged with both "AI" and "research."
2. Sort results by stars (descending) and limit to the top 100.
3. Extract for each entry: name, description, star count, and URL.
4. Format results as a numbered markdown list with bolded names and star counts.
5. Include a one-line note per entry linking to the repository.
6. Validate that all entries are research-focused (filter out non-research AI projects if needed).

**What changed:** Expanded scope from "AI" alone to "AI" + "research" for higher relevance.
