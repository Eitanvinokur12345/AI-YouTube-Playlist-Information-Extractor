# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-735` (dept) · 2026-07-17T14:15:53.282892+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a GitHub search for repositories tagged with "AI" and "research."
2. Filter results to return the top 100 repositories by stars.
3. Extract each repository’s description and primary programming language.
4. Compile the data into a ranked list (highest stars first) with descriptions and languages.
5. Output the list in GitHub-flavored markdown for quick assessment.

**What changed:** Added "research" tag to GitHub search for higher-quality AI repositories.
