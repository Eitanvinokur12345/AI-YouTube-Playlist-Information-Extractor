# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-566` (dept) · 2026-07-30T19:25:44.600570+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Execute `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full transcript for *"How to Build a Resilient Team"* using a residential IP with gentle pacing.
2. Verify real-time retrieval by checking timestamp accuracy and source authenticity (e.g., YouTube captions or auto-generated transcript).
3. Validate completeness by comparing word count/length against video duration and cross-referencing with partial captions (if available).
4. Save the transcript as a `.txt` or `.srt` file with metadata (video title, URL, retrieval timestamp).
5. Confirm successful extraction by logging the file path and size in the project directory.
6. Mark the task as complete only after manual review of the transcript for errors or omissions.

**What changed:** Resolved to prioritize real-time, complete transcript retrieval over partial solutions, with explicit verification steps.
