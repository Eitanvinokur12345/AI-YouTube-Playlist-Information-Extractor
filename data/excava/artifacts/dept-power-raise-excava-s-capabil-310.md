# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-310` (dept) · 2026-08-03T06:26:37.800780+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Test Depth Anything V2’s face-region upscaler in EXCAVA’s pipeline first to improve face fidelity.
**Plan:**
1. Integrate Depth Anything V2's face-region upscaler into EXCAVA's pipeline for testing.
2. Torque will lead the testing and evaluation of the face-region upscaler's performance.
3. Measure face fidelity gains using predefined metrics and compare with current EXCAVA output.
4. If the test shows a measurable face fidelity gain, proceed to optimize the upscaler for seamless integration.
5. Monitor VRAM usage and adjust upscaling resolution as needed to maintain performance.
6. Document the test results, including any trade-offs or limitations, for future reference.
**What changed:** Face fidelity improvement approach shifted from InstantX-ComfyUI's depth-aware upscaler to Depth Anything V2's face-region upscaler to avoid Anthropic lock-in and better preserve micro-expressions.
