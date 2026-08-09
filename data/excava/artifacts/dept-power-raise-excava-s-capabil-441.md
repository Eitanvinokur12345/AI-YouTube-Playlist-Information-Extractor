# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-441` (dept) · 2026-08-03T01:30:52.063079+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run a blind A/B test on 100 faces under three lighting conditions comparing InstantX-ComfyUI’s depth-aware upscaler vs SD3.5 Medium + RealVisXL LoRA.
2. If InstantX wins on clarity, swap it into EXCAVA’s pipeline.
3. If SD3.5 + RealVisXL wins, integrate the LoRA into EXCAVA’s pipeline.
4. Benchmark VRAM usage post-integration and optimize if needed.
5. Validate the 0.5%+ lift in usable output via automated quality scoring.
6. Merge the winning upscaler into EXCAVA’s main branch.

**What changed:** Added InstantX-ComfyUI’s depth-aware upscaler to EXCAVA’s pipeline if it passes the A/B test.
