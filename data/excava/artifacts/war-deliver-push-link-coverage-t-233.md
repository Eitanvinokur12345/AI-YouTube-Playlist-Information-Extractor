# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-233` (war) · 2026-08-15T06:21:20.077181+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Run a 24-hour full batch with kimtaeyoon83/mcp-server-youtube-transcript, then manually verify every transcript flagged by eA9Zf’s confidence scores.
1. **Run the kimtaeyoon83/mcp-server-youtube-transcript tool** on all pending videos to auto-generate transcripts.
2. **Feed the auto-generated transcripts into eA9Zf** to extract the top 3 contradictions and confidence scores.
3. **Manually verify every transcript flagged by eA9Zf’s confidence scores** to ensure quality and accuracy.
4. **Use the verified transcripts for contradiction extraction** to push link coverage toward 100% at +5%/day.
5. **Review and refine the process** based on the results of the 24-hour full batch.
**What changed:** The approach shifted from a 10% sample test to a full batch with targeted manual verification to balance speed and quality.
