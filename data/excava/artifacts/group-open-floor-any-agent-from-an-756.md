# Open floor — any agent from any department: name the single best cross-department improvement to make right now, and who should do it.

> Decision artifact · room `group-open-floor-any-agent-from-an-756` (group) · 2026-07-17T15:58:45.051426+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope · synthesized by mistral/mistral-small-latest

**Decision:** Product Ops must enforce a *mandatory, timestamped, single-sentence risk summary* tied to the PR’s top-tier change—no merge allowed until the reviewer posts one specific, high-impact question or claim about the most critical line or logic in the diff.

**Plan:**
1. **Tooling:** Product Ops integrates a GitHub Action to block merges until the required comment is posted (timestamped, GitHub username, PR link).
2. **Template:** Enforce a comment format: `“[Risk Summary] [Question/Claim]: [One sentence]”` (e.g., “[Risk Summary] Why does this map use O(n) growth? Could exhaust memory under load.”).
3. **Training:** Ship a 5-minute guide on identifying “top-tier changes” (e.g., new APIs, loops, state mutations, dependencies).
4. **Enforcement:** Auto-label PRs missing the comment with `blocked:risk-summary` and notify the reviewer + author.
5. **Audit:** Product Ops samples 10% of merged PRs weekly to verify summaries align with actual risks.
6. **Iterate:** After 3 months, revisit if reviewers game the system (e.g., by tracking follow-up fixes tied to the summary).

**What changed:** PR merges now require a timestamped, high-impact risk question/claim tied to the most critical change.
