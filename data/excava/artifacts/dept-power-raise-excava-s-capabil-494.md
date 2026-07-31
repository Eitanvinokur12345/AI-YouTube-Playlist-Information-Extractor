# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-494` (dept) · 2026-07-31T21:42:50.266491+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Run a 5% blind A/B test of **Claude Mythos 5** vs **Fable 5** with a 0.2% kill-switch and stress-test the top 1% low-confidence outputs from the full pipeline.

**Plan:**
1. Split EXCAVA’s pipeline into a 5% blind A/B test cohort (Mythos 5 vs Fable 5) and a 95% control group (Fable 5).
2. Implement a kill-switch triggered if Mythos 5’s quality drops ≥0.2% below Fable 5’s baseline.
3. Stress-test the top 1% low-confidence outputs from the full pipeline (both Mythos 5 and Fable 5) to validate edge-case robustness.
4. Monitor real-time metrics (latency, accuracy, hallucination rate) for 48 hours.
5. Document results in a GitHub issue with raw data and a go/no-go recommendation.
6. Owner (Gearbox) finalizes rollout decision based on aggregated findings.

**What changed:** Reduced slice size to 5% and added stress-testing to mitigate distribution skew risk.
