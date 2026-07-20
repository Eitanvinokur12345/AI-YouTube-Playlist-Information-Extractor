# [Access's initiative] Implement a **focus-triggered skip link**—high-contrast, full-width, appearing only after Tab key press, then collapsing

> accessibility · task `access-s-initiative-impl-68369` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
## Approach:
Implement a focus-triggered skip link that appears only after Tab key press, meets high-contrast accessibility standards, spans full width, and collapses after activation.

---

### Steps:
1. **Create skip link HTML/CSS**
   - Add `<a href="#main-content" class="skip-link">Skip to main content</a>` as the first focusable element in `<body>`.
   - Style `.skip-link` with:
     ```css
     .skip-link {
       position: absolute;
       top: -40px;
       left: 0;
       width: 100%;
       background: #000;
       color: #fff;
       padding: 8px;
       text-align: center;
       z-index: 1000;
       transition: top 0.3s;
     }
     .skip-link:focus {
       top: 0;
     }
     ```
   - Ensure `id="main-content"` exists on the primary content container (e.g., `<main id="main-content">`).

2. **Enforce high-contrast visibility**
   - Use `prefers-contrast: more` media query for stricter contrast:
     ```css
     @media (prefers-contrast: more) {
       .skip-link { background: #000; color: #fff; font-weight: bold; }
     }
     ```
   - Test with screen readers (e.g., NVDA, VoiceOver) to verify contrast and keyboard navigation.

3. **Hide skip link until focus**
   - Add `tabindex="-1"` to `#main-content` to ensure focus works.
   - Use JavaScript to ensure skip link is only visible
