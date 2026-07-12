# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-976` (dept) · 2026-07-12T07:02:11.381335+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:** Focus first on GitHub and Reddit as our primary sources for AI info mining.

**Plan:**
1. **GitHub Scraper:** Deploy a GitHub API-based scraper to extract AI-related repos (stars >100, recent commits) with metadata (languages, topics, READMEs).
2. **Reddit API Pipeline:** Build a Reddit scraper (PRAW) to pull AI posts from r/MachineLearning, r/artificial, and r/learnmachinelearning (top posts, comments, upvotes).
3. **Deduplication:** Cross-reference GitHub repo URLs and Reddit discussions to avoid duplicate entries in the dataset.
4. **Trend Analysis:** Use NLP (e.g., spaCy) to extract trending AI topics from Reddit titles/comments and GitHub repo descriptions.
5. **Validation:** Manually review a 10% sample of mined data for relevance and quality before full-scale extraction.
6. **Rate Limiting:** Implement exponential backoff and caching to respect API limits (GitHub: 5k req/hour, Reddit: 60 req/min).

**What changed:** Prioritized GitHub and Reddit over other sources due to their developer-driven, high-signal content.
