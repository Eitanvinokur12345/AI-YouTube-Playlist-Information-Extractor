# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-892` (dept) · 2026-07-20T22:47:23.442386+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Design a blind 128K-context head-to-head test for Mistral Large 2, Qwen2.5-72B, and Opus 4.8 on EXCAVA’s longest power task.
2. Torque to own test design, artifact delivery, and evaluation criteria by [date].
3. Execute tests with identical prompts, seeds, and evaluation metrics to ensure fairness.
4. Measure performance lift (accuracy, latency, stability) and cost efficiency for each model.
5. Select the top-performing model based on a weighted score of capability lift and cost.
6. Integrate the chosen model into EXCAVA and monitor for silent failures or regressions.

**What changed:** Added Opus 4.8 to the test suite for direct comparison.
