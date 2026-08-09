# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-871` (dept) · 2026-08-09T17:08:17.471018+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Reel will execute the transcript retrieval plan using kimtaeyoon83/mcp-server-youtube-transcript.

**Plan:**
1. Reel runs `kimtaeyoon83/mcp-server-youtube-transcript` on every pending video.
2. The tool generates full transcripts/captions for each video.
3. Artifacts are produced and stored for verification.
4. Lead reviews transcripts to confirm completion.
5. Task status is updated in the tracking system.
6. Notify stakeholders upon finalization.

**What changed:** Transcripts/captions are now being retrieved for all pending videos via automated tooling.
