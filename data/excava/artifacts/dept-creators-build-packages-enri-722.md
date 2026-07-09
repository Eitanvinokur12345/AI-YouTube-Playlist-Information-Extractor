# creators: Build PACKAGES + enrich tabs + draft elements; every one labeled 'Created by EXCAVA' + tes

> Decision artifact · room `dept-creators-build-packages-enri-722` (dept) · 2026-07-09T23:49:32.652680+00:00
> Participants: Forge, Vet, Nova · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Approve the creation of `excava-core` v0.1.0 with enforced "Created by EXCAVA" headers.

**Plan:**
1. Run `cargo new --lib packages/excava-core` to generate the basic package structure.
2. Immediately overwrite `src/lib.rs` and `tests/mod.rs` to include hard-coded headers with "Created by EXCAVA".
3. Create the `Cargo.toml` manifest and ensure it includes the necessary metadata.
4. Add a `tests/` directory for testing, initializing a `mod.rs` file with the "Created by EXCAVA" header.
5. Perform a full diff check of the generated structure to confirm there are no hidden inconsistencies.
6. Document the process and results to provide evidence of compliance with the attribution requirement.

**What changed:** The decision incorporates Vet's concerns by mandating a full tree diff verification to ensure consistent labeling.
