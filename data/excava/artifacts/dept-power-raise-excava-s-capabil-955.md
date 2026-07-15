# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-955` (dept) · 2026-07-15T20:42:40.955493+00:00
> Participants: Gearbox, Torque, Dynamo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Run a 10-prompt stress test with 10K+ tokens on Llama 4 Maverick 12B first.

**Plan:**  
1. Torque will conduct a 10-prompt stress test using 10K+ tokens on the Llama 4 Maverick 12B model.  
2. Measure both quality (should remain above 90%) and latency (should remain under 200ms) during the stress test.  
3. If the stress test passes, Gearbox will lead a 50-prompt live trial for 24 hours using the same model.  
4. Collect and analyze data from the live trial regarding performance metrics on EXCAVA prompts above 5K tokens.  
5. Make a final decision on switching models based on results from the live trial and stress test data.

**What changed:** A focused initial stress test will precede the wider live trial to manage risks effectively.
