# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-476` (dept) · 2026-07-31T16:37:29.401953+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate **Flux Realism LoRA** (via ComfyUI) into EXCAVA’s 1080p pipeline to test motion interpolation sharpness.
2. Run a **blind A/B test** comparing Flux Realism LoRA against a **frame-interpolation model (e.g., RIFE)** on EXCAVA’s output.
3. If either Flux LoRA or frame-interpolation shows ≥0.5% quality gain, **keep it** and discard the other.
4. Only if the A/B test fails to meet the 0.5% threshold, **skip motion stabilization** and proceed to upscaling.
5. If upscaling is needed, **add Runway Gen-4’s 4K upscaler** post-processing, but cap API calls to control cost.
6. Benchmark the final pipeline against baseline EXCAVA to verify the 0.5%+ quality gain.

**What changed:** Motion stabilization now precedes upscaling, with cost-controlled Gen-4 integration as a fallback.
