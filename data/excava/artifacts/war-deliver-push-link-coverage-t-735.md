# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-735` (war) · 2026-07-22T11:39:30.162652+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Publish the signed append-only log to both Arweave and GitHub Releases immediately.
2. Implement a 48-hour automated hash comparison test using public verification endpoints for both sources.
3. Verify identical hashes from both Arweave and GitHub Releases within the 48-hour window.
4. If hashes match, confirm log integrity and proceed with full deployment.
5. If hashes diverge, halt publishing, investigate discrepancies, and resolve before resuming.
6. Document the process and results for auditability.

**What changed:** Dual-publishing now with automated hash verification to ensure redundancy and integrity.
