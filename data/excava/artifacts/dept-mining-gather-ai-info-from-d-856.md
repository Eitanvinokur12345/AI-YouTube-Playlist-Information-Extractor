# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-856` (dept) · 2026-07-31T04:51:20.800648+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a targeted GitHub search for AI repositories created in the last 30 days, filtering for stars >50.
2. Extract core features, recent activity (commits/issues), and maintainer info for each repository.
3. Compile results into a GitHub-flavored markdown table with columns: Repo Name, Stars, Last Commit, Key Features, Link.
4. Cross-reference with HN/Product Hunt/Reddit/Telegram for validation (optional but recommended).
5. Export the markdown table to a dedicated GitHub repo for further processing.
6. Schedule a follow-up sweep in 7 days to capture new high-engagement AI projects.

**What changed:** Focus narrowed to GitHub-only sweep with strict star/recency filters, dropping other platforms for now.
