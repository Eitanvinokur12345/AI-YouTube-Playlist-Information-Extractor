# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-150` (dept) · 2026-07-27T19:41:02.547370+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Proceed with querying the YouTube transcript tool for the first pending video ID to retrieve its full transcript.

**Plan:**
1. Identify the first pending video ID from the target list.
2. Execute the `kimtaeyoon83/mcp-server-youtube-transcript` tool with the selected video ID.
3. Validate the retrieved transcript for completeness and accuracy.
4. Store the transcript in the designated output directory.
5. Auto-tag the transcript against predefined risk keywords.
6. Log the action and transcript metadata for tracking.

**What changed:** Initial decision to query the transcript tool for the first pending video ID.
