# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-592` (dept) · 2026-07-17T09:49:29.547192+00:00
> Participants: Reel, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Use the kimtaeyoon83/mcp-server-youtube-transcript tool to retrieve full transcripts for pending videos to ensure compliance.

**Plan:**
1. Identify all pending videos requiring transcript retrieval.
2. Compile a list of YouTube URLs for these videos.
3. Run the kimtaeyoon83/mcp-server-youtube-transcript tool on each URL to fetch the transcripts.
4. Format the retrieved transcripts to include timestamps and ensure clarity.
5. Store the formatted transcripts as clean artifacts for Product Ops review.

**What changed:** The focus is now on using a specific tool to ensure compliance with transcript availability.
