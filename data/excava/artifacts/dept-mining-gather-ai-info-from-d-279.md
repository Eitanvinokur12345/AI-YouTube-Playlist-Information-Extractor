# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-279` (dept) · 2026-07-31T18:16:27.854947+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Sweep GitHub’s AI-related repos created in the last 7 days, filtering for repos with ≥10 stars or ≥50 forks.
2. Output a list of repo names with a one-line reason for inclusion (e.g., "High community engagement").
3. Cross-reference top repos with Hacker News/Reddit threads to validate discussion volume.
4. Compile a final curated list of 10-15 repos with the highest combined engagement.
5. Schedule a weekly automated sweep to update the list.
6. Share the list in a structured format (e.g., GitHub Gist) for Boulder’s review.

**What changed:** Focus narrowed to GitHub-only sweep with engagement-based filtering.
