# [Access's initiative] Implement a **persistent, subtle skip link** (1px by 1px underline by default, expands to 2px on keyboard focus) at the 

> accessibility · task `access-s-initiative-impl-10004` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Implement a persistent skip link using CSS/JS with minimal visual footprint that expands on keyboard focus, ensuring WCAG 2.1 AA compliance.

**Steps:**
1. **Add HTML skip link** to `<body>` in `src/templates/base.html` (or equivalent layout file):
   ```html
   <a href="#main-content" class="skip-link">Skip to main content</a>
   ```
2. **Style skip link** in `src/assets/css/accessibility.css`:
   ```css
   .skip-link {
     position: absolute;
     top: -40px;
     left: 0;
     background: #000;
     color: #fff;
     padding: 8px;
     z-index: 9999;
     transition: top 0.3s, width 0.3s, height 0.3s;
     width: 1px;
     height: 1px;
     overflow: hidden;
     text-decoration: underline 1px;
   }
   .skip-link:focus {
     top: 0;
     width: auto;
     height: auto;
     text-decoration: underline 2px;
   }
   ```
3. **Add JavaScript** in `src/assets/js/accessibility.js` to ensure `#main-content` exists:
   ```javascript
   document.addEventListener('DOMContentLoaded', () => {
     if (!document.getElementById('main-content')) {
       const main = document.createElement('main');
       main.id = 'main-content';
       document.body.insertBefore(main, document.body.firstChild);
     }
   });
   ```
4. **Import CSS/JS** in build
