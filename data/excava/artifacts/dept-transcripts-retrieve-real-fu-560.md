# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-560` (dept) · 2026-07-30T22:27:53.292495+00:00
> Participants: Reel, Echo · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Use a third-party transcript tool to fetch full captions for pending videos.
**Plan:**
1. Identify the pending video "How AI is Changing Healthcare in 2024" from the channel "Tech Insights" and another video "How to Build a Resilient Team".
2. Utilize the YouTube transcript tool for "How AI is Changing Healthcare in 2024" and kimtaeyoon83/mcp-server-youtube-transcript tool for "How to Build a Resilient Team".
3. Fetch full, timestamped transcripts for both videos using the respective tools.
4. Output the transcript for "How AI is Changing Healthcare in 2024" to the lead for review.
5. Send the transcript for "How to Build a Resilient Team" to the lead as per previous action.
**What changed:** The approach now combines YouTube's transcript tool with a third-party tool for fetching transcripts.
