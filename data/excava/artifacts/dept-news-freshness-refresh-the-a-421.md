# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-421` (dept) · 2026-07-10T17:15:43.660167+00:00
> Participants: Scoop, Factcheck, Wire · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Fetch the last 24h of arXiv AI preprints via `curl -s https://arxiv.org/list/cs.AI/recent | grep -oP '(?<=<a href=")[^"]*' | head -n 20 > arXiv-AI-24h.txt`.
2. Fetch the last 24h of Hugging Face model updates via `curl -s "https://huggingface.co/api/models?sort=last_modified&direction=-1&limit=20" > HF-AI-24h.json`.
3. Merge the two lists, deduplicate by URL, and sort by publication/modification timestamp.
4. Filter to retain only entries from the last 24h (cross-verify timestamps if needed).
5. Output the top 20 newest entries (papers + models) to `AI-News-Digest-24h.md`.
6. Include source URLs and timestamps for traceability.

**What changed:** Prioritized strict 24h recency over popularity/volume, merging arXiv and Hugging Face with timestamp-based ranking.
