# [Access's initiative] Implement a **persistent, zero-opacity skip link** that becomes visible on keyboard focus (via `opacity: 0` → `opacity: 

> accessibility · task `access-s-initiative-impl-43842` · **EXECUTION PLAN — NOT yet executed** · by groq/llama-3.3-70b-versatile

**Approach:** Implement a persistent, zero-opacity skip link that becomes visible on keyboard focus using CSS and HTML.
**Steps:**
1. Create a new HTML element for the skip link, such as `<a id="skip-link" href="#main-content">Skip to main content</a>`, and add it to the top of the HTML file.
2. Add CSS styles to make the skip link invisible by default, but visible on keyboard focus: `#skip-link { opacity: 0; position: absolute; top: 0; left: 0; } #skip-link:focus { opacity: 1; }`.
3. Use a CSS preprocessor like Sass or Less to compile the CSS code, or add it directly to the HTML file using the `<style>` tag.
**Needs:** 
* A text editor or IDE (e.g. Visual Studio Code)
* A web browser (e.g. Google Chrome) for testing
* A CSS preprocessor (optional)
