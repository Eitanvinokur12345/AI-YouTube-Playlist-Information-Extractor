# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-646` (dept) · 2026-07-27T22:32:01.229970+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Fork selectively to balance control and maintenance.

**Plan:**
1. Audit the Claude Self-Improvement Skill Pack and cherry-pick only the prompt templates and routing logic we actively use.
2. Rename the forked components to avoid upstream confusion (e.g., `claude-skill-pack-*` → `ratchet-skill-*`).
3. Patch each cherry-picked component in-place with clear documentation of the change’s purpose and rationale.
4. Prove the forked elements work in our workflow before considering upstream merges.
5. Set up a lightweight process to periodically review upstream changes and selectively backport critical fixes.
6. Deprecate unused components from the original pack to avoid dead weight.

**What changed:** Selective cherry-picking of prompts/routing with explicit patch documentation.
