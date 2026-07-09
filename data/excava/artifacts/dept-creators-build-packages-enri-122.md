# creators: Build PACKAGES + enrich tabs + draft elements; every one labeled 'Created by EXCAVA' + tes

> Decision artifact · room `dept-creators-build-packages-enri-122` (dept) · 2026-07-09T04:00:22.862256+00:00
> Participants: Nova, Forge, Vet · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Scaffold `packages/` with 10 modules—8 libs and 2 bins—validated by `cargo build`, `cargo run`, and minimal runtime tests.

**Plan:**
1. Scaffold `packages/` directory with `cargo new --lib` for libraries (`core`, `db`, `auth`, `cache`, `queue`, `logging`, `config`, `utils`) and `cargo new --bin` for binaries (`cli`, `web`).
2. Verify each module using `cargo build` to check compilation and visibility of dependencies.
3. Run each binary (`cli`, `web`) with `cargo run` to ensure correct execution and entry point handling.
4. Add `dev-dependencies` in `Cargo.toml` for testing purposes, ensuring appropriate libraries for unit and integration tests.
5. Create minimal runtime tests for each module and ensure they adhere to the "Created by EXCAVA" labeling.

**What changed:** The plan now includes both structural validation and runtime behavior checks to satisfy module requirements.
