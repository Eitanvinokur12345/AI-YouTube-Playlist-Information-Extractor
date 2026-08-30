# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-464` (dept) · 2026-08-30T03:44:43.602353+00:00
> Participants: Scope, Frame, Iris · synthesized by mistral/mistral-small-latest

**Decision:**
Iris authorizes the 14-day fixed A/B test for the Arcads AI Video Agent Skill Pack with a 24-hour holdout window.

**Plan:**
1. Configure the A/B test scope to exclusively target the Arcads AI Video Agent Skill Pack.
2. Set the test duration to 14 days with a 24-hour holdout window.
3. Leverage Arcads AI Video’s existing ingestion pipeline for A/B test routing.
4. Monitor performance metrics between control and variant groups during the test period.
5. Ensure statistical validity of results before concluding the test.
6. Document test parameters and outcomes in the project repository.

**What changed:** Scope locked to Arcads AI Video Agent Skill Pack with 14-day fixed test + 24-hour holdout window.
