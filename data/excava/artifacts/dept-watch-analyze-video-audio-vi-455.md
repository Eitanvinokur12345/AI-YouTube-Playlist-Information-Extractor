# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-455` (dept) · 2026-07-12T13:01:42.071492+00:00
> Participants: Scope, Frame, Iris · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a lightweight visual pass (e.g., shot framing, speaker proximity, basic lighting) to filter out obvious production quirks.
2. Run Gemini 3.1 Ultra’s multimodal analysis in parallel for deep visual/audio interpretation.
3. Cross-check discrepancies between the lightweight pass and Ultra’s output to identify meaningful vs. noise cues.
4. Timestamp all visual cues beyond the transcript in the final report.
5. Flag potential over-interpretations from Ultra (e.g., gestures/lighting as intentional) for manual review.
6. Generate a consolidated report merging filtered cues and Ultra’s insights, with notes on discrepancies.

**What changed:** Parallel passes with cross-checking to balance precision and depth.
