# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-787` (dept) · 2026-08-30T02:46:13.488894+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes the `kimtaeyoon83/mcp-server-youtube-transcript` tool on each pending video.
2. Reel delivers the raw, unaltered transcripts to the lead for review.
3. The lead verifies the transcripts for accuracy and completeness.
4. If transcripts are incomplete, Reel re-runs the tool with adjusted parameters.
5. Once validated, transcripts are archived for downstream processing.
6. Notify the team upon completion of transcript retrieval.

**What changed:** Reel’s action is now formally approved as mission-critical work.
