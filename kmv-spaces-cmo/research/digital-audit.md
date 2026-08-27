# Digital Presence Audit

Audited August 2026. Direct fetching of kmvspaces.com and the major social platforms was blocked by network policy; findings come from search-index data, third-party portals, and screenshots of the live properties. Anything unverifiable is marked as such.

## 1. Headline finding

KMV Spaces does not have a *weak* digital presence. It has a **fragmented** one — which is a different and more fixable problem. Real audiences exist (≈20,800 on Facebook, ≈7,600 on LinkedIn), real content exists (a full YouTube library), and at least one real campaign worked. The failure is architectural: the brand is scattered across **at least seven separate owned identities**, several of them dormant, and no single one accumulates the equity.

## 2. Owned identity map — the core problem

**[OBSERVED]** Identities found for one company:

| Identity | Status | Audience |
|---|---|---|
| kmvspaces.com | Live, primary | — |
| **kmvvivaan.com** | Live, separate microsite | — |
| facebook.com/kmvspaces | **Active, main** | **~20,800** |
| facebook.com/kmvvivaan | Exists, activity unconfirmed | Unknown |
| facebook.com/kmvspaceshyd | Exists, ≥1 post found | Unknown |
| instagram.com/kmvspaces | **Active** (Reels, project content) | Unverified |
| **instagram.com/kmv_spaces** | **Dead — 0 posts, "No posts yet"** | **481 followers** |
| x.com/Kmv_Spaces | Near-dormant | **202** |
| youtube.com/@KMVSpaces | Content library, low discoverability | Unverified |
| linkedin.com/company/kmvspacesllp | Moderate activity | **~7,600** |
| linkedin.com/company/kmvgroup | Parent | ~4,097 |

**[INFERENCE]** Three specific, quantifiable leaks:

1. **481 followers on a dead Instagram account.** People searched for the brand, found `@kmv_spaces`, followed it, and receive nothing. That is an audience actively choosing the brand and being met with an empty profile.
2. **Three Facebook pages** splitting audience, ad-pixel data, review accumulation and social proof across identities. Ad audiences and lookalikes built on a fragmented pixel are materially weaker.
3. **A separate Vivaan microsite and Vivaan Facebook page** structurally guarantee that the company's best-performing project builds equity for *itself* rather than for KMV Spaces — see `/research/company.md` §3.

**Cost of the fix: near zero. Time: days.** This is the highest return-on-effort item in the entire audit.

## 3. Website

**[OBSERVED]** Information architecture is genuinely good and covers four distinct audiences — buyers (Projects, project sub-pages), landowners (Land Owners), channel partners (Business Partners), and talent (Work With Us, careers.kmvspaces.com). Also present: About Us, Contact, Newsletters, FAQ, Blogs, Search, RERA disclaimer. A WhatsApp icon, search, and phone CTA appear in the header **[OBSERVED from screenshot]**.

**[OBSERVED]** Content quality on the About page is high — a "Core Values" section (five named values with descriptions) and an "Awards & Achievements" section.

**[OBSERVED] The blog is effectively invisible.** A `/blogs` link exists in the footer, but no blog post titles or content are indexed by search. Either the page is empty, very new, or not crawlable.

**Not publicly verifiable in this environment:** page-load speed, Core Web Vitals, mobile UX quality, form conversion rates, schema/structured-data implementation, whether pricing or floor plans are gated, downloadable brochure flow, GA4/GTM/pixel configuration.

**[RECOMMENDATION] Website items to audit internally on day one:**
- Mobile page-speed (**[VERIFIED]** benchmark: every second above 2s cuts real-estate landing-page conversion ~12%; getting under 2s typically reduces CPL 20–35% — [Cognitive Marketing](https://www.cognitivemarketing.in/real-estate-digital-marketing-india/))
- Form conversion rate and mobile vs desktop split
- Whether enquiries route into a CRM or an inbox
- Whether every project page carries RERA number, floor plans, location map, and a price indication
- Schema markup for projects/organisation (feeds both Google and AI answer engines)

## 4. Search & discoverability

**[OBSERVED]** Brand search ("kmv spaces") performs well: the site ranks first with sitelinks (Our Projects, About Us, Contact Us, Work With Us, KMV Vivaan The Address), a Google Business Profile panel appears with photos, map, products and CTAs, and LinkedIn/AmbitionBox rank below.

**[INFERENCE]** **Brand search is healthy; non-brand search is the gap.** The brand ranks for its own name — which mostly captures demand that already exists. There is no evidence of visibility on the non-brand queries where new demand is discovered: "villas in Tadepalli," "gated community Amaravati," "net zero homes India," "best villa projects Vijayawada." With no indexed blog and thin deep-page content, the site has little to rank with.

This is the **single largest untapped organic channel**, and it is unusually cheap here because regional competitor content is overwhelmingly promotional rather than useful.

**[OBSERVED] Google Business Profile: 4.7★ across 33 reviews.** Products listed: KMV Vivaan Tower/Apartments, KMV Vivaan Villas. Complete with address, hours, phone, photos.

**[INFERENCE]** 4.7 is a strong rating but 33 reviews is thin for a company with hundreds of delivered homes — and it sits against **454 Justdial ratings** for the project. Google reviews carry disproportionate weight in local search and in buyer due-diligence. A structured review-generation programme among existing residents is low-cost, high-trust, and currently absent.

## 5. Social channels

| Channel | Scale | Activity | Content observed | Assessment |
|---|---|---|---|---|
| **Facebook (main)** | ~20,800 | Active | "Celebrating the Handover at KMV Vivaan," "Favourite Spot at KMV Vivaan" | Largest audience; handover content is genuinely good social proof |
| **LinkedIn** | ~7,600 | Moderate | Project promos, hiring (QS, Senior Architect, Graphic Designer, FMS), #realestate posts | Under-used for the B2B/HNI/channel-partner audience it actually reaches |
| **Instagram (active)** | Unverified | Active, Reels | Handovers, lifestyle, hiring | Content mix diluted across buyer and recruitment audiences |
| **Instagram (dead)** | 481 | **Zero posts** | — | Pure leak |
| **X** | 202 | Near-dormant | ₹10,000 photo contest (Jan 2024) | Lowest priority channel; the contest, however, is the key finding |
| **YouTube** | Unverified | Library exists | "Vivaan by KMV Spaces," "Life at VIVAAN," "Why Vivaan?," "KMV Spaces Testimonials" (Jul 2024), "KMV Spaces Corporate Video," founder playlists | **Right content, wrong distribution** |

**[INFERENCE] YouTube is the most under-exploited owned asset.** The library already contains exactly the formats that sell high-ticket homes — testimonials, lifestyle films, a corporate film, founder content. What is missing is discoverability (SEO titling, thumbnails, description/link structure) and cadence. Video is also the only format that can carry a site-visit experience to an NRI buyer who cannot fly in. Fixing distribution on content that already exists is cheaper than making new content.

## 6. Campaigns and paid media

**[VERIFIED]** One documented consumer campaign: **"Capture the Tallest Building in Vijayawada"** photo contest, January 2024, prize up to ₹10,000, tied to KMV Vivaan Tower.

**[INFERENCE]** This was a genuinely smart campaign and nobody appears to have noticed. It converted a physical asset (the city's tallest building) into participatory user-generated content, at trivial cost, with built-in local reach. It is repeatable seasonally and across projects. That it ran once, on the company's weakest channel, and was not systematised is the clearest single illustration of the gap between KMV's instincts and its marketing infrastructure.

**[OBSERVED]** No verifiable evidence of Google Ads, Meta Ads, YouTube advertising, influencer partnerships, or an external agency. Whether paid media is running is *Not publicly available* and is a day-one internal question.

**[OBSERVED]** A **Business Partners** (channel partner/commission) programme exists — B2B distribution, not consumer campaign activity.

## 7. Reputation

| Source | Rating | Volume |
|---|---|---|
| Justdial (KMV Vivaan) | **4.2 / 5** | **454 ratings** |
| Google (KMV Spaces) | **4.7 / 5** | **33 reviews** |

**[VERIFIED]** Positive themes: security features, senior-citizen-friendly design, community interaction.
**[VERIFIED]** Recurring criticisms: **high pricing**, **water quality (no RO system)**, **possession delay (~1.5 years, attributed to sand availability)**.

No RERA tribunal or consumer-forum records surfaced — but given search-only access this is *absence of evidence*, not a clean record, and should be verified internally.

**[INFERENCE]** A 4.2/5 across 454 ratings is a genuinely good result and an under-used marketing asset. The three criticisms are specific and operational rather than reputational — which makes them addressable. See `/research/traya.md` §2.7: these are the exact objections TRAYA's sales team will face, handed over free.

## 8. Digital gap summary

| Gap | Evidence | Impact | Priority |
|---|---|---|---|
| Seven-plus fragmented identities; dead IG with 481 followers; 3 FB pages | **[OBSERVED]** | Splits audience, pixel data, reviews, search authority | **P0** |
| No indexed blog / non-brand search invisibility | **[OBSERVED]** | Zero top-of-funnel organic discovery | **P0** |
| Lead capture and CRM routing unverifiable | Not publicly available | Potential direct revenue leakage | **P0 (audit)** |
| YouTube content undistributed | **[OBSERVED]** | Best-fit content for high-ticket sale not reaching buyers | **P1** |
| Only 33 Google reviews vs 454 Justdial | **[OBSERVED]** | Weak local-search trust signal | **P1** |
| Proven contest format not systematised | **[VERIFIED]** | Repeatable low-cost reach unused | **P1** |
| Two IGBC certifications barely marketed | **[VERIFIED]** | Sole monopoly asset generating no demand | **P0** |
| Paid media existence/efficiency unknown | Not publicly available | Cannot assess ROI | **P0 (audit)** |
| Broker outranked developer on TRAYA news | **[OBSERVED]** | Loss of launch narrative and first-party leads | **P1** |
| Founder press (HEALTHWAY) disconnected from brand | **[VERIFIED]** | Free credibility unused | **P2** |
| USA toll-free line with no visible NRI programme | **[OBSERVED]** | Either an unused asset or an unmanaged promise | **P2** |
