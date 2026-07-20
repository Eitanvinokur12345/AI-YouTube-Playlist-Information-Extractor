# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-411` (dept) · 2026-07-20T22:47:28.600486+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Ship a *gradual* contrast enforcement system—live warnings first, soft pre-commit blocks after 3 warnings, hard pre-commit blocks only after 7 warnings.

**Plan:**
1. Implement a live contrast checker that flags WCAG AA failures in real time during design changes.
2. Add a pre-commit hook that issues *soft blocks* (warnings + option to override) after 3 contrast violations.
3. Escalate to *hard blocks* (mandatory fixes) after 7 violations, preventing merges.
4. Log all violations and fixes to track designer learning and tool efficacy.
5. Document the system in the design guidelines and onboarding materials.
6. Review enforcement thresholds after 3 months based on designer feedback and violation trends.

**What changed:** Introduced a staged contrast enforcement system to balance speed, learning, and compliance.
