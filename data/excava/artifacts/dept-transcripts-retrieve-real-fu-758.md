# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-758` (dept) · 2026-08-08T05:22:37.068223+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes the `kimtaeyoon83/mcp-server-youtube-transcript` tool on each pending video.
2. The tool retrieves and generates real, complete caption files for all target videos.
3. The lead reviews the generated transcripts for accuracy and completeness.
4. If discrepancies are found, Reel reprocesses the video(s) with adjustments.
5. Validated transcripts are stored in the designated repository or system.
6. Notify the team upon completion of transcript retrieval for all pending videos.

**What changed:** Execution of the transcript retrieval tool is now authorized and prioritized.
