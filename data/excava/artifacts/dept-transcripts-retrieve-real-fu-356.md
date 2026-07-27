# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-356` (dept) · 2026-07-27T19:28:03.916509+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` for the first pending video ID to fetch its raw transcript.
2. Output the retrieved transcript text to the lead for review.
3. Lead reviews transcript and decides next steps (e.g., edits, publishing, or rejection).
4. If approved, proceed to process the next pending video ID.
5. If rejected, log the reason and flag the video for further review.
6. Repeat until all pending video transcripts are retrieved and reviewed.

**What changed:** Transcript retrieval is now automated via the specified tool, replacing manual or uncertain methods.
