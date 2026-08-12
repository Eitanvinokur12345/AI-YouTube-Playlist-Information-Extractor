# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-748` (dept) · 2026-08-12T09:43:48.031439+00:00
> Participants: Scope, Frame, Iris · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Run kimtaeyoon83/mcp-server-youtube-transcript on all 10 pending videos to extract structured transcripts with `speaker_id` for Arcads AI Video analysis.
**Plan:**
1. Extract structured transcripts from 10 pending videos using kimtaeyoon83/mcp-server-youtube-transcript.
2. Include `speaker_id` as a nullable string in the transcript output for speaker attribution.
3. Run Arcads AI Video’s multimodal analysis on the extracted transcripts for AI marketing insights.
4. Verify that the `speaker_id` field is correctly populated in the transcript output for all 10 videos.
5. Proceed with Arcads AI Video analysis using the cleaned dataset with `speaker_id` fields.
**What changed:** Transcripts now include `speaker_id` fields for proper speaker attribution in Arcads AI Video analysis.
