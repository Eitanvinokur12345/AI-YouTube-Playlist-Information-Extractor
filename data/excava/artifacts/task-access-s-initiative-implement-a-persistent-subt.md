# [Access's initiative] Implement a **persistent, subtle skip link** (1px by 1px underline, high contrast on focus) placed *before* the first in

> accessibility · task `access-s-initiative-impl-14543` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Inject a persistent, subtle skip link (1px × 1px underline, high-contrast on focus) positioned before the first interactive element in the DOM.

**Steps:**
1. Open `/src/templates/base.html` (or equivalent root template) and insert:
   ```html
   <a id="skip-link" href="#main-content" style="position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden;text-decoration:underline;color:#000;background:#fff;">Skip to main content</a>
   ```
   immediately before the first `<main>`, `<div id="main-content">`, or landmark role element.

2. Add CSS to `/src/static/css/access.css` (or inline `<style>` in base.html):
   ```css
   #skip-link:focus { position:static;width:auto;height:auto;overflow:visible; }
   ```

3. Ensure `#main-content` exists in `/src/templates/base.html` (or add `<main id="main-content" role="main">`).

4. Build assets and deploy; verify via keyboard tabbing that the link appears on `:focus` with ≥ 4.5:1 contrast.

**Needs:**
- Write access to `/src/templates/base.html` and `/src/static/css/access.css` (or equivalent).
- Browser with keyboard navigation (e.g., Chrome + NVDA/JAWS).
- Contrast checker (e.g., WebAIM Contrast Checker) to confirm ≥ 4.5:1 on focus state.
```
