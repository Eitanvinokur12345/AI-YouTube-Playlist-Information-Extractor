# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-519` (dept) · 2026-08-28T01:34:47.186506+00:00
> Participants: Scope, Frame, Iris · synthesized by mistral/mistral-small-latest

**Decision:**
Tag all zero-speech videos in curation with "AI-captions-ready" and "AI-voiceover-ready" labels to trigger automated captioning and voiceover pipelines.

**Plan:**
1. Update ingestion pipeline to flag zero-speech videos with metadata tags.
2. Add "AI-captions-ready" and "AI-voiceover-ready" labels to curation queue entries.
3. Configure downstream systems to recognize these labels for automated processing.
4. Document label usage in pipeline runbooks.
5. Notify curation and AI teams of the new labeling standard.
6. Monitor pipeline logs for label-triggered actions.

**What changed:**
Zero-speech videos now auto-tagged for AI captioning/voiceover processing.
