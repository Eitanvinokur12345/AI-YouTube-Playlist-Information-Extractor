# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-909` (war) · 2026-09-01T02:59:03.349994+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Run a 48-hour A/B test on 10k clips comparing write-through vs write-back version vectors, measuring both +5%/day link coverage and stale-read errors; Scriv owns the test and must deliver the artifact by EOD Friday.

**Plan:**
1. Split 10k clips evenly (5k each) into write-through and write-back cohorts.
2. Instrument both cohorts to log link coverage delta (+5%/day) and stale-read errors.
3. Deploy dual-log system with version vectors in both modes (write-through/write-back).
4. Freeze non-test changes for 48 hours to isolate metrics.
5. Scriv collects data and drafts a report with raw metrics and recommendations.
6. Present findings in a Friday EOD artifact (GitHub issue + metrics dump).

**What changed:**
Test replaces immediate adoption with empirical validation of trade-offs.
