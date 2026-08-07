# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-461` (dept) · 2026-08-07T13:52:34.159008+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Proceed with transcript retrieval after format validation.

**Plan:**
1. Reel contacts Creative to confirm required transcript format (plain text vs. structured captions).
2. Reel verifies kimtaeyoon83/mcp-server-youtube-transcript output matches Creative’s format needs.
3. Reel runs the tool only on videos tagged "ready" by Creative.
4. Reel delivers transcripts/captions to Creative in the validated format.
5. Reel logs any format mismatches or tool failures for review.

**What changed:** Added format validation step before bulk processing.
