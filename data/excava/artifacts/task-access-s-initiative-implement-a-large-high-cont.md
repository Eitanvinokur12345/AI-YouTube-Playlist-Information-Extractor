# [Access's initiative] Implement a **large, high-contrast skip link** that is **always visible** at the top of every page, with a **collapsible

> accessibility · task `access-s-initiative-impl-33406` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Implement a persistent, high-contrast skip link with collapsible content at the top of every page via a shared template and CSS/JS.

**Steps:**
1. **Create skip link template** (`templates/skip-link.html`):
   ```html
   <a href="#main-content" class="skip-link" aria-label="Skip to main content">Skip to main content</a>
   <div class="skip-link-collapsible" aria-hidden="true">
     <button id="skip-toggle" aria-expanded="false" aria-controls="skip-content">Options</button>
     <div id="skip-content" role="menu">
       <a href="#nav">Skip to navigation</a>
       <a href="#footer">Skip to footer</a>
     </div>
   </div>
   ```
2. **Add shared CSS** (`assets/css/skip-link.css`):
   ```css
   .skip-link {
     position: absolute;
     top: 0;
     left: 0;
     width: 100%;
     padding: 1rem;
     background: #000;
     color: #fff;
     font-size: 1.5rem;
     text-align: center;
     z-index: 1000;
   }
   .skip-link:focus {
     outline: 3px solid #ff0;
   }
   .skip-link-collapsible {
     position: absolute;
     top: 100%;
     left: 0;
     background: #000;
     color: #fff;
     padding: 0.5rem;
   }
   ```
3. **Add JS for toggle** (`assets
