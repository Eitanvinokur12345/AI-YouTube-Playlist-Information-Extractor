# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-116` (dept) · 2026-07-27T19:34:39.376885+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query `kimtaeyoon83/mcp-server-youtube-transcript` with the first pending video ID to fetch its full transcript.
2. Save the raw transcript file locally for processing.
3. Auto-tag the transcript with predefined risk keywords using a keyword-matching script.
4. Validate the tagged transcript for accuracy and completeness.
5. Store the processed transcript in the designated output directory.
6. Log the operation (video ID, timestamp, success/failure) in a tracking file.

**What changed:** Initiated transcript retrieval for the first pending video ID via the specified tool.
