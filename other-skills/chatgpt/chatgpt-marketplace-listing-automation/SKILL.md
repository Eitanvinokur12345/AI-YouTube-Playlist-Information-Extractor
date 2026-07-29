---
name: chatgpt-marketplace-listing-automation
description: "Use when reselling personal items online and you want ChatGPT to price, list, and post them for you instead of doing each step by hand."
---

# ChatGPT Marketplace Listing Automation

## Overview
A four-prompt chain that turns photos of items you want to sell into priced, published
marketplace listings, using ChatGPT's ability to identify objects, write copy, and drive
its own browser to post the listing.

## Key Techniques
- Chain prompts sequentially rather than asking for everything at once — each prompt's
  output (identification, price, copy) feeds the next step.
- Let the model both estimate a realistic price AND write the listing copy from the same
  image, so the price and the pitch stay consistent.
- Use ChatGPT's agentic browser capability to publish the listing directly instead of
  manually copy-pasting into the marketplace.

## How to Apply
1. Upload photos of each item you want to sell.
2. Prompt 1 — ask ChatGPT to identify each item and estimate a realistic current market
   value / selling price from the photo.
3. Prompt 2 — ask it to write a complete marketplace listing per item: a converting title
   and description.
4. Prompt 3 — tell ChatGPT to open its own browser and create/post the listing directly
   (e.g. to Facebook Marketplace) instead of you copy-pasting it manually.
5. (Implied 4th step, not detailed on screen) use ChatGPT to handle buyer negotiation on
   your behalf once inquiries come in.

## Examples
Uploading a photo of a used item yields: an identified item name + estimated price (prompt
1), a full listing title/description (prompt 2), and an auto-published Facebook Marketplace
post (prompt 3) — without the seller writing or pasting anything themselves.

## Source
Extracted from: [I Made ChatGPT Sell My Stuff And Negotiate For Me](https://www.youtube.com/watch?v=eJg5cOqzwIo)
Channel: AI Made Easy
