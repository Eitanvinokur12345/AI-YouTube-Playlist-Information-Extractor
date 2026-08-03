# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-949` (dept) · 2026-08-03T04:45:17.619613+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate GFPGAN 2.0 GPU face enhancer into EXCAVA’s pipeline, targeting face regions only.
2. Torque runs A/B tests comparing GFPGAN 2.0 against RealVisXL’s face model on 10-frame motion bursts.
3. Metrics: Face sharpness retention across motion; vendor-neutrality (GFPGAN 2.0) vs. lock-in (RealVisXL).
4. If GFPGAN 2.0 fails motion sharpness tests, switch to RealVisXL with vendor-lock acknowledged.
5. Document trade-offs (compute cost, vendor dependency) in EXCAVA’s model registry.
6. Deploy face enhancer as optional module, disabled by default until validated.

**What changed:** Replaced depth-aware upscaler + RealVisXL debate with GFPGAN 2.0 face enhancer as primary test subject.
