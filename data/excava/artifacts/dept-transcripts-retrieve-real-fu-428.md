# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-428` (dept) · 2026-09-01T04:31:08.089484+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` to fetch the unaltered captions for the pending video.
2. Scriv receives the raw transcript and verifies its authenticity.
3. Reel uploads the verified transcript to the designated repository or system.
4. Scriv cross-references the transcript with the video for accuracy.
5. Both parties confirm completion and archive the task.
6. Echo closes the room upon final verification.

**What changed:** Reel now fetches the real transcript via the specified tool.
