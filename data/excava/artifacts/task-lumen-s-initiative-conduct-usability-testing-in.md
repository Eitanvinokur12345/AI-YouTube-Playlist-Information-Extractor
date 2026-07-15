# [Lumen's initiative] Conduct usability testing in varied lighting conditions to identify real accessibility issues before implementing any vi

> visualization · task `lumen-s-initiative-condu-9308` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Conduct controlled usability tests across lighting conditions to surface real-world accessibility issues before visual implementation.

**Steps:**
1. **Prepare test environment**
   - Set up a controlled lighting rig (3 conditions: bright daylight, dim ambient, low contrast) using standard lamps (e.g., Philips Hue) and a light meter (e.g., Sekonic L-308X).
   - Use a real device (e.g., iPhone 15 Pro, Samsung Galaxy S23) with system-wide font scaling (100%, 125%, 150%) and dark/light mode toggles.
   - Create a test UI in Figma with static screens (buttons, text, icons) matching the artifact’s specs.

2. **Recruit participants**
   - Target 5 users with varying visual impairments (e.g., low vision, color blindness) via local disability advocacy groups or platforms like UserTesting.com.
   - Screen for familiarity with mobile apps (exclude designers/developers).

3. **Execute tests**
   - Run 15-minute sessions per participant using a scripted task list (e.g., "Find and tap the primary CTA," "Read the body text").
   - Record screen + audio via QuickTime (iOS) or AZ Screen Recorder (Android).
   - Use a lux meter to log ambient light at each condition (target: 500 lux, 50 lux, 10 lux).

4. **Analyze findings**
   - Transcribe recordings and tag issues (e.g., "button unreadable at 10 lux," "text overlaps at 125% scaling").
   - Cross-reference with WCAG 2.2 AA
