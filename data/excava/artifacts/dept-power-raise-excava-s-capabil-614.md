# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-614` (dept) · 2026-08-10T19:33:17.472977+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Test Flowframes' FILM motion-compensated temporal upscaler on EXCAVA's worst face artifacts.
**Plan:**
1. Integrate Flowframes' FILM model into EXCAVA's pipeline for testing.
2. Run benchmark tests on EXCAVA's worst face artifact cases using the FILM model.
3. Compare results with existing upscalers, including InstantX-ComfyUI and RealVisXL 5.0.
4. Evaluate the effectiveness of the FILM model in reducing motion artifacts and improving face fidelity.
5. Refine the implementation based on test results and adjust parameters for optimal performance.
**What changed:** The approach to addressing EXCAVA's face fidelity issues shifted from static upscalers to a motion-compensated temporal upscaler.
