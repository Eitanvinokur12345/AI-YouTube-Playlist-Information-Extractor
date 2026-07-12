# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-619` (war) · 2026-07-12T12:36:08.653364+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:** Run a daily automated scan of all links, rank by real-time traffic impact, and auto-flag only those breaking user flows—manual audits are dropped.

**Plan:**
1. Build a daily script to scan all links, using real-time traffic data to rank impact.
2. Auto-flag only links breaking user flows (e.g., 404s, redirects to irrelevant pages).
3. Log flagged links in a shared sheet with traffic impact and fix priority.
4. Auto-close false positives (e.g., harmless redirects) via a whitelist.
5. Deploy the system in staging, then roll out to production with monitoring.
6. Set up alerts for new high-traffic links missed by the daily scan (edge-case fallback).

**What changed:** Manual audits dropped; daily automation replaces them.
