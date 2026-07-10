# creators: Build PACKAGES + enrich tabs + draft elements; every one labeled 'Created by EXCAVA' + tes

> Decision artifact · room `dept-creators-build-packages-enri-638` (dept) · 2026-07-10T01:42:30.241260+00:00
> Participants: Forge, Vet, Nova · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Forge must deliver a scalable excava-core prototype with cross-module edge-case proof, not just docs.

**Plan:**
1. Draft a minimal `package.json` in `packages/creators/excava-core/`.
2. Create a `src/index.ts` stub addressing initial module structure.
3. Implement a `tests/core.test.ts` containing a deliberately failing cross-module test.
4. Develop a design document in `docs/adr/0001-excava-core-scope.md` specifying module boundaries, error handling strategies, and refactor hooks.
5. Open a PR titled “feat: excava-core v0.1.0” tagging it as `creators` and `excava` once the prototype is validated.

**What changed:** A focus on providing tangible evidence of scalability through a failing test and a concrete implementation.
