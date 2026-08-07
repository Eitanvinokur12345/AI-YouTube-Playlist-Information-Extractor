# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-984` (dept) · 2026-08-07T01:15:09.532691+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Query Product Hunt’s API for all posts tagged "AI" published in the last 30 days.

**Plan:**
1. Use Product Hunt’s API to fetch posts tagged "AI" from the last 30 days.
2. Extract raw data including product names, upvotes, and user comments.
3. Store the data in a structured format (e.g., JSON/CSV) for immediate review.
4. Cross-reference with other sources (GitHub/HN/Reddit/Telegram) to validate trends.
5. Identify top-performing AI products and key themes from comments.
6. Compile a summary report for further analysis.

**What changed:**
Focused on Product Hunt’s API as the first step to gather diverse AI product insights.
