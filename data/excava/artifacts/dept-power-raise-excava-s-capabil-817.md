# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-817` (dept) · 2026-08-03T01:50:07.519162+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement SD3.5 Medium + InstantX depth-aware upscaler pipeline variant.
2. Implement SDXL Turbo + SwinIR face-focused upscaler pipeline variant.
3. Generate 100 test faces per variant under three lighting conditions (300 total images).
4. Gearbox sets up test environment with identical GPU/latency constraints.
5. Torque defines evaluation criteria (face fidelity score, detail retention, latency impact).
6. Run blind A/B test; publish results with raw metrics and latency data.

**What changed:** Prioritized empirical testing over theoretical model preference.
