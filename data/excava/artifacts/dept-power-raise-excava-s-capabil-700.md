# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-700` (dept) · 2026-08-07T21:13:34.399607+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Implement a hybrid approach to enhance EXCAVA's capability by addressing both depth and face fidelity issues.
1. **Test ComfyUI’s FaceDetailer node** with SD3.5’s face model on EXCAVA’s motion-blurred footage to evaluate face fidelity improvement.
2. **Integrate InstantX-ComfyUI’s depth-aware upscaler** into EXCAVA’s pipeline to preserve fine details in complex scenes.
3. **Assess the trade-off** of higher VRAM usage against the benefits of enhanced depth and face fidelity.
4. **Evaluate RealVisXL’s face-preserving upscaler** as a fallback option if FaceDetailer node does not yield desired results.
5. **Explore motion-deblurring models** as a potential long-term solution to address the root cause of motion blur in excavator footage.
**What changed:** The approach now combines testing FaceDetailer node and depth-aware upscaler to achieve a balanced improvement in EXCAVA's capability.
