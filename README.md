# Plan For Coverage — website

Static site, no build step, ready for GitHub Pages.

## Before you publish

The quote form posts to Formspree (endpoint in `contact.html` and `tools/build_site.py`). Phone, email, license number and NPN are already filled in.

## Deploy to GitHub Pages

1. Create a repo (e.g. `planforcoverage`) and push this folder's contents to the `main` branch.
2. Repo → Settings → Pages → Source: *Deploy from a branch*, branch `main`, folder `/ (root)`.
3. Custom domain: the `CNAME` file already contains `planforcoverage.com`. At your registrar, add:
   - `A` records for `@` → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - `CNAME` for `www` → `<your-github-username>.github.io`
4. Back in Settings → Pages, enter `planforcoverage.com` as the custom domain and tick *Enforce HTTPS* once the certificate is issued.
5. Submit `https://planforcoverage.com/sitemap.xml` in Google Search Console.

## Quote form (no backend needed)

The form posts to Formspree. Create a free form at formspree.io, copy the endpoint, and paste it into the `action` attribute in `contact.html`. Submissions arrive in your email. Netlify Forms, Basin or Getform work the same way if you prefer.

## Structure

```
index.html              Home
about.html              About / licensing
contact.html            Quote request form
privacy.html            Privacy + SMS consent language
services/               One page per product + Medicare referral page
california/             Index + ~250 city landing pages (SEO)
assets/style.css, site.js
sitemap.xml, robots.txt, CNAME, .nojekyll
```

## City pages and the generator

The city pages are generated. To add, remove or reword them, edit `ca_cities.txt` (one `City|County` per line) and `build_site.py` in the `tools/` folder, then run `python3 tools/build_site.py`. The script regenerates every page, so make copy edits in the script, not in the HTML, or they'll be overwritten.

A note on SEO: ~250 near-identical city pages are a reasonable start, but Google treats thin duplicate pages skeptically. Over time, add one or two city-specific sentences to the pages for areas you actually work (local carriers, hospital systems, Covered California pricing region) and prune cities you don't care about.

## Future expansion (deliberately not built yet)

- **Tap-to-text link** — `<a href="sms:+14243629253">Text me</a>` next to the call button. No third party involved; opens the visitor's own messaging app.
- **WhatsApp** — a `https://wa.me/14243629253` link works the same way, but WhatsApp Business offers no data-processing agreement and keeps no server-side record (chats live only on your phone), which complicates record retention under your agent agreements.
- **Live chat widget** (Crisp, Tidio, Tawk.to) — single script tag, works on GitHub Pages.
- **AI chatbot** — needs one serverless function (Cloudflare Worker / Netlify Function) to hold the API key; the site itself can stay static. Scope it as a quote-intake bot rather than an advice bot, with a "general information, not advice" disclaimer and transcript logging.
