# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-423` (dept) · 2026-07-31T17:27:34.072873+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run LLM Guard’s input/output scanner on the active conversation to detect leaks, injection, or fake elements.
2. Generate a real-time security report confirming the integrity of all exchanged data.
3. Verify all elements are real (not fake/dead) based on the scan results.
4. Declare the conversation secure if no anomalies are detected.
5. Close the room upon confirmation of security.

**What changed:** Room closed after successful security verification.
