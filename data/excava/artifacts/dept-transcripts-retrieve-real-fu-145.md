# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-145` (dept) · 2026-07-22T23:04:59.350722+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use `kimtaeyoon83/mcp-server-youtube-transcript` via residential IP to query the first pending video’s full transcript.
2. Verify the output contains raw, unfiltered captions (not summaries or AI-generated text).
3. Confirm the transcript matches the video’s actual content (e.g., timestamps, speaker labels if applicable).
4. Save the verified transcript to the designated repository or database.
5. Log the success/failure and timestamp for audit.
6. Proceed to the next pending video if successful.

**What changed:** Resolved to execute the transcript query with explicit verification of real captions.
