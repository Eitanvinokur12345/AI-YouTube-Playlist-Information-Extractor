# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-975` (dept) · 2026-07-29T21:13:17.500896+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**
**Plan:**
1. Run the LLM Guard scanner on all conversation inputs/outputs to detect leaks or injection attempts.
2. Verify all referenced elements (e.g., files, links, tools) are real and accessible.
3. Cross-check scanner results with manual review for false positives/negatives.
4. If threats detected, quarantine affected data and re-scan.
5. Log scan results and actions taken for audit.
6. Proceed only if no confirmed threats remain.

**What changed:** Scanner integration and verification steps added to enforce paranoid guard protocol.
