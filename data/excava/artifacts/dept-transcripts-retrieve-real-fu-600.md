# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-600` (dept) · 2026-07-31T23:12:16.503262+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes the kimtaeyoon83/mcp-server-youtube-transcript tool to fetch the full YouTube transcript for *"The Science of Sleep Optimization"*.
2. Reel saves the retrieved real transcript to the designated archive for review.
3. Reel verifies the transcript integrity (completeness, accuracy) against the video content.
4. Reel notifies Echo upon successful archival with a confirmation message.
5. Echo reviews the transcript and approves for downstream use.
6. Archive the transcript with metadata (video title, timestamp, source URL).

**What changed:** Transcript retrieval is now actioned via the specified tool and archived for review.
