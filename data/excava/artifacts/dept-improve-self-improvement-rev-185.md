# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-185` (dept) · 2026-07-14T06:36:50.781517+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt staged hybrid scans—exact string matching first, then semantic analysis only on flagged prompts—to balance coverage with compute cost.

**Plan:**
1. Implement weekly automated scans using exact string matching for all prompts.
2. Add semantic similarity analysis as a secondary step, triggered only for prompts flagged by the initial scan.
3. Configure false-positive thresholds to minimize unnecessary rework.
4. Integrate the hybrid scanner into the existing CI/CD pipeline for automated execution.
5. Log all flagged prompts and review false positives monthly to refine thresholds.
6. Document the staged process in the team’s prompt management guidelines.

**What changed:** Hybrid scanning now runs in two stages, reducing compute cost while improving detection of prompt drift.
