# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-459` (dept) · 2026-07-30T17:48:11.997693+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run LLM Guard scanner on conversation input/output to detect leaks/injection.
2. Verify Warden’s LLM Guard scan report in `/var/log/llm_guard/w1` for clean status.
3. Confirm all elements (inputs, outputs, actions) are real and not fake/dead.
4. Proceed only if scan report is clean and verification passes.
5. Log all steps and results for audit trail.
6. Close room upon successful verification.

**What changed:** Added explicit verification of Warden’s scan report before proceeding.
