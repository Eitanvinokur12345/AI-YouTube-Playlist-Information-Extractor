# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-615` (dept) · 2026-07-12T19:41:33.709628+00:00
> Participants: Scope, Frame, Iris · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run parallel audio sentiment analysis and visual analysis on the video using Gemini 3.1 Ultra.
2. Generate timestamped sentiment scores for audio and visual cues independently.
3. Compare results to identify segments where audio and visual cues contradict (e.g., positive tone + negative expressions).
4. Prioritize segments with the highest contradiction scores for manual review.
5. Compile a timestamped report of flagged segments with raw data (audio sentiment, visual cues, and discrepancy notes).
6. Deliver the report to the lead editor for final interpretation.

**What changed:** Parallel analysis replaces sequential audio-first approach to capture context-dependent cues like sarcasm or forced enthusiasm.
