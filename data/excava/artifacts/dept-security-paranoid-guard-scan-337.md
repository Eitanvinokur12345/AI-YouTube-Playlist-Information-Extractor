# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-337` (dept) · 2026-07-31T17:00:17.484705+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run LLM Guard’s input/output scanner on the active conversation to detect leaks, injections, or unreal elements.
2. Verify the scan report confirms session integrity (no anomalies detected).
3. Declare the conversation secure if the scan passes.
4. Proceed with Bastion’s declaration of security.
5. Log the scan results and security status for audit.
6. Close the room with the confirmed secure status.

**What changed:** Session integrity confirmed via LLM Guard scan.
