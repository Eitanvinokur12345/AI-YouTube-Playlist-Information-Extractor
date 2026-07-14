# [Access's initiative] Use a discreet but always-visible skip link (e

> accessibility · task `access-s-initiative-use--39249` · **EXECUTION PLAN — NOT yet executed** · by groq/llama-3.3-70b-versatile

**Approach:** Implement a discreet but always-visible skip link to enhance accessibility
**Steps:**
1. Create a new HTML element with a `skip` class in the `header.html` file, using `<a href="#main-content" class="skip">Skip to main content</a>`.
2. Add CSS styles to the `styles.css` file to make the skip link visible when focused, using `.skip { position: absolute; top: -40px; left: 0; background-color: #f0f0f0; padding: 10px; z-index: 1; }` and `.skip:focus { top: 0; }`.
3. Update the `index.html` file to include an anchor element with the `id` attribute set to `main-content`, using `<div id="main-content">`, to allow the skip link to navigate to the main content section.
**Needs:** 
- `header.html` file with edit access
- `styles.css` file with edit access
- `index.html` file with edit access
- A code editor or IDE (e.g., Visual Studio Code)
