# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-901` (dept) · 2026-07-30T20:09:09.932248+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the kimtaeyoon83/mcp-server-youtube-transcript tool to fetch the full transcript for the pending video.
2. Verify the transcript is complete and accurate (no summaries or AI-generated paraphrasing).
3. Save the transcript in a structured format (e.g., `.txt` or `.md`) for further use.
4. Cross-check the transcript against the video’s captions (if available) for consistency.
5. Store the transcript in a designated directory (e.g., `/transcripts/pending/`).
6. Notify the user via a GitHub issue or comment that the transcript is ready.

**What changed:** Tool-based retrieval replaces manual or AI-generated transcript methods.
