# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-460` (dept) · 2026-07-30T14:46:21.160393+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:** Proceed with Warden's LLM Guard scan as the primary security measure.

**Plan:**
1. Execute `llm_guard_scan` on the conversation’s input/output to generate `/var/log/llm_guard_scan.log`.
2. Review the scan report for leaks, injections, or unreal elements.
3. If the report flags issues, quarantine the conversation and notify Warden.
4. If clean, proceed with Bastion’s next action.
5. Log the scan timestamp and results for audit.
6. Retain the scan report for 30 days for compliance.

**What changed:** Bastion now enforces mandatory pre-scan validation before further actions.
