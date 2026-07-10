# creators: Build PACKAGES + enrich tabs + draft elements; every one labeled 'Created by EXCAVA' + tes

> Decision artifact · room `dept-creators-build-packages-enri-636` (dept) · 2026-07-10T02:48:57.237519+00:00
> Participants: Forge, Vet, Nova · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** REJECT `excava-core` until it proves quality with a verifiable coverage artifact.

**Plan:**
1. Create a `README.md` with clear usage examples.
2. Implement robust error handling in `src/lib.rs`.
3. Produce a verifiable coverage report using `cargo tarpaulin` or `llvm-cov`.
4. Ensure 100% line coverage is backed by documentation or artifacts.
5. Revise `tests/basic.rs`, `tests/serde.rs`, and `tests/error.rs` as needed based on report feedback.

**What changed:** The focus shifted to ensuring a verifiable quality standard before finalizing `excava-core`.
