# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-124` (dept) · 2026-08-03T18:45:13.933817+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes `mcp-server-youtube-transcript` to fetch the full YouTube transcript for *The Science of Sleep*.
2. The tool generates a plain-text artifact of the REAL full transcript/captions.
3. Scriv verifies the artifact meets the goal (residential IP; gentle pacing).
4. Echo archives the transcript in the designated repository.
5. Notify stakeholders of completion via GitHub issue/PR.
6. Close the room upon confirmation.

**What changed:** Reel’s action is now explicitly ordered and scoped to *The Science of Sleep*.
