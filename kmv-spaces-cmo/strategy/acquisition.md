# Acquisition & Channel Strategy

## 1. Channel prioritisation

Priority reflects **expected contribution to bookings**, not reach. Full rationale after the table.

| Channel | Funnel stage | Audience | Priority | Primary KPI |
|---|---|---|---|---|
| **Existing customers & referral** | All | Residents, past buyers | **HIGH** | Referral bookings; cost per referral booking |
| **Channel partners / brokers** | Mid–bottom | Local HNI networks | **HIGH** | Bookings per active partner |
| **Google Search (high-intent)** | Mid–bottom | Active searchers | **HIGH** | CPSV, cost per booking |
| **Meta (FB + IG)** | Top–mid | Geo/interest/lookalike | **HIGH** | CPQL, site-visit rate |
| **Website + landing pages** | All | All traffic | **HIGH** | LP conversion rate, speed |
| **CRM + WhatsApp automation** | Mid–bottom | Captured leads | **HIGH** | Speed-to-lead, contact rate |
| **SEO / content** | Top | Researchers | **MEDIUM-HIGH** | Non-brand organic leads |
| **YouTube (organic)** | Top–mid | Researchers, NRIs | **MEDIUM-HIGH** | Video → enquiry |
| **Remarketing** | Mid–bottom | Site visitors | **MEDIUM-HIGH** | Cost per returning lead |
| **PR / earned media** | Top | Region-wide | **MEDIUM** | Coverage, brand search lift |
| **On-ground & site experience** | Bottom | Visitors | **MEDIUM** | Visit → booking rate |
| **Outdoor (site + arterial)** | Top | Local | **MEDIUM** | Brand search lift, walk-ins |
| **LinkedIn (organic)** | Top–mid | Professionals, HNI, partners | **MEDIUM** | Engagement, partner enquiries |
| **Email** | Mid | Database | **MEDIUM** | Re-engagement rate |
| **Events (resident, NRI, partner)** | Mid–bottom | Curated | **MEDIUM** | Bookings per event |
| **Google Display / YouTube ads** | Top | Broad | **LOW** initially | Assisted conversions |
| **Influencer / creator** | Top | Broad | **LOW** | Reach quality |
| **Print / radio** | Top | Mass local | **LOW** | Unmeasurable — brand only |
| **X / Twitter** | — | Minimal | **LOW** | Maintain, don't invest |

## 2. Why this ranking

**[INFERENCE] Referral and existing customers rank first** because KMV has several hundred delivered households rated 4.2/5 across 454 ratings, and a natural apartment→villa→second-home upgrade ladder. This is the cheapest, highest-converting demand available and there is no public evidence it is being systematically worked.

**[INFERENCE] Channel partners rank second** because a broker published TRAYA's pre-launch information before KMV's own channels did — distribution is already influential and currently uncontrolled. In Indian residential real estate, channel partners frequently drive a large share of premium bookings.

**[INFERENCE] Google Search outranks Meta** despite higher CPL. **[VERIFIED]** Google CPLs in Indian real estate (₹800–1,500) exceed Meta's (₹400–900), but Google lead quality measured by site-visit and booking conversion is "substantially better" ([Cognitive Marketing](https://www.cognitivemarketing.in/real-estate-digital-marketing-india/)). At ₹3 Cr AOV, quality beats cost — the reasoning in `/strategy/marketing-economics.md` §1.

**[INFERENCE] Display, influencer, print and radio rank low** because at 60 bookings/year the objective is not awareness volume, it is qualified, high-intent buyers. Mass channels generate reach that cannot be attributed and leads that cannot be qualified.

## 3. Google Search

**Campaign structure**

| Campaign | Intent | Example terms | Budget share |
|---|---|---|---|
| Brand defence | Existing demand | "kmv spaces", "kmv vivaan", "traya tadepalli" | 10% |
| Project — TRAYA | High | "villas tadepalli", "gated community tadepalli", "new projects amaravati" | 30% |
| Category — villas | High | "luxury villas vijayawada", "4bhk villa amaravati" | 25% |
| Category — apartments | High | "3bhk flats vijayawada", "ready to move apartments vijayawada" | 15% |
| Competitor conquest | High | Competitor project names | 10% |
| Sustainability niche | Medium | "net zero homes india", "igbc platinum villas" | 10% |

**[RECOMMENDATION]** Negative keywords are as important as keywords at this price point: exclude *rent, PG, hostel, 1BHK, cheap, affordable, plot, land, job, salary, careers*. Every unqualified click at ₹30+ CPC is pure waste, and unqualified leads corrupt the funnel metrics that govern budget decisions.

**[RECOMMENDATION]** Bid to **cost per qualified site visit**, not CPC or CPL. Feed CRM booking data back into Google via offline conversion imports so smart bidding optimises toward revenue rather than form fills.

## 4. Meta

| Campaign | Objective | Audience | Creative |
|---|---|---|---|
| TRAYA launch — local | Leads | Vijayawada/Guntur 35–60, HNI interests | Launch film, villa reveal |
| TRAYA — Hyderabad | Leads | Hyderabad, AP-origin signals, lookalike | "Come home to the capital region" |
| NRI | Leads | US/Gulf AP diaspora | Video walkthrough, NRI process |
| Ready-to-move apartments | Leads | Local, narrower income band | "Move in now, zero construction risk" |
| Resident proof | Traffic/video | Broad local | Testimonials, handover films |
| Remarketing | Conversions | Site visitors, video viewers, form abandoners | Objection-handling content |

**[RECOMMENDATION]** Build lookalike audiences from **actual bookers**, not from lead-form submitters. A lookalike built on people who filled a form teaches the algorithm to find form-fillers. A lookalike built on people who paid ₹3 crore teaches it to find buyers. This requires CRM→Meta conversion feedback and is one of the highest-leverage technical changes available.

**[OBSERVED]** Pixel data is currently split across at least three Facebook pages — consolidation (`/research/digital-audit.md` §2) is a prerequisite for any of this to work properly.

## 5. Landing pages

**[VERIFIED]** Every second of load time above 2s cuts real-estate landing page conversion ~12%; getting under 2s typically reduces CPL 20–35%.

**[RECOMMENDATION]** One dedicated page per project per major segment. Required elements:

1. Above the fold: project name, location, configuration, price band, single primary CTA
2. **RERA number visible** — a compliance requirement and a trust signal
3. Video walkthrough or drone footage
4. Floor plans and master plan
5. **Quantified net-zero savings** in rupees per year
6. Resident testimonials with names and faces
7. Location map with schools, hospitals, commute times
8. Developer credibility block — KMV Projects' institutional portfolio
9. Short form (name, phone, and *one* qualifying question) + WhatsApp CTA + click-to-call
10. Objection FAQ answering price, timeline, water, delivery

**[RECOMMENDATION] Form design at this price point:** fewer fields raise volume but lower quality. Add exactly one qualifying question — *"When are you looking to buy?"* or *"Budget range?"* — because at ₹3 Cr AOV, a 20% drop in volume for a 2× lift in qualification is strongly value-accretive.

## 6. Content & SEO

**[OBSERVED]** No indexed blog; no non-brand search visibility. **[INFERENCE]** This is the largest untapped organic channel and is unusually cheap here because regional competitor content is overwhelmingly promotional rather than useful.

Priority clusters:
- **"Buying in the capital region"** — process, approvals, RERA, what to check
- **"Net zero / green homes"** — what it means, what it saves, certification explained (**uncontested nationally at regional level**)
- **"Tadepalli / Amaravati locality"** — infrastructure, connectivity, price trends, schools
- **"Villa vs apartment vs plot"** — genuinely useful comparison content that reframes the plot competitor
- **"NRI buying guide"** — process, documentation, remote purchase, repatriation

**[RECOMMENDATION]** Also optimise for AI answer engines: structured schema, clear Q&A formatting, and factual, citable content. Buyers increasingly ask assistants "best villa developers in Vijayawada" — and thin regional content means the citation slot is currently winnable.

## 7. WhatsApp

**[OBSERVED]** A WhatsApp icon already appears in the site header.

**[RECOMMENDATION]** WhatsApp is the primary conversation channel in this market and should carry: instant enquiry acknowledgement (supporting the <5 minute standard), brochure and floor-plan delivery, site-visit confirmation and reminders, construction-progress updates to booked customers, and a broadcast list for existing residents. Requires WhatsApp Business API integrated with CRM — see `/strategy/crm.md`.

## 8. Budget allocation

**[ASSUMPTION] Illustrative only.** Actual allocation requires current performance data.

### Phase 1 (Months 1–3) — Prove the funnel
| Line | Share | Note |
|---|---|---|
| Google Search | 35% | Highest intent, fastest learning |
| Meta | 30% | Volume + audience building |
| Landing pages / web / tech | 15% | Foundation — one-time weighted |
| Content / SEO | 10% | Compounds later |
| Remarketing | 10% | Cheap, high-intent |

*Referral, resident activation and channel partners run in parallel at minimal media cost — they are process, not spend.*

### Phase 2 (Months 4–9) — TRAYA launch scale
| Line | Share |
|---|---|
| Meta (launch + NRI + Hyderabad) | 35% |
| Google Search | 30% |
| Remarketing + YouTube | 12% |
| Content / SEO / PR | 12% |
| Events + channel partner enablement | 11% |

### Phase 3 (Months 10–12) — Optimise
Reallocate to whatever demonstrates the lowest **cost per booking** in CRM data — by then the model should be running on KMV's real numbers, not benchmarks.

**[RECOMMENDATION]** Hold 15% of budget unallocated as a test reserve. In a market with this little reliable local benchmark data, the ability to test and reallocate quickly is worth more than a perfectly planned split.
