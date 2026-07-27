# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-861` (dept) · 2026-07-27T17:30:42.693961+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Query the YouTube transcript tool for each pending video ID using the kimtaeyoon83/mcp-server-youtube-transcript integration.
2. Retrieve and store the full, real transcripts for all pending videos.
3. Validate transcripts for accuracy and completeness.
4. Organize transcripts by video ID for easy access.
5. Ensure transcripts are saved in a structured format (e.g., JSON or text files).
6. Confirm all pending videos have their transcripts retrieved before proceeding.

**What changed:** Automated transcript retrieval replaces manual or partial methods.
