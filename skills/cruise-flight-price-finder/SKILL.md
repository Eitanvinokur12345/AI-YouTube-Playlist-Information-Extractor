---
name: cruise-flight-price-finder
description: "Use when comparing cruise and flight prices together for a trip, since no consumer tool like Google Flights exists for cruises."
---

# Cruise & Flight Price Finder

## Overview
A Claude Code skill that fills the gap Google Flights leaves for cruises: given travel dates
and an ideal trip, it pulls live cruise pricing through Apify and cross-checks it against a
Google Flights scraper, returning the cheapest cruise-and-flight combination together.

## Key Techniques
- Ask the user for dates and their ideal trip shape as structured input.
- Pull cruise pricing data via an Apify actor/scraper (no first-party cruise price API exists).
- Cross-check candidate dates against a Google Flights scraper for matching flight costs.
- Present a short list (top picks) and a full list, plus a direct booking link.

## How to Apply
1. Collect the user's travel window and trip preferences (destination region, cabin type, etc.).
2. Query cruise pricing through an Apify-based scraper for that window.
3. For each candidate cruise date, query a Google Flights scraper for matching flight prices.
4. Combine cruise + flight cost per option, rank by total price, and output a short list, a full
   list, and the booking link for the top pick.

## Examples
The video shows a single command that takes trip dates/preferences and returns the cheapest
cruise-plus-flight combination, sourced from Apify cruise data cross-checked against scraped
Google Flights pricing.

## Source
Extracted from: [One Claude Skills Finds Your Cheapest Cruise & Flight](https://www.youtube.com/watch?v=frZ6QZ1FM6I)
Channel: Charlie Automates
