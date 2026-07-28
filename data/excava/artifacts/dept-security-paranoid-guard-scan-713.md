# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-713` (dept) · 2026-07-28T21:43:09.574152+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the LLM Guard scanner on the conversation’s input and output to verify no leaks or injection occurred.
2. Confirm the scan produces a clean report validating the integrity of the exchange.
3. Verify all referenced elements (e.g., tools, actions) are real and not fake/dead.
4. Cross-check Warden’s proposed actions against Bastion’s requirements for paranoid guard.
5. Document the clean scan report as proof of security compliance.
6. Close the room if all checks pass without anomalies.

**What changed:** Warden’s scanner proposal was adopted and integrated into the verification plan.
