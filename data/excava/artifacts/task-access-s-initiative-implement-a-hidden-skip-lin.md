# [Access's initiative] Implement a hidden skip link that appears when focused via keyboard, delivering WCAG compliance and better keyboard navi

> accessibility · task `access-s-initiative-impl-16100` · **EXECUTION PLAN — NOT yet executed** · by groq/llama-3.3-70b-versatile

**Approach:** Implement a hidden skip link using HTML, CSS, and JavaScript to ensure WCAG compliance and better keyboard navigation.
**Steps:**
1. Create a new HTML element for the skip link, adding it to the top of the page's structure, and assign a `tabindex` attribute to enable keyboard focus.
2. Write CSS to visually hide the skip link by default, using `position: absolute` and `clip: rect(1px, 1px, 1px, 1px)`, and then make it visible when focused using the `:focus` pseudo-class.
3. Add JavaScript to handle the skip link's functionality, listening for the `keydown` event to check if the skip link is focused, and then scrolling to the main content area using `window.location` or `window.scrollTo`.
**Needs:** 
* A code editor (e.g., Visual Studio Code)
* A web browser (e.g., Google Chrome) for testing
* Basic knowledge of HTML, CSS, and JavaScript
* A screen reader (e.g., NVDA) for accessibility testing
