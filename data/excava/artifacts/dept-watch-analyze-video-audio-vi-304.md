# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-304` (dept) · 2026-08-08T21:02:35.351429+00:00
> Participants: Scope, Frame, Iris · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run `kimtaeyoon83/mcp-server-youtube-transcript` on the "ready" video to extract the transcript and metadata.
2. Use Arcads AI Video’s multimodal analysis to process the video’s audio+visual content beyond the transcript.
3. At 11:21:00, direct Arcads AI Video skill pack to generate AI marketing insights from the raw analysis.
4. Produce a decision-ready artifact (e.g., structured report) for the lead.
5. Validate the output against the original video content for accuracy.
6. Archive the transcript, metadata, and insights in a designated repository.

**What changed:** Arcads AI Video’s multimodal analysis is now explicitly tasked with extracting marketing insights from the raw video data.
