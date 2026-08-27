# Marketing Economics & Funnel Model

## 1. The reframe this section exists to make

**[VERIFIED]** KMV's average booking value is approximately **₹3 crore** (Vivaan villas ₹2.95–3.8 Cr).

**[INFERENCE]** At that ticket size, standard digital-marketing optimisation is actively harmful. Consider two campaigns:

| | Campaign A | Campaign B |
|---|---|---|
| Spend | ₹10,00,000 | ₹10,00,000 |
| CPL | **₹500** | **₹2,500** |
| Leads | 2,000 | 400 |
| Qualified rate | 5% | 30% |
| Qualified leads | 100 | 120 |
| Site-visit rate (of QL) | 20% | 45% |
| Site visits | 20 | 54 |
| Bookings @ 20% | 4 | **11** |
| **Revenue @ ₹3 Cr** | **₹12 Cr** | **₹33 Cr** |
| **Cost per booking** | ₹2,50,000 | **₹90,909** |

Campaign A wins on every metric a normal marketing dashboard reports. Campaign B produces **₹21 crore more revenue** on identical spend.

**A CPL-optimised real-estate marketing function at this price point systematically destroys value.** The entire measurement architecture in this project is built to prevent that, by making **cost per booking** and **cost per qualified site visit** the primary metrics and CPL a diagnostic one.

*(Illustrative rates above are [ASSUMPTION] for demonstration — see §4 for sourced benchmark ranges.)*

## 2. Metric definitions and formulas

### Traffic and engagement
| Metric | Formula | Purpose |
|---|---|---|
| Impressions | Count of ad/content servings | Reach ceiling |
| Reach | Unique people served | Audience saturation check |
| CTR | Clicks ÷ Impressions × 100 | Creative and message resonance |
| CPC | Spend ÷ Clicks | Auction cost efficiency |
| Landing Page Conversion Rate | Leads ÷ Landing page sessions × 100 | Page effectiveness — **highest-leverage fixable number** |

### Lead layer
| Metric | Formula | Purpose |
|---|---|---|
| Lead Volume | Count of enquiries with valid contact | Raw pipeline input |
| **CPL** | Spend ÷ Leads | Diagnostic only — never a target |
| Lead Qualification Rate | Qualified Leads ÷ Total Leads × 100 | **Lead quality — the number CPL hides** |
| **CPQL** | Spend ÷ Qualified Leads | First genuinely useful efficiency metric |
| MQL | Meets budget + location + timeline + intent criteria | Marketing's deliverable |
| SQL | MQL accepted by sales after contact | Sales' acceptance of that deliverable |

### Sales conversion layer
| Metric | Formula | Purpose |
|---|---|---|
| Sales Contact Rate | Leads contacted ÷ Leads received × 100 | Detects leads dying in the CRM |
| Speed-to-Lead | Median time from enquiry to first contact | **Highest-leverage operational metric** (see §4) |
| Lead-to-Conversation Rate | Meaningful conversations ÷ Leads × 100 | Real engagement, not dials |
| Site Visit Rate | Site visits ÷ Qualified Leads × 100 | Mid-funnel health |
| **CPSV** | Spend ÷ Completed site visits | **Primary campaign optimisation metric** |
| Site Visit Show Rate | Visits completed ÷ Visits scheduled × 100 | No-show leakage |
| Site Visit → Booking | Bookings ÷ Site visits × 100 | Sales capability and product-market fit |

### Commercial layer
| Metric | Formula | Purpose |
|---|---|---|
| **Cost Per Booking** | Total S&M spend ÷ Bookings | **The number that matters most** |
| Booking Value | Average realised price per unit | Revenue driver |
| Revenue | Bookings × Booking Value | Output |
| **CAC** | Total sales + marketing acquisition cost ÷ New customers | True acquisition cost incl. salaries, brokerage |
| **ROAS** | Revenue attributed ÷ Marketing spend | Channel efficiency |
| Marketing Cost Ratio | Marketing spend ÷ Revenue × 100 | Budget discipline |
| Marketing ROI | (Revenue − Marketing cost) ÷ Marketing cost × 100 | Board-level return |
| Contribution Margin | (Revenue − direct project + S&M cost) ÷ Revenue | Requires internal cost data |

### Lifetime value — and an honest caveat
**[INFERENCE]** Conventional LTV is a poor fit for residential real estate: most buyers purchase once. LTV is meaningful here only through **referral and repeat purchase**, which for KMV is genuinely live given the apartment→villa→second-home ladder in `/research/projects.md` §3.

**Practical definition:**
```
Customer Lifetime Value = Booking Value
                        + (Repeat Purchase Probability × Avg Booking Value)
                        + (Referrals Generated × Referral Conversion Rate × Avg Booking Value)
```
**[INFERENCE]** If one satisfied resident refers even 0.3 successful bookings on average, their effective LTV is ~₹3.9 Cr against ~₹3 Cr — a 30% uplift for the cost of a relationship programme. **This is the strongest financial argument for funding customer experience and referrals**, and it is currently invisible in most developer P&Ls.

## 3. The funnel, stage by stage

```
IMPRESSIONS ─── CTR ──▶ CLICKS ─── LP CVR ──▶ LEADS
                                                 │
                                    Lead Qualification Rate
                                                 ▼
                                        QUALIFIED LEADS ──── CPQL
                                                 │
                                    Speed-to-Lead · Contact Rate
                                                 ▼
                                          CONVERSATIONS
                                                 │
                                          Site Visit Rate
                                                 ▼
                                    SITE VISITS SCHEDULED
                                                 │
                                            Show Rate
                                                 ▼
                                    SITE VISITS COMPLETED ─── CPSV
                                                 │
                                       Visit → Booking Rate
                                                 ▼
                                            BOOKINGS ──── Cost Per Booking
                                                 │
                                          × Booking Value
                                                 ▼
                                             REVENUE
                                                 │
                                      Referral Rate ──▶ back to LEADS
```

## 4. Benchmarks — clearly labelled as benchmarks

**These are industry reference points, not KMV's performance. KMV's actual figures are *Not publicly available*.**

| Metric | Sourced benchmark | Recommended initial target for KMV | Why |
|---|---|---|---|
| CPL — premium apartments/villas (India) | **₹1,500–3,000** ([Tatva Digital](https://tatva.digital/real-cost-of-real-estate-leads-in-india/)) | ₹1,500–3,000 | KMV sits squarely in premium villa |
| CPL — luxury (India) | **₹3,000–6,000+** (same) | Upper band acceptable for TRAYA villas | ₹3 Cr AOV supports it |
| CPL — Google Ads real estate India | **₹800–1,500** ([Cognitive Marketing](https://www.cognitivemarketing.in/real-estate-digital-marketing-india/)) | Expect above this band | Higher intent, premium segment |
| CPL — Meta real estate India | **₹400–900** (same) | Expect above this band | Same reason |
| Real-estate site conversion rate | **~4.7% avg; 3.2% organic** ([First Page Sage](https://firstpagesage.com/reports/real-estate-marketing-metrics-benchmarks/)) | 3–5% on a dedicated landing page | Dedicated pages beat generic |
| Speed-to-lead effect | **<5 min response → 4× site-visit conversion** ([Cognitive Marketing](https://www.cognitivemarketing.in/real-estate-digital-marketing-india/)) | **<5 minutes, business hours** | Highest-ROI operational fix available |
| Page speed effect | **Every second >2s cuts conversion ~12%; <2s cuts CPL 20–35%** (same) | <2s mobile | Cheapest CPL reduction available |

**[ASSUMPTION] Funnel rates for modelling only** — these must be replaced with KMV's real numbers before any budget is committed:

| Stage | Conservative | Base | Aggressive |
|---|---|---|---|
| Lead → Qualified | 15% | 25% | 35% |
| Qualified → Site visit | 25% | 35% | 45% |
| Site visit → Booking | 10% | 15% | 20% |
| **Implied Lead → Booking** | **0.38%** | **1.31%** | **3.15%** |

**[INFERENCE]** The spread matters more than the midpoint. Between conservative and aggressive there is an **8× difference in leads required per booking**. That gap is not closed by media buying — it is closed by lead qualification, speed-to-lead, and sales capability. **Which is the entire argument for prioritising sales alignment and CRM over ad spend in the first 90 days.**

## 5. Allowable acquisition cost

**[INFERENCE]** Working from ₹3 Cr AOV:

| Marketing cost ratio | Allowable cost per booking | Assessment |
|---|---|---|
| 0.5% | ₹1,50,000 | Very lean |
| **1.0%** | **₹3,00,000** | Efficient |
| **1.5%** | **₹4,50,000** | Reasonable for premium |
| 2.0% | ₹6,00,000 | Acceptable during launch |
| 3.0% | ₹9,00,000 | Launch-phase ceiling only |

**[RECOMMENDATION]** Target blended **1.5–2% of revenue**, with launch phases permitted up to 3% and steady-state driven toward 1.5%. Compare against brokerage: channel-partner commissions in Indian residential real estate commonly run **2%+ of unit value**, so a direct-marketing cost of 1.5% that produces the same booking is *already* competitive with the outsourced alternative — a useful framing for promoters who instinctively prefer paying only on success.

## 6. Variables KMV leadership must plug in

Nothing in §7 is trustworthy until these are supplied from internal systems:

| Variable | Source | Why it matters |
|---|---|---|
| Annual booking target by project | Sales/finance | Anchors the whole model |
| Actual average realised price | Finance | Revenue per booking |
| Current lead volume and source split | CRM | Baseline |
| Current qualification rate | CRM/sales | Biggest model swing factor |
| Current site-visit and show rates | Sales | Mid-funnel truth |
| Current site-visit → booking rate | Sales | Sales capability measure |
| Current marketing spend by channel | Finance | Efficiency baseline |
| Current speed-to-lead | CRM | Fastest available improvement |
| Referral share of past bookings | Sales | Sizes the cheapest channel |
| Sales team capacity (visits/month) | Sales | **Hard ceiling on the funnel** |

**[INFERENCE] On that last point:** if sales can host 100 site visits a month, generating demand for 200 wastes half the budget and damages every lead's experience. **Marketing must be planned to sales capacity, not to budget availability** — a discipline most developer marketing functions ignore.
