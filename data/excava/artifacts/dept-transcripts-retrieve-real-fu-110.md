# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-110` (dept) · 2026-07-30T17:32:50.745287+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use `kimtaeyoon83/mcp-server-youtube-transcript` to fetch the full transcript for the pending video via YouTube’s auto-generated captions.
2. Ensure the output is a plain-text transcript in English with timestamps and speaker labels (if available).
3. Validate the transcript for completeness and accuracy (e.g., no missing segments, correct speaker attribution).
4. Save the transcript in a structured format (e.g., `.txt` file) with a clear filename referencing the video.
5. Cross-check the transcript against the video’s auto-generated captions for consistency.
6. Deliver the final transcript to the requester with a confirmation of successful retrieval.

**What changed:** Adopted direct transcript fetching via `mcp-server-youtube-transcript` instead of manual methods.
