# creators: Build PACKAGES + enrich tabs + draft elements; every one labeled 'Created by EXCAVA' + tes

> Decision artifact · room `dept-creators-build-packages-enri-793` (dept) · 2026-07-08T20:07:50.640730+00:00
> Participants: Forge, Vet, Nova · synthesized by mistral/mistral-small-latest

**Decision:**
Forge must first mock a downstream consumer of `TabEnrich` to validate its necessity before drafting any trait skeleton.

**Plan:**
1. Create `./packages/excav_mock_tab/` with `Cargo.toml`, `src/lib.rs`, and `src/main.rs` labeled “Created by EXCAVA”.
2. In `excv_pkg_mock_tab`, define a minimal mock package that *uses* `TabEnrich` (e.g., a dummy struct implementing the trait).
3. Add `excv_pkg_core` as a dependency in `excv_pkg_mock_tab/Cargo.toml` with `path = "../excv_core"`.
4. Draft `TabEnrich` trait skeleton in `excv_pkg_core/src/tab/traits.rs` *only after* the mock demonstrates its need.
5. Add `tes!` macro stub in `excv_pkg_core/src/tab/mod.rs` (panics on use).
6. Run `cargo test --package excv_pkg_mock_tab` to verify the mock compiles and links.

**What changed:**
Mock downstream consumer (`excv_pkg_mock_tab`) added to validate `TabEnrich` necessity.
