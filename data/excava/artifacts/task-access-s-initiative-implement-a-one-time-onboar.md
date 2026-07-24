# [Access's initiative] Implement a one-time onboarding hint that appears only on first visit, then fades, to inform users about the skip link

> accessibility · task `access-s-initiative-impl-49412` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Implement a one-time onboarding hint for the skip link that auto-fades after first visit, using localStorage to track visibility.

**Steps:**
1. Add HTML/CSS/JS for the hint element (`.skip-link-hint`) with fade-out animation, positioned near the skip link.
2. Insert JavaScript to check `localStorage.getItem('skipLinkHintSeen')`; if missing, show the hint and set the key to `true`.
3. Ensure the hint is keyboard-focusable and screen-reader-friendly (ARIA live region or `role="alert"`).
4. Test with keyboard navigation and screen readers (NVDA/JAWS) to confirm dismissal and focus order.

**Needs:**
- Access to the project’s HTML template or component file (e.g., `src/templates/base.html`).
- CSS file for styling/animations (e.g., `src/styles/main.css`).
- JavaScript file for logic (e.g., `src/scripts/accessibility.js`).
- Testing tools: keyboard, screen reader (NVDA/JAWS), browser dev tools.
```
