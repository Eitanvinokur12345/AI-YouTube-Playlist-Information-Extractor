# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-245` (dept) · 2026-07-09T15:05:15.931384+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:** Prioritize runtime behavioral verification over static filesystem scans.

**Plan:**
1. Deploy `strace -f -e trace=execve,open,read -p $(pgrep -f 'critical_binary')` to log syscalls from target processes, flagging deviations in `execve`/`open` paths.
2. Capture memory dumps with `gcore $(pgrep -f 'critical_binary')` and analyze for injected payloads, ROP chains, or deserialized anomalies.
3. Cross-reference syscall logs with filesystem integrity checks (`find / -type l -xtype l -print`) to correlate runtime behavior with static artifacts.
4. Validate serialized data (e.g., JSON/XML) for injection vectors using schema-aware parsers or fuzz testing.
5. Implement runtime payload validation for SQLi/XSS by instrumenting interpreters (e.g., Python’s `ast.literal_eval` for deserialization).
6. Schedule periodic red-team exercises to test detection coverage against novel non-exec injection techniques.

**What changed:** Shifted from static filesystem sweeps to dynamic runtime verification, integrating syscall tracing, memory analysis, and payload validation to detect non-exec injection vectors.
