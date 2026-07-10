# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-640` (dept) · 2026-07-10T02:49:11.142521+00:00
> Participants: Scoop, Factcheck, Wire · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Use arXiv JSON API with UTC timestamp filtering and parse titles via `jq` for safety.  
**Plan:**  
1. Utilize the arXiv JSON API endpoint with the query `search_query=cat:cs.LG&sortBy=submittedDate&max_results=100`.  
2. Implement UTC timestamp filtering to ensure papers are within the last 24 hours.  
3. Use `jq` to safely parse titles from the JSON response.  
4. Extract necessary information: paper IDs, titles, abstracts, submit times (UTC), and source URLs.  
5. Compile the data into `ai-news-digest.json`.  
**What changed:** Decision shifted from using regex with XML to a robust JSON API with error handling.
