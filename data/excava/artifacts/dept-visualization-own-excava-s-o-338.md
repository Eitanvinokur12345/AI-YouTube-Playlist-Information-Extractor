# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-338` (dept) · 2026-07-20T11:24:42.931614+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Ship a real-time contrast overlay that flashes red on violations *as you work* in the live preview—no build blocks, no warnings to ignore.

**Plan:**
1. Implement a live contrast checker that runs in the background of the preview pane.
2. Highlight contrast violations with a red flash overlay *immediately* after any design change.
3. Log violations in a non-intrusive sidebar (e.g., count + quick links to issues).
4. Add a toggle to silence the overlay for 10 minutes (prevents annoyance while preserving visibility).
5. Run a 1-week trial with the team, tracking how often violations are fixed *during* edits vs. post-submission.
6. Iterate based on trial data (e.g., adjust flash duration, add sound cues for severe violations).

**What changed:** Contrast issues are now visible *in the moment*, not just before shipping.
