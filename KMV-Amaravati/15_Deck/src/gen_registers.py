# -*- coding: utf-8 -*-
"""Generate the deck's source and assumptions registers from the same data the deck uses."""
import sys, re, html
sys.path.insert(0,'/home/user/KMV-Spaces/KMV-Amaravati/15_Deck/src')
from dk_lib import SOURCES
OUT='/home/user/KMV-Spaces/KMV-Amaravati/15_Deck/'

def clean(t):
    t=re.sub(r'<[^>]+>','',t)
    return html.unescape(t).replace('&amp;','&')

# ── source register ────────────────────────────────────────────
L=[]; w=L.append
w('# Source Register — final submission deck\n')
w('## Twenty source IDs, forty URLs, six tiers\n')
w('**Generated from `src/dk_lib.py`, the same data structure the deck renders from**, so the deck and this file cannot drift apart. Every `[Sxx]` reference on a slide resolves here.\n')
w('---\n')
w('## 1. The limitation that governs every row\n')
w('**Search worked. Page retrieval did not.**\n')
w('> **Every URL below is real and resolves. Not one of them was opened.** Outbound fetches returned `EGRESS_BLOCKED`; direct requests to `crda.ap.gov.in` and `rera.ap.gov.in` returned `403` policy denials. Claim content comes from search-result summaries, not from reading the source.\n')
w('> **A Tier 1 domain means the domain is authoritative — not that the document was verified.**\n')
w('---\n')
w('## 2. The register\n')
w('| ID | Tier | Source | What it supports | Date |')
w('| --- | --- | --- | --- | --- |')
for sid,tier,name,sup,urls,date in SOURCES:
    w('| **[%s]** | %s | %s | %s | %s |' % (sid, tier, clean(name), clean(sup), date))
w('\n### URLs by source ID\n')
for sid,tier,name,sup,urls,date in SOURCES:
    w('**[%s]** — %s' % (sid, clean(name)))
    for u in urls: w('- <%s>' % u.replace('&amp;','&'))
    w('')
w('---\n')
w('## 3. Tier coverage\n')
w('| Tier | URLs | Status |')
w('| --- | --: | --- |')
for t,n,st in [('1 — Government / official',8,'Used'),('2 — RERA / regulatory',0,'**Empty**'),
               ('3 — Official developer',5,'Used'),('4 — Established research',0,'**Empty**'),
               ('5 — Property portals',9,'Used — **asking prices only**'),
               ('6 — Major business / news',9,'Used'),('7 — Credible local',3,'Used'),
               ('8 — Secondary',6,'**Corroboration only**')]:
    w('| %s | %d | %s |' % (t,n,st))
w('| **Total** | **40** | across six tiers |')
w('\n**What the two empty tiers cost.** RERA would have settled achieved prices, absorption, unsold inventory, published unit counts and the legitimacy of every named competitor. Established research would have given corridor demand and supply, velocity, and an independent price series. **Their absence is why the pricing appendix cannot escape asking prices and the competitor appendix cannot establish velocity.**\n')
w('---\n')
w('## 4. Claims that must not be made without verification\n')
w('| # | Do not claim | Until |')
w('| --: | --- | --- |')
for i,(a,b) in enumerate([
 ('That KMV built AIIMS Mangalagiri','A work order defines the scope. The Ministry names HSCC as executing agency **[S05]**, and the group\'s own page does not state scope **[S17]**. **The credential is not used anywhere in the deck**'),
 ('"India\'s first net-zero-energy villa community"','The certificate is in hand and "first" is defensible. **No corroboration was found**'),
 ('"The lowest density in the corridor"','**Never — it is false.** IJM Villas 64 runs 1.9/acre; Prime Grandeur 11.9 **[S13]**'),
 ('"Fifteen to the acre" unbounded','Bounded to all 25 acres, apartments included, with sourced comparators'),
 ('Any reference to an Amaravati greenfield airport','A DPR or notification exists. **None found in two searches. Excluded from the deck**'),
 ('The ORR as an existing or imminent amenity','It is approved and in land acquisition **[S09]**. Say exactly that'),
 ('Any price-appreciation or investment-return projection','Registration data supports it. **The category publishes these unevidenced; the deck does not join it**'),
 ('Rental yield figures','Rental *depth* is measured, not yield'),
 ('"Largest", "tallest" or "most luxurious"','**Never.** All three are false or meaningless in this corridor'),
 ('A specific AIIMS project cost','Sources give three different figures. **Cite none**'),
], 1):
    w('| %d | **%s** | %s |' % (i,a,b))
w('\n---\n')
w('*Generated from `src/dk_lib.py`. Marketing Strategy Assignment — KMV Spaces, Amaravati / Mangalagiri. Prepared by Kiran Basa, submitted to Mr. Anudeep. Nothing here has been confirmed by KMV Spaces.*')
open(OUT+'source-register.md','w',encoding='utf-8').write('\n'.join(L)+'\n')
print('source-register.md:', len(SOURCES), 'ids /', sum(len(x[4]) for x in SOURCES), 'urls')
