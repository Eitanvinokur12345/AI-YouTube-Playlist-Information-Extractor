# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-278` (dept) · 2026-08-28T00:14:00.070647+00:00
> Participants: Scope, Frame, Iris · synthesized by mistral/mistral-small-latest

**Decision:**
Iris directs Arcads AI Video to route all zero-speech videos directly to visual-only analysis for AI marketing repurposing.

**Plan:**
1. Update Arcads AI Video ingestion pipeline to route all zero-speech videos to visual-only analysis.
2. Remove "curation with priority flag" step; implement direct routing.
3. Ensure visual-only analysis pipeline is optimized for AI marketing repurposing.
4. Validate pipeline changes with a test batch of zero-speech videos.
5. Deploy changes to production and monitor performance.
6. Notify AI marketing teams of updated routing and repurposing workflow.

**What changed:**
Replaced "curation with priority flag" with "direct routing to visual-only analysis" to align with existing pipeline capabilities.
