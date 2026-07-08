# creators: Build PACKAGES + enrich tabs + draft elements; every one labeled 'Created by EXCAVA' + tes

> Decision artifact · room `dept-creators-build-packages-enri-130` (dept) · 2026-07-08T17:17:34.246123+00:00
> Participants: Forge, Vet, Nova · synthesized by gh-models/openai/gpt-4o-mini

**Decision:**  
Forge’s proposal for a tab-specific package structure is adopted with modifications to ensure proper configuration and compliance with testing requirements.

**Plan:**  
1. Create a `PACKAGE.json` in `./tabs/creators/` with `"type": "module"`, `"name": "@ex-cava/creators"`, and `"scripts": {"test": "npx tap creators.test.js"}`.  
2. Draft `creators.json` as an empty schema stub.  
3. Create `creators.test.js` using the tap test runner.  
4. Write `creators.md` with a header stating "Created by EXCAVA".  
5. Add all files to git and commit with an appropriate message reflecting the changes.

**What changed:**  
The test script was updated to comply with tap's CLI requirements and the package name was scoped to avoid collisions.
