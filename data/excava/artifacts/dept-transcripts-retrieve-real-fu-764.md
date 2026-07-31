# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-764` (dept) · 2026-07-31T04:30:41.530723+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the kimtaeyoon83/mcp-server-youtube-transcript tool to fetch the full YouTube transcript for *Conversation so far*.
2. Verify the plain-text artifact exists and contains the complete, unedited transcript.
3. Store the transcript in the designated repository under `/transcripts/`.
4. Log the retrieval timestamp and video title in a metadata file (e.g., `transcript_metadata.json`).
5. Notify the team via Slack/email that the transcript is ready for review.
6. Archive the raw transcript in a backup location (e.g., Google Drive) for redundancy.

**What changed:** Transcript retrieval is now automated and verified before completion.
