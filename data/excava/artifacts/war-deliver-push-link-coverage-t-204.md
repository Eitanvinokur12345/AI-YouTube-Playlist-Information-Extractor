# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-204` (war) · 2026-08-22T14:42:24.220366+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Fetch the YouTube page raw for `e2Z5eBVDrKM`, then use YouTube’s API to pull the full description and transcript in one call.

**Plan:**
1. Fetch the raw YouTube page HTML for `e2Z5eBVDrKM`.
2. Use YouTube’s API to extract the full video description and transcript in a single call.
3. Parse both sources to extract all links (transcript + description).
4. Deduplicate and verify links against the video’s content.
5. Log cleanup time and link yield for comparison.
6. Commit verified links to the coverage tracker.

**What changed:** Prioritized YouTube API + raw HTML over kimtaeyoon83/mcp-tool to avoid missing description links.
