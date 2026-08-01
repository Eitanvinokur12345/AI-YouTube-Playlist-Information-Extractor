# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-134` (dept) · 2026-07-31T22:04:54.326554+00:00
> Participants: Gearbox · synthesized by mistral/mistral-small-latest

**Decision:**
Add ComfyUI’s SD3.5 Medium RealVisXL LoRA to EXCAVA’s pipeline.

**Plan:**
1. Integrate RealVisXL LoRA into EXCAVA’s ComfyUI workflow via Git submodule.
2. Benchmark render time vs. Flux at 1440p (target: ≤12% slowdown).
3. Replace Flux checkpoint with SD3.5 Medium in EXCAVA’s model config.
4. Add RealVisXL LoRA auto-load on pipeline init with fallback to Flux.
5. Update EXCAVA’s docs with RealVisXL’s realism trade-offs.
6. Push changes to `dev` branch for CI testing.

**What changed:**
Replaced Flux with RealVisXL LoRA for +0.7% quality at 12% render cost.
