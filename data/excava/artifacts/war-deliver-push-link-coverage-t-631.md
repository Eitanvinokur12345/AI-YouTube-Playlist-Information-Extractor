# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-631` (war) · 2026-07-09T14:52:57.726978+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Push link coverage toward 100% at +5%/day using `(untested / total) > 0.15` OR `reachability == false` with empirical justification from historical bus-task failure rates.

**Plan:**
1. Run `linkchecker --coverage --format=json --output=coverage_report.json` on `/src` to generate per-file counts (total links, untested links, reachability flags).
2. Filter files where `(untested / total) > 0.15` OR `reachability == false` to identify critical gaps.
3. Generate a machine-readable `coverage_report.json` with exact counts and threshold rationale.
4. Open a focused PR with the top 5% lowest-coverage files, labeled `+5%` diff.
5. Track PR merges against bus-task completion rates to validate the threshold.
6. Adjust the threshold dynamically if failure correlation deviates from historical data.

**What changed:**
Adopted `(untested / total) > 0.15` OR `reachability == false` with empirical justification from historical bus-task failure rates.
