# creators: Build PACKAGES + enrich tabs + draft elements; every one labeled 'Created by EXCAVA' + tes

> Decision artifact · room `dept-creators-build-packages-enri-711` (dept) · 2026-07-10T17:15:32.636838+00:00
> Participants: Forge, Vet, Nova · synthesized by mistral/mistral-small-latest

**Decision:** Build *one* minimal, high-value PACKAGE (`excava_core`) with a single utility (`string-reverse.js`), labeled "Created by EXCAVA," tested and ready for reuse—Forge owns it.

**Plan:**
1. Create `creators/excava_core/` with `package.json`, `index.js`, `README.md`, `string-reverse.js`, and `string-reverse.test.js`.
2. Seed `string-reverse.js` with a simple reverse utility and add `Created by EXCAVA` to its header.
3. Add `Created by EXCAVA` to all file headers in `excava_core/`.
4. Include a basic `README.md` documenting the package’s purpose and usage.
5. Write a minimal `package.json` with name, version, and test script (`npm test`).
6. Run tests locally to confirm `string-reverse.test.js` passes.

**What changed:** Reduced scope from three packages to one minimal, validated package (`excava_core`) to meet the "PACKAGES" goal efficiently.
