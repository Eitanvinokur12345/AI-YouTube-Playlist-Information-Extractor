# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-825` (war) · 2026-07-25T09:24:25.322916+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Adopt dual thresholds—baseline for fast pass, tighter for auto-escalation—with Data reviewing exceptions only after ingestion, not before.  

**Plan:**  
1. Establish baseline thresholds for all data ingest sources to ensure consistency.  
2. Implement a secondary, tighter threshold for triggering auto-escalation on datasets that breach baseline scores.  
3. Create a clear process for Data team to review and document exceptions post-ingestion, rather than pre-approval.  
4. Monitor ingestion performance and risk exposure to adjust thresholds periodically based on historical data patterns.  
5. Train the Data team on the new dual-threshold process and the importance of timely adjustments to maintain ingestion speed.  

**What changed:** The decision allows for fast ingestion while ensuring high-risk datasets are monitored without significant delays.
