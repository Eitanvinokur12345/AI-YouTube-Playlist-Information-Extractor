# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-186` (dept) · 2026-08-10T20:01:02.088458+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate Flowframes’ FILM motion-compensated temporal upscaler into EXCAVA’s pipeline to reduce motion blur in source frames.
2. Benchmark FILM’s impact on motion artifact reduction and VRAM/performance overhead.
3. If motion blur persists post-FILM, test InstantX-ComfyUI’s depth-aware upscaler for fine detail preservation.
4. If faces remain the bottleneck after FILM, integrate RealVisXL 5.0’s face lock for targeted facial fidelity.
5. Optimize VRAM usage by adjusting FILM/InstantX parameters or splitting processing across frames.
6. Finalize pipeline with the most effective combination of tools based on empirical results.

**What changed:** Prioritized motion blur reduction via FILM before upscaling/face locking.
