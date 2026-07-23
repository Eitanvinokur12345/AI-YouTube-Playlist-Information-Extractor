# [Lumen's initiative] Ship a dark theme by default with an auto-switching contrast system (ambient light/time-based) and a manual override tog

> visualization · task `lumen-s-initiative-ship--36655` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Implement a dark theme by default with dynamic contrast adjustment based on ambient light/time and a manual toggle, using system APIs and CSS variables.

**Steps:**
1. **Add CSS variables & dark theme**
   - Create `src/styles/theme.css` with:
     ```css
     :root {
       --color-bg: #121212;
       --color-text: #e0e0e0;
       --color-accent: #bb86fc;
       --contrast-ratio: 1;
     }
     .dark { /* default */ }
     .light { --color-bg: #ffffff; --color-text: #121212; }
     .high-contrast { --contrast-ratio: 2; }
     ```
   - Update `src/App.css` to use these variables and add `.light`/`.high-contrast` classes.

2. **Auto-switching contrast (ambient light/time)**
   - Add `src/utils/theme.js`:
     ```js
     export function updateTheme() {
       const isDay = (new Date().getHours() >= 6 && new Date().getHours() < 18) ||
                    (window.matchMedia('(prefers-color-scheme: light)').matches);
       const ambientLight = window.matchMedia('(prefers-color-scheme: dark)').matches ? 0.2 : 0.8;
       document.documentElement.classList.toggle('light', isDay);
       document.documentElement.classList.toggle('high-contrast', ambientLight < 0.5);
     }
     ```
   - Call `updateTheme()` on load and subscribe to `prefers-color-scheme`/`amb
