# 00 — Project Assumptions

## What was given, what was researched, and what is still assumed

**This file exists to keep three things separate that are easy to conflate**: the parameters handed to the exercise, the findings produced by it, and the assumptions still carrying weight. Everything downstream depends on knowing which is which.

---

## 1. The framing constraint, stated first

> **This is a hypothetical strategic exercise.** Nothing in this repository describes an actual KMV Spaces project, land holding, commitment or launch. **The developer/brand context is an assumption of the exercise, not a verified fact**, and no project here should be represented as real.

---

## 2. Given parameters — fixed by the brief, not researched

| Parameter | Value | Note |
| --- | --- | --- |
| Location | **Amaravati–Mangalagiri corridor, Andhra Pradesh** | Exact micro-location **not fixed** — to be recommended, not assumed |
| Land parcel | **25 acres** | Contiguity assumed, never verified |
| Total project value | **₹500 crore** | Treated as revenue potential |
| Structure | **4 residential communities (A, B, C, D)** | Tiering **not** pre-assigned |
| Product spectrum | **2BHK apartments → premium residences → villas** | The only fixed product requirement |
| Market timing | Launch into the current market | — |
| Pricing | **To be researched, not assumed** | See `03_Pricing/` |
| Audience | **To be determined through research, not assumed** | See `06_Audience/` |

**Three instructions shaped the method as much as the parameters did:**

1. **Do not automatically assign** A = 2BHK, B = 3BHK, C = premium, D = villas unless research supports it. *(Phase 6 rebuilt the structure; the assumed tiering did not survive.)*
2. **Do not treat future announcements as existing infrastructure.** *(Enforced by the grading system in `02_Infrastructure/`.)*
3. **Do not represent the project as an actual KMV Spaces project unless independently verified.**

---

## 3. Derived parameters — produced by research, now load-bearing

**These are outputs, not inputs.** Each can be traced to the phase that produced it.

| Parameter | Value | Produced by |
| --- | --- | --- |
| Unit count | **376** | `07_Community_ABCD/` — from the land model |
| Community split | A 169 · B 84 · C 60 · D 63 | `07_Community_ABCD/` |
| Density | **15.0 units/acre** | `07_Community_ABCD/` |
| Blended realisation | **₹6,098/sq ft** | `03_Pricing/` |
| Revenue | **₹506.7 Cr** | `07_Community_ABCD/` |
| Sales task | **~397 units** *(revised down from ~600)* | `06_Audience/` §5.5 |
| Marketing budget | **₹31.75 Cr — 6.27% of GDV** | `08_Funnel_Economics/` |
| Segments | **Eight, ranked** | `06_Audience/` |

> **The largest single correction in the exercise.** Phase 1 sized the sales task at ~600 units; Phase 5 corrected it to **~397**, which raised allowable marketing cost per unit from ₹3.6–6.2 L to **₹5.0–6.3 L**. Everything downstream uses the corrected figure.

---

## 4. Assumptions still carrying weight

**Fifteen assumptions hold the plan up.** The full register with replacement sources is in `12_Strategy/13-research-dossier.md` §17. **The five that would change the strategy if wrong:**

| # | Assumption | If it breaks |
| --: | --- | --- |
| **1** | **KMV's AIIMS Mangalagiri scope is documentable** | The proof-led brand position collapses; fall back to density arithmetic and ungated pricing, both provable without credentials |
| **2** | **The ₹2.2–2.8 Cr villa band is occupied** | ₹158.8 Cr re-cuts toward Community C |
| **3** | **The ladder clears a 50% premium to the locality average** | The whole price model re-bases — **Community A is most exposed** |
| **4** | **Development gross margin of 28%** | A placeholder. No cost data exists anywhere in this exercise |
| **5** | **25 contiguous acres are assemblable and buildable** | There is no project |

---

## 5. What was never established, across all thirteen phases

**Stated plainly, because a set of assumptions that hides its own gaps is not a register.**

- **No primary buyer research.** No surveys, interviews, focus groups, CRM data or walk-in analysis. Every behavioural attribute across eight segments is hypothesis.
- **No transaction data.** Every price in this repository is an **asking** price. Registration data was never obtained.
- **No construction cost data.** Margin, and therefore every ROI figure, rests on a placeholder.
- **No RERA record and no established research report** was retrieved — the two source tiers that would settle pricing, absorption and legitimacy.
- **No verified 2026 headcount** for government staff working in Amaravati.

---

## 6. The retrieval limitation

**Phases 1–12 were built without the ability to open a single web page.** Sources were recorded by name and tier, never by URL.

**Phase 13 added working search — but not page retrieval.** Every fetch returned `EGRESS_BLOCKED`; direct requests to `crda.ap.gov.in` and `rera.ap.gov.in` returned `403` policy denials.

> **So the URLs in `13_Sources/` are real and they resolve — but not one of them was opened.** Every citation is search-surfaced rather than read. **A Tier 1 domain means the domain is authoritative, not that the document was verified.**

**This is why `13_Sources/source-register.md` carries a verification checklist rather than a bibliography.**

---

## 7. Reading order

| If you want | Start at |
| --- | --- |
| **The short version** | `12_Strategy/13-research-dossier.md` §0 — the six findings that overturned earlier phases |
| **The strategy** | `12_Strategy/strategic-recommendation.md` |
| **What to verify before acting** | `13_Sources/source-register.md` |
| **The full argument in sequence** | `01_Market/` → `13_Sources/`, in folder order |
| **What is still wrong or missing** | `11_Gaps/` |

---

*Hypothetical strategic exercise. Not represented as an actual KMV Spaces development.*
