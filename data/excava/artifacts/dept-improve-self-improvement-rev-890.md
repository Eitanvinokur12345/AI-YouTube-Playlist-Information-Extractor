# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-890` (dept) · 2026-07-16T17:23:22.834167+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Run semantic-only scanning live for low latency, queue exact-string matches for offline batch processing to catch 100% of reworded prompts without SLA risk.
**Plan:**
1. Implement semantic-only scanning for live traffic to ensure low latency and meet SLAs.
2. Develop an offline batch processing system for exact-string matches to catch 100% of reworded prompts.
3. Integrate the offline batch processing system with the live semantic-only scanning system.
4. Monitor and evaluate the performance of the hybrid system to identify areas for further improvement.
5. Optimize the offline batch processing system to minimize compute costs and reduce processing time.
**What changed:** The approach now prioritizes low-latency semantic-only scanning for live traffic, with exact-string matching handled offline to ensure comprehensive coverage without risking SLA breaches.
