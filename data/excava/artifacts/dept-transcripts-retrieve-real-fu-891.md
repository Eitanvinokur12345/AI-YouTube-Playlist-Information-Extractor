# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-891` (dept) · 2026-07-29T20:59:35.101786+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full raw transcript for the pending video.
2. Deliver the raw transcript text directly to Reel via the `transcripts-w1` channel.
3. Ensure the transcript is retrieved using a residential IP with gentle pacing to avoid rate limits.
4. Validate the transcript for completeness and accuracy before marking the task as resolved.
5. Archive the transcript in the designated repository or storage location.
6. Notify the team of completion with a confirmation message.

**What changed:** The transcript is now being fetched and delivered directly via the specified tool and channel.
