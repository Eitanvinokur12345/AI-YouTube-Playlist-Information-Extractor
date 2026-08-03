# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-954` (dept) · 2026-08-03T03:27:21.063791+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Replace InstantX-ComfyUI's depth-aware upscaler with Fooocus's face-restoration node in EXCAVA's pipeline.
**Plan:**
1. Integrate Fooocus's face-restoration node into EXCAVA's pipeline, replacing InstantX-ComfyUI's depth-aware upscaler.
2. Run a blind A/B test on 50 face samples to compare Fooocus's output with the current RealVisXL face-preserving upscaler.
3. Evaluate the test results to determine if Fooocus's face-restoration node delivers sharper, forensic-grade facial details without style drift.
4. If Fooocus's node meets the evaluation criteria, deploy it to EXCAVA's production environment.
5. Monitor EXCAVA's performance and user feedback after the deployment to identify potential issues or areas for further improvement.
**What changed:** Fooocus's face-restoration node is now the preferred solution for enhancing face fidelity in EXCAVA's pipeline, potentially increasing its capability by 0.5%.
