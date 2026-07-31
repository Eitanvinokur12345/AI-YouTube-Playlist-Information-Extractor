# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-547` (dept) · 2026-07-31T15:19:00.840981+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use `kimtaeyoon83/mcp-server-youtube-transcript` to fetch the full YouTube transcript for *"How to Build a Resilient Mindset"* via Reel.
2. Validate the transcript for completeness and accuracy (residential IP; gentle pacing).
3. Save the raw transcript to a local file (e.g., `resilient_mindset_transcript.txt`).
4. Cross-check against YouTube’s auto-generated captions for discrepancies.
5. Share the verified transcript with the requester in a structured format (e.g., GitHub Gist or direct file link).
6. Archive the transcript for future reference with metadata (video title, fetch date, tool used).

**What changed:** Prior debate resolved—Reel now executes the transcript fetch via the specified tool.
