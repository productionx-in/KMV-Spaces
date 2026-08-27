# Analytics & Attribution

## 1. The question this must answer

> **"Which rupee of marketing spend actually produced revenue?"**

**[OBSERVED]** Today this is *Not publicly available* — and in most mid-sized developers it is not answerable internally either, because leads arrive by phone, WhatsApp, walk-in, broker and form, and nothing joins them to a booking.

## 2. Why standard attribution fails in real estate

| Model | Why it breaks here |
|---|---|
| **Last-click** | Credits the final brand search — the buyer had already decided. Systematically over-credits brand/retargeting and under-credits discovery, leading to defunding the top of funnel. |
| **First-click** | Credits discovery only; ignores the 6–18 month consideration period where trust is built. |
| **Platform-reported** | Meta and Google each claim the same booking. Summed platform-reported conversions routinely exceed actual bookings. Never report these to leadership as revenue. |
| **Digital-only models** | **The fatal flaw.** The decisive events — site visit, RM conversation, family discussion, broker recommendation — are offline and invisible to every ad platform. |

**[INFERENCE]** Real-estate attribution cannot be solved in the ad platforms. It can only be solved in the **CRM**, because the CRM is the only system that sees both the digital origin and the offline booking.

## 3. The recommended model: CRM-anchored, multi-touch informed

**Principle:** the CRM is the single source of truth for revenue. Ad platforms are optimisation tools, not reporting tools.

```
Every touchpoint stamped to ONE CRM lead record
        │
   ┌────┴─────┬──────────┬───────────┬──────────┐
 UTM on     Call      WhatsApp    Broker     Walk-in
  forms   tracking     source   registration   source
   │          │           │          │           │
   └──────────┴─────┬─────┴──────────┴───────────┘
                    ▼
        CRM LEAD ID ──▶ Site visit ──▶ Booking ──▶ ₹ Revenue
                    │
      ┌─────────────┴──────────────┐
      ▼                            ▼
 Reporting to leadership    Fed back to Google
 (CRM = truth)              offline conversions
                            & Meta CAPI (optimisation)
```

## 4. Tracking requirements

| Requirement | Implementation | Why |
|---|---|---|
| **UTM discipline** | Rigid convention on every link, enforced by a builder template | Inconsistent UTMs make source analysis worthless |
| **Call tracking** | Dynamic numbers by source; recording | Phone is a primary channel in this market |
| **WhatsApp source** | Distinct click-to-chat links per campaign/page | Otherwise all WhatsApp collapses into "direct" |
| **Form → CRM** | Direct integration, source fields passed | Manual re-entry destroys attribution |
| **Broker registration** | Portal with timestamp | Resolves ownership disputes |
| **Walk-in capture** | Mandatory "how did you hear about us?" at site | The only way to measure outdoor, PR, word-of-mouth |
| **Site visit logging** | Every visit in CRM with source | Enables CPSV, the key optimisation metric |
| **Booking → source** | Booking record joined to originating lead | The whole point |
| **Offline conversion upload** | Google Ads + Meta CAPI, weekly | Lets platforms optimise to buyers, not form-fillers |
| **GA4 + GTM** | Standard events, server-side where possible | Baseline behavioural data |
| **Schema markup** | Organisation, Product/Residence, FAQ | Search + AI answer-engine visibility |

**[RECOMMENDATION]** The mandatory *"how did you hear about us?"* field at site visit is unglamorous and disproportionately valuable. It is the only mechanism that captures the offline and word-of-mouth influence that digital analytics is structurally blind to — and in a referral-heavy category, that is a large share of reality.

## 5. Practical attribution reporting

**[RECOMMENDATION]** Report three views. Leadership should see all three, because each answers a different question.

**View 1 — Source of first contact (discovery)**
*Which channels create awareness?* Credits the first recorded touch. Protects top-of-funnel investment from last-click bias.

**View 2 — Source of booking (CRM primary source)**
*Which channels close?* The lead's CRM-assigned source. **This is the revenue number** and the basis for cost-per-booking.

**View 3 — Assisted influence**
*What contributed along the way?* All touchpoints on converting leads. Prevents defunding channels that assist but rarely close (content, YouTube, PR).

**[INFERENCE]** A channel can look weak in View 2 and be essential in View 3. Content and YouTube typically behave exactly this way — they build the confidence that makes a later branded search convert. Killing them on last-click logic is one of the most common and expensive mistakes in this category.

## 6. Honest limits

**[RECOMMENDATION]** State these to leadership up front. Over-claiming attribution precision destroys credibility the first time the numbers don't reconcile.

1. **Multi-touch, long-cycle purchases cannot be attributed to a single source.** A 9-month, ₹3 Cr decision involves family, brokers, site visits and offline conversation. Attribution shows *contribution patterns*, not causation.
2. **Word of mouth is systematically under-measured.** It will always appear as "direct" or "referral" — likely the most valuable and least visible channel.
3. **Platform-reported conversions overlap.** Never sum them.
4. **Small numbers are statistically noisy.** At ~60 bookings a year, a single booking shifts a channel's cost-per-booking materially. Judge channels over quarters, not weeks, and use site visits (higher volume) as the faster-signal proxy.

**[INFERENCE]** That last point is a genuine analytical constraint of this business and should shape the reporting rhythm: **optimise weekly on cost per qualified site visit; judge quarterly on cost per booking.**

## 7. Measurement roadmap

| Phase | Weeks | Deliverable |
|---|---|---|
| **Foundation** | 1–4 | Audit existing tracking; GA4/GTM verified; UTM convention published; CRM source fields defined; call tracking live |
| **Integration** | 5–8 | Forms → CRM; WhatsApp source links; broker portal; walk-in capture at site; site-visit logging enforced |
| **Closed loop** | 9–12 | Booking → source join; offline conversions to Google & Meta; first cost-per-booking report |
| **Optimisation** | 13+ | Three-view attribution reporting; lookalikes rebuilt on bookers; budget reallocated on CRM evidence |

**[INFERENCE]** Until the closed loop exists (~week 12), every budget decision is directional rather than evidence-based. That is the honest reason the 90-day plan front-loads measurement infrastructure over media scale — scaling spend into an unmeasurable funnel is how developers lose money without ever knowing which part failed.
