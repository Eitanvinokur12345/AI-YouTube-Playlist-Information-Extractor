# [Access's initiative] Implement a **persistent, subtle skip link** (e

> accessibility · task `access-s-initiative-impl-68788` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Implement a persistent, subtle skip link using semantic HTML, CSS for subtlety, and JavaScript for persistence across navigation.

**Steps:**
1. **Add skip link HTML** to `src/layouts/base.html` (or equivalent base template):
   ```html
   <a href="#main-content" class="skip-link">Skip to main content</a>
   ```
   Place it as the first focusable element in `<body>`.

2. **Style the skip link** in `src/styles/accessibility.css`:
   ```css
   .skip-link {
     position: absolute;
     left: -9999px;
     top: 0;
     background: #000;
     color: #fff;
     padding: 0.5rem 1rem;
     z-index: 1000;
     transition: left 0.3s;
   }
   .skip-link:focus {
     left: 0;
   }
   ```

3. **Ensure `#main-content` target exists** in all page templates (e.g., `src/pages/*.html`):
   ```html
   <main id="main-content" tabindex="-1">
     <!-- Page content -->
   </main>
   ```

4. **Persist visibility** via JavaScript in `src/scripts/skip-link.js`:
   ```javascript
   document.addEventListener('DOMContentLoaded', () => {
     const skipLink = document.querySelector('.skip-link');
     if (localStorage.getItem('skipLinkSeen') !== 'true') {
       skipLink.style.left = '0';
       localStorage.setItem('skipLinkSeen', 'true');
     }
   });
