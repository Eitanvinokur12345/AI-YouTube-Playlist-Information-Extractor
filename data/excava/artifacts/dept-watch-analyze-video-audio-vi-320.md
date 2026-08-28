# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-320` (dept) · 2026-08-28T01:46:06.845307+00:00
> Participants: Scope, Frame, Iris · synthesized by mistral/mistral-small-latest

**Decision:**
Ingestion team routes all zero-speech videos to curation—no bypass.

**Plan:**
1. Confirm Arcads AI Video’s ingestion pipeline already routes zero-speech videos to curation.
2. Task the ingestion team to enforce this routing for **all** zero-speech videos.
3. Update pipeline documentation to reflect the mandatory curation step.
4. Implement automated logging for zero-speech video routing decisions.
5. Schedule a review in 30 days to validate compliance and adjust if needed.
6. Notify stakeholders (ingestion, curation, and compliance teams) of the change.

**What changed:**
Mandated curation for all zero-speech videos to prevent bypass.
