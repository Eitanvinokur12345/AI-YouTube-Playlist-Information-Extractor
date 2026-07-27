# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-590` (dept) · 2026-07-27T21:57:58.167866+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run LLM Guard scanner on the conversation’s input/output stream to detect leaks/injection.
2. Verify all elements (inputs/outputs) are real and not fake/dead.
3. Generate a security report confirming integrity of the interaction.
4. Execute Warden’s actions post-verification.
5. Close the room upon successful validation.

**What changed:** Room closed after security verification.
