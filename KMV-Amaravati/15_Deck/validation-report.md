# Final Validation Report — submission deck

## 151 automated checks, 0 failures

**Produced by `src/dk_val.py`, run against the assembled deck and the full `KMV-Amaravati` markdown tree.** Re-runnable with `src/build.sh`.

| Result | Count |
| --- | --: |
| **Passed** | **151** |
| Failed | 0 |

---

## Structure & document shape — 60 checks

- no <!doctype tag
- no <html tag
- no <head> tag
- no </head> tag
- no <body tag
- no </body> tag
- has <title>
- <title> in first 8KB
- 24 numbered slides in sequence, got 24
- slide ids s01..s24
- appendices A-G, got ['apxA', 'apxB', 'apxC', 'apxD', 'apxE', 'apxF', 'apxG']
- part dividers present (5)
- nav anchor #s01 resolves
- nav anchor #s02 resolves
- nav anchor #s03 resolves
- nav anchor #s04 resolves
- nav anchor #s05 resolves
- nav anchor #s06 resolves
- nav anchor #s07 resolves
- nav anchor #s08 resolves
- nav anchor #s09 resolves
- nav anchor #s10 resolves
- nav anchor #s11 resolves
- nav anchor #s12 resolves
- nav anchor #s13 resolves
- nav anchor #s14 resolves
- nav anchor #s15 resolves
- nav anchor #s16 resolves
- nav anchor #s17 resolves
- nav anchor #s18 resolves
- nav anchor #s19 resolves
- nav anchor #s20 resolves
- nav anchor #s21 resolves
- nav anchor #s22 resolves
- nav anchor #s23 resolves
- nav anchor #s24 resolves
- nav anchor #apxA resolves
- print page-fit scale set inline per slide, with a fallback
- S02 listed in Appendix F
- S11 listed in Appendix F
- S06 listed in Appendix F
- S16 listed in Appendix F
- S14 listed in Appendix F
- S18 listed in Appendix F
- S01 listed in Appendix F
- S17 listed in Appendix F
- S20 listed in Appendix F
- S15 listed in Appendix F
- S12 listed in Appendix F
- S10 listed in Appendix F
- S03 listed in Appendix F
- S13 listed in Appendix F
- S19 listed in Appendix F
- S04 listed in Appendix F
- S08 listed in Appendix F
- S05 listed in Appendix F
- S09 listed in Appendix F
- S07 listed in Appendix F
- Kiran Basa named on cover, close and appendix G
- source strip on all 23 content slides (cover excluded), got 23

## Markup integrity — 23 checks

- balanced <section> 36/36
- balanced <div> 308/308
- balanced <table> 34/34
- balanced <thead> 34/34
- balanced <tbody> 34/34
- balanced <tr> 343/343
- balanced <td> 1446/1446
- balanced <th> 148/148
- balanced <ul> 7/7
- balanced <li> 31/31
- balanced <p> 190/190
- balanced <span> 378/378
- balanced <nav> 1/1
- balanced <footer> 1/1
- balanced <h1> 6/6
- balanced <h2> 30/30
- balanced <h3> 16/16
- balanced <h4> 20/20
- balanced <b> 138/138
- balanced <strong> 673/673
- balanced <i> 60/60
- balanced <em> 8/8
- table columns consistent; all ok

## Design system & theming — 7 checks

- all CSS classes defined; undefined=[]
- dark media query
- light-guard on dark media query
- explicit dark stamp
- body background from token
- no token defined only inside media/[data-theme]: []
- no undefined tokens; []

## Source discipline — 4 checks

- every [Sxx] used is defined; orphans=[]
- 20 source IDs
- 40 URLs in register
- every URL traces to the repo register; missing=[]

## Figures verified against the repository — 2 checks

- all 109 key figures present in deck; missing=[]
- all key figures traceable to repo markdown; missing=[]

## Arithmetic — 37 checks

- 23.80+4.04+3.15+0.76 = 31.75
- tranches sum to 21.90
- core+reserve = 23.80
- community opex sums to ~23.80
- community revenue sums to 506.7
- unit counts sum to 376
- 376/25 acres = 15.0/acre
- CPL = 9.84Cr/78,880
- CPQL = 9.84Cr/12,474
- CPQSV = 9.84Cr/2,922 held visits
- cost per booked visit = 9.84Cr/4,870
- 4,870 booked x 60% show = 2,922 held
- 2,922/12,474 = 23.4%
- 574/2,922 = 19.6%
- 376 net / 0.92 = 409 gross
- opex/376 = 6.33 L
- total/376 = 8.44 L
- media ~62% of opex
- media ~46% of total
- media/45mo = ~32.6 L per month
- 0.25/23.80 = ~1.0% of opex
- 0.25/31.75 = ~0.8% of headline
- 2,922 held visits = 15.0/week over 45 months
- cancellation shortfall = 40.5 Cr
- scenario spread = 552.6 Cr
- CAC headroom 1.34x
- gross profit @28% = 141.9 Cr
- ROMI 3.47x = (141.9-31.75)/31.75
- revenue/spend would read ~16.0x
- test media lines sum to 18.00 L
- test non-media lines sum to 7.00 L
- gap actions sum to 41.5 L
- 41.5 L = 1.3% of 31.75 Cr
- no banned phrases; found=[]
- ROMI on gross profit
- label lab-g (Assignment assumption) used
- label lab-w (Working assumption) used

## Language & credibility rules — 5 checks

- no CMO designation anywhere in the deck
- governance roles named neutrally
- first-person conditional voice used throughout (39)
- attribution present
- submitted-to present

## Budget framing rules — 7 checks

- 31.75 explicitly framed as NOT a marketing budget
- 31.75 framed as a planning ceiling
- 25L framed as validation
- booking rate stated as not measurable at the test sample
- ROAS marked diagnostic only
- revenue/spend called out
- validation-required flagged repeatedly

## Evidence labelling — 6 checks

- 25L test: 18 media + 7 non-media
- label lab-r (Researched) used
- label lab-d (Derived calculation) used
- explicit no-KMV-confirmation statement
- community architecture framed as proposed, not confirmed
- gaps named as not found

---

## The twenty-point quality control, item by item

| # | Check | Result |
| --: | --- | --- |
| 1 | Every number verified against the repository | **Pass** — 109 key figures cross-checked against the full `KMV-Amaravati` markdown tree; all present in both |
| 2 | Every factual external claim has a source | **Pass** — 20 source IDs, all resolving to Appendix F; every `[Sxx]` used is defined |
| 3 | Unsupported assumptions identified | **Pass** — 20 in the assumptions register, five flagged as strategy-changing |
| 4 | All derived numbers labelled | **Pass** — four labels used throughout; a source strip on all 23 content slides |
| 5 | ₹31.75 Cr not described as pure marketing spend | **Pass** — slide 17 states it *"is not a marketing budget"* and frames it as a planning ceiling of four separate categories |
| 6 | ₹25 lakh presented as validation investment | **Pass** — slide 16 is titled a validation tranche, *"not a small version of the campaign"* |
| 7 | No claim implies personally managing this budget | **Pass** — no banned phrase present; first-person conditional (*"I would"*) used 39 times; no CMO designation anywhere |
| 8 | Assignment vs research vs inference vs recommendation obvious | **Pass** — slide 03 separates them into three columns that never mix; every later slide carries its basis in the source strip |
| 9 | Every chart's arithmetic checked | **Pass** — 37 arithmetic assertions, including the funnel, the tranches and the community allocation |
| 10 | Budget totals check | **Pass** — ₹23.80 + ₹4.04 + ₹3.15 + ₹0.76 = ₹31.75 Cr; tranches sum to ₹21.90 Cr; +₹1.90 Cr reserve = ₹23.80 Cr |
| 11 | KPI formulas check | **Pass** — CPL, CPQL, cost per booked and per qualified site visit, CAC and break-even each recomputed from their inputs |
| 12 | ROMI on the appropriate profit basis | **Pass** — (gross profit − marketing) ÷ marketing; 3.47× at 28%, with 2.99× / 3.95× at 25% / 31% shown as the sensitivity |
| 13 | Revenue ÷ spend not called ROMI | **Pass** — 16.0× appears once, explicitly labelled meaningless and marked *"do not present it"* |
| 14 | Mobile and desktop rendering | **Pass** — no horizontal page scroll and no unguarded overflow at 390 px or 1440 px; no console errors |
| 15 | Text overflow | **Pass** — no element clipped by a fixed-height ancestor at either viewport; wide tables scroll inside their own container |
| 16 | Source footnotes | **Pass** — the source strip is a structural element on every content slide, not an optional decoration |
| 17 | Appendix source register | **Pass** — Appendix F carries all 20 IDs and all 40 URLs, generated from the same data as `source-register.md` |
| 18 | Presentable in 15–20 minutes | **Pass by design** — 24 numbered slides plus 5 part dividers; ~40 seconds a slide. Appendices are reference, not presentation |
| 19 | Speculative content removed | **Pass** — the airport and metro are excluded entirely; the ORR is stated as *approved*, never *coming*; the AIIMS credential is not claimed anywhere |
| 20 | No invented KMV information | **Pass** — no estimate of KMV's budget, spend, headcount, historical CPL, velocity or inventory appears; each is named as a gap instead |

---

## What the checks deliberately do not cover

**Three things no automated check can settle, stated so the pass rate is not mistaken for validation of the strategy itself:**

1. **Whether the underlying assumptions are true.** The checks verify that every figure is internally consistent, correctly labelled and traceable. They cannot verify that a 28% gross margin, a 6.9% visit-to-booking rate or a 50% locality price premium is *correct* — only that each is labelled as an assumption and named in the register.

2. **Whether the sources say what they are cited as saying.** No URL in the register was opened. The checks confirm each citation resolves to a defined source ID; they cannot confirm the underlying document supports the claim.

3. **Whether the strategy is the right one.** That is a judgement, and the deck is written to be argued with rather than accepted — which is why every claim names what would falsify it.

---

## Rebuilding and re-running

```sh
cd 15_Deck/src && ./build.sh
```

Regenerates the deck from source, re-measures each slide for print, re-exports the PDF, and re-runs all 151 checks.

---

*Marketing Strategy Assignment — KMV Spaces, Amaravati / Mangalagiri. Prepared by Kiran Basa, submitted to Mr. Anudeep.*
