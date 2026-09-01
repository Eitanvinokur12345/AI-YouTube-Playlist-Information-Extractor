# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-824` (dept) · 2026-09-01T04:06:54.349675+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` to fetch the full transcript for the pending video.
2. Reel delivers the complete, real transcript text to the lead for the pending video.
3. Scriv verifies the transcript meets requirements (residential IP, gentle pacing).
4. Lead reviews the transcript for accuracy and completeness.
5. If approved, the transcript is archived in the designated repository.
6. If rejected, Reel re-attempts with adjusted parameters (e.g., retry pacing).

**What changed:** Tool execution confirmed; transcript retrieval is now actionable.
