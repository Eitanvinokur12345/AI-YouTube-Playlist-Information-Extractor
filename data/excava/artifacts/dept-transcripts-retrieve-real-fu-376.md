# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-376` (dept) · 2026-07-29T21:20:19.848762+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full transcript for the pending video.
2. If the transcript is available, output the complete real transcript text.
3. If unavailable, confirm the unavailability with a clear message.
4. Ensure the output is in GitHub markdown format, adhering to the specified structure.
5. Maintain a gentle pacing suitable for residential IP constraints.
6. Close the room after synthesizing the decision.

**What changed:** The debate was synthesized into a concrete, actionable plan for transcript retrieval.
