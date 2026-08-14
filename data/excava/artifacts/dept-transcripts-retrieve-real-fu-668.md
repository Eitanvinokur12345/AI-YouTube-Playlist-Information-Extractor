# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-668` (dept) · 2026-08-14T09:38:54.808182+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the `kimtaeyoon83/mcp-server-youtube-transcript` tool on the pending video ID `e2Z5eBVDrKM`.
2. Verify the output is a full transcript/captions file (not a summary or excerpt).
3. Confirm completeness by checking for full coverage of the video’s content.
4. If valid, mark the transcript as retrieved and ready for use.
5. If incomplete, re-run the tool with adjusted parameters (e.g., slower pacing for residential IP).
6. Document the final transcript file path for future reference.

**What changed:** Tool execution and verification now explicitly include completeness checks.
