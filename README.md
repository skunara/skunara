# Skunara

**AI product intelligence for e-commerce sellers.** Skunara scans live marketplaces every morning and uses AI to surface winning product ideas matched to your store — with real supplier links and clear reasoning for every pick.

This repository holds the public website ([skunara.dev](https://skunara.dev)) and project docs. The application backend is private.

## What Skunara does

1. **Company profiling** — tell us what you sell; the AI builds a profile of your catalog.
2. **Live marketplace scans** — our scraper collects real listings daily.
3. **AI shortlist** — each cycle the AI picks the most promising products, with a written reason for each: why it stands out, who it fits, and the margin angle.
4. **Morning digest** — fresh picks in your dashboard and inbox. A product never repeats inside your feed.
5. **Live search fallback** — if your feed runs dry, Skunara fires a live marketplace search for your niche and imports what it finds.

## This site

Static, no build step. Open `index.html` or serve the folder:

```bash
npx serve .
# or
python3 -m http.server 8000
```

Deployed on Vercel from the `main` branch, served at `skunara.dev`.

## Project structure

```
index.html      Landing page
styles.css      Editorial theme (paper / ink / deep green)
app.js          Mobile nav, scroll reveals, footer year
assets/         Static assets
docs/           Project documentation
```

## Contact

Questions about the product, plans, or partnerships: [contact@skunara.dev](mailto:contact@skunara.dev)

Built by [Verse DKH](https://versedkh.online) — independent software studio.

## License

Site content and code in this repo are MIT licensed (see `LICENSE`), except brand assets.
