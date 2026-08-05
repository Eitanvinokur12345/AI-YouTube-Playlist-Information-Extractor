# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-185` (dept) · 2026-08-05T23:04:12.561847+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel queries the `kimtaeyoon83/mcp-server-youtube-transcript` tool with the pending video IDs.
2. Reel delivers the retrieved full, real transcripts to the `transcripts-checker` for verification.
3. `transcripts-checker` confirms authenticity and completeness of the transcripts.
4. If verified, transcripts are stored in the designated repository.
5. If unverified, Reel re-queries or escalates for manual review.
6. Progress is logged in the transcripts-checker system.

**What changed:** Action assigned to Reel with tool integration and verification steps.
