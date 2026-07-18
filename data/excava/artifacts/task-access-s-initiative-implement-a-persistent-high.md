# [Access's initiative] Implement a **persistent, high-contrast skip link** at the top of every page, styled with reduced visual weight (e

> accessibility · task `access-s-initiative-impl-40607` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Implement a persistent, high-contrast skip link at the top of every page with reduced visual weight for Access compliance.

**Steps:**
1. **Add skip link HTML** to the base template (e.g., `src/templates/base.html`):
   ```html
   <a href="#main-content" class="skip-link">Skip to main content</a>
   ```
2. **Style the skip link** in CSS (e.g., `src/styles/access.css`):
   ```css
   .skip-link {
     position: absolute;
     top: -40px;
     left: 0;
     background: #000;
     color: #fff;
     padding: 8px;
     z-index: 1000;
     transition: top 0.3s;
   }
   .skip-link:focus {
     top: 0;
   }
   ```
3. **Ensure `#main-content` anchor exists** in page templates (e.g., `src/templates/page.html`):
   ```html
   <main id="main-content" tabindex="-1">
   ```
4. **Test keyboard navigation** (Tab key) and screen reader compatibility (NVDA/JAWS).
5. **Deploy changes** via CI/CD pipeline (e.g., `git commit -m "Add persistent skip link" && git push`).

**Needs:**
- Access to the project’s base template (`src/templates/base.html`).
- CSS file (`src/styles/access.css`) for styling.
- CI/CD pipeline for deployment.
- Testing tools (keyboard, screen reader).
```
