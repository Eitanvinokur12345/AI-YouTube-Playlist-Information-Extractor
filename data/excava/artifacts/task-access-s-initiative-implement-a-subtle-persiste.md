# [Access's initiative] Implement a **subtle, persistent skip link** (1px by 1px by default) that smoothly expands to a high-contrast, large lin

> accessibility · task `access-s-initiative-impl-88662` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Implement a CSS/JS-driven skip link that starts at 1×1px, expands smoothly on focus/hover, and meets WCAG 2.2 AA contrast (4.5:1) with large text when active.

**Steps:**
1. Create `skip-link.css` with:
   ```css
   .skip-link {
     position: absolute;
     top: -40px;
     left: 0;
     width: 1px;
     height: 1px;
     padding: 12px;
     background: #005fcc;
     color: #ffffff;
     z-index: 9999;
     transition: width 0.3s ease, height 0.3s ease, top 0s;
   }
   .skip-link:focus {
     top: 0;
     width: auto;
     height: auto;
     clip-path: none;
   }
   ```
2. Add HTML in `<body>`:
   ```html
   <a href="#main-content" class="skip-link">Skip to main content</a>
   <main id="main-content" tabindex="-1">...</main>
   ```
3. Inject CSS/JS via a browser extension (e.g., Stylus + Tampermonkey) for testing:
   ```javascript
   // Tampermonkey script
   (function() {
     const link = document.createElement('a');
     link.href = '#main-content';
     link.className = 'skip-link';
     link.textContent = 'Skip to main content';
     document.body.insertBefore(link, document.body.firstChild);
     const style = document.createElement('style');
     style.text
