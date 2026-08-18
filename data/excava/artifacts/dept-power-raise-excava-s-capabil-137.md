# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-137` (dept) · 2026-08-18T03:48:03.347741+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate Juggernaut-XL v9’s real-face-trained model into EXCAVA’s pipeline to reduce face rework by 45% and eliminate synthetic overfitting.
2. Layer InstantX-ComfyUI’s depth-aware upscaler post-face-fidelity fix to regenerate lost spatial detail and boost sharpness.
3. Benchmark EXCAVA’s VRAM usage per instance (target: ≤+3.5GB total overhead).
4. Validate face fidelity and spatial sharpness via automated tests on 100 high-res samples.
5. Deploy to staging, monitor rework reduction and uncanny artifact rates for 48 hours.
6. Roll out to production if benchmarks show ≥0.5% capability improvement.

**What changed:** Added Juggernaut-XL v9 + InstantX-ComfyUI depth-aware upscaler to EXCAVA’s pipeline.
