# Skunara × Claude for Startups — Complete A-to-Z Setup Guide

**Date:** 8 October 2026
**Goal:** Anthropic ke **Claude for Startups** program me apply karna
**Reward (agar approve hua):** 1 saal Claude Team (5 Premium seats, Claude Code included) + **$1,000** Claude API credits (6 mahine me use karne hain) + partner perks
**Total kharcha:** ₹1,854.29 (sirf domain — baaki sab free)

---

## Kahani short me

Claude for Startups program early-stage startups ko free me Claude Team aur API credits deta hai. Apply karne ke liye chahiye tha: ek real company website (custom domain par), company email, public code, aur Claude Console account. Ye guide batata hai ki 8 Oct 2026 ko ye sab ek din me kaise setup kiya gaya — step by step, taaki dobara karna ho to yehi follow karo.

---

## Step 1 — Domain khareedo: skunara.dev

**Kya kiya:** `skunara.dev` domain GoDaddy se 1 saal ke liye khareeda.

- **Account:** Personal GoDaddy account (Google sign-in: krishnasaxena987155@gmail.com)
- **Registrant:** Krishna Saxena, 150 Old Awas Vikas, Moradabad, UP 244001, India
- **Kimmat:** ₹1,854.29 (subtotal ₹1,552.43 + GST/fees ₹301.86)
- **Renewal:** October 2027 se ₹2,329.13/saal
- **Important rule (user ka order):** "Koi protection mat lena… sirf domain" — koi privacy protection, email, ya hosting add-on NAHI liya

**Kyoon zaroori tha:** Program application me company website aur company-domain email chahiye tha. Gmail se apply karne par application kamzor lagti.

> ⚠️ Lesson: Client ka GoDaddy account (fablootsofficial@gmail.com) personal kaam ke liye kabhi use mat karo. Hamesha apne personal account se khareedo.

---

## Step 2 — Website live karo: Vercel + DNS

**Kya kiya:** Skunara ki public landing site banayi aur `skunara.dev` par live ki.

- **Source code:** `~/workspace/skunara-public/` (local)
- **Design:** Editorial "paper/ink/deep-green" theme — jaanboojhkar generic AI-template look NAHI diya
- **Hosting:** Vercel project `skunara` (Project ID: `prj_LyBNDcV6oseJjeMCoHyueKJ0SOOe`)
- **Live URLs:**
  - https://skunara.dev
  - https://www.skunara.dev
  - Preview: https://skunara-carvenza.vercel.app/
- **GoDaddy DNS records (nameservers GoDaddy ke hi rahe):**

| Type  | Host | Value                  |
|-------|------|------------------------|
| A     | @    | 76.76.21.21            |
| CNAME | www  | cname.vercel-dns.com   |

- **Verify:** Dono URLs par HTTPS 200 aaya

**Kyoon zaroori tha:** Anthropic wale website kholkar dekhte hain ki company real hai ya nahi. Live professional site = trust.

---

## Step 3 — Company email: contact@skunara.dev

**Kya kiya:** Free email forwarding setup ki (koi paid mailbox nahi liya).

- **Service:** ImprovMX (free plan)
- **Alias:** `contact@skunara.dev` → `krishnasaxena987155@gmail.com` (Gmail me forward hota hai)
- **GoDaddy DNS records:**

| Type | Host | Value                          | Priority |
|------|------|--------------------------------|----------|
| MX   | @    | mx1.improvmx.com               | 10       |
| MX   | @    | mx2.improvmx.com               | 20       |
| TXT  | @    | v=spf1 include:spf.improvmx.com ~all | —  |

- **Verify:** ImprovMX dashboard me domain "Active" (MX + SPF green checks). GitHub ka verification email `contact@skunara.dev` par bheja → Gmail me aa gaya. End-to-end working.

**Kyoon zaroori tha:** Application "Applying as" field me company email chahiye tha. `contact@skunara.dev` professional lagta hai, Gmail nahi.

> 🔐 ImprovMX password sirf yahan hai: `~/workspace/skunara-public/.secrets/improvmx_pw` (kabhi chat ya repo me mat daalna)

---

## Step 4 — GitHub: public repo

**Kya kiya:** Naya GitHub account + public repository banaya.

- **Username:** `skunara`
- **Email:** `contact@skunara.dev` (verified)
- **Repo:** https://github.com/skunara/skunara
- **Branch:** master
- **Andar kya hai:** Sirf public marketing site + docs
- **Andar kya NAHI hai:** Asli product/backend code (`~/workspace/skunara/` private raha), koi API key, database password, ya secret nahi

**Kyoon zaroori tha:** Application me code ka proof chahiye tha. Public repo dikhata hai ki real kaam ho raha hai.

> 🔐 GitHub password + PAT (30-day, repo scope) sirf yahan: `~/workspace/skunara-public/.secrets/github_pw` aur `github_pat`
> ⚠️ Signup form me Country default "United Kingdom" aaya tha — baad me GitHub settings me India kar dena.

---

## Step 5 — Claude Console account

**Kya kiya:** https://platform.claude.com par account banaya.

- **Email:** `contact@skunara.dev` (magic-link sign-in)
- **Name:** Krishna Saxena
- **Organization:** Skunara (type: Small or medium business, location: India)
- **API use-case:** product analysis, company-profile generation, margin/fragility reasoning (Data Analysis tag)
- **Onboarding choices:** Customers = External, API India ke bahar bhi use hogi = Yes
- **Dashboard:** https://platform.claude.com/dashboard

---

## Step 6 — Application submit

**Kya kiya:** https://platform.claude.com/offers/startups-application par form bharkar **Submit** kiya (8 Oct 2026).

**Jo answers diye gaye:**

| Field | Answer |
|---|---|
| Applying as | contact@skunara.dev |
| Organization | Skunara |
| Name | Krishna Saxena |
| Job title | Founder |
| Company website | https://skunara.dev |
| Country | India |
| Founded | October 2026 |
| Latest funding round | Not yet raised |
| Anthropic monthly AI spend | 0–20% |
| Support chahiye | API credits: Claude API for product analysis, company-profile generation, aur margin/fragility reasoning (daily digest pipeline). Team seats: Claude Code for daily development. |
| What are you building | Skunara ek AI product-intelligence platform hai jo e-commerce sellers ko winning products discover karne me help karta hai — roz live marketplaces scan karke LLMs se shortlisted picks: written reasoning, margin analysis, real supplier links. Claude API se sellers ke morning digests me deeper product reasoning. Code: https://github.com/skunara/skunara |

**Submit ke baad message:** *"Thanks for submitting! Our team is reviewing your application and will follow up with next steps. Please allow for up to 72 hours."*

**Status:** ⏳ Review pending. Decision `contact@skunara.dev` (Gmail forwarded) par aayega. Roz subah auto-check lagaya gaya hai — mail aate hi turant pata chal jayega.

---

## Approval kaise milega? (Tips)

Ye program har application ko manually review karta hai — approval guaranteed nahi hai. Lekin in cheezon se chances badhte hain:

1. **Real, live product dikhao** — sirf idea nahi. Hamare paas live site + public repo + working product hai.
2. **Custom domain + company email** — `skunara.dev` aur `contact@skunara.dev` professionalism dikhate hain. Gmail se apply karna kamzor padta.
3. **Claude ka specific use-case likho** — vague "we use AI" nahi. Hamne likha: product analysis, company-profile generation, margin/fragility reasoning, daily digest pipeline, Claude Code for development. Reviewer ko exact pata chalta hai credits kahan lagenge.
4. **Early-stage dikho** — ye program pre-seed/seed startups ke liye hai. "Not yet raised" + "Founded Oct 2026" sahi bracket me hai.
5. **Details consistent rakho** — website, GitHub, email, application me company ka naam aur kaam ek jaisa ho.
6. **Hype mat pheko** — dollar figure ya exaggerated claims description me mat daalo (hamne $1,000 ka zikr description se hataya tha — wahi sahi call tha).
7. **72 hours wait karo** — dobara apply ya follow-up spam mat karo.

**Approve hua to redeem karna hai:**
- 1-year Claude Team (up to 5 Premium seats)
- Claude Code access
- $1,000 first-party Claude API credits (grant ke 6 mahine ke andar use karne hain)
- Partner perks

---

## Poora kharcha (8 Oct 2026)

| Cheez | Kharcha |
|---|---|
| Domain skunara.dev (1 saal) | ₹1,854.29 |
| Vercel hosting | Free |
| ImprovMX email forwarding | Free |
| GitHub account + public repo | Free |
| Claude Console | Free |
| Application | Free |
| **Total** | **₹1,854.29** |

---

## Important links

- 🌐 Website: https://skunara.dev
- 💻 Code: https://github.com/skunara/skunara
- 📝 Program: https://claude.com/programs/startups
- 🖥️ Console: https://platform.claude.com/dashboard
- 📄 Application page: https://platform.claude.com/offers/startups-application

## Secrets kahan hain (values kabhi share mat karna)

- `~/workspace/skunara-public/.secrets/improvmx_pw` — ImprovMX password
- `~/workspace/skunara-public/.secrets/github_pw` — GitHub password
- `~/workspace/skunara-public/.secrets/github_pat` — GitHub PAT (30-day expiry)
- `~/workspace/skunara/.env` — product ke saare keys (chmod 600)

---

*Ye guide Skunara repo ka hissa hai. Kuch badle to isko update kar dena.*
