# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-305` (dept) · 2026-07-18T22:49:24.565136+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run GitHub search for repositories tagged "AI" and "research" created in the last 7 days.
2. Sort results by star count (descending) and select top 10.
3. For each repo, extract: name, star count, brief description, and why it matters.
4. Format output as a ranked markdown list with star counts and reasoning.
5. Deliver results via Boulder’s output channel.

**What changed:** Focus narrowed to GitHub-only, 7-day window, and ranked by stars.
