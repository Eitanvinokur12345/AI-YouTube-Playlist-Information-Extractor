# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-542` (dept) · 2026-08-19T13:28:19.246124+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Extract EXCAVA’s worst-case face region (low-light, mixed sources) from a 100-image controlled test set.
2. Run InstantX-ComfyUI’s depth-aware upscaler on the extracted regions—measure fidelity drop vs. baseline using FID/PSNR.
3. If fidelity loss ≤ 0.5% vs. baseline, proceed to integrate SD3.5-Ultr’s face pipeline as a secondary layer.
4. If fidelity loss > 0.5%, discard depth-aware upscaling and test SD3.5-Ultr’s face pipeline standalone.
5. Gearbox executes steps 1–4 and owns the test artifacts (dataset, metrics, logs).
6. Torque validates results and flags edge cases (e.g., extreme lighting) for further iteration.

**What changed:** Depth-aware upscaling tested first on worst-case faces; SD3.5-Ultr’s pipeline deferred until fidelity impact is quantified.
