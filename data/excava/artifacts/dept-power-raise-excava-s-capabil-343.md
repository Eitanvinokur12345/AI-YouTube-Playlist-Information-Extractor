# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-343` (dept) · 2026-08-11T01:24:44.823055+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Torque tests DiffBIR’s video mode on a 10-frame burst for motion deblurring efficacy.
2. If DiffBIR improves face fidelity, Gearbox integrates it into EXCAVA’s pipeline.
3. If DiffBIR fails, Gearbox tests InstantX-ComfyUI’s depth-aware upscaler as fallback.
4. If depth-aware upscaling works, Gearbox implements it with depth map guidance.
5. If neither works, Gearbox tests Real-ESRGAN’s face model on post-processed frames.
6. Dynamo reviews results and adjusts pipeline based on Torque’s DiffBIR test.

**What changed:** Skipped Flowframes VFI and InstantX upscaler; prioritized DiffBIR deblurring first.
