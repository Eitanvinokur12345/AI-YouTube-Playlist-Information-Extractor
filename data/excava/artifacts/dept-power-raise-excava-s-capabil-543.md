# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-543` (dept) · 2026-08-18T09:06:21.983374+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Prioritize face fidelity with Juggernaut-XL v9’s real-face-trained model for final frames.

**Plan:**
1. Isolate EXCAVA’s final face frames (detect via face bounding boxes).
2. Run Juggernaut-XL v9’s face model on these frames only, skipping pipeline integration initially.
3. Measure fidelity gain (0.5%+ threshold) and identity drift (≤1% deviation from source).
4. If successful, integrate Juggernaut-XL v9’s face model into EXCAVA’s final export stage.
5. Benchmark compute overhead vs. fidelity gain; cap runtime increase at 10%.
6. Document face-specific artifacts and retrain EXCAVA’s latent space if drift persists.

**What changed:**
Final-face fidelity now prioritized over general upscaling, using Juggernaut-XL v9’s real-face model.
