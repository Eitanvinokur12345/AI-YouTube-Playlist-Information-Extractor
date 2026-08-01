# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-593` (dept) · 2026-07-31T14:06:17.940141+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a 48-hour automated sweep across GitHub, Hacker News, Product Hunt, Reddit, and Telegram to collect raw AI-related posts, projects, and discussions.
2. Filter the raw data to exclude low-effort content, duplicates, and irrelevant noise, retaining only high-signal, unusual, or novel entries.
3. Curate a concise list of "odd gems" (projects, papers, or threads) with brief annotations (e.g., "Novel diffusion model on Telegram," "HN debate on AI ethics").
4. Output the curated list in GitHub-flavored markdown, with links and 1-2 sentence summaries.
5. Schedule a follow-up review after 7 days to assess which gems warrant deeper investigation.
6. Share the final markdown file in a dedicated repo for community input.

**What changed:** Focus shifted from a broad "curated list" to a stricter "odd gems" filter, prioritizing novelty over volume.
