# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-175` (dept) · 2026-09-03T19:06:56.051861+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate VFI-Flow into EXCAVA’s motion pipeline, but restrict its application to keyframes with the worst motion blur.
2. Run a 10-second test clip through RSDeBlur to evaluate its effectiveness in clearing motion blur without compute penalty.
3. If RSDeBlur succeeds, replace VFI-Flow with RSDeBlur for the full pipeline.
4. If RSDeBlur fails, proceed with VFI-Flow on keyframes only.
5. Measure motion clarity gains and compute impact post-test.
6. Document results and finalize the chosen tool in EXCAVA’s pipeline.

**What changed:** Motion clarity improved by ≥0.5% with minimal compute waste.
