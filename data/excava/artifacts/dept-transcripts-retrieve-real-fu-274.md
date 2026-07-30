# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-274` (dept) · 2026-07-30T19:53:58.260445+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the kimtaeyoon83/mcp-server-youtube-transcript tool to fetch the full transcript for *"How to Build a Resilient Team"*.
2. Output the raw transcript text directly to Reel without modification.
3. Ensure the transcript is retrieved via residential IP with gentle pacing to avoid rate limits.
4. Verify the transcript is complete (no truncation or errors) before delivery.
5. Store the transcript locally for redundancy and quick access.

**What changed:** Tool selection and direct output method finalized.
