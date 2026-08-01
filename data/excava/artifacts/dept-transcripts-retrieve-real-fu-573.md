# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-573` (dept) · 2026-07-31T18:16:58.108149+00:00
> Participants: Reel, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes the `kimtaeyoon83/mcp-server-youtube-transcript` tool on pending video #1 to fetch its full captions.
2. Reel generates a clean, readable transcript file from the tool’s output.
3. Reel posts the transcript file to the room for lead review.
4. Lead reviews the transcript for accuracy and completeness.
5. If corrections are needed, Reel revises the transcript based on lead feedback.
6. Final transcript is archived for downstream use.

**What changed:** Tool execution and transcript delivery initiated for pending video #1.
