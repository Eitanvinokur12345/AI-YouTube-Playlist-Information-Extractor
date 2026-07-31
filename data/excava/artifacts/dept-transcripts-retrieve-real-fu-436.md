# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-436` (dept) · 2026-07-31T04:37:46.377402+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the kimtaeyoon83/mcp-server-youtube-transcript MCP server to fetch the full YouTube transcript for the video titled "pen".
2. Save the complete captions file locally for review.
3. Validate the transcript for completeness and accuracy.
4. If needed, re-run the fetch with adjusted parameters (e.g., language, pacing) for gentler retrieval.
5. Store the final transcript in the designated repository under `/transcripts/pending/`.
6. Notify the team via Slack/email upon successful retrieval.

**What changed:** Transcript retrieval is now actionable via MCP server.
