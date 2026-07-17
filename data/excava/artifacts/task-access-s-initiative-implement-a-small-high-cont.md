# [Access's initiative] Implement a small, high-contrast skip link that collapses into a visible icon on keyboard focus

> accessibility · task `access-s-initiative-impl-10034` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Implement a minimal, high-contrast skip link that collapses into a visible icon when focused via keyboard, ensuring WCAG 2.1 AA compliance for keyboard navigation.

**Steps:**
1. **Create skip link HTML/CSS:**
   - Add `<a href="#main-content" class="skip-link">Skip to main content</a>` before `<main>` in `index.html`.
   - Style `.skip-link` with `position: absolute; left: -9999px; top: 0; background: #000; color: #fff; padding: 8px; z-index: 1000;` and `:focus { left: 0; }`.
   - Add `aria-hidden="true"` to hide the link visually until focused.

2. **Add collapse-to-icon behavior:**
   - Insert `<svg>` icon (e.g., `↓`) after the skip link text, styled to appear only when `.skip-link:focus` (e.g., `display: none; .skip-link:focus & { display: inline; }`).

3. **Test keyboard navigation:**
   - Verify `Tab` moves focus to the skip link, revealing it/high-contrast state.
   - Ensure `Enter` skips to `#main-content` and focus returns to the page.

4. **Validate contrast/accessibility:**
   - Use browser dev tools to confirm 4.5:1 contrast ratio for text/icon.
   - Test with screen reader (e.g., NVDA/VoiceOver) to confirm announcement.

5. **Deploy changes:**
   - Commit to `main` branch with message: "Add high-contrast skip link with icon collapse".
