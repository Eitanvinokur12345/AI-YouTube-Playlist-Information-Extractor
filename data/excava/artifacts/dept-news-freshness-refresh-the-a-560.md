# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-560` (dept) · 2026-07-08T20:08:06.835204+00:00
> Participants: Scoop, Factcheck, Wire · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Fetch AI papers via arXiv API (`http://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=descending`) with SHA-256 hashes of PDFs for integrity checks.
2. Pull official updates from NVIDIA (API), Google DeepMind (RSS + JSON), Microsoft (blog RSS), and EU AI Act registry (XML feed) with submission timestamps.
3. Cross-verify sources: Compare arXiv API dates with RSS feeds; validate NVIDIA/Google/Microsoft posts against their official domains.
4. Filter duplicates using SHA-256 hashes and timestamps (reject if hash/timestamp mismatch).
5. Compile verified items into `ai-news-digest-2024-06-20.md` with columns: *Title*, *Source*, *Timestamp*, *SHA-256 Hash*, *URL*.
6. Append a "Verification Log" section listing checks performed (e.g., "arXiv PDF hash verified", "EU AI Act timestamp validated").

**What changed:** Replaced fragile heuristics with direct APIs, cryptographic hashes, and timestamp cross-checks for verifiable recency/authenticity.
