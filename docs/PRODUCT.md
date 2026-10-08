# Skunara — product overview

Skunara is an AI product-intelligence platform for e-commerce sellers. It answers one question every morning: **what should I sell next?**

## Problem

Product research is the most tedious part of running an online store: hours of scrolling marketplaces, guessing at demand, spreadsheets that go stale in a week. Most sellers either copy competitors blindly or freeze on analysis.

## Solution

Skunara automates the research loop:

- **Marketplace scraper** (Python, async Playwright) collects live listings daily.
- **Company profiler** — an LLM reads what each seller sells and builds a structured profile (categories, price bands, audience).
- **AI shortlist** — each cycle, the model reviews the product pool and picks the most promising ideas, writing a reason for each: why it stands out, who it fits, the margin angle, weight and shipping fragility.
- **Digest delivery** — fresh picks land in the dashboard every morning. A product never repeats inside a company's feed.
- **Live search fallback** — when the feed runs dry for a niche, the system fires a live marketplace search and imports what it finds.

## Status

Live product with paying-structure plans (weekly tiers). The public marketing site is in this repo; the application backend is private.

## Roadmap

- Claude API integration for deeper product reasoning and margin analysis.
- Multi-marketplace coverage beyond the current sources.
- Team workspaces for agencies managing multiple stores.

## Contact

contact@skunara.dev
