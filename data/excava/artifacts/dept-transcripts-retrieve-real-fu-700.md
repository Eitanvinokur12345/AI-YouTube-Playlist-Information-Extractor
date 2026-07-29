# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-700` (dept) · 2026-07-29T21:58:21.346147+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full transcript for the pending video.
2. Save the output as a real transcript file (e.g., `.txt` or `.md`) via Echo.
3. Verify the transcript is complete and clean (no truncation or errors).
4. Store the file in the designated repository or directory.
5. Confirm the file is accessible and properly formatted for downstream use.
6. Notify Reel upon completion with the file path or link.

**What changed:** Resolved redundancy by formalizing the action into a structured plan.
