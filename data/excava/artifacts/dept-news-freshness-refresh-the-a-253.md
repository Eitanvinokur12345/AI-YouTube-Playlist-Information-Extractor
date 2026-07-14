# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-253` (dept) · 2026-07-14T17:43:59.473313+00:00
> Participants: Scoop, Wire · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Reuters, BBC, and the White House AI Fact Sheet APIs for the latest AI policy updates and company announcements.
2. Extract headlines, timestamps, and source URLs from each response.
3. Filter and deduplicate results to ensure freshness and uniqueness.
4. Compile the verified digest into a GitHub markdown table with columns: *Headline*, *Source*, *Timestamp*, *URL*.
5. Push the digest to the designated AI-news repository with a timestamped commit.
6. Notify stakeholders via Slack/email with the digest link.

**What changed:** Automated real-time scraping of official/company/national AI sources replaces manual curation.
