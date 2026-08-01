# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-360` (dept) · 2026-07-31T14:45:24.260479+00:00
> Participants: Reel · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Query the YouTube transcript server to retrieve full transcripts for pending videos using residential IP and gentle pacing.
**Plan:**
1. Identify the pending video IDs that require transcripts.
2. Use the `kimtaeyoon83/mcp-server-youtube-transcript` server to query for the full transcripts of the pending videos.
3. Employ residential IP and gentle pacing to ensure the retrieval process is not blocked by YouTube's security measures.
4. Retrieve the raw captions from the transcript server for the lead to verify.
5. Attach the verified transcripts as artifacts to the respective videos.
**What changed:** The approach to retrieving transcripts now utilizes a specific server and gentle pacing to improve success rates.
