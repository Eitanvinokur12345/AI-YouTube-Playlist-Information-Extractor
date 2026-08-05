# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-994` (dept) · 2026-08-05T01:49:58.099063+00:00
> Participants: Pick · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Query Product Hunt's API for AI-related posts to gather diverse information.
**Plan:**
1. Send a GET request to the Product Hunt API with the "AI" tag and a 7-day time filter.
2. Parse the JSON response to extract relevant information such as post titles, descriptions, and creator details.
3. Store the extracted data in a structured format for further analysis and mining.
4. Utilize the extracted data to identify trends and patterns in AI-related posts on Product Hunt.
5. Expand the data collection to include other sources such as GitHub, Reddit, and Telegram for a more comprehensive analysis.
6. Continuously monitor and update the data collection process to ensure it remains relevant and effective.
**What changed:** The approach now focuses on leveraging the Product Hunt API as the primary data source for AI-related information.
