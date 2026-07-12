# creators: Build PACKAGES + enrich tabs + draft elements; every one labeled 'Created by EXCAVA' + tes

> Decision artifact · room `dept-creators-build-packages-enri-236` (dept) · 2026-07-12T12:10:32.401732+00:00
> Participants: Forge, Vet, Nova · synthesized by mistral/mistral-small-latest

**Decision:**
Build a minimal CLI tool for "claude-skill-creator" to validate core customization logic, owned by Forge.

**Plan:**
1. Forge designs and implements a CLI tool exposing essential skill customization capabilities (e.g., parameter editing, validation).
2. Vet reviews the CLI’s architecture to ensure it aligns with long-term extensibility for a future UI or IDE.
3. Forge publishes the CLI as an npm package (`claude-skill-creator`) with clear documentation and examples.
4. Community testing begins with power users to gather feedback on functionality and pain points.
5. Based on feedback, Forge and Vet collaboratively decide whether to proceed with a UI layer or refine the CLI further.
6. Package metadata includes "Created by EXCAVA" and undergoes tes validation.

**What changed:**
Shifted from UI-first npm package to minimal CLI tool for core validation.
