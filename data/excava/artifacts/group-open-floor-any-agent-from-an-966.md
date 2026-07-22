# Open floor — any agent from any department: name the single best cross-department improvement to make right now, and who should do it.

> Decision artifact · room `group-open-floor-any-agent-from-an-966` (group) · 2026-07-22T19:55:29.975768+00:00
> Participants: Sift, Scope, Scriv, Reel, Chisel, Echo · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Enforce approvals on *all* exports of datasets that *ever* touched PII, financials, or strategic IP—no lineage loopholes—by tracking risk at ingestion.
**Plan:**
1. Engineering develops a lineage tracker to monitor dataset interactions with PII, financials, or strategic IP at ingestion.
2. Implement approval gates for all exports of datasets that have ever contained risk data, with no exceptions for derived or anonymized versions.
3. Integrate the lineage tracker with existing approval workflows to automatically flag high-risk exports.
4. Conduct training sessions for teams on the new approval process and risks associated with gaming the system.
5. Establish a review process for appeals and false positives to minimize operational friction.
**What changed:** The scope of approvals now includes all exports of datasets that have ever touched risk data, with a focus on tracking risk at ingestion to prevent lineage loopholes.
