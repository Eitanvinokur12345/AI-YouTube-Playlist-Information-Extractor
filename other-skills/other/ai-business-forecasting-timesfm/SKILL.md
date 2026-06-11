---
name: ai-business-forecasting-timesfm
description: "Use when you need to forecast business metrics (sales, traffic, demand) from historical data using a zero-shot open-source model, without ML expertise."
---

# AI Business Forecasting with TimesFM

## Overview
Google's TimesFM is an open-source time-series foundation model that produces business forecasts from historical data without any fine-tuning or data science expertise. It handles sales, inventory demand, and traffic forecasting as a zero-shot task—just provide your historical time series and get predictions back.

## Key Techniques
- Provide historical time-series data (CSV or DataFrame) directly to TimesFM
- Use zero-shot mode—no training or fine-tuning required
- Combine with Claude for natural-language interpretation of forecasts

## How to Apply
1. Install TimesFM from the Google GitHub repo
2. Prepare your historical data as a time series (date column + value column)
3. Load into TimesFM and call the forecast method
4. Specify forecast horizon (e.g., next 30 days)
5. Export the predictions and visualize with matplotlib or a BI tool
6. Use Claude to interpret the forecast in plain English for stakeholders

## Examples
- Forecasting next quarter's sales from 2 years of daily revenue data
- Predicting website traffic spikes before seasonal campaigns
- Estimating inventory demand for a retail product line

## Source
Extracted from: [Free AI that predicts your sales before they happen](https://www.youtube.com/watch?v=enz9BsazyN0)
Channel: Sebastian Hardy | AI Marketing
