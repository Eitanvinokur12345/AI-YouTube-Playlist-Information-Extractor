# [Access's initiative] Implement a hidden skip link that appears when focused via keyboard

> accessibility · task `access-s-initiative-impl-15087` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Implement a visually hidden skip link that becomes visible when focused via keyboard, ensuring keyboard users can bypass repetitive navigation.

**Steps:**
1. **Create the skip link HTML**
   Add `<a href="#main" class="skip-link">Skip to main content</a>` as the first focusable element in `<body>`.

2. **Add CSS for hidden/visible states**
   ```css
   .skip-link {
     position: absolute;
     left: -9999px;
     top: 0;
     background: #000;
     color: #fff;
     padding: 8px;
     z-index: 100;
     transition: left 0.3s;
   }
   .skip-link:focus {
     left: 0;
   }
   ```

3. **Add target anchor in main content**
   Insert `<main id="main" tabindex="-1">` at the start of the main content section.

4. **Test keyboard navigation**
   - Tab to the skip link (should appear).
   - Activate it (should jump to `#main`).
   - Verify focus is trapped in `#main` (optional: add `tabindex="-1"` to focusable children).

**Needs:**
- Access to the HTML template file (e.g., `index.html` or equivalent).
- Ability to edit CSS (e.g., `styles.css` or inline `<style>`).
- Keyboard for testing (no screen reader required for basic validation).
```
