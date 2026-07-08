# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-660` (dept) · 2026-07-08T02:47:55.074463+00:00
> Participants: Scope, Frame, Iris · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Extract raw A/V losslessly, validate sync via frame-accurate checksums + audio RMS parity, then feed verified streams to gemini-2.0-flash with frame-level timestamps in metadata.

**Plan:**
1. Use `ffmpeg` to extract `audio.wav` and `visual.mkv` from `watch_analysis_input.mp4`.
2. Generate checksums (MD5/SHA256) for each frame in `visual.mkv` and calculate the RMS difference with `audio.wav`.
3. Create a control group to analyze potential frame drops or corruption in `visual.mkv`.
4. Ensure audio and visual streams maintain synchronization throughout by reporting frame-level metadata.
5. Feed the validated and synchronized streams to the gemini-2.0-flash model for analysis.

**What changed:** The need for a control group and frame-accurate validation was emphasized to ensure data integrity before analysis.
