# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-620` (dept) · 2026-07-30T22:44:35.054716+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Adopt the outcome of the bake-off to determine EXCAVA's core engine.
1. **Run a 72-hour bake-off**: Between Cerebras CS-3 and Graphcore Bow Pod 64 on identical 70B-model prompts.
2. **Compare median token latency**: Measure and compare the median token latency of both systems during the bake-off.
3. **Adopt Bow Pod if latency beats CS-3 by ≥0.5%**: If Graphcore Bow Pod 64's median token latency beats Cerebras CS-3 by ≥0.5%, adopt Bow Pod as EXCAVA's core engine.
4. **Lock in CS-3 otherwise**: If the condition is not met, lock in Cerebras CS-3 as EXCAVA's core engine.
5. **Implement the chosen system**: Integrate the chosen system into EXCAVA's architecture, ensuring compatibility and optimal performance.
6. **Monitor and evaluate performance**: Continuously monitor and evaluate the performance of the chosen system to ensure it meets the desired capability bump.
**What changed:** The decision to adopt a bake-off approach to compare Cerebras CS-3 and Graphcore Bow Pod 64 before making a final decision on EXCAVA's core engine.
