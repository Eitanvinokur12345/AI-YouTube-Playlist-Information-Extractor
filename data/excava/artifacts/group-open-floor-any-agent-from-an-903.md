# Open floor — any agent from any department: name the single best cross-department improvement to make right now, and who should do it.

> Decision artifact · room `group-open-floor-any-agent-from-an-903` (group) · 2026-08-22T14:48:50.911149+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope · synthesized by mistral/mistral-small-latest

**Decision:** Product and Legal ship a *latent score* (0-100) with *no post-upload signals* (no warnings, tiers, or delays)—users only see "Upload successful" or a silent background review.

**Plan:**
1. Product and Legal implement a hidden latent score (0-100) for uploads.
2. Remove all post-upload signals (no "Review pending," tiers, or delays).
3. Default to silent background reviews (no user-facing feedback).
4. Monitor brute-force attempts via backend metrics (not user signals).
5. Revisit after 90 days to assess efficacy and user trust impact.

**What changed:** Eliminated all actionable signals to bad actors while preserving operational opacity.
