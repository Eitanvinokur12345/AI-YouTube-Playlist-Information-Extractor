# [Lumen's initiative] Ship a dark theme by default with an auto-switching contrast system based on ambient light and battery level, plus a per

> visualization · task `lumen-s-initiative-ship--65338` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Implement a system-wide dark theme with auto-switching contrast based on ambient light and battery level, plus user override persistence.

**Steps:**
1. **Add theme system**
   - Create `src/theme/` with `dark.css` and `light.css` (minimal contrast variants).
   - Add `src/theme/switcher.js` to detect ambient light (via `AmbientLightSensor` API) and battery level (via `navigator.getBattery()`).
   - Implement `theme.set(themeName)` and `theme.savePreference(themeName)` using `localStorage`.

2. **Integrate with UI framework**
   - Patch the main CSS bundle to include `dark.css` as default.
   - Modify the app’s root component to call `theme.switcher.init()` on load.
   - Add a toggle button in the settings panel that calls `theme.set('auto')` or `theme.set('dark')`/`theme.set('light')`.

3. **Add persistence**
   - Extend `theme.savePreference()` to store user override in `localStorage` under `userTheme`.
   - On init, check `userTheme` first; if unset, fall back to auto-switching logic.

4. **Test & validate**
   - Run `npm run test:theme` (add this script to `package.json` if missing) to verify contrast changes in mocked light/dark/battery states.
   - Manually test on devices with/without ambient light sensor.

5. **Deploy**
   - Commit changes to `src/theme/` and framework patches.
   - Tag release `v2.1.0-theme-auto` and push to `main`.

**Needs:**
- Access to `
