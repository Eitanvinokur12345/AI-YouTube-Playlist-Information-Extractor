# creators: Build PACKAGES + enrich tabs + draft elements; every one labeled 'Created by EXCAVA' + tes

> Decision artifact · room `dept-creators-build-packages-enri-791` (dept) · 2026-07-28T17:39:05.127023+00:00
> Participants: Forge, Nova · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Forge publishes the UGC Factory npm package with a `package.json` including `name`, `version`, `description`, and `author: "EXCAVA"`.
2. Forge adds a `README.md` with clear usage instructions and a header: "Created by EXCAVA".
3. All generated artifacts (e.g., templates, scripts) include a comment/header: "Created by EXCAVA".
4. Forge runs `npm publish` and tags the release with `v1.0.0` (or next minor version).
5. Nova verifies the package is public and artifacts are labeled correctly.
6. Forge shares the published package link in the team channel.

**What changed:** UGC Factory npm package is now live with EXCAVA branding and usage docs.
