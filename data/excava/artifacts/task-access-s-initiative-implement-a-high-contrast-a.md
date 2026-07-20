# [Access's initiative] Implement a **high-contrast, always-visible skip button** styled like a button in the top-left corner of every page—test

> accessibility · task `access-s-initiative-impl-89382` · **EXECUTION PLAN — NOT yet executed** · by groq/llama-3.3-70b-versatile

**Approach:** Implement a high-contrast, always-visible skip button in the top-left corner of every page
### Steps:
1. **Modify the base HTML template**: Edit the `index.html` file to include a `button` element with a high-contrast background color and foreground color, positioned at the top-left corner of the page using CSS.
2. **Add CSS styles**: Create a new CSS class (e.g., `.skip-button`) in the `styles.css` file, defining the button's appearance, position, and visibility, ensuring it meets WCAG 2.1 contrast guidelines.
3. **Implement button functionality**: Write JavaScript code in the `script.js` file to handle the button's click event, allowing users to skip to the main content of the page.
4. **Test and validate**: Use tools like Lighthouse, WAVE, and a screen reader to test the skip button's visibility, contrast, and functionality on different devices and browsers.
5. **Commit and deploy changes**: Commit the modified files to the repository using Git and deploy the updated code to the production environment.

**Needs:**
* Access to the `index.html`, `styles.css`, and `script.js` files
* A code editor (e.g., Visual Studio Code)
* Git version control system
* Lighthouse and WAVE accessibility testing tools
* A screen reader (e.g., NVDA) for testing
* Deployment access to the production environment
