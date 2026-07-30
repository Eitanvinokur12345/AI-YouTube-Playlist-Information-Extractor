# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-513` (dept) · 2026-07-30T23:39:19.747535+00:00
> Participants: Reel, Echo · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Fetch full transcript for pending video using YouTube transcript tool and verify completeness.
**Plan:**
1. Use the YouTube transcript tool to fetch the full transcript for the pending video "How to Build a Resilient Team".
2. Verify the completeness of the fetched transcript to ensure it includes all captions as text.
3. Utilize kimtaeyoon83/mcp-server-youtube-transcript for fetching the transcript if necessary.
4. Declare the transcript missing only if verification confirms it is incomplete.
5. Review and adjust the transcript fetching process as needed to ensure accuracy and completeness.
**What changed:** The approach to fetching transcripts now includes verification of completeness before declaring a transcript missing.
