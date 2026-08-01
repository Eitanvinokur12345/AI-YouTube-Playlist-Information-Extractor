# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-431` (dept) · 2026-07-30T20:02:01.122176+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Fetch the full transcript for *"How to Build a Resilient Team"* using the kimtaeyoon83/mcp-server-youtube-transcript tool.

**Plan:**
1. Use the kimtaeyoon83/mcp-server-youtube-transcript tool to retrieve the complete transcript for *"How to Build a Resilient Team"*.
2. Verify the fetched transcript is complete and matches the pending video.
3. If the transcript is missing or incomplete, re-attempt the fetch with gentle pacing.
4. Save the verified transcript to the designated repository or system.
5. Mark the video as processed in the pending queue.
6. Log the action and timestamp for audit purposes.

**What changed:**
The transcript fetch is now explicitly assigned to Reel with verification steps and gentle pacing.
