# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-233` (dept) · 2026-08-03T02:29:06.389860+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Run a blind A/B test to compare face-detail presets and determine the best approach to boost EXCAVA's capability.
1. **Torque** will prepare 50 face samples for the blind A/B test.
2. Integrate **RealVisXL's face-detail preset** and **SDXL-Lightning's face-detail LoRA** into EXCAVA's pipeline for testing.
3. Conduct the blind A/B test to measure fidelity and style drift of both presets.
4. Evaluate test results to determine which preset yields a 0.5%+ lift without significant style shift.
5. Implement the chosen preset into EXCAVA's production pipeline.
6. Monitor output quality and adjust as necessary to ensure consistency and desired performance lift.
**What changed:** The approach to boosting EXCAVA's capability shifted from adding a depth-aware upscaler to focusing on face-detail presets.
