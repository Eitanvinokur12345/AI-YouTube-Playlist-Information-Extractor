# [Access's initiative] Implement a **focus-triggered skip link**—high-contrast, full-width, and triggered by keyboard tab—with a fallback alway

> accessibility · task `access-s-initiative-impl-87288` · **EXECUTION PLAN — NOT yet executed** · by groq/llama-3.3-70b-versatile

**Approach:** Implement a focus-triggered skip link with a fallback using HTML, CSS, and JavaScript.
**Steps:**
1. Create a new HTML element with an ID, e.g., `skip-link`, and add it to the top of the page, with a `tabindex` attribute set to 0, and `style` set to `position: absolute; left: -1000px;` to hide it from view.
2. Add a CSS rule to display the `skip-link` element when it receives focus, using the `:focus` pseudo-class, with `position: static; width: 100%; background-color: #000; color: #fff; padding: 1em;`.
3. Write a JavaScript function to add an event listener to the `skip-link` element, which listens for a click event and then focuses on the main content element, using `document.getElementById('main-content').focus()`.
**Needs:** 
- A code editor (e.g., Visual Studio Code)
- A web browser (e.g., Google Chrome) for testing
- Basic knowledge of HTML, CSS, and JavaScript
