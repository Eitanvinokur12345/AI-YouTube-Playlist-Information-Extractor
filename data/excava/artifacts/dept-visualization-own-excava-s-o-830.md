# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-830` (dept) · 2026-07-19T23:31:01.341424+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Ship a real-time contrast overlay that flags *only* the worst offenders in the canvas during changes, but blocks submission only if contrast drops below WCAG AA.

**Plan:**
1. Implement a live contrast overlay that highlights elements with contrast below WCAG AA in real-time during design changes.
2. Limit the overlay to flag only the most severe failures (e.g., text on background with contrast < 3:1) to avoid noise.
3. Add a pre-submission gate that blocks final export/approval if any element fails WCAG AA contrast.
4. Integrate the overlay into the canvas UI with minimal visual intrusion (e.g., subtle red outlines for failures).
5. Log all flagged issues for designers to review post-change, but do not interrupt workflow.
6. Provide a one-click "Fix" button for flagged elements to auto-adjust contrast to WCAG AA compliance.

**What changed:**
Added a real-time, low-noise contrast overlay with a strict pre-submission gate for WCAG AA failures.
