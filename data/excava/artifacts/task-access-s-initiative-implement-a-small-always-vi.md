# [Access's initiative] Implement a small, always-visible skip link icon that expands to a full link on focus/hover

> accessibility · task `access-s-initiative-impl-58808` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Implement a minimal, always-visible skip-link trigger (icon) that expands into a full skip link when focused or hovered, ensuring keyboard and screen reader accessibility.

**Steps:**
1. **Create HTML/CSS structure:**
   - Add a `<button>` or `<a>` element with `aria-label="Skip to main content"` containing an SVG icon (e.g., `skip-icon.svg`).
   - Position it fixed in the top-left corner (e.g., `top: 1rem; left: 1rem;`).
   - Hide the text label by default (`opacity: 0; width: 0; overflow: hidden`) and expand it on `:focus` or `:hover` (e.g., `width: auto; opacity: 1; transition: width 0.2s`).

2. **Link target:**
   - Ensure the skip link points to the main content container (e.g., `<main id="main-content">`).
   - Add `tabindex="-1"` to the target for focus management.

3. **JavaScript (optional for dynamic states):**
   - Use `element.addEventListener('focus', () => { /* expand */ })` for keyboard users if CSS transitions are insufficient.

4. **Test accessibility:**
   - Verify with keyboard navigation (Tab key) and screen reader (NVDA/JAWS).
   - Check contrast (WCAG 2.1 AA) for the icon and expanded link.

5. **Deploy:**
   - Merge changes into the main branch and deploy via CI/CD (e.g., GitHub Actions).

**Needs:**
- Access to the project’s HTML/CSS/JS files (e.g., `src/components/skip-link
