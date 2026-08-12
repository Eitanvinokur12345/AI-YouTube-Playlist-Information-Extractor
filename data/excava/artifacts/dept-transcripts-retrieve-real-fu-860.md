# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-860` (dept) · 2026-08-12T11:24:53.460206+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Execute the transcript retrieval for the pending video.

**Plan:**
1. Run `kimtaeyoon83/mcp-server-youtube-transcript` on `e2Z5eBVDrKM` to fetch the full transcript.
2. Validate the output for completeness and `speaker_id` fields.
3. Store the transcript in the designated repository under `/transcripts/pending/`.
4. Mark the video as "transcribed" in the tracking system.
5. Notify the team via Slack #transcripts channel with the file path.
6. Proceed to the next pending video if no errors occur.

**What changed:** Initiated transcript fetch for `e2Z5eBVDrKM`.
