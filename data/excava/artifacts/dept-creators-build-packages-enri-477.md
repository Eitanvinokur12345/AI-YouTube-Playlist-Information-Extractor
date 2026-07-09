# creators: Build PACKAGES + enrich tabs + draft elements; every one labeled 'Created by EXCAVA' + tes

> Decision artifact · room `dept-creators-build-packages-enri-477` (dept) · 2026-07-09T14:41:40.455868+00:00
> Participants: Forge, Vet, Nova · synthesized by mistral/mistral-small-latest

**Decision:**
Vet blocks `excava-core/v0.1.0` until Forge submits a design doc + CI proof + signed-off API contract.

**Plan:**
1. Forge drafts `design.md` outlining scope, API contract, and failure modes for `excava-core`.
2. Forge implements `Cargo.toml` (v0.1.0), `lib.rs` (`dummy()` stub), and `tests/dummy_test.rs` with `// Created by EXCAVA` headers.
3. Forge submits PR with artifact for team review and API contract sign-off.
4. Forge sets up CI (e.g., GitHub Actions) and provides log proving `cargo test` passes.
5. Team approves design doc, API contract, and CI proof before tagging `v0.1.0`.
6. Forge tags `excava-core/v0.1.0` post-approval.

**What changed:**
Forge must now align `excava-core` with team consensus before tagging.
