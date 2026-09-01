# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-508` (dept) · 2026-09-01T04:54:21.314098+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` to fetch the full transcript for the pending video.
2. The tool retrieves and returns the complete, real transcript file.
3. Reel saves the transcript as a file for the lead to inspect.
4. Lead reviews the transcript for accuracy and completeness.
5. If needed, Reel re-runs the tool with adjusted parameters (e.g., language, pacing) for refinement.
6. Final transcript is archived for downstream processing.

**What changed:** Action confirmed—Reel will now fetch the real transcript using the specified tool.
