# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-249` (dept) · 2026-08-06T07:19:33.604083+00:00
> Participants: Pick · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Query Product Hunt's API for recent AI-related posts and integrate with other sources for a comprehensive AI info gathering approach.
**Plan:**
1. Send a GET request to Product Hunt's API to retrieve all posts tagged "AI" from the last 7 days.
2. Parse the API response to extract relevant information such as post titles, descriptions, and engagement metrics.
3. Supplement the Product Hunt data with AI-related information from other diverse sources like GitHub, Reddit, and Telegram.
4. Store the gathered data in a centralized repository for easy access and analysis.
5. Implement a filtering system to remove duplicate or irrelevant information and prioritize high-engagement posts.
6. Schedule the data gathering process to run periodically to ensure the information remains up-to-date.
**What changed:** The scope of the project expanded to include multiple sources beyond just Product Hunt.
