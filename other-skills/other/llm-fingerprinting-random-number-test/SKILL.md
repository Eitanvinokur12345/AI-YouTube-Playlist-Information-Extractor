---
name: llm-fingerprinting-random-number-test
description: "Use when you need to guess which underlying LLM powers a black-box AI product or feature, without API access."
---

# LLM Fingerprinting via Random-Number Test

## Overview
Different LLMs have distinct statistical biases in how they generate a random number when asked. Repeating the request and tallying the distribution of answers acts as a lightweight fingerprint for telling models apart, without needing API-level access.

## Key Techniques
- Ask the model to "pick a random number between 1 and 100" (or similar) many times in independent turns/sessions.
- Tally the frequency distribution of the returned numbers.
- Compare the shape of that distribution against known reference distributions for candidate models.

## How to Apply
1. Send the same random-number prompt to the target product N times (fresh context each time).
2. Record every returned number.
3. Build a frequency histogram.
4. Compare against reference histograms for candidate models (build your own references by running the same test against known models).
5. The closest-matching distribution is your best guess at the underlying model (reported ~80% accuracy in the source video).

## Examples
Source video demonstrates asking a chat product for random numbers repeatedly and shows the skewed distribution differs measurably between models, letting the presenter infer which model was actually running behind an unlabeled product.

## Source
Extracted from: [Every AI has a fingerprint and here'''s how to find it](https://www.youtube.com/watch?v=D6cBsAWwCd0)
Channel: Will Francis
