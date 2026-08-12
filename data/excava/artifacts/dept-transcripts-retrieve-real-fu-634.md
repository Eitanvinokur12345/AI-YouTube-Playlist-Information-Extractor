# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-634` (dept) · 2026-08-12T08:03:09.188263+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch full transcripts for all 10 pending videos.
2. Ensure each transcript includes speaker IDs (where available) and complete text content.
3. Store the transcripts in a structured format (e.g., JSON or text files) for easy retrieval.
4. Verify the transcripts match the tool’s documented capabilities (full text, speaker IDs).
5. Mark the videos as processed in the tracking system.
6. Log any errors or missing transcripts for follow-up.

**What changed:** Expanded action from 1 to all 10 pending videos.
