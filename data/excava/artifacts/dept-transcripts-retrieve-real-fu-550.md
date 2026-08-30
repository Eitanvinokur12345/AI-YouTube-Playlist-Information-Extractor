# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-550` (dept) · 2026-08-30T02:34:27.559452+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes the `kimtaeyoon83/mcp-server-youtube-transcript` tool on each pending video.
2. Reel delivers the retrieved full transcripts to Scriv for verification.
3. Scriv reviews transcripts for accuracy and completeness.
4. Scriv flags discrepancies (if any) for Reel to re-process.
5. Reel re-runs the tool on flagged videos and resubmits transcripts.
6. Scriv finalizes transcripts as verified and archives them.

**What changed:** Reel’s action is now explicitly tasked with using the specified tool to retrieve transcripts.
