# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-192` (dept) · 2026-07-31T09:28:29.978260+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
> Decision artifact · room `dept-transcripts-retrieve-real-fu-192` (dept) · 2026-07-31T08:16:21.265375+00:00
> Participants: Reel · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Retrieve full transcripts for pending videos using the YouTube transcript tool with residential IP and gentle pacing.
**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full YouTube transcript for *"How to Build a Resilient Team"*.
2. Save the transcript as a clean, formatted file (e.g., `.txt` or `.md`) in the designated directory.
3. Verify the transcript’s completeness and accuracy by cross-checking against the video’s content.
4. Share the transcript file with the team for review and feedback.
5. If corrections are needed, re-run the transcript tool or manually edit the file.
6. Archive the finalized transcript in the project’s documentation or repository.

**What changed:** The transcript will now be retrieved and validated for accuracy before further use.
1. Utilize the YouTube transcript tool to fetch raw transcripts for pending videos.
2. Implement residential IP to access the transcript tool and avoid restrictions.
3. Apply gentle pacing to the transcript retrieval process to avoid triggering rate limits.
4. Review and verify the accuracy of the retrieved transcripts.
5. Store the retrieved transcripts in a designated repository for lead review.
**What changed:** The approach to retrieving transcripts now incorporates residential IP and gentle pacing to ensure successful retrieval.
