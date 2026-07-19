# [Access's initiative] Implement a **1px tall, persistent skip link underline** that shrinks to 1px on blur, tested with screen readers—owned b

> accessibility · task `access-s-initiative-impl-55779` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Implement a persistent 1px underline for skip links that shrinks to 1px on blur, ensuring WCAG 2.2 AA contrast and screen reader compatibility.

**Steps:**
1. **Add HTML/CSS:**
   - Add `<a href="#main" class="skip-link">Skip to main content</a>` before `<main>` in templates.
   - Add CSS:
     ```css
     .skip-link {
       position: absolute;
       top: -40px;
       left: 0;
       background: #005fcc;
       color: white;
       padding: 8px;
       z-index: 9999;
       text-decoration: underline;
       text-decoration-thickness: 1px;
       text-underline-offset: 2px;
       transition: text-decoration-thickness 0.2s;
     }
     .skip-link:focus {
       top: 0;
     }
     .skip-link:focus-visible {
       text-decoration-thickness: 1px;
     }
     ```

2. **Test Contrast:**
   - Verify `#005fcc` (blue) on white meets WCAG 2.2 AA (4.5:1) using [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/).

3. **Screen Reader Test:**
   - Test with NVDA (Windows), VoiceOver (macOS/iOS), and JAWS (Windows) to confirm:
     - Skip link is announced on focus.
     - Underline persists until blurred.

4. **Blur Shrink Logic:**
   - Add JS to shrink underline on blur (if CSS `:focus-visible`
