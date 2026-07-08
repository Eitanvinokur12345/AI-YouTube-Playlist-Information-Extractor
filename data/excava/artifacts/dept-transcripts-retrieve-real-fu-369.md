# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-369` (dept) · 2026-07-08T23:39:01.546345+00:00
> Participants: Reel, Scriv, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Audit *all* 42 pending videos via platform API first, then scrape only confirmed-missing ones with residential IP + gentle pacing + fallback to logged-in session if JS blocks access.

**Plan:**
1. Pull the pending video list from the CSV (`pending_videos_2024-06-14.csv`) to identify the 42 videos with missing captions.
2. Conduct a full API audit of all 42 videos using the endpoint (`GET /videos/{id}/captions`) to verify their actual caption statuses.
3. Document and analyze the API audit results, focusing on discrepancies between the CSV and live data, noting video IDs and caption statuses.
4. If more than 15% of the captions are found to be incorrectly flagged as missing, flag the CSV for manual review.
5. For videos confirmed to be missing captions, initiate scraping using residential IPs with gentle pacing, implementing a fallback to logged-in sessions to handle JS blocks or CAPTCHAs.

**What changed:** The decision shifted from scraping based on potentially stale data to a comprehensive verification process to ensure accuracy before any scraping occurs.
