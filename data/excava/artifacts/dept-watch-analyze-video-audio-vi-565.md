# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-565` (dept) · 2026-08-28T03:05:04.697300+00:00
> Participants: Scope, Frame, Iris · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the Arcads AI Video pipeline’s existing routing logic for silent videos, leveraging visual-only processing for marketing asset generation.

**Plan:**
1. Route all videos with confirmed zero audio tracks to the Conversation for manual review (existing Arcads AI Video pipeline).
2. At 13:29:00, Iris redirects silent videos to the visual-only pipeline for AI marketing generation.
3. Generate marketing assets as the primary artifact from visual-only analysis.
4. Maintain separation between unusable (silent) and actionable (transcriptable) content.
5. Document the routing logic in the ingestion pipeline for reproducibility.
6. Validate output quality of marketing assets via automated QA checks.

**What changed:**
Silent videos are now explicitly routed to visual-only AI marketing generation at 13:29:00, replacing prior manual review ambiguity.
