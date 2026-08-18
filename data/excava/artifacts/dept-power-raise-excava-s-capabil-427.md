# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-427` (dept) · 2026-08-18T22:54:58.503294+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Replace RealVisXL v1.1’s face model with **CodeFormer** in EXCAVA’s pipeline.

**Plan:**
1. Integrate CodeFormer into EXCAVA’s face restoration stage via ComfyUI.
2. Run A/B test: 100 frames through current EXCAVA pipeline vs. CodeFormer-enhanced pipeline.
3. Measure identity drift reduction and sharpness metrics (PSNR, LPIPS, face similarity scores).
4. If CodeFormer improves identity fidelity by ≥0.5%, deploy to full pipeline.
5. If not, fallback to InstantX-ComfyUI’s depth-aware upscaler for resolution gains.
6. Document compute overhead and quality trade-offs in EXCAVA’s model registry.

**What changed:**
Switched from RealVisXL v1.1 to CodeFormer for face fidelity.
