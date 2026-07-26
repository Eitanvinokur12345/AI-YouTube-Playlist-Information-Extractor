# Open floor — any agent from any department: name the single best cross-department improvement to make right now, and who should do it.

> Decision artifact · room `group-open-floor-any-agent-from-an-688` (group) · 2026-07-26T00:57:07.596354+00:00
> Participants: Scriv, Reel, Chisel, Sift, Scope · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt joint Engineering and Data Protection approval of the automated risk scoring model’s logic before ingestion, with pre-approved thresholds for real-time overrides.

**Plan:**
1. **Joint Model Approval:** Engineering and Data Protection co-define the scoring model’s logic (e.g., decision trees, risk formulas) and publish it in plain language before any data ingestion.
2. **Pre-Approved Thresholds:** Set static, non-negotiable risk boundaries (e.g., "flag if risk > 0.8") for real-time scoring, eliminating black-box overrides.
3. **Override Mechanism:** Data Protection retains a mandatory toggle to halt ingestion if thresholds are breached, but only for flagged cases—not per-ingest negotiations.
4. **Public Documentation:** Maintain a living document of threshold choices and model logic, auditable by all teams.
5. **Liability Distribution:** Shared accountability—Engineering owns model accuracy, Data Protection owns threshold defensibility.
6. **Pilot Phase:** Test the plan for 30 days with a single high-risk data stream, then iterate.

**What changed:** Switched from dynamic overrides to pre-approved thresholds with joint model approval, balancing transparency, speed, and accountability.
