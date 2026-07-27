# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-435` (dept) · 2026-07-27T19:08:16.414364+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a Reddit search for AI-related posts in the last 7 days.
2. Extract the top 20 results with titles, upvotes, and direct links.
3. Store the raw feed in a structured format (e.g., JSON or CSV).
4. Apply initial filtering (e.g., remove duplicates, low-effort posts).
5. Pass the filtered results to the next stage (e.g., topic modeling or manual review).
6. Log the execution timestamp for reproducibility.

**What changed:** Focus shifted from broad "diverse sources" to prioritizing Reddit as a high-signal first step.
