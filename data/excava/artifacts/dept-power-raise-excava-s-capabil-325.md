# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-325` (dept) · 2026-08-25T17:08:40.189192+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Combine MPRNet blind-deblurring with InstantX-ComfyUI’s depth-aware upscaler and test RIFE v4.17 vs. VFI-Flow on target hardware.

**Plan:**
1. Integrate MPRNet blind-deblurring into EXCAVA’s preprocessing pipeline to sharpen inputs before upscaling.
2. Add InstantX-ComfyUI’s depth-aware upscaler to EXCAVA’s pipeline for static frame enhancement.
3. Implement RIFE v4.17 as the default temporal interpolation model in EXCAVA’s motion pipeline.
4. Parallelly test VFI-Flow against RIFE v4.17 on a 10-second clip using the slowest target hardware.
5. Benchmark both models for throughput (fps) and output quality (motion blur reduction).
6. Finalize the pipeline with the model that maintains ≥30fps on target hardware.

**What changed:**
MPRNet blind-deblurring added pre-upscaling; RIFE v4.17 replaces VFI-Flow pending hardware validation.
