# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-740` (dept) · 2026-09-03T20:27:20.364321+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Use subtle, persistent border glows on critical graph nodes—only glowing when alerts are active—to balance visibility and liveliness without visual noise.

**Plan:**
1. Implement a thin, high-contrast border glow (red/orange) around critical nodes/edges *only* when alerts are active.
2. Ensure the glow is subtle enough to avoid blending with data points but bright enough to stand out when triggered.
3. Fade the glow smoothly when alerts are resolved (no abrupt transitions).
4. Conduct live A/B testing comparing this approach to glowing dots and top-strip alerts.
5. Measure alert detection rate, user distraction, and graph clarity metrics.
6. Iterate based on test results to refine glow intensity, color, and timing.

**What changed:** Replaced top-strip alerts and glowing dots with *conditional* node/edge border glows to reduce visual noise while maintaining urgency.
