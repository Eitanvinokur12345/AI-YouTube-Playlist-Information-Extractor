# watch: Analyze video AUDIO+VISUAL (Gemini) for content beyond the transcript.

> Decision artifact · room `dept-watch-analyze-video-audio-vi-916` (dept) · 2026-07-31T18:10:11.207812+00:00
> Participants: Scope, Iris · synthesized by mistral/mistral-small-latest

**Decision:**
Execute the Arcads AI Video "AI Marketing" skill pack on target video `t` to produce a minimum-viable teaser for human review.

**Plan:**
1. **Input Target Video:** Load video `t` into Arcads AI Video’s "AI Marketing" skill pack.
2. **Generate Teaser:** Run the skill pack’s teaser-generation pipeline (AUDIO+VISUAL analysis) to extract key moments.
3. **Output Artifact:** Save the teaser as a single, self-contained file (e.g., `.mp4` or `.mov`) for human QA.
4. **Validate Output:** Ensure the teaser meets minimum-viable criteria (e.g., <30s, highlights core message).
5. **Prepare Delivery:** Package the teaser with metadata (e.g., source video ID, skill pack version) for the reviewer.
6. **Queue for Review:** Mark the artifact as ready in the human reviewer’s queue.

**What changed:** Finalized the execution plan to prioritize a single, automated teaser artifact for human validation.
