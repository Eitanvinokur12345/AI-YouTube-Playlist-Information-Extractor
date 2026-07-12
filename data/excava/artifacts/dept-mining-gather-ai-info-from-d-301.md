# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-301` (dept) · 2026-07-12T12:49:26.993311+00:00
> Participants: Pick, Assay, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**
Split the sample—Telegram for adoption pain points, Reddit for technical signals.

**Plan:**
1. **Telegram Harvest:** Manually scrape 100 messages each from *AI Hub* and *Future of AI* channels, prioritizing posts with >5 reactions or replies.
2. **Reddit Harvest:** Scrape top 200 posts (last 6 months) from r/MachineLearning and r/artificial, filtering for "github.com", "paper", or "repo" in titles/comments.
3. **Filtering:** Telegram—tag pain points (e.g., "cost", "latency") and language (EN/RU/ES/...); Reddit—tag technical depth (e.g., "benchmark", "architecture") and language (EN only).
4. **Cross-Validation:** Manually verify 20% of Telegram pain points against Reddit threads for consistency; discard duplicates.
5. **Export:** Output two markdown lists (`telegram_pain_points.md`, `reddit_technical_links.md`) with headers: `Source | Title | Summary | Tags | Language`.
6. **Owner Tag:** Append `Owner: [YourHandle]` to each artifact.

**What changed:** Balanced signal/noise by splitting sources and enforcing structured filtering.
