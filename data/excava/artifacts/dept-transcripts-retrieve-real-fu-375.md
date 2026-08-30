# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-375` (dept) · 2026-08-30T03:10:39.485254+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Replace Deepgram’s real-time transcription with `kimtaeyoon83/mcp-server-youtube-transcript` for pending videos.
2. Fetch full YouTube captions directly via the MCP server to avoid latency and cost risks.
3. Generate a verbatim transcript file for each pending video.
4. Validate transcript accuracy by cross-referencing with the source video.
5. Store transcripts in a designated folder (e.g., `./transcripts/`) with filenames matching video IDs.
6. Log failures for videos where captions are unavailable or incomplete.

**What changed:** Switched from Deepgram’s real-time API to direct YouTube caption extraction via `kimtaeyoon83/mcp-server-youtube-transcript`.
