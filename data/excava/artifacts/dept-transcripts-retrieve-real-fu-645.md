# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-645` (dept) · 2026-07-31T18:45:33.100933+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use `kimtaeyoon83/mcp-server-youtube-transcript` to fetch the full transcript for the pending video titled *"Orchestrated AI"*.
2. Output the raw transcript text directly to `transcripts-w1` without modification.
3. Verify the transcript is complete and correctly formatted in `transcripts-w1`.
4. Confirm the transcript retrieval via a brief log entry in the repository.
5. Close the room and archive the task.

**What changed:** Resolved to execute transcript fetch via the specified tool.
