# [Access's initiative] Implement a hybrid skip link—always visible but hidden off-screen until focused, with a fallback to server-side if JS fa

> accessibility · task `access-s-initiative-impl-8555` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Implement a hybrid skip link that is always present in the DOM but visually hidden off-screen until focused, with a server-side fallback if JavaScript fails to initialize the client-side behavior.

**Steps:**
1. **Add HTML Skip Link**
   - In `src/layout/base.html` (or equivalent), insert a skip link at the top of `<body>`:
     ```html
     <a href="#main-content" class="skip-link">Skip to main content</a>
     ```
   - Style it in `src/styles/components/skip-link.scss`:
     ```scss
     .skip-link {
       position: absolute;
       top: -40px;
       left: 0;
       background: #000;
       color: #fff;
       padding: 8px;
       z-index: 9999;
       transition: top 0.3s;
       &:focus {
         top: 0;
       }
     }
     ```

2. **Add Main Content Target**
   - Ensure the main content container has `id="main-content"` in `src/layout/base.html`:
     ```html
     <main id="main-content" tabindex="-1">
     ```

3. **JavaScript Enhancement**
   - In `src/js/skip-link.js`, add client-side focus handling:
     ```js
     document.querySelector('.skip-link')?.addEventListener('click', (e) => {
       e.preventDefault();
       document.querySelector('#main-content')?.focus();
     });
     ```
   - Load this script in `src/js/main.js` with a fallback to server-side if JS fails.

4. **Server-Side Fallback**
   - In the backend
