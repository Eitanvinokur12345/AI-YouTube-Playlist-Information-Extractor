# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-516` (dept) · 2026-07-28T23:13:19.210802+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to query YouTube’s transcript server for all pending video IDs.
2. Execute the query via a residential IP to ensure gentle pacing and avoid rate-limiting.
3. Retrieve full transcripts or captions for each pending video ID returned by the query.
4. Store the transcripts/captions in a structured format (e.g., JSON or text files) for further processing.
5. Validate the completeness of the transcripts (e.g., check for missing segments or errors).
6. Log the results (success/failure per video ID) for tracking and debugging.

**What changed:** Residential IP requirement added to the initial plan.
