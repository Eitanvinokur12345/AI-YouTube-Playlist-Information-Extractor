# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-700` (dept) · 2026-07-31T16:31:20.266796+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep GitHub’s AI-related repos created in the last 7 days using GitHub’s API or scraping tools.
2. Extract repo names, descriptions, stars, and creation dates for each relevant repo.
3. Clean and deduplicate the data into a structured format (e.g., CSV/JSON).
4. Output a markdown table with columns: **Repo Name**, **Description**, **Stars**, **Creation Date**.
5. Deliver the clean list to the lead for review.
6. Log the action in the project tracker.

**What changed:** Focus shifted from Product Hunt to GitHub per Boulder’s directive.
