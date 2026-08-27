# KPI Framework & CMO Dashboard

## 1. Design principle

**[RECOMMENDATION]** Five levels, each for a different audience and rhythm. Promoters see Level 1. The marketing team lives in Level 3. Nobody should be shown a level that isn't theirs to act on — a promoter looking at CTR is a symptom of a marketing function that hasn't connected its work to revenue.

Machine-readable version: `/data/kpi-framework.csv`

---

## LEVEL 1 — BUSINESS *(Promoters / Board)*

| KPI | Formula | Cadence |
|---|---|---|
| Revenue booked | Σ booking values | Monthly |
| Bookings | Count | **Weekly** |
| Average booking value | Revenue ÷ Bookings | Monthly |
| Sales velocity | Bookings ÷ Month | Monthly |
| Inventory movement | Units sold ÷ Total units × 100 | Monthly |
| Inventory remaining by project | Count | Monthly |
| **Marketing cost ratio** | Marketing spend ÷ Revenue × 100 | Monthly |
| Forecast vs target | Projected ÷ Target × 100 | Monthly |

**[RECOMMENDATION] Target for marketing cost ratio: 1.5–2% steady state, up to 3% in launch quarters** (reasoning: `/strategy/marketing-economics.md` §5).

---

## LEVEL 2 — FUNNEL *(Leadership / CMO / Sales Head)*

| KPI | Formula | Cadence |
|---|---|---|
| Total leads | Count | Weekly |
| **Qualified leads (MQL)** | Count meeting all 4 criteria | **Weekly** |
| Lead qualification rate | MQL ÷ Leads × 100 | Weekly |
| SQL acceptance rate | SQL ÷ MQL × 100 | Weekly |
| Site visits scheduled | Count | Weekly |
| **Site visits completed** | Count | **Weekly** |
| Site visit show rate | Completed ÷ Scheduled × 100 | Weekly |
| **Site visit → booking rate** | Bookings ÷ Visits completed × 100 | Monthly |
| Lead → booking rate | Bookings ÷ Leads × 100 | Monthly |
| **CAC** | Total S&M cost ÷ Bookings | Monthly |
| Pipeline value | Open opportunities × avg value | Weekly |

**[INFERENCE]** Site visits completed is the **best single leading indicator of revenue** in this business. It has enough volume to be statistically meaningful weekly (unlike bookings), and it correlates directly with bookings. If one number were shown daily, it should be this.

---

## LEVEL 3 — MARKETING *(Marketing team)*

| KPI | Formula | Cadence |
|---|---|---|
| Spend by channel | Σ | **Daily** |
| CPL by channel | Spend ÷ Leads | Daily *(diagnostic only)* |
| **CPQL by channel** | Spend ÷ MQL | **Weekly** |
| **CPSV by channel** | Spend ÷ Site visits completed | **Weekly — primary optimisation metric** |
| **Cost per booking by channel** | Spend ÷ Bookings | Monthly |
| ROAS by channel | Attributed revenue ÷ Spend | Monthly |
| CTR | Clicks ÷ Impressions × 100 | Daily |
| CPC | Spend ÷ Clicks | Daily |
| Landing page CVR | Leads ÷ Sessions × 100 | Weekly |
| Page load time (mobile) | Seconds | Weekly |
| Creative performance | CTR / CVR by asset | Weekly |

**[RECOMMENDATION] CPL is listed but explicitly labelled diagnostic.** It is useful for spotting auction shifts or a broken landing page. It must never be a target — see the worked comparison in `/strategy/marketing-economics.md` §1 where the campaign with 5× the CPL produced ₹21 Cr more revenue.

---

## LEVEL 4 — BRAND *(CMO / Leadership)*

| KPI | Formula | Cadence |
|---|---|---|
| Brand search volume | Searches for "KMV Spaces"/"TRAYA"/"KMV Vivaan" | Monthly |
| Non-brand organic sessions | GA4 organic minus brand terms | Monthly |
| Direct traffic | Sessions | Monthly |
| Keyword rankings (priority set) | Position | Monthly |
| **Share of voice** | KMV mentions ÷ total category mentions | Quarterly |
| **Google review count & rating** | Count, average | Monthly |
| Referral share of bookings | Referral bookings ÷ Total × 100 | Monthly |
| Audience growth (consolidated) | Followers by platform | Monthly |
| Engagement quality | Saves, shares, comments ÷ Reach | Monthly |
| Video completion rate | % watched >50% | Monthly |
| Earned media | Article count, publication tier | Quarterly |

**[INFERENCE] Brand search volume is the most honest brand-health metric available** — it measures whether people are actively seeking KMV rather than whether ads reached them. It is also the cleanest way to prove that upper-funnel work (PR, content, outdoor, the photo contest) is working, since those channels rarely close deals directly but reliably lift branded search.

**[INFERENCE] Google review count deserves board visibility.** 33 reviews against 454 Justdial ratings is a fixable, measurable trust gap that directly affects local search and buyer due diligence.

---

## LEVEL 5 — SALES *(Sales Head / CMO)*

| KPI | Formula | Cadence |
|---|---|---|
| **Speed-to-lead (median)** | Enquiry → first contact | **Daily** |
| Speed-to-lead SLA breaches | Count >5 min | Daily |
| Contact rate | Contacted ÷ Received × 100 | Daily |
| Attempts per lead | Σ attempts ÷ Leads | Weekly |
| Follow-up compliance | Leads with ≥5 attempts ÷ Unreachable × 100 | Weekly |
| Site visit show rate | Completed ÷ Scheduled × 100 | Weekly |
| **Visit → booking rate by RM** | Bookings ÷ Visits per RM × 100 | Monthly |
| Time to booking | Median lead → booking days | Monthly |
| Reason-for-loss distribution | % by code | Monthly |
| CRM hygiene | % records with complete fields | Weekly |

**[VERIFIED]** Speed-to-lead is daily because <5 minute response drives **4× site-visit conversion**. **[INFERENCE]** It is the single most improvable number in the business and requires no budget — only discipline. A daily breach report makes it self-correcting.

---

## 2. Reporting rhythm summary

| Cadence | Audience | Content |
|---|---|---|
| **Daily** | Marketing ops + pre-sales | Leads, spend, speed-to-lead breaches, contact rate |
| **Weekly** | CMO + Sales Head | MQLs, site visits, CPQL, CPSV, LP conversion, pipeline |
| **Monthly** | Leadership | Bookings, revenue, cost per booking, CAC, ROAS, brand metrics, loss reasons |
| **Quarterly** | Promoters / Board | Strategy, share of voice, brand health, budget reallocation, roadmap |

## 3. The five KPIs that matter most

**[RECOMMENDATION]** If leadership tracked only five:

1. **Bookings** — the business outcome
2. **Cost per booking** — commercial efficiency; the number that should govern budget
3. **Site visits completed** — the best leading indicator of revenue
4. **Speed-to-lead** — the cheapest, highest-leverage improvement available
5. **Qualified lead rate** — the number that determines whether media spend compounds or leaks

**[INFERENCE]** Note what is deliberately absent: impressions, reach, followers, likes, CPL. None of them tell a promoter whether the company sold a house. In a business with ~60 transactions a year at ₹3 crore each, marketing must be measured in bookings — anything else invites a conversation about activity instead of revenue.

## 4. Targets — how to set them honestly

**[ASSUMPTION]** Every target below is a *starting point pending baseline data*, not a claim about KMV's performance.

| KPI | Initial target | Basis |
|---|---|---|
| Speed-to-lead | <5 min business hours | **[VERIFIED]** 4× site-visit uplift |
| Landing page CVR | 3–5% | **[VERIFIED]** real-estate avg 4.7% |
| Mobile page load | <2s | **[VERIFIED]** 20–35% CPL reduction |
| CPL (premium villa) | ₹1,500–3,000 | **[VERIFIED]** India premium benchmark |
| SQL acceptance rate | ≥70% | **[ASSUMPTION]** — reset after baseline |
| Site visit show rate | ≥80% | **[ASSUMPTION]** |
| Marketing cost ratio | 1.5–2% steady state | **[INFERENCE]** vs 2%+ typical brokerage |
| Google reviews | 150+ within 12 months | **[INFERENCE]** vs 454 Justdial ratings held |

**[RECOMMENDATION]** Re-baseline all of these after 90 days on KMV's own data. Benchmarks are for setting a starting direction; they are not a substitute for knowing your own numbers, and presenting them as KMV's performance would be exactly the error this framework exists to prevent.
