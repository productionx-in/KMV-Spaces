# CRM & Marketing Automation Architecture

## 1. Why this ranks above advertising

**[VERIFIED]** Properties responding to enquiries within 5 minutes convert to site visits at **4× the rate** of those responding after an hour ([Cognitive Marketing](https://www.cognitivemarketing.in/real-estate-digital-marketing-india/)).

**[INFERENCE]** A 4× improvement in site-visit conversion is larger than any realistic gain from creative, targeting or bidding optimisation — and it costs process discipline rather than budget. At ₹3 Cr AOV, a single additional booking recovered through faster response is worth more than an entire quarter's media spend for most regional developers.

**[OBSERVED]** Whether KMV currently operates a CRM, and what its speed-to-lead is, is *Not publicly available.* This is the **first thing I would audit on day one**, because everything downstream depends on it.

## 2. Target architecture

```
LEAD SOURCES
Meta · Google · Organic · Direct · WhatsApp · Portals
Channel partners · Referrals · Walk-ins · Calls · Events
        │
        ▼
CAPTURE — every source writes to ONE system, UTM + source tagged
        │
        ▼
ENRICHMENT — auto: source, campaign, project interest, geography, device
        │
        ▼
AUTO-RESPONSE (< 60 seconds) — WhatsApp + SMS acknowledgement, brochure
        │
        ▼
QUALIFICATION — scoring + human call (< 5 min business hours)
        │
        ├── Disqualified → nurture or suppress
        │
        ▼
CRM — SQL accepted, RM assigned, SLA clock starts
        │
        ▼
SITE VISIT — scheduled → reminder sequence → completed → feedback logged
        │
        ▼
NEGOTIATION → BOOKING → POST-BOOKING NURTURE → REFERRAL
```

**[RECOMMENDATION] The single non-negotiable principle:** every lead from every source lands in one system with its source attached. Without this, attribution is impossible, budget allocation is guesswork, and the reverse-funnel model in `/strategy/growth-strategy.md` cannot be run on real data.

## 3. CRM stages

| Stage | Definition | Owner | Exit criterion |
|---|---|---|---|
| **New** | Captured, uncontacted | System | Contact attempted <5 min |
| **Contacted** | Two-way conversation occurred | Pre-sales | Qualification complete |
| **Qualified (SQL)** | Meets budget, timeline, intent, location | Pre-sales | Accepted by sales RM |
| **Site Visit Scheduled** | Date and time confirmed | Sales RM | Visit occurs or is rescheduled |
| **Site Visit Completed** | Visit happened, feedback logged | Sales RM | Interest level recorded |
| **Negotiation** | Unit, price, payment under discussion | Sales RM | Terms agreed or lost |
| **Booked** | Booking amount received | Sales RM | Agreement executed |
| **Post-Booking** | Construction updates, documentation | CRM/Customer care | Possession |
| **Advocate** | Post-possession referral source | Customer care | Ongoing |
| **Lost / Nurture** | Not now, with a dated reason | Pre-sales | Re-engagement or suppression |

## 4. Lead scoring

**[RECOMMENDATION]** Simple, transparent, sales-trusted. A model salespeople don't believe is a model they ignore.

| Signal | Points |
|---|---|
| Budget matches project band | +30 |
| Timeline within 6 months | +25 |
| Specific project named in enquiry | +15 |
| Site-visit request | +20 |
| Returning website visitor | +10 |
| Watched project video >50% | +10 |
| Referral from existing resident | **+35** |
| Channel-partner registered | +20 |
| NRI with documented intent | +15 |
| Budget clearly below band | **−40** |
| Rental/PG intent | **−50** |
| Outside serviceable geography with no relocation intent | −20 |

**Bands:** 60+ Hot (contact <5 min, RM assigned) · 35–59 Warm (contact <30 min, nurture) · <35 Cold (automated nurture, no RM time)

**[INFERENCE]** Referral scores highest deliberately — it is the highest-converting source in premium real estate and should never sit in a queue behind a cold paid lead.

## 5. Automation vs human

| Task | Automated | Human |
|---|---|---|
| Instant acknowledgement | ✓ WhatsApp + SMS <60s | |
| Brochure / floor plan delivery | ✓ | |
| Lead scoring & routing | ✓ | |
| First qualification call | | ✓ Pre-sales <5 min |
| Site-visit scheduling | ✓ booking link | ✓ confirmation call |
| Visit reminders (T-24h, T-2h) | ✓ | |
| Site visit itself | | ✓ Sales RM |
| Follow-up after visit | ✓ trigger | ✓ RM call same day |
| Objection handling / negotiation | | ✓ Sales RM |
| Construction updates to booked buyers | ✓ monthly | ✓ milestone calls |
| Lost-lead reactivation | ✓ sequence | ✓ on re-engagement |
| Referral request | ✓ trigger post-possession | ✓ relationship |

**[RECOMMENDATION] The dividing line:** automate *speed and consistency*; keep humans for *trust and judgement*. At ₹3 Cr, no buyer converts through a chatbot — but every buyer expects an instant acknowledgement. Automation buys the human time to matter.

## 6. Follow-up cadence

**Qualified, not yet visited**
Day 0: instant WhatsApp + call <5 min · Day 1: call + brochure · Day 3: video walkthrough · Day 7: resident testimonial · Day 14: construction update · Day 21: site-visit invitation · Day 30 → monthly nurture

**Visited, not booked**
Same day: thank-you + call · Day 2: answer specific objection raised · Day 5: comparison/FAQ content · Day 10: RM call · Day 20: payment-plan discussion · Monthly: progress updates

**[RECOMMENDATION]** Follow-up must reference the **specific objection logged at the visit**. Generic follow-up on a ₹3 Cr consideration reads as indifference; a message that answers the exact concern raised reads as competence.

**Lost-lead reactivation** — quarterly, triggered on new phase launch, price revision, milestone completion, or possession announcement. **[INFERENCE]** Real-estate "lost" leads are frequently only *early* — a buyer who was 12 months away last year is buying now. This database is a genuine asset and is usually neglected.

## 7. Post-booking — where referral is earned

**[INFERENCE]** The period between booking and possession is where referral value is created or destroyed, and where KMV has a **[VERIFIED]** documented weakness (possession delay complaints on Vivaan). A buyer who is kept informed through a delay forgives it; one left in silence does not, and tells others.

**Recommended cadence:** monthly construction update with photos · milestone notifications · a named point of contact · a documentation checklist · a pre-possession walkthrough · handover as an event (a format KMV already produces well — its Facebook handover content is genuinely good) · referral request at 3 months post-possession.

## 8. Tooling

**[RECOMMENDATION]** Requirements over brand names: real-estate-appropriate CRM (Zoho CRM, LeadSquared and Sell.Do are all commonly used in Indian real estate) · WhatsApp Business API · call tracking with recording · GA4 + GTM + Meta CAPI + Google offline conversion import · a scheduling tool for site visits.

**The critical integration** is CRM → ad platforms. Feeding actual bookings back to Meta and Google lets both optimise toward buyers rather than form-fillers, and makes lookalike audiences genuinely valuable (`/strategy/acquisition.md` §4).

## 9. Day-one audit questions

*Not publicly available* — all of these:

1. Is there a CRM, and does every source write to it?
2. Current median speed-to-lead?
3. What % of leads are never contacted at all?
4. Is lead source captured accurately end-to-end?
5. Are site visits logged systematically?
6. Are reasons-for-loss recorded?
7. Can any booking be traced to its originating campaign?
8. Is there any post-booking communication programme?
9. Is there a referral programme, and what has it produced?
10. Are call recordings reviewed for objection patterns?

**[INFERENCE]** In most mid-sized developers, questions 3, 6, 7 and 9 reveal the largest recoverable revenue in the business — and none of them require additional media spend to fix.
