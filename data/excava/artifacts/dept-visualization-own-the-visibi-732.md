# visualization: Own the visibility AND ACCESSIBILITY of the whole interface — liveliness, info access, enj

> Decision artifact · room `dept-visualization-own-the-visibi-732` (dept) · 2026-07-08T20:09:15.431106+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Fork `interface-liveliness` from `main` and create `/docs/audit/liveliness-audit.md`.
2. Run `npm run test:visual-a11y -- --screens all --timeout 10000` to auto-capture Lighthouse accessibility scores for all routed screens.
3. Manually test 5 key screens (home, dashboard, settings, profile, search) + modals/error states for real-user friction.
4. Log raw Lighthouse scores in `/docs/audit/liveliness-audit.md`.
5. Document manual test notes (modals, errors, keyboard flows) in the same file.
6. Perform gap analysis comparing automated scores vs. manual findings.

**What changed:** Combined automated audits with real-user testing to validate visibility and accessibility gaps.
