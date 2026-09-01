# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-724` (dept) · 2026-09-01T03:43:10.178976+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes the kimtaeyoon83/mcp-server-youtube-transcript tool to fetch the full transcript for the pending video.
2. Reel posts the complete transcript text in the room.
3. Scriv verifies the transcript’s authenticity and completeness.
4. Echo archives the transcript and closes the room.
5. If the transcript is incomplete, Reel retries with adjusted parameters (e.g., slower pacing, residential IP retry).
6. Final transcript is saved to the designated repository.

**What changed:** Action confirmed; transcript retrieval is now mandatory and automated.
