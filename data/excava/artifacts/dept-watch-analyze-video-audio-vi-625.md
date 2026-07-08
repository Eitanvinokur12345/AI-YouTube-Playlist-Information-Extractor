# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-625` (dept) · 2026-07-08T17:19:17.907664+00:00
> Participants: Scope, Frame, Iris · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Proceed with full-video ProRes 422 HQ transcode and dual-pass Gemini analysis.

**Plan:**
1. Transcode the full `scope_watch_20240605.mp4` to ProRes 422 HQ.
2. Run a controlled dual-pass analysis with Gemini-1.5-Pro on the full ProRes video.
3. Maintain a log of storage and compute costs associated with the ProRes transcoding.
4. Generate and diff the JSON outputs from both the ProRes and 768p H.264 downscaled versions.
5. Conduct failure mode analysis on edge cases, focusing on fast cuts, low-light conditions, and text overlays.

**What changed:** Decision to conduct full video analysis overrides initial test scope due to concerns about real-world application.
