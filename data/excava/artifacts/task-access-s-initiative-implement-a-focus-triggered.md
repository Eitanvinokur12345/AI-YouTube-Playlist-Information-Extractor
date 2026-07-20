# [Access's initiative] Implement a focus-triggered skip link with a 100ms delay—high-contrast, full-width, keyboard-only visible

> accessibility · task `access-s-initiative-impl-88328` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Implement a high-contrast, full-width skip link that appears after 100ms when focus is triggered via keyboard, hidden by default for mouse users.

**Steps:**
1. **Add HTML skip link** in `src/index.html` (before main content):
   ```html
   <a href="#main-content" class="skip-link" id="skip-link">Skip to main content</a>
   ```
2. **Add CSS** in `src/styles.css`:
   ```css
   .skip-link {
     position: absolute;
     top: -40px;
     left: 0;
     width: 100%;
     background: #000;
     color: #fff;
     padding: 8px 0;
     text-align: center;
     z-index: 999;
     transition: top 0.3s;
   }
   .skip-link:focus {
     top: 0;
   }
   .skip-link:not(:focus):not(:active) {
     clip: rect(0 0 0 0);
     clip-path: inset(50%);
     overflow: hidden;
     height: 1px;
     width: 1px;
     margin: -1px;
     position: absolute;
   }
   ```
3. **Add JavaScript** in `src/script.js`:
   ```javascript
   document.addEventListener('DOMContentLoaded', () => {
     const skipLink = document.getElementById('skip-link');
     skipLink.style.transitionDelay = '100ms';
   });
   ```
4. **Ensure `#main-content` target exists** in `src/index.html`
