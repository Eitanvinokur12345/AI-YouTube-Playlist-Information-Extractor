# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-656` (dept) · 2026-07-27T19:47:22.901272+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` for the first pending video ID to fetch its raw transcript.
2. Save the retrieved transcript as a `.txt` file in the designated transcripts directory.
3. Verify the transcript’s completeness (no missing segments) and confirm it matches the video’s content.
4. Mark the video as "transcribed" in the tracking system (e.g., spreadsheet or database).
5. Repeat the process for the next pending video ID, maintaining a gentle pacing (e.g., 1 video per 10 minutes).
6. Log any errors (e.g., missing transcripts) and escalate unresolved cases after 3 retries.

**What changed:** Automated transcript retrieval replaces manual scraping.
