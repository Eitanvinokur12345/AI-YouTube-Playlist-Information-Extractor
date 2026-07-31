# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-115` (dept) · 2026-07-31T17:14:01.632807+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**
Sweep Product Hunt’s "AI" launches from the last 7 days and extract the top 20 with name, tagline, launch date, upvotes, and direct link.

**Plan:**
1. Use Product Hunt’s API or web scraping to fetch AI-related launches from the last 7 days.
2. Filter results to include only products tagged as "AI" or with "AI" in their name/description.
3. Sort by upvotes and select the top 20 entries.
4. Extract name, tagline, launch date, upvotes, and direct link for each.
5. Format the data into a clean dataset (GitHub markdown table).
6. Deliver the dataset to the lead for review.

**What changed:**
Focused on Product Hunt only for a quick, high-signal dataset instead of a broader multi-source sweep.
