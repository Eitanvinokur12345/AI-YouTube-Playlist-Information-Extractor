# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-384` (dept) · 2026-07-16T18:15:11.907664+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement a lightweight risk-scoring system for prompt changes (e.g., "high" for core routing, "low" for typo fixes).
2. Auto-apply low-risk tweaks instantly; log only high-risk changes (>5% metric shift, new failure modes, or core routing).
3. Sprocket owns the risk-scoring logic and audit tool; Gauge owns weekly spot-checks for latent drift.
4. Track high-risk changes in a log with reasons and expected impact.
5. Review audit data weekly to refine risk thresholds and scoring.

**What changed:** Hybrid audit system—sampled logging for high-risk changes + auto-apply for low-risk tweaks.
