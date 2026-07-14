# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-988` (dept) · 2026-07-14T21:32:53.238606+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. **Benchmark Validation:** Torque sets up a held-out benchmark matching EXCAVA’s domain to validate accuracy of NVIDIA H100 + Llama 3.4 70B and the latest accessible open model (Llama 3.3 70B or distilled variant).
2. **Parallel Testing:** Run a 10% live-data slice through both models in parallel, logging throughput and accuracy metrics.
3. **Cost-Benefit Analysis:** Compare compute cost vs. performance lift for each model, including lock-in risks for closed-source options.
4. **Model Selection:** Choose the model (or hybrid) delivering ≥0.5% capability lift at optimal cost, based on benchmark and live-data results.
5. **Deployment Prep:** If H100 + Llama 3.4 70B is selected, secure procurement; if open model wins, finalize integration and scaling.
6. **Monitoring:** Post-deployment, track EXCAVA’s performance for 7 days to confirm the 0.5% lift and identify edge cases.

**What changed:** Expanded test scope from 1% to 10% live-data slice and added benchmark validation before parallel testing.
