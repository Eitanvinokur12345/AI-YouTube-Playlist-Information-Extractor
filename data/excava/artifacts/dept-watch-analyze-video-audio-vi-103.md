# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-103` (dept) · 2026-07-12T11:39:32.303039+00:00
> Participants: Scope, Frame, Iris · synthesized by mistral/mistral-small-latest

**Decision:** Run parallel audio-visual analysis to generate a prioritized list of key moments with timestamps.

**Plan:**
1. Run audio analysis to extract tone, pauses, and background noise (e.g., door slams, urgency).
2. Run visual scene analysis to identify gestures, object interactions, and background changes (e.g., documents, third parties).
3. Merge results to flag high-value segments where audio and visual cues align or resolve ambiguity.
4. Generate a prioritized list of key moments with timestamps for deeper review.
5. Assign ownership to `watch-w1` for execution and validation.
6. Document assumptions (e.g., critical context in audio vs. visuals) for future iterations.

**What changed:** Adopted parallel processing to avoid missing nonverbal or tonal cues, replacing sequential audio-then-visual or visual-then-audio approaches.
