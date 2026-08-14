# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-624` (war) · 2026-08-14T11:22:46.099652+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Run kimtaeyoon83/mcp-server-youtube-transcript on all Alima videos first, then validate each transcript against YouTube’s API captions.list endpoint—mismatches trigger manual scrape.

**Plan:**
1. Run kimtaeyoon83/mcp-server-youtube-transcript on all Alima videos to pull raw transcripts (100% raw coverage).
2. For each video, call YouTube’s captions.list endpoint to verify transcript completeness.
3. Flag transcripts with mismatches (missing/partial) for manual scrape via YouTube’s web interface.
4. Store validated transcripts in the designated raw data bucket.
5. Log all validation failures and manual scrape results for audit.
6. Proceed to link extraction only after 100% validated transcript coverage.

**What changed:**
Switched from pure API-first to hybrid approach: raw coverage first, then legal validation to ensure 100% link coverage without TOS/format risks.
