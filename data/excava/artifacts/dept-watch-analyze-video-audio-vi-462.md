# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-462` (dept) · 2026-07-09T14:43:11.330680+00:00
> Participants: Scope, Frame, Iris · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Extract original audio (`ffmpeg -i input.mp4 -ar 48000 -ac 2 original.wav`) and transcript (`yt-dlp --write-auto-sub --sub-lang en --skip-download`).
2. Generate processed audio (`ffmpeg -i input.mp4 -af "aresample=async=1:first_pts=0" -ar 48000 -ac 2 output.wav`).
3. Compute spectral centroid diff (`ffmpeg -i output.wav -af "astats=metadata=1:reset=1" -f null - 2>&1 | grep "Overall"` vs. original).
4. Run phase coherence blind A/B test (`ffmpeg -i original.wav -i output.wav -filter_complex "ametadata=print:file=phase.txt" -f null -`).
5. Calculate waveform SNR (`ffmpeg -i original.wav -i output.wav -filter_complex "sarn=1" -f null - 2>&1 | grep "SNR"`).
6. Measure timestamp alignment error (compare `.vtt` timestamps vs. manual alignment).

**What changed:** Added phase coherence and SNR validation to spectral centroid and timestamp checks.
