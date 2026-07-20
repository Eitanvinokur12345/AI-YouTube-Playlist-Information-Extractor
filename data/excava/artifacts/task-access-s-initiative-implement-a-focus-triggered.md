# [Access's initiative] Implement a **focus-triggered skip link**—high-contrast, full-width, appearing on first tab press and hiding after navig

> accessibility · task `access-s-initiative-impl-70540` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Implement a focus-triggered skip link that appears on first `Tab` press, meets high-contrast WCAG 2.1 AA, spans full width, and auto-hides after navigation.

**Steps:**
1. **Add HTML/Skip Link:**
   - Insert `<a href="#main-content" class="skip-link">Skip to main content</a>` at the top of `<body>` in `src/index.html`.
   - Add `#main-content` as an `<main id="main-content">` wrapper around primary content.

2. **CSS Styling:**
   - Create `src/css/skip-link.css` with:
     ```css
     .skip-link {
       position: absolute;
       top: -40px;
       left: 0;
       width: 100%;
       background: #000;
       color: #fff;
       padding: 8px;
       text-align: center;
       z-index: 9999;
       transition: top 0.3s;
     }
     .skip-link:focus {
       top: 0;
     }
     ```
   - Import into `src/css/main.css` via `@import url('skip-link.css');`.

3. **JavaScript Logic:**
   - Add `src/js/skip-link.js`:
     ```javascript
     document.addEventListener('keydown', (e) => {
       if (e.key === 'Tab') {
         document.querySelector('.skip-link').style.display = 'block';
         document.removeEventListener('keydown', arguments.callee);
       }
     });
     ```
   - Import into `src/js/main.js` and bundle via `npm run build`.

4. **Test
