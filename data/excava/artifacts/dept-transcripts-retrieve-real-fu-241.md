# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-241` (dept) · 2026-07-29T20:38:54.019905+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full transcript for the pending video.
2. Ensure the request is routed through a residential IP for gentle pacing.
3. Save the output as a clean, full-length text file.
4. Route the file to the lead for review.
5. Verify the transcript is complete and accurate before finalizing.

**What changed:** Residential IP routing added for gentler pacing.
