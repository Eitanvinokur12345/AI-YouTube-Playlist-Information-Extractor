# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-271` (dept) · 2026-07-12T12:23:33.028779+00:00
> Participants: Scope, Frame, Iris · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. **First-pass scan:** Use Gemini 3.1 Ultra to timestamp all visual-audio cues (demeanor, tone, background) that contradict or expand *any* high-stakes claim in the transcript (e.g., "I’m 100% certain," "no conflicts of interest").
2. **Filter by core claims:** Retain only timestamps where contradictions directly impact the transcript’s primary assertions (e.g., smirk during certainty, tone shift during conflict denial).
3. **Prioritize high-risk cues:** Over-index on speaker demeanor (smirks, fidgeting, eye rolls) and tone shifts for claims with binary stakes (e.g., absolute statements, denials).
4. **Exclude low-signal data:** Skip subtle background cues (e.g., dated objects) unless they directly refute a core claim (e.g., a calendar showing a future date during a past-tense denial).
5. **Output format:** Deliver a concise report with timestamps, contradiction type (visual/audio), and core claim affected.
6. **Manual review trigger:** Flag the top 3 contradictions for human review if ambiguity remains.

**What changed:** Adopted a two-pass scan to balance depth and efficiency, focusing on high-stakes contradictions first.
