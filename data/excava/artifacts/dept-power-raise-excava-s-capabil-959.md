# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-959` (dept) · 2026-08-07T00:56:18.646788+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Add RealVisXL 4.0’s face-preserving upscaler to EXCAVA’s pipeline now.

**Plan:**
1. Integrate RealVisXL 4.0’s face-preserving upscaler into EXCAVA’s upscaling pipeline.
2. Conduct stress tests to validate facial fidelity retention under EXCAVA’s heaviest loads.
3. Measure performance impact (12% slowdown) and confirm quality gains (≥0.5% facial fidelity).
4. Document integration steps and trade-offs in EXCAVA’s technical wiki.
5. Assign EXCAVA lead to monitor Anthropic’s updates and report risks quarterly.
6. Prepare fallback plan (hybrid depth + face model) if lock-in risks materialize.

**What changed:**
RealVisXL 4.0 face-preserving upscaler replaces generic upscaler in EXCAVA’s pipeline.
