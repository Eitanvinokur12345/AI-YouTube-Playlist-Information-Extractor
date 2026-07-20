# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-491` (dept) · 2026-07-20T17:32:11.735705+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt Llama3.1-8B-32K as the default for EXCAVA now—run a 100K-token stress test on Mistral Large 2.1 by EOD Friday; if it passes, switch to it next sprint. Torque owns the stress test and quality drop measurement.

**Plan:**
1. Deploy Llama3.1-8B-32K as EXCAVA’s default model immediately.
2. Torque to execute a 100K-token stress test on Mistral Large 2.1 by EOD Friday.
3. Measure output quality drop during the stress test (Torque).
4. If Mistral Large 2.1 passes the stress test, schedule its adoption for the next sprint.
5. Maintain Llama3.1-8B-32K as the fallback until Mistral is validated.
6. Log all test results in the EXCAVA model comparison repo.

**What changed:**
Default model switched to Llama3.1-8B-32K pending Mistral Large 2.1 validation.
