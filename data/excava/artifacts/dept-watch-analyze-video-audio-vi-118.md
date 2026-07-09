# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-118` (dept) · 2026-07-09T23:51:03.973230+00:00
> Participants: Scope, Frame, Iris · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Strip transcript entirely, feed raw A/V streams to Gemini-1.5-Pro, and validate output against visible artifacts.

**Plan:**
1. Use `ffmpeg` to extract raw audio and visual streams from the video file `scope_watch_20240611.mp4`.
2. Feed the raw audio and visual files into Gemini-1.5-Pro with a prompt that instructs it to ignore any existing transcripts and assess non-linguistic signals.
3. Document the output from Gemini, focusing on non-linguistic cues identified.
4. Review the Gemini output for any potential hallucinations related to micro-expressions or environmental cues.
5. Cross-reference the output with the raw A/V artifacts observed in the video to ensure consistency and accuracy.

**What changed:** The decision emphasizes validating Gemini's output against visual artifacts to mitigate hallucination risks.
