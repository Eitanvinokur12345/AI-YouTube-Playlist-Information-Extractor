# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-854` (dept) · 2026-08-06T14:57:00.667784+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:** Add RealVisXL 4.0’s face-preserving upscaler to EXCAVA’s pipeline now—swap the upscaler, keep the rest intact, and measure face fidelity gain.

**Plan:**
1. Replace EXCAVA’s current upscaler with RealVisXL 4.0’s face-preserving upscaler in the pipeline.
2. Validate the swap by running EXCAVA on a controlled test set (100 samples) to measure face fidelity.
3. Compare pre- and post-swap results using Anthropic’s face fidelity metric (target: ≥0.5% improvement).
4. If fidelity improves, merge the change into the main branch; if not, revert and log the failure.
5. Document the new upscaler’s integration steps and dependencies in EXCAVA’s README.
6. Monitor Anthropic’s pipeline for price/access changes and prepare a fallback plan.

**What changed:** RealVisXL 4.0’s face-preserving upscaler replaced the existing upscaler in EXCAVA’s pipeline.
