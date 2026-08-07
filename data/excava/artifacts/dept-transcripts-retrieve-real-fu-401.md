# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-401` (dept) · 2026-08-07T01:02:30.785176+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel runs the `kimtaeyoon83/mcp-server-youtube-transcript` tool against the pending video list.
2. The tool fetches real, complete captions for each video.
3. Scriv verifies the transcripts for accuracy and completeness.
4. Store the transcripts in the designated repository or database.
5. Update the video metadata to reflect the availability of full transcripts.
6. Notify stakeholders of the completed transcript retrieval.

**What changed:** Reel executes the transcript retrieval tool on the pending video list.
