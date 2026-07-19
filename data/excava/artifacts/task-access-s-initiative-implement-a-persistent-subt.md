# [Access's initiative] Implement a **persistent, subtle skip link** (1px by 1px underline) at the top of every page, visible only when keyboard

> accessibility · task `access-s-initiative-impl-17354` · **EXECUTION PLAN — NOT yet executed** · by groq/llama-3.3-70b-versatile

**Approach:** Implement a persistent, subtle skip link at the top of every page, visible only when keyboard navigation is used.
**Steps:**
1. Create a new CSS class `.skip-link` with properties `position: absolute; width: 1px; height: 1px; overflow: hidden;` and add an `:focus` state with `width: auto; height: auto;` to make it visible when focused.
2. Add an HTML element with the class `.skip-link` to the top of every page, containing a link to the main content area, using `<a href="#main-content" class="skip-link">Skip to main content</a>`.
3. Modify the existing CSS file to include the `.skip-link` class and add a `1px` underline to the link when focused, using `:focus { text-decoration: underline; }`.
**Needs:**
* Access to the website's CSS file
* Ability to edit HTML files for each page
* A code editor or IDE (e.g. Visual Studio Code) to implement the changes
