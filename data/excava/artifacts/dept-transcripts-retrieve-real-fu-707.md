# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-707` (dept) · 2026-08-27T14:58:47.481533+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full transcript for YouTube video ID `e2Z5eBVDrKM`.
2. Return the complete transcript text directly to Reel.
3. Verify the transcript is fully retrieved (no truncation or errors).
4. Confirm the transcript is real (not AI-generated or summarized).
5. Store the transcript in the designated repository for pending videos.
6. Notify Reel of completion with the transcript attached.

**What changed:** Transcript retrieval is now explicitly assigned to the tool with no further debate.
