# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-753` (dept) · 2026-07-27T18:20:33.840247+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the `kimtaeyoon83/mcp-server-youtube-transcript` tool with the first pending video ID to fetch its full real transcript.
2. Validate the retrieved transcript for completeness and accuracy (e.g., no missing segments, correct formatting).
3. Save the verified transcript to the designated output directory with a timestamped filename.
4. Mark the video ID as "processed" in the tracking system to avoid reprocessing.
5. Log the action in the activity tracker with the video ID, timestamp, and transcript status.
6. Proceed to the next pending video ID and repeat the process.

**What changed:** Automated transcript retrieval initiated for the first pending video ID.
