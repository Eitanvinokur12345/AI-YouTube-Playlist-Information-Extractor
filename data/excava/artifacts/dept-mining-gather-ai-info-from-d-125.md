# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-125` (dept) · 2026-07-31T21:50:25.434355+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use GitHub’s API to fetch AI-related repos created in the last 7 days, filtering for ≥10 stars or ≥50 upvotes.
2. Sort results by stars/upvotes and select the top 15-20 projects.
3. For each project, write a 1-2 sentence plain-language summary of its purpose and significance.
4. Format the output as a GitHub-flavored markdown list with project names, links, and summaries.
5. Validate that all links are accessible and summaries are accurate.
6. Output the final list in the specified format.

**What changed:** Focus narrowed to GitHub-only sweep with strict time/engagement filters.
