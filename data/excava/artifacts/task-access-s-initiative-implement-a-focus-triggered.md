# [Access's initiative] Implement a **focus-triggered skip link**—high-contrast, full-width, visible only after first tab press, hidden until ne

> accessibility · task `access-s-initiative-impl-71692` · **EXECUTION PLAN — NOT yet executed** · by groq/llama-3.3-70b-versatile

**Approach:** Implement a focus-triggered skip link using HTML, CSS, and JavaScript to ensure accessibility compliance.
**Steps:**
1. Create a new HTML element for the skip link and add it to the `index.html` file: `<a href="#main-content" class="skip-link">Skip to main content</a>`
2. Add CSS styles to `styles.css` to make the skip link visible only after the first tab press: `.skip-link { position: absolute; top: -40px; left: 0; width: 100%; background-color: #000; color: #fff; padding: 10px; text-align: center; z-index: 1000; } .skip-link:focus { top: 0; }`
3. Update the JavaScript file `script.js` to handle the focus event and display the skip link after the first tab press: `document.addEventListener('keydown', (e) => { if (e.key === 'Tab' && !document.querySelector('.skip-link').classList.contains('visible')) { document.querySelector('.skip-link').classList.add('visible'); } });`
**Needs:** 
* `index.html` file with access to the HTML structure
* `styles.css` file for adding CSS styles
* `script.js` file for updating JavaScript code
* A code editor (e.g., Visual Studio Code) for editing files
* A web browser (e.g., Google Chrome) for testing the implementation
