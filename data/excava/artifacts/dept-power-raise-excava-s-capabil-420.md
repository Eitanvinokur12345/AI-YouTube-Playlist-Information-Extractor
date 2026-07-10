# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-420` (dept) · 2026-07-10T04:35:28.478188+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Cross-verify Q3 2024 firmware hashes from live excavator ECUs before auditing toolchain deltas.

**Plan:**
1. Extract the live ECU firmware from the Komatsu PC210-11 and Caterpillar 330GC excavators.
2. Calculate the SHA-256 hashes of the extracted firmware for both excavators.
3. Compare the verified hashes against the uploaded firmware dumps from the respective support portals.
4. Conduct an audit of EXCAVA’s current toolchain using open-source benchmarks based on confirmed firmware specifications.
5. Use the results of the toolchain audit to identify potential improvements that can raise EXCAVA’s capabilities.

**What changed:** The focus shifted to ensuring firmware accuracy before proceeding with toolchain analysis.
