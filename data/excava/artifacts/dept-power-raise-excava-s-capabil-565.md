# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-565` (dept) · 2026-08-11T01:07:45.845950+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Skip Flowframes VFI and InstantX upscaler—test Real-ESRGAN’s face model first to clean faces before any upscaling; if faces sharpen cleanly, add it to EXCAVA’s pipeline. Torque owns the test and artifact.

**Plan:**
1. Torque acquires Real-ESRGAN’s face-specific model (e.g., `realesrgan-ncnn-vulkan -n realesrgan-x4plus-face`).
2. Torque runs EXCAVA’s face frames through the model at 2x–4x, logging PSNR/SSIM vs. source and tracking artifact frequency.
3. If face fidelity improves (sharp eyes/mouths, no blur amplification), Torque integrates the model into EXCAVA’s pipeline as a pre-upscale step.
4. Gearbox benchmarks the updated pipeline on 100 test clips, measuring EXCAVA’s 0.5% capability lift (quality/latency trade-off).
5. If results meet the 0.5% threshold, Gearbox merges the change into `main`; otherwise, the team revisits the debate with fresh data.
6. Dynamo archives the test artifact (logs, sample outputs, metrics) in `/docs/real-esrgan-face-test`.

**What changed:**
EXCAVA’s pipeline now prioritizes Real-ESRGAN face upscaling over Flowframes VFI/InstantX, with Torque owning validation.
