# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-534` (dept) · 2026-08-11T17:30:56.561970+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Re-run the `kimtaeyoon83/mcp-server-youtube-transcript` tool on all 10 pending videos.
2. For each video, extract only the raw transcript text and pair it with the corresponding `video_id`.
3. Store the results in a structured format (e.g., JSON or CSV) with two fields per entry: `video_id` and `transcript_text`.
4. Verify the output for completeness and accuracy (e.g., no missing transcripts or malformed data).
5. Save the final dataset to a designated repository or directory.
6. Notify stakeholders of completion and provide access to the raw transcripts.

**What changed:** Dropped the four-field schema in favor of a simplified `video_id`-paired raw transcript output.
