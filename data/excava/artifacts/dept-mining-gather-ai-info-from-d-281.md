# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-281` (dept) · 2026-07-12T04:09:28.947053+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**
Focus first on GitHub and Reddit as our primary sources, then expand to Product Hunt and Telegram once we’ve built a repeatable process.

**Plan:**
1. **Scrape GitHub** for AI-related repos (keywords: "AI", "LLM", "transformer") and extract READMEs, issues, and discussions.
2. **Monitor Reddit** via subreddits (r/MachineLearning, r/artificial, r/learnmachinelearning) and log posts with >10 upvotes.
3. **Build a pipeline** to deduplicate, categorize, and store scraped data in a structured format (e.g., JSON/CSV).
4. **Validate signals** by cross-referencing GitHub trends with Reddit discussions to identify high-signal sources.
5. **Expand to Product Hunt** after 2 weeks, targeting AI tool launches with >50 upvotes.
6. **Add Telegram** (AI-focused channels) after 1 month, scraping messages with >10 reactions.

**What changed:** Prioritized GitHub/Reddit first for raw, unfiltered signals before scaling to broader sources.
