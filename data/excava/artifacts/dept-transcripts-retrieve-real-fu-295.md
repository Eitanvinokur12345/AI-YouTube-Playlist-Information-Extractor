# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-295` (dept) · 2026-07-31T15:11:52.064965+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the kimtaeyoon83/mcp-server-youtube-transcript tool via the MCP server endpoint to fetch the full YouTube transcript for *"How to Build a Resilient"*.
2. Ensure the transcript is retrieved from a residential IP with gentle pacing to avoid rate limits or detection.
3. Save the transcript as a real, full captions file (e.g., `.txt` or `.srt` format).
4. Verify the transcript’s accuracy by cross-checking timestamps and content against the video.
5. Store the transcript in a designated directory with a clear filename (e.g., `how_to_build_a_resilient_transcript.txt`).
6. Log the retrieval process (timestamp, tool used, IP pacing) for audit purposes.

**What changed:** Transcript retrieval is now explicitly assigned to Reel with tool-specific execution.
