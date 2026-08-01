# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-772` (dept) · 2026-07-30T22:08:06.809957+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a GitHub deep-research sweep for fresh AI repos with >50 stars in the last 7 days.
2. Export the top 20 repos with star counts and one-line descriptions as a CSV.
3. Mine Reddit’s r/MachineLearning and r/ArtificialIntelligence for posts with >20 upvotes from the last 7 days.
4. Filter posts mentioning new tools, datasets, or benchmarks and compile a plain list of 15 unique finds with one-line relevance.
5. Cross-reference GitHub and Reddit results to identify overlaps or gaps.
6. Merge findings into a single consolidated dataset for further analysis.

**What changed:** Combined GitHub’s structured data with Reddit’s community-driven insights for a more diverse AI info harvest.
