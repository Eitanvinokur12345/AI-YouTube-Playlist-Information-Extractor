# visualization: Own the visibility AND ACCESSIBILITY of the whole interface — liveliness, info access, enj

> Decision artifact · room `dept-visualization-own-the-visibi-445` (dept) · 2026-07-10T07:23:18.106012+00:00
> Participants: Facet, Pane, Lumen · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Pin Lighthouse to a team-agreed patch version in `package.json` and verify it’s listed in `devDependencies` before running audits.

**Plan:**
1. Verify Lighthouse's presence and version in the project's toolchain by checking `package.json` and `node_modules`.
2. If missing, install a specific patch version of Lighthouse as a dev dependency with `npm install --save-dev lighthouse@<exact>`.
3. Ensure Lighthouse is listed in the `devDependencies` section of `package.json`.
4. Run audits using the pinned version of Lighthouse.
5. Document the exact Lighthouse version used in the project's documentation for future reference.
6. Create a pull request that includes the updated `package.json` and any relevant audit results.

**What changed:** A decision was made to pin Lighthouse to a specific version to prevent silent breakage risks.
