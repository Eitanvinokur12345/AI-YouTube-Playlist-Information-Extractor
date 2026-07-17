# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-430` (dept) · 2026-07-17T14:16:05.732358+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the `kimtaeyoon83/mcp-server-youtube-transcript` tool on the first pending video to extract its full transcript with timestamps.
2. Verify the transcript is verbatim and includes all spoken content with accurate timestamps.
3. Save the transcript as a `.txt` or `.md` file in the designated repository folder.
4. Cross-check the transcript against the video to ensure no omissions or errors.
5. Mark the video as "transcript retrieved" in the tracking system.
6. Proceed to the next pending video if the transcript is complete.

**What changed:** Transcript extraction is now automated for the first pending video.
