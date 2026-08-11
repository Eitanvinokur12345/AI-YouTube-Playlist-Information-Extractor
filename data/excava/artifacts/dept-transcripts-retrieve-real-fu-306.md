# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-306` (dept) · 2026-08-11T15:32:01.682175+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Execute `kimtaeyoon83/mcp-server-youtube-transcript` on all 10 pending videos.
2. Ensure output is strict JSON with only `video_id`, `transcript_text`, and `language` fields.
3. Validate transcripts for completeness and language accuracy.
4. Store results in a structured format (e.g., JSON file per video).
5. Log any failures or edge cases (e.g., missing captions) for review.
6. Notify stakeholders upon completion.

**What changed:** Action confirmed; tool re-run initiated.
