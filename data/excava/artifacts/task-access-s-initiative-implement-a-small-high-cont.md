# [Access's initiative] Implement a small, high-contrast skip link that collapses into a thin line when not focused, fully visible when keyboard

> accessibility · task `access-s-initiative-impl-30797` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Implement a high-contrast skip link that remains visible when keyboard-focused and collapses to a thin line otherwise, using semantic HTML, CSS, and minimal JavaScript.

**Steps:**
1. **Create HTML structure** in `src/components/skip-link.html`:
   ```html
   <a href="#main-content" class="skip-link">Skip to main content</a>
   <main id="main-content">...</main>
   ```
2. **Add CSS** in `src/styles/skip-link.css`:
   ```css
   .skip-link {
     position: absolute;
     top: 0;
     left: 0;
     width: 100%;
     padding: 0.5rem;
     background: #000;
     color: #fff;
     text-align: center;
     z-index: 9999;
     transition: height 0.3s ease;
   }
   .skip-link:not(:focus) {
     height: 0;
     overflow: hidden;
     padding: 0;
   }
   ```
3. **Link CSS/JS** in `src/index.html`:
   ```html
   <link rel="stylesheet" href="styles/skip-link.css">
   <script src="js/skip-link.js"></script>
   ```
4. **Add minimal JS** in `src/js/skip-link.js` (fallback for older browsers):
   ```javascript
   document.querySelector('.skip-link').addEventListener('blur', function() {
     this.style.height = '0';
   });
   ```
5. **Test** with keyboard navigation and screen reader (NVDA/JAWS) in Chrome/Fire
