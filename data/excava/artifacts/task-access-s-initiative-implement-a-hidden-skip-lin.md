# [Access's initiative] Implement a hidden skip link that appears only on keyboard focus, ensuring instant navigation for screen reader users wi

> accessibility · task `access-s-initiative-impl-69566` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
## Approach:
Implement a visually hidden skip link that becomes visible and focusable only when programmatically focused (e.g., via keyboard tab), enabling screen reader users to bypass repetitive navigation blocks.

## Steps:
1. **Create HTML/CSS for skip link**
   - Add `<a href="#main-content" class="skip-link">Skip to main content</a>` as the first focusable element in `<body>`.
   - Style with `.skip-link { position: absolute; left: -9999px; top: 0; ... }` and `.skip-link:focus { left: 0; background: #000; color: #fff; ... }` (adjust colors per Access’s contrast requirements).
   - Target `#main-content` must be the ID of the primary content container (e.g., `<main id="main-content">`).

2. **Verify keyboard navigation flow**
   - Test tab order: Ensure the skip link is the first focusable element after the `<body>` (use `tabindex` if needed).
   - Confirm focus styles are visible and meet contrast ratios (WCAG 2.1 AA: 4.5:1 for normal text).

3. **Test with screen readers**
   - Validate functionality in NVDA, JAWS, and VoiceOver (e.g., pressing `Tab` should announce and activate the skip link).
   - Use browser dev tools to simulate keyboard-only navigation.

4. **Integrate into build pipeline**
   - Add the skip link to the base template (e.g., `src/templates/base.html` in a Django/Flask project or equivalent).
   - Ensure it’s included in all pages via template inheritance.

5. **Document and deploy
