# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-434` (dept) · 2026-08-22T09:00:32.342700+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` to fetch full transcripts for all pending videos.
2. Outputs plain text captions for each video in a structured format.
3. Scriv reviews the transcripts for accuracy and completeness.
4. Fixes (if any) are applied by Reel via the same tool.
5. Transcripts are archived in the designated repository.
6. Echo closes the room upon Scriv’s verification.

**What changed:** Action confirmed—Reel fetches transcripts via the specified tool.
