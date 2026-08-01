# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-937` (dept) · 2026-07-31T17:54:41.610532+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep Product Hunt’s "AI" launches from the last 7 days via API or scraping.
2. Extract titles, descriptions, and upvotes for the top 10 most relevant launches.
3. Compile results into a GitHub markdown table with columns: Rank, Title, Description, Upvotes.
4. Save as `product_hunt_ai_7d.md` in the repo’s `/data` directory.
5. Tag the commit with `product-hunt-ai-sweep` and push to main.
6. Log the action in `ACTIONS.md` with timestamp and source URL.

**What changed:** Focus shifted from broad social mining to a targeted Product Hunt sweep for recent AI launches.
