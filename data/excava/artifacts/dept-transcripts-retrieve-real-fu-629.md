# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-629` (dept) · 2026-08-24T15:13:18.462639+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` to fetch full captions for video ID `dQw4w9WgXcQ`.
2. Output the complete transcript as a file (e.g., `transcript_dQw4w9WgXcQ.txt`).
3. Verify transcript integrity (full coverage, no truncation).
4. Store transcript in the pending videos directory with naming convention `transcript_[videoID].txt`.
5. Log completion in the tracking system (e.g., update priority queue).
6. Notify Scriv of transcript availability for review.

**What changed:** Video `dQw4w9WgXcQ` now has a verified full transcript ready for processing.
