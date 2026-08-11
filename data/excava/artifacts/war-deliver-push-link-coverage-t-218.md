# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-218` (war) · 2026-08-11T13:58:01.384715+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Run kimtaeyoon83/mcp-server-youtube-transcript on all 10 pending videos today, with Kaedim’s paid API as a fallback.

**Plan:**
1. Execute kimtaeyoon83/mcp-server-youtube-transcript on all 10 pending videos immediately.
2. Validate output JSON for timestamps, speaker IDs, and raw text integrity.
3. If any video fails or produces malformed JSON, switch to Kaedim’s paid API for that video.
4. Store all successful transcripts in the designated repo directory with versioned filenames.
5. Log failures and fallback actions in a `transcript_errors.log` for maintenance review.
6. Mark the access gate as complete upon 100% coverage.

**What changed:** Added fallback to Kaedim’s paid API for robustness.
