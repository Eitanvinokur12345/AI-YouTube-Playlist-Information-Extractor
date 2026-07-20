# [Access's initiative] Implement a **focus-triggered skip link**—high-contrast, full-width, visually hidden until focus arrives, then revealed—

> accessibility · task `access-s-initiative-impl-69455` · **EXECUTION PLAN — NOT yet executed** · by groq/llama-3.3-70b-versatile

**Approach:** Implement a focus-triggered skip link using HTML, CSS, and JavaScript to enhance accessibility.
1. **Create the skip link element**: Add an HTML element, such as an anchor tag (`<a>`) with a class of "skip-link", to the top of the page, containing the text "Skip to main content".
2. **Style the skip link for visual hiding and revealing**: Write CSS to make the skip link visually hidden by default, using properties like `position: absolute`, `white-space: nowrap`, and `transform: translateY(-100%)`, and then reveal it when focused using the `:focus` pseudo-class, removing the `transform` property and adjusting visibility.
3. **Ensure screen reader compatibility**: Use JavaScript to add an `aria-label` attribute and ensure that the skip link is announced by screen readers when focused, and that the link's destination is correctly identified.
**Needs:** A code editor, a terminal or command prompt for running build tools, and a screen reader like NVDA or VoiceOver for testing.
