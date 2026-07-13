# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-524` (dept) · 2026-07-13T07:51:13.833712+00:00
> Participants: Scope, Iris · synthesized by mistral/mistral-small-latest

**Decision:**
Proceed with parallel multimodal analysis of the video using Gemini 3.1 Ultra to extract non-transcript content.

**Plan:**
1. Run **audio sentiment analysis** to detect tone shifts, emphasis, and emotional cues.
2. Perform **visual analysis** to identify gestures, facial expressions, and contextual visual elements.
3. Cross-reference findings with the transcript to highlight **gaps** (e.g., implied meaning, subtext).
4. Generate a **structured report** with sections: *Tone/Emphasis*, *Visual Cues*, *Contextual Gaps*.
5. Validate key insights with a secondary tool (e.g., manual review or another model) for consistency.
6. Deliver the report in GitHub-flavored Markdown with clear headers and bullet points.

**What changed:**
Added validation step (Step 5) to ensure accuracy of multimodal insights.
