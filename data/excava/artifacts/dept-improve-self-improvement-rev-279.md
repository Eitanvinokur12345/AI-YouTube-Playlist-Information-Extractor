# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-279` (dept) · 2026-07-14T02:19:20.391267+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by transcript-summary (no engine)

**Decision:** DECISION: Run weekly hybrid scans—exact string matching first to catch trivial duplicates, then keyword-tied semantic scans to flag near-duplicates only when they share a core function keyword. Result

**Plan (from the debate):**
1. Do weekly automated scans of all prompts using exact string matching to flag duplicates. This catches exact copies faster than semantic scans, cutting noise in reviews. Trade-off: misses near-duplicat
2. Exact string matching fails when prompts change slightly—like adding a comma or a space. A light semantic scan still risks false positives—two prompts may embed similar ideas but serve different purpo
3. Run weekly hybrid scans: exact string matching first, then light semantic scans. Exact matching catches obvious duplicates fast; semantic scans catch rephrased near-duplicates without drowning in fals
4. Light semantic scans still risk false positives—two prompts may embed similar ideas but serve different intents, wasting review time. A better alternative: run exact matching first, then only flag sem
5. DECISION: Run weekly hybrid scans—exact string matching first to catch trivial duplicates, then keyword-tied semantic scans to flag near-duplicates only when they share a core function keyword. Result

**What changed:** first real room artifact.
