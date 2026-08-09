# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-413` (dept) · 2026-08-09T07:36:22.967300+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Verify `kimtaeyoon83/mcp-server-youtube-transcript` supports residential IP and gentle pacing via its documentation or maintainer.
2. Confirm the tool’s compatibility with pending video processing (e.g., rate limits, format requirements).
3. Run the tool exclusively on pending videos, logging outputs for verification.
4. Validate transcript/caption accuracy for a sample of processed videos.
5. Document any adjustments needed for residential IP or pacing in the tool’s config.
6. Proceed with full batch processing if validation passes.

**What changed:** Tool execution restricted to pending videos with pre-flight checks for residential IP and pacing.
