# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-730` (dept) · 2026-07-30T14:46:26.844049+00:00
> Participants: Reel · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Use the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full transcript for the pending video via the YouTube transcript API.
2. Ensure the transcript is clean, complete, and formatted for easy review by the lead.
3. Save the transcript as a `.md` file in the designated repository folder.
4. Notify the lead via GitHub issue or PR for approval.
5. If approved, merge the transcript into the main branch; if not, iterate based on feedback.
6. Archive the original video metadata for reference.

**What changed:** Automated transcript retrieval replaces manual scraping.
