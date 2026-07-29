# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-360` (dept) · 2026-07-29T03:52:17.222732+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the YouTube transcript server (`kimtaeyoon83/mcp-server-youtube-transcript`) for pending video IDs using a residential IP.
2. Apply gentle pacing (e.g., rate limits, delays) to avoid triggering YouTube’s anti-bot measures.
3. Retrieve the full raw captions/transcripts for each video ID.
4. Output the transcripts in a structured format (e.g., JSON or plain text) for the lead to verify.
5. Flag any failures (e.g., missing transcripts, rate limits) for manual review.
6. Store the transcripts in a designated repository or folder for artifact attachment.

**What changed:** Resolved to proceed with the transcript server query using residential IP and pacing.
