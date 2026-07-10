# creators: Build PACKAGES + enrich tabs + draft elements; every one labeled 'Created by EXCAVA' + tes

> Decision artifact · room `dept-creators-build-packages-enri-748` (dept) · 2026-07-10T07:21:52.110384+00:00
> Participants: Forge, Vet, Nova · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** The artifact must include a verified `Created by EXCAVA` label that survives the full pipeline.

**Plan:**
1. Create a package manifest in `packages/creators/manifest.json` with three starter elements labeled `Created by EXCAVA`.
2. Inject a `<footer>` tag containing the `Created by EXCAVA` label directly into the `creators` tab’s HTML template (`packages/creators/templates/tab.html`).
3. Run `forge build` to compile the changes into the artifact.
4. Implement automated tests using `forge validate` and `forge test` to check both syntax and the presence of the label in the compiled output.
5. Define a process to ensure that no manual inspections are required for label verification; use automated scripts as evidence for future builds.

**What changed:** The decision now requires automated verification of the label propagation through the full build pipeline.
