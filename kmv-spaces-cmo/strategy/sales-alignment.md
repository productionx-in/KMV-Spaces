# Marketing ↔ Sales Alignment

## 1. Why this is the highest-stakes relationship in the company

**[INFERENCE]** In a business with ~₹3 Cr average booking value and perhaps 60 bookings a year, a single mishandled qualified lead is a **₹3 crore** event. There is no marketing optimisation that compensates for a sales handoff that leaks.

The reverse-funnel model in `/strategy/growth-strategy.md` showed a **29× difference in required media spend** between a weak and a strong funnel — and almost all of that difference sits at the marketing/sales boundary: qualification, speed-to-lead, show rate, and closing.

**This document is therefore not an administrative annex. It is the highest-leverage section in the strategy.**

## 2. Definitions — agreed once, in writing

Ambiguity here is where accountability dies. "We sent you 500 leads" / "they were all rubbish" is the classic failure, and it is a definitional problem, not a personality one.

| Term | Definition | Owner |
|---|---|---|
| **Enquiry** | Any inbound contact with valid name + phone | Marketing |
| **Lead** | Enquiry with a stated project or category interest | Marketing |
| **MQL** | Lead meeting **all four**: (1) budget within project band, (2) purchase timeline ≤12 months, (3) serviceable geography or stated relocation intent, (4) end-user or investor intent — not rental/PG/job | **Marketing** |
| **SQL** | MQL contacted by sales and **accepted** as genuine opportunity | **Sales** |
| **Site Visit Scheduled** | Confirmed date/time in CRM | Sales |
| **Site Visit Completed** | Visit occurred, feedback logged same day | Sales |
| **Opportunity** | Specific unit and price under discussion | Sales |
| **Booking** | Booking amount received | Sales |

**[RECOMMENDATION] The critical clause:** sales may **reject** an MQL, but must record a **reason code**. Rejection without a reason is not permitted. Those codes are the feedback loop that makes marketing better — without them, targeting never improves.

## 3. The SLA

### Marketing commits to
| Commitment | Standard |
|---|---|
| MQL definition applied consistently | 100% |
| Lead delivered to CRM with full source attribution | <60 seconds |
| Automated acknowledgement to lead | <60 seconds |
| Minimum MQL quality | ≥70% sales acceptance rate |
| Volume planned to sales capacity | Agreed monthly, not exceeded |
| Campaign, creative and offer context visible to sales | Before campaign launch |
| Weekly lead-quality review | Every week |

### Sales commits to
| Commitment | Standard |
|---|---|
| **First contact attempt** | **<5 minutes** (business hours), <12 hours otherwise |
| Minimum contact attempts before "unreachable" | **5 attempts across 3 days, varied times** |
| MQL accept/reject with reason code | <24 hours |
| Site-visit feedback logged | Same day |
| CRM stage hygiene | Daily |
| Reason-for-loss recorded | 100% of lost opportunities |
| Weekly pipeline review | Every week |

**[VERIFIED] justification for the 5-minute standard:** <5 minute response → 4× site-visit conversion.
**[INFERENCE] justification for 5 attempts:** at ₹3 Cr AOV, the expected value of a sixth call attempt on a qualified lead vastly exceeds its cost. Most sales teams stop at two.

## 4. Reason codes

**Rejection (MQL → not SQL)** — tells marketing what to fix
`BUDGET_LOW` · `WRONG_GEOGRAPHY` · `RENTAL_INTENT` · `TIMELINE_TOO_LONG` · `DUPLICATE` · `INVALID_CONTACT` · `UNREACHABLE_5_ATTEMPTS` · `COMPETITOR_BOOKED` · `JOB_ENQUIRY`

**Loss (opportunity → lost)** — tells the business what to fix
`PRICE_TOO_HIGH` · `CHOSE_COMPETITOR` (name it) · `LOCATION_PREFERENCE` · `POSSESSION_TIMELINE` · `FINANCE_DECLINED` · `FAMILY_DECISION` · `DEFERRED_PURCHASE` · `PRODUCT_MISMATCH` · `TRUST_CONCERN`

**[INFERENCE]** These codes convert anecdote into evidence. If `PRICE_TOO_HIGH` dominates, the answer is a better value narrative — the quantified net-zero running-cost argument in `/research/traya.md`. If `CHOSE_COMPETITOR: Aparna` dominates, it is a positioning problem. If `TRUST_CONCERN` appears, the delivery-proof story is not reaching people. **You cannot fix what you cannot name.**

## 5. Closed-loop reporting

```
AD / SOURCE ──▶ LEAD ──▶ MQL ──▶ SQL ──▶ SITE VISIT ──▶ BOOKING ──▶ REVENUE
     │            │        │       │          │            │           │
   utm_*      CRM ID   MQL flag  accept    visit ID    booking ID  ₹ value
     └────────────────── all joined on CRM lead ID ─────────────────────┘
                                   │
                         ▼ pushed back to ▼
                    Google offline conversions
                       Meta Conversions API
```

**[RECOMMENDATION]** The test of whether this works: leadership should be able to ask *"which campaign produced last month's bookings, and at what cost per booking?"* and get an answer from a dashboard, not a debate. Today that answer is *Not publicly available* — externally or, quite possibly, internally.

## 6. Operating rhythm

| Forum | Frequency | Attendees | Agenda |
|---|---|---|---|
| **Lead flow stand-up** | Daily, 15 min | Pre-sales + marketing ops | Yesterday's leads, speed-to-lead breaches, today's priorities |
| **Pipeline review** | Weekly, 45 min | Sales head + CMO | SQL acceptance, site visits, bookings, blockers |
| **Lead quality review** | Weekly, 30 min | Marketing + sales | Rejection codes, campaign adjustments |
| **Call listening** | Fortnightly, 60 min | Marketing + sales | 5 real calls — objections heard, language used |
| **Commercial review** | Monthly | Leadership | Cost per booking, ROAS, inventory, forecast |
| **Strategy review** | Quarterly | Promoters | Positioning, budget, roadmap |

**[RECOMMENDATION]** The fortnightly **call listening** session is the one most companies skip and the one that changes marketing most. Hearing five real buyers raise the same objection in their own words produces better creative than any brief. It is also how marketing earns sales' trust — by demonstrably listening.

## 7. Shared incentives

**[INFERENCE]** Marketing measured on leads and sales measured on bookings guarantees conflict. Marketing optimises volume; sales complains about quality; both are rationally responding to their own targets.

**[RECOMMENDATION]** Marketing's primary KPI should be **cost per booking**, not CPL — the same commercial outcome sales carries. Secondary: SQL acceptance rate (quality) and cost per qualified site visit (efficiency). Sales carries speed-to-lead and site-visit-to-booking rate. Both share the booking number.

When marketing is accountable for bookings, it stops buying cheap leads on its own initiative — no policing required.

## 8. Sales enablement marketing must supply

**[RECOMMENDATION]** Marketing's job does not end at the lead. Deliverables:

- **Objection-handling one-pagers** for the three verified Vivaan complaints — price, water quality, possession delay
- **Quantified net-zero savings sheet** — rupees per year, from real resident data where available
- **Competitor comparison cards** — honest, factual, versus Aparna, SRK, IJM, TAG and plotted land
- **The delivery-proof pack** — Vivaan photos, resident ratings, KMV Projects' institutional portfolio
- **Structured Vivaan site-visit script** — using the completed community as the proof asset (`/strategy/../execution/90-day.md`)
- **NRI process pack** — documentation, FEMA, remote purchase, property management
- **Channel-partner kit** — see `/strategy/channel-partners.md`

**[INFERENCE]** Most of this is assembly of assets KMV already owns rather than new production. That makes it fast, cheap, and among the highest-return work available in the first 60 days.
