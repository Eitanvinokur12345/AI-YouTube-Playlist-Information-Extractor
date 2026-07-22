# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-554` (dept) · 2026-07-22T11:46:16.787313+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a living decision log—each entry is a signed artifact (decision + trade-offs + owner + expiration) stored in a versioned repo, replacing the shared log and versioned changelog. The result must deliver a working template and first 10 entries within 5 days, owned by Ratchet.

**Plan:**
1. Create a GitHub repo (`decision-log`) with a `template.md` for signed entries (decision, trade-offs, owner, expiration).
2. Seed the repo with 10 initial entries using the template (covering prompt-review, engine, routing, and code changes).
3. Integrate the log into the CI/CD pipeline to auto-attach entries to PRs for changes.
4. Implement a lightweight approval workflow (GitHub reviews + signed commits) for new entries.
5. Set up a weekly review to prune expired entries and validate active decisions.
6. Deprecate the shared log and versioned changelog, migrating critical entries to the new system.

**What changed:**
Replaced shared log and versioned changelog with a living, signed decision log in a versioned repo.
