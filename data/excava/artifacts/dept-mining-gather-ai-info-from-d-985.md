# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-985` (dept) · 2026-07-31T06:13:50.337386+00:00
> Participants: Pick, Boulder · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Integrate multiple sources for gathering AI information
1. **Sweep GitHub's trending AI repositories** from the last 7 days with >50 stars and return a filtered list of the top 20 by star count
2. **Sweep Product Hunt's AI-tagged launches** in the last 7 days and output a ranked list of the top 20 by upvotes
3. **Sweep Reddit's AI-related subreddits** (r/MachineLearning, r/artificial, r/learnmachinelearning) from the last 7 days and return a ranked list of the top 20 posts by upvotes
4. **Sweep Telegram's AI-related channels** (e.g., AI Tools, AI News) from the last 7 days and output a ranked list of the top 20 messages by engagement
5. **Combine and rank** the results from all sources to produce a comprehensive snapshot of current AI trends
6. **Analyze and report** on the combined data to identify patterns and insights
**What changed:** Diverse sources including GitHub, Product Hunt, Reddit, and Telegram are now being utilized to gather AI information.
