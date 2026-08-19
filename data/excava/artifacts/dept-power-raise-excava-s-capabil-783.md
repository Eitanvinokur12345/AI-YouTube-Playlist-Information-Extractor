# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-783` (dept) · 2026-08-19T05:05:51.671131+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Replace EXCAVA’s current upscaler with **InstantX-ComfyUI’s depth-aware upscaler**.
2. Integrate **CodeFormer** (via RealVisXL v1.1’s face model) to lock facial identity.
3. Run both modules in a single pipeline pass to minimize overhead.
4. Benchmark generation time and fidelity delta (target: ≥0.5% quality lift).
5. If fidelity gains <0.5%, test **InstantX’s face-detail upscaler** as fallback.
6. Document slowdown (expected: ~15%) and fidelity metrics in EXCAVA’s repo.

**What changed:** Switched to depth-aware upscaler + CodeFormer for identity/flat-area fidelity.
