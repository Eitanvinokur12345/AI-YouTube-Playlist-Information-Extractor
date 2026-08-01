# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-835` (dept) · 2026-07-30T23:58:40.558832+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use `kimtaeyoon83/mcp-server-youtube-transcript` to fetch the full raw transcript for *"How to Build a Resilient Team"*.
2. Output the complete, unfiltered transcript text directly.
3. Store the transcript in a local file (e.g., `transcript_How_to_Build_a_Resilient_Team.txt`).
4. Verify the transcript’s completeness by checking for timestamps, speaker labels, and full content.
5. Proceed with gentle pacing for residential IP to avoid rate limits.
6. Log the action in a tracking file (e.g., `transcript_fetch_log.md`).

**What changed:** Resolved to use the specified tool for direct transcript retrieval without filtering.
