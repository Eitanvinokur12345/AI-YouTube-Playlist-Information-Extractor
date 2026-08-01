# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-522` (dept) · 2026-07-30T20:23:20.233345+00:00
> Participants: Pick, Boulder · synthesized by mistral/mistral-small-latest

**Decision:**
Run a dual-phase sweep: Phase 1 targets Product Hunt for recent AI launches, Phase 2 expands to GitHub/HN/Reddit/Telegram for broader signal.

**Plan:**
1. Sweep Product Hunt (last 7 days) for AI products, output 20–30 items with names, launch dates, and one-line descriptions.
2. Sweep GitHub (last 30 days) for repos tagged “AI,” “machine learning,” or “LLM,” curate 50–100 high-signal items.
3. Sweep Hacker News (last 30 days) for AI posts, extract titles, sources, and one-line relevance.
4. Sweep Reddit (last 30 days) for AI threads in r/MachineLearning, r/artificial, r/learnmachinelearning, filter top posts.
5. Sweep Telegram for AI channels/groups (e.g., AI/ML communities), extract recent posts with AI keywords.
6. Merge all outputs into a single GitHub markdown list, deduplicated and ranked by recency/signal.

**What changed:**
Added Product Hunt focus as Phase 1, kept broader sweep for Phase 2.
