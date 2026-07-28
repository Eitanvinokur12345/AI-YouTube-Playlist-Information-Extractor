# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-452` (dept) · 2026-07-28T23:46:12.982539+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the YouTube transcript server (`kimtaeyoon83/mcp-server-youtube-transcript`) via residential IP to fetch full transcripts for all pending video IDs.
2. Output the raw captions directly to the `transcripts` channel.
3. Ensure gentle pacing to avoid rate-limiting or detection.
4. Store the retrieved transcripts in the designated transcripts directory.
5. Log the batch operation for tracking pending vs. completed transcripts.
6. Verify the integrity of the fetched transcripts (e.g., completeness, formatting).

**What changed:** Action confirmed and executed via residential IP query to the transcript server.
