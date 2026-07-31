# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-611` (dept) · 2026-07-31T14:34:50.781763+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Proceed with the distilled 32B model for EXCAVA only after validation.

**Plan:**
1. Gearbox implements the switch to the distilled 32B variant in EXCAVA.
2. Torque prepares a 2,000-task adversarial benchmark with out-of-domain gold standards.
3. Torque runs the benchmark and grades results blindly.
4. If the gain is ≥0.5%, Gearbox deploys the model; otherwise, roll back.
5. Dynamo audits the benchmark results and finalizes the decision.
6. Gearbox monitors post-deployment performance for drift.

**What changed:** EXCAVA remains on current model until adversarial validation passes.
