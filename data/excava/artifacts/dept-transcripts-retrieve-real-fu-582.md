# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-582` (dept) · 2026-07-20T20:11:11.216830+00:00
> Participants: Reel, Echo · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Run the YouTube transcript tool and verify transcript existence to retrieve real full transcripts for pending videos.
**Plan:**
1. Run the YouTube transcript tool on every video marked "pending" to pull full transcripts.
2. Verify the existence of fetched transcripts to ensure accuracy and completeness.
3. Check for any gaps in the record to identify potential missing transcripts.
4. Declaring a video's transcript as missing only after verification and gap checks.
5. Document verified transcripts for pending videos.
**What changed:** The approach now includes a verification step to confirm transcript existence and check for gaps.
