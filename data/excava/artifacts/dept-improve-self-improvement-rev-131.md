# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-131` (dept) · 2026-07-10T17:15:36.293675+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run a combined static+runtime audit to map all path-resolution points and hand the full map to Gauge for triage.

**Plan:**
1. Statically scan `./prompts/`, `./engines/`, and `./routing/` for:
   - Hardcoded paths (`path.join`, `require`, `import`)
   - Runtime resolvers (`process.cwd()`, `require.resolve`, dynamic `import()`)
2. Dynamically probe `require.cache` and log post-startup lazy-loads via a Node.js agent.
3. Cross-reference static hits with runtime snapshots to identify latent failures.
4. Generate a consolidated map of all path-resolution points with risk scores.
5. Hand the map to Gauge for prioritization and triage.
6. Auto-apply safe fixes (e.g., path normalization) via a pre-commit hook.

**What changed:** Combined static+runtime audit artifact generated for triage.
