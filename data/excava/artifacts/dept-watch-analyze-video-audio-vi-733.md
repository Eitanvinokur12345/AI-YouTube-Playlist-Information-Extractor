# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-733` (dept) · 2026-07-12T23:01:19.919332+00:00
> Participants: Scope, Iris · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the video through **Gemini 3.1 Ultra** with parallel **audio sentiment analysis** (tone, pauses, emphasis) and **visual analysis** (facial expressions, body language, scene composition).
2. Generate a **structured report** with sections for:
   - **Non-verbal cues** (e.g., micro-expressions, gestures, lighting/color shifts).
   - **Emotional tone** (e.g., stress, confidence, deception cues via voice pitch/volume).
   - **Scene-level insights** (e.g., framing, object interactions, environmental context).
3. Cross-reference **audio-visual anomalies** (e.g., inconsistencies between speech and facial expressions).
4. Extract **key moments** (e.g., hesitations, sudden tone shifts, visual distractions) for deeper analysis.
5. Compile findings into a **GitHub markdown report** with timestamps and confidence scores.
6. Validate outputs with a **secondary tool** (e.g., manual review or another AI model) for bias/accuracy.

**What changed:** Scope expanded from transcript-only to **full multimodal analysis** (audio + visual + contextual cues).
