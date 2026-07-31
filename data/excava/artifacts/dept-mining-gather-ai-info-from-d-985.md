# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-985` (dept) · 2026-07-31T03:51:42.296255+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep GitHub’s trending AI repositories from the last 7 days with >50 stars.
2. Filter and rank the results by star count, returning the top 20.
3. Cross-reference with Product Hunt’s AI-tagged launches from the last 7 days.
4. Output a combined ranked list of the top 20 projects by GitHub stars + Product Hunt upvotes.
5. Include metadata (repo name, star count, upvotes, URL) for each entry.
6. Append a summary of trends observed in the last 7 days.

**What changed:** Prioritized GitHub + Product Hunt over single-source approach.
