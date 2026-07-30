# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-348` (dept) · 2026-07-30T18:22:17.490502+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a 100-hour blind A/B test on 5,000 live EXCAVA tasks comparing Llama 3.4 405B Instruct vs. current default.
2. Measure quality lift (target: ≥0.5% improvement) and end-to-end latency under load.
3. Torque designs the test, including latency benchmarks and slice selection.
4. Gearbox deploys Llama 3.4 405B Instruct for the test group.
5. Dynamo owns final sign-off based on results.

**What changed:** Llama 3.4 405B Instruct replaces current default pending bake-off results.
