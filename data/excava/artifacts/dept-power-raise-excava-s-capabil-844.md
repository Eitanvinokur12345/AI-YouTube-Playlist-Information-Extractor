# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-844` (dept) · 2026-08-12T21:23:03.865452+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Integrate RealVisXL's previous stable face model into EXCAVA's pipeline if it outperforms InstantX's depth upscaler for face fidelity.
**Plan:**
1. Test RealVisXL's previous stable face model on face crops to evaluate its face fidelity performance.
2. Compare the results with InstantX-ComfyUI's depth-aware upscaler to determine which one performs better for face detail enhancement.
3. If RealVisXL's previous stable face model outperforms InstantX, integrate it into EXCAVA's pipeline.
4. Monitor pipeline stability and performance after integration.
5. Consider adding InstantX-ComfyUI's depth-aware upscaler to EXCAVA's pipeline if it is found to be complementary to RealVisXL's face model.
**What changed:** The approach now prioritizes testing and integrating a stable face model to specifically address face fidelity drop in EXCAVA's output.
