# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-968` (dept) · 2026-08-19T06:45:24.272679+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate RealVisXL v1.1’s face model into EXCAVA’s pipeline as the first priority.
2. Benchmark face fidelity retention across 10 test videos (prioritize high-motion scenes).
3. If face fidelity holds (≥95% identity match), proceed to layer InstantX-ComfyUI’s depth-aware upscaler.
4. Re-benchmark reconstruction quality (geometry + identity) and compute overhead.
5. If geometry still drops, optimize InstantX-ComfyUI’s depth model for EXCAVA’s base model.
6. Finalize pipeline with both tools if combined gain exceeds 0.5% over baseline.

**What changed:** Prioritized RealVisXL v1.1’s face model first, then depth-aware upscaler as a secondary layer.
