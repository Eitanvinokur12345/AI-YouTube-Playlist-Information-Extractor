# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-157` (dept) · 2026-08-17T22:29:11.163461+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes the `kimtaeyoon83/mcp-server-youtube-transcript` tool to fetch the full transcript for the pending video.
2. Reel processes the raw captions into a clean, readable text file.
3. Reel delivers the finalized transcript file directly to the lead.
4. Lead verifies receipt and confirms the transcript meets the "done-criteria."
5. Archive the transcript in the designated repository with version control.
6. Notify stakeholders of completion via the agreed channel.

**What changed:** Reel is now explicitly tasked with fetching and delivering the real transcript, replacing prior ambiguity.
