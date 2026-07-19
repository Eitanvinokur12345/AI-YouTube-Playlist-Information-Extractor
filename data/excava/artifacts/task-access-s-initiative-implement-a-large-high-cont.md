# [Access's initiative] Implement a **large, high-contrast skip link that collapses to a visible icon on mobile**, visible by default but compac

> accessibility · task `access-s-initiative-impl-96443` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Implement a skip link with progressive enhancement: large high-contrast button visible by default, collapses to a visible icon on mobile via CSS/JS.

**Steps:**
1. Create `skip-link.scss` with:
   - `.skip-link` (large high-contrast button, `position: absolute`, `top: 0`, `left: 0`, `z-index: 1000`)
   - `.skip-link--mobile` (hidden by default, media query `@media (max-width: 768px)` shows icon-only)
   - Transition for collapse/expand (e.g., `transform`, `opacity`)
2. Add `skip-link.js` to toggle `.skip-link--mobile` on button click (if needed for dynamic states)
3. Insert skip link HTML in `base.html` (or equivalent layout file):
   ```html
   <a href="#main-content" class="skip-link skip-link--mobile">Skip to content</a>
   ```
4. Update `#main-content` to include `tabindex="-1"` for focus management
5. Run `npm run build` (or equivalent) to compile CSS/JS; verify in browser dev tools

**Needs:**
- Access to project’s Sass/JS pipeline (e.g., `sass`, `webpack`, or `vite`)
- Existing skip link HTML structure (or permission to modify `base.html`)
- Mobile breakpoint value (default: `768px` unless specified otherwise)
- High-contrast color palette (WCAG 2.1 AA compliant)
- Test device/emulator for mobile behavior
```
