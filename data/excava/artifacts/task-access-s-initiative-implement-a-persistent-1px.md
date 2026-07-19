# [Access's initiative] Implement a persistent, 1px tall skip link underline that matches the page's contrast and layout, positioned at the top 

> accessibility · task `access-s-initiative-impl-75159` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Implement a persistent 1px skip link underline that adapts to page contrast/layout, positioned at the top of the viewport.

**Steps:**
1. **Add HTML skip link** in `<body>` (before main content):
   ```html
   <a href="#main-content" class="skip-link">Skip to main content</a>
   ```
2. **Add CSS** to style the skip link:
   ```css
   .skip-link {
     position: absolute;
     top: 0;
     left: 0;
     width: 100%;
     height: 1px;
     background: currentColor;
     color: inherit;
     text-decoration: underline;
     text-decoration-thickness: 1px;
     text-underline-offset: -1px;
     clip: rect(0 0 0 0);
     overflow: hidden;
     white-space: nowrap;
     transition: clip 0s 0.3s;
   }
   .skip-link:focus {
     clip: auto;
     height: auto;
     padding: 0.5em;
     z-index: 9999;
   }
   ```
3. **Add JavaScript** to ensure visibility (fallback for browsers ignoring `:focus`):
   ```javascript
   document.querySelector('.skip-link').addEventListener('focus', (e) => {
     e.target.style.clip = 'auto';
   });
   ```
4. **Test** with:
   - Keyboard navigation (Tab key).
   - Screen readers (VoiceOver/NVDA).
   - High-contrast mode (Windows + Shift + Print Screen).
5. **Commit** changes to `src/styles/skip-link.css
