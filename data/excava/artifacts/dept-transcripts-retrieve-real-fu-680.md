# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-680` (dept) · 2026-07-30T18:00:32.943529+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full auto-generated transcript for the pending video via YouTube’s captions.
2. Verify the transcript’s completeness by checking for gaps, timestamps, or missing segments.
3. If the transcript is incomplete or missing, flag it as such and note the reason (e.g., no captions available, partial extraction).
4. For residential IP environments, implement a gentle retry mechanism (e.g., 2-3 attempts with delays) if the initial fetch fails.
5. Log the transcript (or failure) in the pending video’s metadata for tracking.
6. Proceed to the next pending video only after confirming the transcript’s status.

**What changed:** Resolved ambiguity by mandating tool usage and verification steps.
