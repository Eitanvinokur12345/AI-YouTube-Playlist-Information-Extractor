# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-533` (dept) · 2026-07-31T11:35:39.744515+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Reject auto-applying whitespace patches to third-party dependencies.

**Plan:**
1. Add a CI check (e.g., `prettier --check`) to flag formatting drift in third-party dependencies.
2. Document the policy: auto-formatting only applies to our own codebase; third-party code must pass checks.
3. Fork critical dependencies once, apply formatting fixes, and pin the fork in the lockfile.
4. Update `CONTRIBUTING.md` to require CI checks for PRs touching third-party code.
5. Add a `format-third-party` script (optional) to assist manual fixes when drift is detected.

**What changed:** Added CI-driven formatting checks for third-party dependencies.
