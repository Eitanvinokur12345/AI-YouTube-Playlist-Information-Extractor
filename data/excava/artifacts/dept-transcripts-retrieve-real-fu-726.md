# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-726` (dept) · 2026-07-28T17:39:53.555972+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` via residential IP to fetch full transcripts/captions for all pending video IDs.
2. Validate transcript completeness and format for each video.
3. Store transcripts in a structured directory (e.g., `transcripts/pending/{video_id}.json`).
4. Log errors for failed retrievals and retry with exponential backoff.
5. Notify user upon completion or if manual intervention is required.
6. Archive processed video IDs to avoid duplicate queries.

**What changed:** Residential IP usage confirmed for gentle pacing; full transcripts will be retrieved in one batch.
