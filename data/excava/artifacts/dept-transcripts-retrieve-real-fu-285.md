# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-285` (dept) · 2026-07-30T07:17:07.476983+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full transcript for the pending video.
2. Verify the transcript contains real content (e.g., speaker attributions, timestamps, or full text) before proceeding.
3. If the transcript is valid, save it as the final output for the pending video.
4. If the transcript is incomplete or missing, retry once with the same tool.
5. If still invalid, log the failure and escalate for manual review.
6. Confirm completion by marking the task as resolved in the system.

**What changed:** Now using a dedicated YouTube transcript tool with validation before finalizing.
