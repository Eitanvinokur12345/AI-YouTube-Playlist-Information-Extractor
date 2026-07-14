# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-425` (dept) · 2026-07-14T01:42:45.536881+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by transcript-summary (no engine)

**Decision:** DECISION: Run weekly exact-string scans for duplicates first, then add a lightweight semantic check (small embeddings model) only if false negatives become a problem—own it yourself.

**Plan (from the debate):**
1. Run weekly automated scans of all prompts using exact string matching to flag duplicates. This catches near-matches we might miss manually and keeps the prompt library clean without heavy engineering 
2. The real risk with exact string matching isn't just false positives, but also false negatives - it may miss similar prompts that use different wording or phrasing. A better alternative might be to use
3. Use a hybrid scan: weekly exact-string matching to catch obvious duplicates, plus a lightweight semantic check (e.g., embeddings with a small model) to catch near-duplicates. This balances speed and a
4. The real risk with a hybrid approach is that it may introduce unnecessary complexity—now you’re maintaining two systems instead of one, and the semantic model’s false positives could waste more time t
5. DECISION: Run weekly exact-string scans for duplicates first, then add a lightweight semantic check (small embeddings model) only if false negatives become a problem—own it yourself.

**What changed:** first real room artifact.
