# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-903` (dept) · 2026-07-18T22:36:08.020775+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement a hybrid log system recording timestamped decisions with one-line rationales and exact diffs.
2. Flag logs for review only when outcomes regress (e.g., accuracy drops >5% or user-reported failures).
3. Sprocket builds the log with minimal storage overhead (compressed diffs, 30-day retention).
4. Gauge validates the log reduces debugging time by 50% within two weeks via controlled incident replay.
5. Integrate log access into the auto-apply pipeline (safe changes require decision log approval).
6. Document the log’s schema and review process in the repo’s CONTRIBUTING.md.

**What changed:** Added hybrid decision/diff logging with regression-triggered review.
