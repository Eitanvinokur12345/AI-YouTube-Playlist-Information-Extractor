# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-485` (dept) · 2026-07-31T22:44:34.413418+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the LLM Guard scanner on the input/output stream to detect injection or leakage.
2. Verify the LLM Guard container is running and healthy using ToolHive.
3. Confirm the scanner is operational and ready to detect leaks or injection.
4. Proceed only if the scanner returns "CLEAN" and the container is "HEALTHY."
5. Close the room if both conditions are met.

**What changed:** Room closed after security verification.
