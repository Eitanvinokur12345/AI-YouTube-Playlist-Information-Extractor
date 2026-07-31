# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

<<<<<<< HEAD
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
=======
> Decision artifact · room `dept-power-raise-excava-s-capabil-494` (dept) · 2026-07-31T21:40:46.292702+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Proceed with a controlled, risk-balanced test of **Claude Mythos 5** vs **Fable 5** on EXCAVA’s pipeline.

**Plan:**
1. Run a **blind A/B test** of **Claude Mythos 5** vs **Fable 5** on a **5% slice** of EXCAVA’s pipeline.
2. Implement a **0.2% kill-switch**—if Mythos 5’s quality drops below baseline by ≥0.2%, roll back to Fable 5.
3. **Stress-test** the top 1% of low-confidence outputs from the full pipeline to validate Mythos 5’s edge in edge cases.
4. Measure **real-world performance** on reasoning tasks (primary metric) and stability (secondary metric).
5. If Mythos 5 passes the stress test and improves reasoning by ≥0.5% without violating the kill-switch, **gradually expand** its usage to 10% of the pipeline.
6. Document findings in a **post-test report** comparing Mythos 5’s lift vs. Fable 5’s stability.

**What changed:** Balanced risk with leverage—smaller slice (5%) + tighter kill-switch (0.2%) + stress test to validate edge cases.
>>>>>>> 05eb4e404a4005fd0bbf5d2e4c0ee0a4f3ffe443
