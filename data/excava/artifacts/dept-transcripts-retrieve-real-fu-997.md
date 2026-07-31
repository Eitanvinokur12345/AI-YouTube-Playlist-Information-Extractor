# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-997` (dept) · 2026-07-31T14:16:40.379647+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**
Proceed with querying the YouTube transcript server for pending video IDs using residential IP with gentle pacing to retrieve full, real transcripts/captions.

**Plan:**
1. Authenticate with the `kimtaeyoon83/mcp-server-youtube-transcript` server using residential IP.
2. Identify all pending video IDs from the target repository or dataset.
3. Execute the transcript query with gentle pacing to avoid rate limits or detection.
4. Save the retrieved plain text transcripts/captions as artifacts in the designated output directory.
5. Validate the completeness and accuracy of each transcript against the original video.
6. Log the process and results for auditing and future reference.

**What changed:** Resolved to use residential IP with gentle pacing for reliable transcript retrieval.
