# [Access's initiative] Implement a **large, high-contrast skip link** that is **always visible** at the top of every page, with reduced motion 

> accessibility · task `access-s-initiative-impl-67169` · **EXECUTION PLAN — NOT yet executed** · by groq/llama-3.3-70b-versatile

**Approach:** Implement a large, high-contrast skip link at the top of every page with reduced motion using HTML, CSS, and JavaScript.
**Steps:**
1. Create a new HTML element for the skip link in the `header.html` file: `<a href="#main-content" class="skip-link">Skip to main content</a>`.
2. Add CSS styles to `styles.css` to make the skip link always visible and high-contrast: `.skip-link { position: absolute; top: 0; left: 0; background-color: #000; color: #fff; padding: 1em; font-size: 1.5em; }`.
3. Use JavaScript in `script.js` to add reduced motion to the skip link: `document.addEventListener('DOMContentLoaded', () => { const skipLink = document.querySelector('.skip-link'); skipLink.addEventListener('focus', () => { document.body.classList.add('reduce-motion'); }); skipLink.addEventListener('blur', () => { document.body.classList.remove('reduce-motion'); }); });`.
**Needs:** `header.html`, `styles.css`, `script.js`, a code editor (e.g. Visual Studio Code), a web browser (e.g. Google Chrome) for testing.
