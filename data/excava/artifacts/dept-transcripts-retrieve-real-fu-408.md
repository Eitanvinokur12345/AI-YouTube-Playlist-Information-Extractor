# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-408` (dept) · 2026-08-08T13:29:56.972774+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Use the kimtaeyoon83/mcp-server-youtube-transcript tool for transcript retrieval, with Scriv verifying completeness.

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` on all pending videos via residential IP.
2. Scriv checks each transcript for completeness against video metadata.
3. If transcripts are incomplete, flag the video for re-processing.
4. Mark artifacts as "done" only after Scriv confirms full transcript accuracy.
5. Log failures and retry up to 3 times before escalating.
6. Archive raw transcripts and verification results in the project’s `/transcripts` directory.

**What changed:**
Tool dependency (mcp-server-youtube-transcript) is approved despite instability, contingent on Scriv’s verification.
