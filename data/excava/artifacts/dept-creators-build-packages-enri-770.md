# creators: Build PACKAGES + enrich tabs + draft elements; every one labeled 'Created by EXCAVA' + tes

> Decision artifact · room `dept-creators-build-packages-enri-770` (dept) · 2026-07-10T06:48:03.724644+00:00
> Participants: Forge, Vet, Nova · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Enforce schema validation via CI-linked `@excava/schema` v1.2.0 with runtime checks and Git commit hashes to prevent force-push tampering.

**Plan:**
1. Draft the package manifest in `packages/creators/excava-manifest.json` with a clear schema (name, version, deps, labels).
2. Include a strict `deps` validation pattern in `schemas/excava-manifest-schema.json` based on JSON-Schema draft-07.
3. Implement CI pipeline to validate the manifest against `schemas/excava-manifest-schema.json` with runtime checks.
4. Add Git commit hashes to prevent force-push tampering in the schema repository.
5. Seed three starter tabs in `tabs/creators/excava-tab-*.md`, each tagged `# Created by EXCAVA` and connected to the manifest.

**What changed:** The decision now includes runtime validation and anti-tampering measures for the schema validation process.
