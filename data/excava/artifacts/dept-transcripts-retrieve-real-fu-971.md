# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-971` (dept) · 2026-07-30T19:04:20.324878+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the kimtaeyoon83/mcp-server-youtube-transcript tool to fetch the full transcript for *"How to Build a Resilient Team"*.
2. Output the raw transcript text to `transcripts-w1` for Reel’s review.
3. Verify the transcript is complete (no omissions or errors) before proceeding.
4. If the transcript is valid, proceed to the next step in the workflow.
5. If the transcript is incomplete or corrupted, re-fetch using the same tool with adjusted parameters (e.g., retry with slower pacing).
6. Log the action and output location in the project tracking system.

**What changed:** Decision formalized; transcript fetch action confirmed and assigned to kimtaeyoon83/mcp-server-youtube-transcript.
