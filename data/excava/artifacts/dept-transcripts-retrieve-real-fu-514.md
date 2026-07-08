# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-514` (dept) · 2026-07-08T02:13:55.364915+00:00
> Participants: Reel, Scriv, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:**  

1. Execute Reel's SQLite query to verify the freshness of the pending video list.  
2. Cross-check each pending video ID's captions using `youtube-dl --list-subs` to ensure availability and accuracy.  
3. If confirmed valid, run `youtube-dl --write-auto-sub --sub-lang en --skip-download` on each valid video ID to retrieve the transcripts.  
4. Ensure results are real, full transcripts/captions, and verify against YouTube’s API or scraping as necessary.  
5. Document any discrepancies found during the verification process for future reference.  

**What changed:** The decision now includes validation steps to prevent unnecessary downloads of stale captions.
