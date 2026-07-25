# [Access's initiative] Implement a **bold, full-width skip bar** that appears only when keyboard-focused, with high contrast and no hover/focus

> accessibility · task `access-s-initiative-impl-36111` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Add a keyboard-only, full-width skip bar with forced high contrast and no hover/focus states via CSS/JS.

**Steps:**
1. Create `skip-bar.css` with:
   - `position: fixed; top: 0; left: 0; width: 100%; height: 3rem; background: #000; color: #fff; font-size: 1.25rem; text-align: center; line-height: 3rem; z-index: 9999;`
   - `opacity: 0; transition: opacity 0.2s;` (hidden by default)
   - `.skip-bar--visible { opacity: 1; }` (applied via JS)
   - No `:hover` or `:focus-visible` selectors.
2. Add `skip-bar.js` to:
   - Listen for `keydown` (Tab key) and set `.skip-bar--visible` on the bar.
   - Remove the class on first `click` or `keydown` (Enter/Space) on the bar.
3. Insert `<div class="skip-bar" role="navigation" aria-label="Skip to main content">Skip to content</div>` into `<body>` (before main content).
4. Add `skip-bar.css` and `skip-bar.js` to the build pipeline (e.g., via `import` in JS or `<link>`/`<script>` in HTML).
5. Test with:
   - Keyboard-only navigation (Tab key).
   - Screen reader (NVDA/JAWS) to confirm announcement.
   - High-contrast mode (Windows HC) to verify visibility.

**Needs:**
- Access to the
