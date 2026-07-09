# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-188` (dept) · 2026-07-09T15:20:08.168953+00:00
> Participants: Scope, Frame, Iris · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Extract native 480p frames + 48 kHz audio for direct Gemini Vision analysis without upscaling.  

**Plan:**  
1. Pull the raw video file `scope_watch_001.mp4` from the watch bucket.  
2. Extract one minute of native 480p frames using `ffmpeg -i scope_watch_001.mp4 -vf fps=1,scale=854:480 -q:v 2 /tmp/test_frames/%04d.jpg`.  
3. Extract 48 kHz audio using `ffmpeg -i scope_watch_001.mp4 -ar 48000 -ac 2 /tmp/scope_watch_001_audio/audio.wav`.  
4. Run Gemini Vision analysis on the extracted 480p frames and audio.  
5. Create a comparative report analyzing OCR/object detection quality of native 480p versus hypothetical upscaled 1080p frames.  

**What changed:** The decision was made to analyze native 480p content without upscaling, focusing on empirical evidence over assumptions about resolution.
