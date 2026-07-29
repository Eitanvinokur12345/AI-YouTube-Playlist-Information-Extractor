# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-149` (dept) · 2026-07-29T15:10:31.979289+00:00
> Participants: Ramp, Reader, Access · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Ship a high-contrast focus ring with a 125ms delay, visible until focus moves again.  

**Plan:**  
1. Update CSS to implement a high-contrast focus ring that remains visible with a 125ms delay.  
2. Ensure that the focus ring transitions to a subtle outline when focus shifts to enhance user experience.  
3. Perform accessibility testing to ensure effectiveness across various devices, especially for keyboard navigation.  
4. Conduct performance testing to confirm that the transition does not lag on slower machines.  
5. Create documentation for developers about the new focus ring implementation for future reference.  

**What changed:** Decision made to balance high-contrast visibility with distraction levels through a delayed transition.
