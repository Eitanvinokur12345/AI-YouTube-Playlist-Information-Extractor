# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-493` (dept) · 2026-08-11T01:59:42.267625+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Scriv re-checks the output of `kimtaeyoon83/mcp-server-youtube-transcript` to confirm it retrieves full transcripts (not just captions).
2. If confirmed, Scriv runs the tool on the 10 pending videos to fetch their full transcripts.
3. Scriv verifies the retrieved transcripts for completeness and accuracy.
4. Scriv archives the transcripts for use in downstream tasks.
5. Scriv logs the results and any issues encountered.
6. Scriv reports completion to the team.

**What changed:** Added verification step before bulk processing.
