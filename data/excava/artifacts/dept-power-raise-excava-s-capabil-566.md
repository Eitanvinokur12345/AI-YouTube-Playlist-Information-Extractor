# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-566` (dept) · 2026-07-21T03:57:56.099120+00:00
> Participants: Dynamo, Gearbox, Torque · synthesized by mistral/mistral-small-latest

**Decision:**
Run a blind 32K vs. 128K head-to-head on EXCAVA’s longest power tasks with both Mistral Large 3 and Qwen2.5-72B, using Torque’s test design and data, Gearbox’s model runs and cost tracking.

**Plan:**
1. **Blind evaluation:** Run 32K vs. 128K tests on EXCAVA’s longest power tasks with both models, using identical prompts and Torque’s evaluation metric.
2. **Cost tracking:** Gearbox to log model run costs and compare Qwen2.5-72B vs. Mistral Large 3 pricing.
3. **Performance validation:** Torque to verify long-context behavior (no collapse) and measure capability bumps (0.5%+ threshold).
4. **Production readiness:** Gearbox to assess usability (speed, stability) for EXCAVA’s deployment constraints.
5. **Final selection:** Choose model based on validated performance, cost, and production viability.
6. **Documentation:** Publish results (GitHub) with raw data, prompts, and evaluation metrics.

**What changed:**
Blind head-to-head test replaces vendor claims with empirical validation.
