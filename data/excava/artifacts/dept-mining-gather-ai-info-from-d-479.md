# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-479` (dept) · 2026-07-18T01:23:03.383430+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub’s advanced search to query repositories tagged with both "AI" and "research."
2. Sort results by stars (descending) and limit to the top 100 entries.
3. Extract for each entry: repository name, star count, description, and URL.
4. Format the output as a GitHub-flavored markdown table with columns: #, Repository, Stars, Description, Link.
5. Validate links and descriptions for accuracy before finalizing.
6. Append a note: "Data sourced from GitHub (as of [current date])."

**What changed:** Scope expanded from "AI" to "AI + research" for higher signal-to-noise ratio.
