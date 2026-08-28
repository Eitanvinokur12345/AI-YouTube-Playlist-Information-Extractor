# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-536` (dept) · 2026-08-28T03:16:25.757800+00:00
> Participants: Scope, Frame, Iris · synthesized by mistral/mistral-small-latest

**Decision:**
Silent videos are routed to Arcads AI Video’s visual-only analysis pipeline for marketing potential assessment.

**Plan:**
1. Confirm existing routing logic sends videos with zero audio tracks to visual-only analysis.
2. Ensure ingestion pipeline extracts no transcriptable audio before routing.
3. Trigger visual-only analysis for silent videos to assess marketing potential.
4. Generate a decision artifact in the Conversation for each silent video processed.
5. Document the decision in the project’s workflow documentation.
6. Notify stakeholders of the confirmed routing logic.

**What changed:**
No changes—proceed with current routing logic.
