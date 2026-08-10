# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-114` (war) · 2026-08-10T13:59:22.029427+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run `kimtaeyoon83/mcp-server-youtube-transcript` on all pending videos immediately to maximize coverage gains.
2. Manually verify each transcript for timestamp accuracy and completeness.
3. Add missing timestamps or metadata where required to ensure structured links.
4. Upload the verified transcripts to the access gate repository.
5. Track daily coverage progress toward +5%/day and adjust if needed.
6. Document any failures or edge cases for future automation improvements.

**What changed:** Prioritized raw transcript scraping with manual cleanup over Luma’s built-in tool due to scalability and reliability risks.
