# [Access's initiative] Implement a **focus-triggered skip link**—high-contrast, full-width, animated on focus—visible only to keyboard users, w

> accessibility · task `access-s-initiative-impl-78252` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Implement a focus-triggered skip link with high contrast, full-width animation, visible only to keyboard users.

**Steps:**
1. **Create skip link HTML/CSS:**
   - Add `<a href="#main-content" class="skip-link">Skip to main content</a>` as the first focusable element in `<body>`.
   - Style `.skip-link` with `position: absolute; left: -9999px; top: 0; background: #000; color: #fff; padding: 0.5rem 1rem; z-index: 1000; transition: left 0.3s ease;` and animate `left: 0` on `:focus` (within 50ms of focus).
   - Ensure `outline: none` is overridden with a visible focus style (e.g., `outline: 2px solid #ff0;`).

2. **Add target anchor:**
   - Insert `<main id="main-content" tabindex="-1">` before the main content section.

3. **Test keyboard navigation:**
   - Verify tab order includes the skip link before other elements.
   - Confirm skip link appears on focus and returns to `-9999px` when blurred.

4. **Validate accessibility:**
   - Use `axe-core` or WAVE to check for missing skip links and focus visibility.
   - Test with screen readers (NVDA/JAWS) and keyboard-only navigation.

5. **Deploy changes:**
   - Commit to `src/components/skip-link.css` and `src/index.html` with a PR labeled `feat: focus-triggered skip link`.

**Needs:**
- Access to the project’s HTML/CSS
