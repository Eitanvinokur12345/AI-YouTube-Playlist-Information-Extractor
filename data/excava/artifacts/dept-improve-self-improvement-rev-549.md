# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-549` (dept) · 2026-07-31T14:33:44.815803+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Reject auto-applying whitespace patches to third-party dependencies; run Pret only for manual review.

**Plan:**
1. Configure Pret to generate whitespace-only patches for third-party dependencies.
2. Store patches in a dedicated `whitespace-patches/` directory with metadata (file, diff, timestamp).
3. Trigger Pret manually via CI workflow (`pret-review.yml`) on dependency updates or weekly.
4. Enforce review via Gauge’s PR gate: patches must be approved before merging.
5. Log all reviewed patches in `whitespace-patches/REVIEWED.md` for auditability.
6. Exclude third-party files from auto-formatters (e.g., Prettier) to prevent conflicts.

**What changed:** Third-party deps no longer auto-receive whitespace patches; Pret runs only for manual inspection.
