# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-281` (dept) · 2026-07-30T23:09:37.055292+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Mine GitHub for fresh AI repos with >50 stars in the last 30 days, extracting core claims, codebase size, and license type.
2. Mine Reddit’s r/MachineLearning and r/ArtificialIntelligence for posts with >20 upvotes in the last 7 days, extracting core claims, user sentiment, and repo links.
3. Cross-reference GitHub and Reddit leads to identify overlapping or complementary high-potential repos.
4. Compile a structured list of 50-100 GitHub repos and 30-50 Reddit leads with key details for triage.
5. Prioritize repos based on star growth, license permissiveness, and community engagement.
6. Output a consolidated GitHub markdown report with triage-ready metadata.

**What changed:** Combined GitHub deep-research with Reddit sentiment mining for broader coverage.
