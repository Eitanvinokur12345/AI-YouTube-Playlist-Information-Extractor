# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-314` (dept) · 2026-07-14T02:00:52.516246+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by transcript-summary (no engine)

**Decision:** DECISION: Run weekly exact-string scans first for trivial duplicates, then route the remaining prompts to a human for light semantic review—own it.

**Plan (from the debate):**
1. Do a weekly automated scan of all prompts using exact string matching to flag duplicates. This catches obvious duplicates reliably and is cheap to run, but misses near-duplicates and semantic duplicat
2. Exact string matching fails when prompts change slightly—like adding a comma or rewording—so it won’t catch near-duplicates, but the real risk is that it *overlooks* semantic duplicates that look diff
3. Do a weekly light semantic scan of prompts using a small embeddings model. This catches near-duplicates and semantic duplicates that exact string matching misses, reducing wasted effort on redundant w
4. A light semantic scan still risks false positives—two prompts may embed similarly but serve distinct purposes, like "summarize this document" vs. "extract key points." A better alternative is a two-st
5. DECISION: Run weekly exact-string scans first for trivial duplicates, then route the remaining prompts to a human for light semantic review—own it.

**What changed:** first real room artifact.
