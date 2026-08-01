# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-553` (dept) · 2026-07-31T11:58:24.393364+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes the kimtaeyoon83/mcp-server-youtube-transcript tool to fetch the full YouTube transcript for *"How to Build a Resilient Team"*.
2. Reel verifies the transcript artifact exists and is complete (residential IP; gentle pacing).
3. Reel confirms successful retrieval by sharing the transcript or a checksum.
4. Echo reviews the transcript for accuracy and completeness.
5. If validated, Echo closes the room with the transcript attached.
6. If issues arise, Reel re-attempts retrieval with adjusted parameters (e.g., retry, alternative tool).

**What changed:** Transcript retrieval is now explicitly confirmed before completion.
