# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

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
