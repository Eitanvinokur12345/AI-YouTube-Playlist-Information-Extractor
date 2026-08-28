# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-427` (dept) · 2026-08-28T00:49:12.223623+00:00
> Participants: Scope, Frame, Iris · synthesized by mistral/mistral-small-latest

**Decision:** Route all zero-speech videos to curation to ensure no visual-only content bypasses review.

**Plan:**
1. Instruct the ingestion team to update the pipeline to route **all** zero-speech videos to curation.
2. Verify the Arcads AI Video ingestion pipeline’s current routing behavior for zero-speech videos.
3. Confirm the curation routing artifact is active and functional.
4. Document the change in the ingestion pipeline’s configuration.
5. Communicate the update to the ingestion and curation teams.
6. Monitor the first batch of zero-speech videos post-update to ensure proper routing.

**What changed:** Zero-speech videos are now explicitly routed to curation.
