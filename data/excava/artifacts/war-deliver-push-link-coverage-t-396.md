# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-396` (war) · 2026-07-22T14:36:24.087340+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:** Publish the signed append-only log to Arweave first, then replicate to GitHub after 24 hours.

**Plan:**
1. Generate and sign the append-only log using a dedicated key pair.
2. Publish the signed log to Arweave immediately for tamper-proof anchoring.
3. Monitor for key compromise for 24 hours before any further action.
4. If no compromise is detected, replicate the log to a public GitHub repository.
5. Maintain a changelog of all public postings for transparency.
6. Security Ops retains exclusive control over key management and replication timing.

**What changed:** GitHub replication delayed to 24 hours post-Arweave anchoring to mitigate key-compromise risk.
