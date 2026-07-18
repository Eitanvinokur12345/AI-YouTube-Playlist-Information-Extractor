# [Access's initiative] Implement a **persistent, high-contrast skip link** (visible by default but compact) that expands to full visibility on 

> accessibility · task `access-s-initiative-impl-46167` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Implement a persistent skip link with high-contrast styling that expands to full visibility on focus, ensuring keyboard and screen reader accessibility.

**Steps:**
1. **Create skip link HTML/CSS:**
   - Add `<a class="skip-link" href="#main-content">Skip to main content</a>` as the first focusable element in `<body>`.
   - Style with `.skip-link { position: absolute; top: -40px; left: 0; background: #000; color: #fff; padding: 8px; z-index: 1000; transition: top 0.3s; }` and `.skip-link:focus { top: 0; }`.
   - Ensure high contrast meets WCAG 2.1 AA (e.g., `#000` on `#fff` or `#0056b3` on `#fff`).

2. **Add JavaScript for persistent visibility:**
   - Use `localStorage` to track user preference for expanded state (e.g., `localStorage.setItem('skip-link-expanded', 'true')` on click/focus).
   - Apply `.skip-link { top: 0; }` if `localStorage.getItem('skip-link-expanded') === 'true'`.

3. **Test keyboard/screen reader flow:**
   - Verify tab order places skip link first.
   - Confirm screen readers announce "Skip to main content" and focus moves to `#main-content`.
   - Test with high-contrast mode enabled (e.g., Windows HC or browser extensions).

4. **Integrate into build pipeline:**
   - Add CSS/JS to existing bundle (e.g., `src/styles/skip-link.css
