# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-414` (dept) · 2026-09-02T16:13:35.385152+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Proceed with fetching the full real transcript for the pending video.

**Plan:**
1. Reel executes the kimtaeyoon83/mcp-server-youtube-transcript tool to retrieve the complete transcript.
2. The tool outputs the full transcript file (residential IP; gentle pacing).
3. Scriv receives the transcript file for verification.
4. Scriv confirms the transcript’s authenticity and completeness.
5. If verified, Scriv marks the transcript as ready for further processing.
6. If issues arise, Reel reattempts with adjusted parameters (e.g., retry or alternative tool).

**What changed:**
Action shifted from debate to execution—Reel now actively fetches the transcript via the specified tool.
