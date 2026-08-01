# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-428` (dept) · 2026-07-30T21:20:38.179428+00:00
> Participants: Scoop · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query Reuters, BBC, and the White House press releases for AI-related headlines from the last 24 hours.
2. Extract and compile the newest AI developments into a raw digest.
3. Format the digest as a GitHub markdown table with columns: *Source*, *Headline*, *URL*, and *Timestamp*.
4. Validate URLs for accessibility and update timestamps to UTC.
5. Publish the digest to the designated AI-news repository under `/digests/latest.md`.
6. Log the operation in the project’s `CHANGELOG.md` with the current UTC timestamp.

**What changed:** Fresh AI-news digest generated from the latest official/company/national sources.
