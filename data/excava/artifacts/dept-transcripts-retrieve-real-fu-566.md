# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-566` (dept) · 2026-08-10T11:33:59.739637+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. For pending videos in the Luma ecosystem, use Luma’s built-in transcript tool to generate clean, structured transcripts.
2. For pending videos outside the Luma ecosystem, use Luma’s built-in transcript tool to ensure consistent quality.
3. Avoid using `kimtaeyoon83/mcp-server-youtube-transcript` to prevent unstructured raw text output.
4. Batch-process all pending videos through the chosen tool to maintain gentle pacing and residential IP compliance.
5. Store generated transcripts in a structured format (e.g., JSON or text files) for downstream use.
6. Log any failures or inconsistencies for manual review or reprocessing.

**What changed:** Switched from scraping raw text to using Luma’s built-in tool for all pending videos to enforce quality and structure.
