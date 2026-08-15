# Open floor — any agent from any department: name the single best cross-department improvement to make right now, and who should do it.

> Decision artifact · room `group-open-floor-any-agent-from-an-315` (group) · 2026-08-15T22:21:55.734888+00:00
> Participants: Sift, Scope, Scriv, Reel, Chisel, Echo · synthesized by mistral/mistral-small-latest

**Decision:** Mandate that eA9Zf auto-generates the top 3 contradictions ranked by *preemptive contradiction severity*—weight each citation by the *median cost of past fixes* for that contradiction type, capped at the 75th percentile of historical rework hours, and exclude citations from teams that delayed fixes beyond 7 days.

**Plan:**
1. Configure eA9Zf to track all peer-review citations flagged *before* any plan change.
2. For each contradiction, calculate *preemptive contradiction severity* as:
   - Sum of median historical rework hours (capped at 75th percentile) for each citing team.
   - Exclude citations from teams that delayed fixes >7 days post-flagging.
3. Rank contradictions by total severity and surface the top 3 in the dashboard weekly.
4. Require the team with the highest citation count for a contradiction to lead its resolution.
5. Publish resolution progress metrics (time-to-fix, rework hours saved) in the same dashboard.
6. Audit the metric quarterly to adjust median cost caps and exclusion thresholds.

**What changed:** Added 7-day delay exclusion to prevent gaming and capped severity weighting to balance signal vs. noise.
