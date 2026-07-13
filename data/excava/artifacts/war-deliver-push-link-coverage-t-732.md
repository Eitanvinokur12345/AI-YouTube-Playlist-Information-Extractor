# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-732` (war) · 2026-07-13T09:38:53.241306+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:** Adopt a hybrid triage system—prioritize high-impact links by risk/urgency first, then rotate the rest in strict order to guarantee 100% coverage without gaming the metric.

**Plan:**
1. **Risk/Impact Scoring:** Assign each link a priority score (e.g., 1-5) based on potential impact/urgency (e.g., broken critical paths, security risks).
2. **Daily Priority Queue:** Process top 50% of high-scoring links first (adjust % based on velocity).
3. **Rotating Triage Queue:** Process remaining links in strict rotation, replacing failed links immediately with the next in queue.
4. **Quality Gate:** Flag any failed link for deeper analysis (e.g., manual review, root cause) and reject trivial fixes.
5. **Metrics Tracking:** Log coverage % daily, time-to-review for high-priority links, and fail rates.
6. **Retrospective:** Review queue efficiency weekly, adjusting priority thresholds or rotation speed.

**What changed:** Hybrid system replaces pure rotation with urgency-aware prioritization while keeping strict 100% coverage guarantee.
