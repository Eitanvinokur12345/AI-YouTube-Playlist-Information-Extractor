# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-979` (dept) · 2026-07-18T01:40:35.140671+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Ship a live contrast score with a one-click "Accept risk" toggle that updates in real time, logs the risk on submission, and blocks only if the user confirms unreadable colors.

**Plan:**
1. Implement a real-time contrast score overlay that updates as users adjust colors.
2. Add a one-click "Accept risk" toggle visible only when contrast fails WCAG AA/AAA thresholds.
3. Log unreadable submissions (with user confirmation) for moderation review.
4. Block submission only if the user toggles "Accept risk" for unreadable colors (WCAG < 3:1).
5. Ensure the score and toggle are visually distinct and persist until dismissed or fixed.
6. Add a post-submission notice for users who accepted unreadable risks.

**What changed:**
Replaced static warnings with a live contrast score + forced confirmation for unreadable colors.
