# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-744` (dept) · 2026-08-17T20:57:56.778104+00:00
> Participants: Scope, Frame, Iris · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run Arcads AI Video on the AI marketing content to extract top 3 contradictions from AUDIO+VISUAL layers (not just transcript).
2. Output a ranked list with timestamps and visual context for each contradiction.
3. Prioritize contradictions based on severity (e.g., factual vs. stylistic) and relevance to the video’s claims.
4. Include a brief visual description (e.g., "on-screen text contradicts voiceover at 02:33") for each entry.
5. Validate contradictions by cross-referencing AUDIO and VISUAL layers independently before finalizing.
6. Deliver the ranked list in GitHub markdown format with no preamble.

**What changed:** Scope expanded from transcript-only to full AUDIO+VISUAL multimodal analysis.
