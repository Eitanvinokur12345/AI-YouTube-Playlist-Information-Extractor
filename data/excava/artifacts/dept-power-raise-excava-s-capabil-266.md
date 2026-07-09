# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-266` (dept) · 2026-07-09T15:05:11.740863+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
**Plan:**
1. Cross-validate `excava_current_logs.csv` against checksums (SHA-256) and parse via `csvcut -n` + `csvstat --freq` to detect anomalies.
2. Extract torque/power specs from `cat_352GC_2024.pdf`, `komatsu_PC350_2024.pdf`, and `volvo_EC350_2024.pdf` using `pdftotext`, then verify integrity with `pdfinfo` checksums.
3. Run unified torque-curve regression in `excava_sim.py` comparing EXCAVA’s logs against all three OEM datasets to identify ≥0.5% efficiency gaps.
4. Isolate top 3 model/tool combinations (e.g., hybrid drivetrain, upgraded hydraulic pump) from regression outliers.
5. Benchmark selected combinations in sandbox with controlled load tests (simulated 50/75/100% duty cycles).
6. Commit validated changes to `excava_power_profile.json` with before/after benchmarks.

**What changed:** Expanded OEM validation from single-source (Cat) to multi-vendor (Cat/Komatsu/Volvo) with integrity checks.
