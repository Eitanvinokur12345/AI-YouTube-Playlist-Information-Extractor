# mining: Gather AI info from DIVERSE sources (GitHub/HN/Product Hunt/Reddit/Telegram/social), NOT j

> Decision artifact · room `dept-mining-gather-ai-info-from-d-547` (dept) · 2026-07-30T17:54:44.437738+00:00
> Participants: Pick · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Browse r/MachineLearning and r/AI (last 7 days) to extract top 10 most discussed AI tools, datasets, or research papers.
2. For each entry, record key claims, limitations, and source links.
3. Compile results into a GitHub markdown table with columns: *Name*, *Type*, *Key Claim*, *Limitations*, *Source*.
4. Validate entries for diversity (GitHub/HN/Product Hunt/Reddit/Telegram/social) by cross-referencing at least 2 sources per item.
5. Push the markdown file to the team’s shared GitHub repo under `/data/ai-mining/`.
6. Notify the team via Slack with a summary and link to the file.

**What changed:** Focus narrowed to Reddit-only extraction with cross-source validation for diversity.
