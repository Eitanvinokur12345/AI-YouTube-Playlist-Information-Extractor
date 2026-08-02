# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-318` (dept) · 2026-08-02T15:40:45.577211+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Use subtle 3-second edge glow for new data + node border pulse for idle attention (A/B tested).

**Plan:**
1. Implement edge glow (soft, persistent color shift for 3s post-data arrival).
2. Add node border pulse (single, brief highlight when idle).
3. A/B test two variants: glow+pulse vs. shrink+pulse (track clicks/dwell time).
4. Default to winning variant; log false positives (ignored signals).
5. Add kill switch for edge glow if dwell time drops >20% in any cohort.
6. Document thresholds in code comments (e.g., glow opacity = 0.3).

**What changed:**
Replaced node shrink + edge pulse with node border pulse + edge glow.
