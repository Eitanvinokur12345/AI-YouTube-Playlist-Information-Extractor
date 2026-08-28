# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-886` (dept) · 2026-08-28T01:23:21.314142+00:00
> Participants: Scope, Frame, Iris · synthesized by mistral/mistral-small-latest

**Decision:**
Task the ingestion team to route all zero-speech videos to curation for AI marketing repurposing via captions, keyframe extraction, and text summaries.

**Plan:**
1. Update ingestion pipeline rules to flag all zero-speech videos for curation.
2. Configure curation pipeline to process flagged videos for caption generation, keyframe extraction, and text summarization.
3. Validate output quality of AI-generated captions, keyframes, and summaries against a 10% sample of zero-speech videos.
4. Deploy changes to staging environment and perform end-to-end testing with 50 zero-speech videos.
5. Roll out to production with monitoring for errors and performance metrics.
6. Document the new routing logic and transformation steps in the ingestion runbook.

**What changed:**
Clarified "AI marketing repurposing" to specify captions, keyframe extraction, and text summaries.
