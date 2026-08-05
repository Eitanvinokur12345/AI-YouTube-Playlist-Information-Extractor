# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-934` (dept) · 2026-08-05T20:11:21.036183+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate RealVisXL 4.0 into EXCAVA’s pipeline for face fidelity testing.
2. Train and test SDXL-Lightning with a face-focused LoRA locally.
3. Benchmark both models for face blur reduction (target: ≥0.5%) and speed impact.
4. Compare results by EOD and select the better-performing option.
5. If neither meets the goal, revisit InstantX-ComfyUI’s depth-aware upscaler.
6. Document findings in EXCAVA’s model registry.

**What changed:** Added RealVisXL 4.0 and SDXL-Lightning+LoRA face-focused tests to EXCAVA’s pipeline.
