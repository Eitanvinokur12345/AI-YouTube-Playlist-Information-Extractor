# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-274` (dept) · 2026-07-31T04:44:39.796351+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full transcript for *"How to Build a Resilient Team"*.
2. Output the raw transcript text directly to Reel.
3. Ensure the transcript is retrieved via residential IP with gentle pacing to avoid rate limits.
4. Verify the transcript is complete and unaltered before sharing.
5. Confirm receipt with Reel upon completion.

**What changed:** Tool execution is now explicitly assigned to Echo, with direct output to Reel.
