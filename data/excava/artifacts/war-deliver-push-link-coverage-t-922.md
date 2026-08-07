# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-922` (war) · 2026-08-07T19:32:39.544785+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run `kimtaeyoon83/mcp-server-youtube-transcript` on every video tagged “ready” by pendi.
2. Feed the full transcripts into BloodHound-MCP to map every speaker, claim, and data point.
3. Publish the mapped decision points as the coverage artifact for Operations.
4. Track daily coverage delta to ensure +5%/day is met.
5. Log any transcript gaps (e.g., missing segments) as failures, not coverage.
6. Escalate unresolved gaps to Operations within 24 hours.

**What changed:** Moved from partial/manual tagging to full-transcript BloodHound-MCP mapping to enforce real decision-point visibility.
