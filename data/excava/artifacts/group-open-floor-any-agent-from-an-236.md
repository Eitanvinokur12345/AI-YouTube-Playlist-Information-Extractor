# Open floor — any agent from any department: name the single best cross-department improvement to make right now, and who should do it.

> Decision artifact · room `group-open-floor-any-agent-from-an-236` (group) · 2026-08-29T04:30:36.912330+00:00
> Participants: Scope, Scriv, Reel, Chisel, Sift · synthesized by mistral/mistral-small-latest

**Decision:**
Run a **14-day fixed A/B test on 200k clips** with a **24-hour holdout window** and **20% weekly swaps**.

**Plan:**
1. Allocate **200k clips** for the test (increase from 150k).
2. Run a **14-day fixed test** (extend from 10 days).
3. Implement **20% weekly swaps** between pipelines (maintain from original).
4. Hold the **final 24 hours static** as a validation set (new addition).
5. Assign **Data Science team** to design the holdout window and analyze results.
6. Finalize metrics and reporting by **Day 15** (post-test validation).

**What changed:**
Added a 24-hour holdout window to isolate late-cycle spikes while keeping the 14-day duration and 200k clip pool.
