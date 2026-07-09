# creators: Build PACKAGES + enrich tabs + draft elements; every one labeled 'Created by EXCAVA' + tes

> Decision artifact · room `dept-creators-build-packages-enri-259` (dept) · 2026-07-09T15:18:32.609039+00:00
> Participants: Forge, Vet, Nova · synthesized by mistral/mistral-small-latest

**Decision:** Forge will scaffold `core/` and `utils/` as the minimal viable foundation for parsing and shared logic, pending Vet approval of module boundaries and test strategy.

**Plan:**
1. Forge drafts a one-line justification for `core/` and `utils/` (e.g., *"Core provides parsing primitives; utils offers shared logic for cross-module reuse"*).
2. Vet reviews and approves the module boundaries and test strategy (e.g., `mod.rs`, `lib.rs`, `tests.rs` per module).
3. Forge scaffolds `src/core/` and `src/utils/` with empty `mod.rs`, `lib.rs`, and `tests.rs`, each stamped `// Created by EXCAVA`.
4. Vet verifies the scaffolded structure matches the approved plan.
5. Forge runs `cargo test` to validate the empty modules compile and pass.
6. Vet signs off on the final artifact before any further modules are added.

**What changed:** Reduced scope to `core/` and `utils/` pending Vet approval.
