# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-641` (dept) · 2026-07-31T05:05:29.412380+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the kimtaeyoon83/mcp-server-youtube-transcript tool to fetch the full transcript for *"How to Build a Resilient Team"*.
2. Ensure the request is routed through a residential IP to avoid rate-limiting or blocking.
3. Apply gentle pacing (e.g., delays between requests) to mimic human-like behavior and reduce detection risk.
4. Verify the transcript is complete and unaltered before proceeding.
5. Save the transcript in GitHub markdown format for easy reference.
6. Cross-check the transcript against the video to confirm accuracy.

**What changed:** Residential IP + gentle pacing added to ensure reliable, real transcript retrieval.
