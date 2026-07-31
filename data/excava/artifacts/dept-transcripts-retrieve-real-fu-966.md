# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-966` (dept) · 2026-07-31T02:04:40.313071+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full transcript for *"How to Build a Resilient Team"*.
2. Verify the transcript contains real, complete content (e.g., non-empty, coherent text).
3. If valid, confirm retrieval and store the transcript securely.
4. If invalid or empty, retry once with adjusted parameters (e.g., retry flag, retry delay).
5. Log the outcome (success/failure) with timestamp and transcript metadata.
6. Notify stakeholders of completion or escalate if unresolved.

**What changed:** Transcript retrieval is now explicitly conditional on content validation.
