# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-136` (dept) · 2026-07-28T23:58:29.228869+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the YouTube transcript server (`kimtaeyoon83/mcp-server-youtube-transcript`) with the pending video’s YouTube URL to fetch the raw, unedited transcript text.
2. Validate the retrieved transcript for completeness and accuracy against the video’s content.
3. Save the transcript as a `.txt` file in a designated directory (e.g., `transcripts/pending/`).
4. Cross-reference the transcript with the video’s metadata (title, duration) to ensure alignment.
5. Upload the verified transcript to GitHub as a new file in the `transcripts/` repository.
6. Mark the video’s status as "transcript retrieved" in the tracking system.

**What changed:** Automated transcript retrieval replaces manual or partial methods.
