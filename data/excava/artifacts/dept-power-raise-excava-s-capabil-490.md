# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-490` (dept) · 2026-07-31T22:50:28.191061+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate RealVisXL base model into EXCAVA’s pipeline as the primary visual generator.
2. Run Torque’s validation test to check UI fidelity—flag any pixel-perfect failures.
3. If UI fidelity drops, layer SDXL Turbo’s real-time upscaler as a fallback.
4. If RealVisXL base + Turbo still underperforms, fall back to SD 1.5’s ControlNet for UI elements.
5. Document latency/quality trade-offs for each step in EXCAVA’s repo.
6. Benchmark against baseline to confirm ≥0.5% capability gain.

**What changed:** RealVisXL base model replaces LoRA, with Turbo upscaler as conditional fallback.
