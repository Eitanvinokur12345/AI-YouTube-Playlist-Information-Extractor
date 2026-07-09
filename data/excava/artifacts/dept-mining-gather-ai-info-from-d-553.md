# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-553` (dept) · 2026-07-09T23:49:45.992205+00:00
> Participants: Pick, Assay, Boulder · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Merge GitHub (>100★, 30d) and HF Spaces (>50dl, 30d) scrapes, cross-check 30% overlap, export `ai_sources_2024-06-20.json` with repo/space metadata, download counts, last-updated, and overlap flags.

**Plan:**  
1. Launch a GitHub scrape for AI repositories with more than 100 stars and updated in the last 30 days using `gh search repos` with relevant keywords.  
2. Export the results to `ai_repos_2024-06-20.json`, limited to a maximum of 500 results sorted by stars.  
3. Launch a Hugging Face scrape for AI/ML applications with over 50 downloads in the last 30 days using the `huggingface_hub` CLI.  
4. Export the results to `hf_spaces_2024-06-20.json`, limited to a maximum of 300 entries.  
5. Cross-check 30% of entries from both datasets for overlap, noting any corresponding flags in the final export.  
6. Compile the final output into a single file, `ai_sources_2024-06-20.json`, with relevant metadata.

**What changed:** The decision now incorporates a more comprehensive cross-checking approach while addressing concerns about the accuracy of download counts in the Hugging Face scrape.
