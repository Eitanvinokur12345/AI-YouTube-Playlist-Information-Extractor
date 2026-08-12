# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-507` (dept) · 2026-08-12T15:31:51.838410+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Proceed with retrieving the full transcript for the pending video using the specified tool.

**Plan:**
1. Execute `kimtaeyoon83/mcp-server-youtube-transcript` on the video ID `e2Z5eBVDrKM`.
2. Ensure the output is a complete caption file with speaker IDs (where available).
3. Save the transcript locally with a clear filename (e.g., `e2Z5eBVDrKM_transcript.txt`).
4. Verify the transcript’s completeness by checking for timestamps and speaker labels.
5. Mark the video as processed in the pending queue.
6. Log the action in the project’s activity log.

**What changed:**
The tool will now be re-run on the specified video to generate the full transcript.
