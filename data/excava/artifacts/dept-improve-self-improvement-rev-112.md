# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-112` (dept) · 2026-07-31T13:07:55.233620+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Reject auto-applying whitespace patches to third-party dependencies and instead run Pret in CI as a linter to flag issues for human approval.
**Plan:**
1. Implement Pret as a linter in the CI pipeline to flag whitespace issues in third-party dependencies.
2. Update the CI configuration to block merges with Pret-flagged whitespace issues.
3. Assign Gauge as the owner to implement the linter and Sprocket as the owner to update the CI configuration.
4. Review and test the new CI pipeline to ensure it correctly flags and blocks whitespace issues.
5. Document the new process for handling whitespace issues in third-party dependencies.
**What changed:** CI pipeline now blocks merges with Pret-flagged whitespace issues, requiring human approval for safe changes.
