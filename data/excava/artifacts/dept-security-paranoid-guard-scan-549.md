# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-549` (dept) · 2026-07-31T12:12:48.047874+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:** Approve the Warden’s LLM Guard integration for real-time pipeline scanning.

**Plan:**
1. Warden deploys LLM Guard on the input/output pipeline.
2. Warden generates and shares a security report after each scan.
3. Bastion verifies the report confirms "No leaks or injection vectors detected."
4. Warden repeats scans for every new input/output interaction.
5. Bastion cross-checks report authenticity with prior scans.
6. Warden logs all scan results for audit trails.

**What changed:** LLM Guard now actively monitors the pipeline in real time.
