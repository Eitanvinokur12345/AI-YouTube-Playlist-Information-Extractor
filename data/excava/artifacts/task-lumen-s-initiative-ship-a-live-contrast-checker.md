# [Lumen's initiative] Ship a live contrast checker in the editor that flags issues in real time without blocking submission, forcing users to 

> visualization · task `lumen-s-initiative-ship--74319` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

**Approach:**
Integrate a real-time contrast checker into the editor that flags contrast issues without blocking submission, using an existing accessibility library and editor hooks.

**Steps:**
1. **Add a contrast checker dependency**
   - Install `chroma-js` (or `tinycolor2`) via npm:
     ```bash
     npm install chroma-js --save-dev
     ```
   - Add to `package.json` under `dependencies` or `devDependencies` as needed.

2. **Create a contrast checker utility**
   - Add `src/utils/contrastChecker.js`:
     ```javascript
     import chroma from 'chroma-js';

     export function checkContrast(foreground, background) {
       const ratio = chroma.contrast(foreground, background);
       return {
         ratio,
         passes: ratio >= 4.5, // WCAG AA threshold
         message: ratio < 4.5 ? `Contrast ratio ${ratio.toFixed(2)}:1 fails WCAG AA` : null
       };
     }
     ```

3. **Integrate into the editor**
   - Hook into the editor’s `onChange` event (e.g., in `src/editor/Editor.jsx`):
     ```javascript
     import { checkContrast } from '../utils/contrastChecker';

     // Inside component
     const handleChange = (content) => {
       const { foreground, background } = extractColors(content); // Implement this
       const result = checkContrast(foreground, background);
       if (!result.passes) {
         showInlineWarning(result.message); // Non-blocking UI flag
       }
     };
     ```

4. **Add UI feedback**
   - Create a warning component (e.g., `src/components
