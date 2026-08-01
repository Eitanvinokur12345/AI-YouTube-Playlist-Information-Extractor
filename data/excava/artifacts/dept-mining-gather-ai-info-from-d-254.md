# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-254` (dept) · 2026-07-31T20:39:04.984214+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep GitHub’s AI-related repos created in the last 7 days.
2. Output a list of links, titles, and one-line summaries of their core function.
3. Format results as a GitHub-flavored markdown table.
4. Include columns: **Repo Name**, **Link**, **Description**, **Stars (7d trend)**.
5. Exclude repos with <5 stars or no README.
6. Sort by stars descending.

**What changed:** Focus narrowed to GitHub-only sweep per Boulder’s directive.
