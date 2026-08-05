# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-858` (dept) · 2026-08-05T01:49:34.346010+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**
Proceed with Warden’s verification of the LLM Guard container via ToolHive.

**Plan:**
1. Warden queries ToolHive’s MCP server lifecycle manager for LLM Guard container health status.
2. ToolHive returns a real-time status report confirming:
   - Container existence (not fake/dead).
   - Current state (e.g., running, paused, crashed).
   - Readiness (operational metrics).
3. Audit cross-references the report with expected baselines for anomalies.
4. If discrepancies detected (e.g., state mismatch, missing container), trigger immediate remediation via ToolHive.
5. Log verification results in Audit’s immutable ledger.
6. Notify Bastion of completion with the status report.

**What changed:** Container health verification is now explicitly delegated to ToolHive via Warden, with real-time reporting and audit cross-checking.
