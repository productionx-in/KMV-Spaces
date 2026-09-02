# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/claude-0/-home-user/a5dd8d44-0929-5495-aca9-31c380eaeac4/scratchpad')
from dk_lib import *
P=[]; w=P.append

def apx(aid, letter, title, dek):
    w('\n<section class="apx" id="%s">' % aid)
    w('  <p class="ax">Appendix %s</p>' % letter)
    w('  <h2>%s</h2>' % title)
    w('  <p class="sdek">%s</p>' % dek)
def endapx(): w('</section>')

w(band('Appendices','The working papers','Seven appendices: assumptions, pricing evidence, competitor evidence, the budget model, KPI definitions, the full source register, and what this research could not establish.'))

# ═══ A — ASSUMPTIONS ═══
apx('apxA','A','Assumptions register',
 'Every number in this deck that is not sourced. <strong>Each one requires KMV validation, and each names what would replace it.</strong>')
w(table(['#','Assumption','Value used','Label','What would replace it'],[
 ['A1','Unit count on 25 acres','<strong>376 units</strong> · 15.0/acre','Derived','A masterplan and approvals'],
 ['A2','Community mix','A 169 · B 84 · C 60 · D 63','Derived','A product decision'],
 ['A3','Price ladder','₹5,150 / 5,700 / 6,500 / 7,200 per sq ft','Derived from researched competitor tickets','IGRS registration data, 24 months'],
 ['A4','Blended realisation','<strong>₹6,098/sq ft</strong>','Derived','As above'],
 ['A5','Revenue','<strong>₹506.7 Cr</strong>','Derived','As above'],
 (['A6','<strong>Development gross margin</strong>','<strong>28%</strong>','<strong>Working assumption &mdash; a placeholder</strong>','<strong>Contractor quotations. No cost data exists anywhere behind this work</strong>'],'hl'),
 ['A7','Sell window','45 months <i>(51 including clearance)</i>','Working assumption','Construction and handover milestones'],
 ['A8','Cost per lead','₹1,247 blended','Derived from the media assumption','24 months of historical lead data'],
 ['A9','Lead &rarr; qualified','15.81% compound <i>(45% &times; 55% &times; 63.9%)</i>','Working assumption &mdash; a decomposition','90 days of CRM data'],
 ['A10','Qualified &rarr; site visit held','23.4%','Working assumption','As above'],
 ['A11','Site-visit show rate','60%','Working assumption','As above'],
 ['A12','Site visit &rarr; booking','6.9%','Working assumption','<strong>Two quarters of live trading &mdash; not a ₹25 lakh test</strong>'],
 ['A13','Source mix','53% marketing · 28% channel partner · 19% referral','Working assumption','First-touch attribution field'],
 (['A14','<strong>Cancellation rate</strong>','<strong>8%</strong>','<strong>Working assumption &mdash; the model originally had none</strong>','<strong>Historical cancellation data. Moves revenue by ₹40.5 Cr</strong>'],'hl'),
 ['A15','Reach','6,573,000','Working assumption &mdash; <strong>an output of the lead rate, not an input</strong>','Platform reach data once live'],
 ['A16','Marketing opex','₹23.80 Cr','Derived by reclassifying the ₹31.75 Cr model','A committee decision on the envelope'],
 ['A17','Internal marketing team','₹1.53&ndash;3.06 Cr over the window','<strong>Working assumption &mdash; a range, not a quote</strong>','KMV&rsquo;s actual team structure and payroll'],
 ['A18','Performance agency fee','12% of digital media','Working assumption','An agency contract'],
 ['A19','Referral rate','18.5% of bookings, flat','Working assumption &mdash; <strong>structurally back-loaded</strong>','Should be modelled ramping from ~0% in year one'],
 ['A20','Segment sizes and behaviour','Eight segments, scored','<strong>Working assumption throughout</strong>','<strong>Primary buyer research. None exists</strong>'],
]))
w(co('The five that would change the strategy if wrong',
 ['<strong>A6 (gross margin)</strong> &mdash; every ROI figure rests on it. <strong>A3/A4 (the price ladder)</strong> &mdash; a 50% premium to the locality asking average, untested. <strong>A12 (visit-to-booking)</strong> &mdash; ₹39.4 Cr per point. <strong>A14 (cancellation)</strong> &mdash; ₹40.5 Cr. <strong>A20 (segments)</strong> &mdash; the entire targeting plan.']))
endapx()

# ═══ B — PRICING EVIDENCE ═══
apx('apxB','B','Pricing evidence',
 'How every ₹/sq ft figure was derived, the external benchmark it was tested against, and the exposure that testing revealed.')
w('<h3 class="sh">The method</h3>')
w('<p class="fine">Published locality averages for this micro-market disagree by up to 40%. So every rate here is derived as <strong>published ticket price &divide; published unit size</strong>, for named projects. <strong>Seven of the eight projects publishing both ends of a range agree internally within 0.7%</strong>, which is why derived bands are preferred over any locality average.</p>')
w(table(['Reference point','#₹/sq ft','Type','Source'],[
 ['Mangalagiri locality average, asking <i>(Sept 2025)</i>','<strong>4,062</strong>','Portal',sid_('S11')],
 ['Mangalagiri, June 2025','4,098','Portal',sid_('S11')],
 ['Wider micromarket, Mar 2025','4,805','Portal',sid_('S11')],
 ['Wider micromarket, Dec 2025','5,489','Portal',sid_('S11')],
 ['SLV Amaravathi Pride','4,210','Portal, project-level',sid_('S15')],
 (['<strong>Manjeera Monarch &mdash; delivered comparable</strong>','<strong>5,100</strong>','Portal, project-level',sid_('S12')],'hl2'),
 ['Prime Grandeur','5,394&ndash;5,403','Portal, project-level',sid_('S13')],
 ['IJM Villas 64','10,143','Portal, project-level',sid_('S13')],
 (['<strong>&mdash; This plan, blended</strong>','<strong>6,098</strong>','<strong>Derived calculation</strong>','&mdash;'],'hl'),
]))
w('<div class="g2">')
w(co('What the comparison says',
 ['<strong>The plan asks a 50% premium to the Mangalagiri locality average and 11% to the wider micromarket.</strong>',
  'That is not automatically wrong &mdash; a 15-per-acre scheme with villas <em>should</em> price above a locality average dominated by towers. <strong>But the premium had never been sized before, and it is the largest commercial assumption in the project.</strong>']))
w(co('Community A is the exposure nobody flagged',
 ['At ₹5,150/sq ft, Community A prices <strong>above a delivered apartment comparable at ₹5,100</strong> in the same locality <span class="sid">[S12]</span> and 27% above the locality average.',
  '<strong>A is 169 units &mdash; 45% of the scheme &mdash; and the community least able to command a premium</strong>, because a garden apartment competes directly on rate.']))
w('</div>')
w(co('And a finding that points the other way',
 ['KMV Vivaan asks <strong>₹3.59 Cr (Phase I) and ₹5.21 Cr (Phase II)</strong> <span class="sid">[S14]</span>. If those clear, Community D at ₹2.30&ndash;2.74 Cr sits <strong>below the developer&rsquo;s own achieved range</strong> &mdash; and may be under-priced.',
  '<strong>These two observations point in opposite directions, and both are testable from data KMV already holds.</strong> Note also that Vivaan is at Poranki / Penamaluru, east Vijayawada &mdash; <strong>not on the corridor</strong>, so it is a pricing reference, not a location comparable.'],'ev'))
w('<p class="fine"><strong>The caveat that governs this entire appendix: every price above is an asking price.</strong> No transaction or registration data was obtained. IGRS AP registration data for Mangalagiri and Thullur mandals &mdash; a 24-month series &mdash; is the single highest-value missing source behind this work, and it would settle up to <strong>₹50.7 crore</strong> of price risk for about ₹2.5 lakh.</p>')
endapx()

# ═══ C — COMPETITOR EVIDENCE ═══
apx('apxC','C','Competitor evidence',
 'The screen, the field, and the three claims that did <em>not</em> survive it.')
w(table(['Project','Developer','Scale · density','Price evidence','Positioning','Weakness','Source'],[
 ['<strong>Raintree Park Dwaraka Krishna</strong>','IJM Lingamaneni (IJM + LEPL)','120 ac · ~3,300 planned','Apartments ~₹3,900/sq ft; villas to ₹10,143','&ldquo;International class integrated township&rdquo;','<strong>Has the full ladder and never markets it as one</strong> &mdash; five names, 18 years',sid_('S13')],
 ['<strong>IJM Villas 64</strong>','IJM Lingamaneni','33.69 ac · 64 villas · <strong>1.9/acre</strong>','From ₹3.75 Cr','&ldquo;A private enclave of just 64 homes&rdquo;','₹3.75 Cr floor excludes almost the whole corridor buyer base; <strong>no proof layer</strong>',sid_('S13')],
 ['<strong>Prime Grandeur</strong>','Prime Constructions','10 ac · 119 villas · 11.9/acre','₹1.34&ndash;1.82 Cr · ₹5,394&ndash;5,403/sq ft','Mid-premium villa living, value-led','<strong>The most direct competitor.</strong> No delivery evidence published','&mdash;'],
 ['<strong>Manjeera Monarch</strong>','Manjeera Constructions','Apartments · 113/acre','<strong>₹5,100/sq ft &mdash; delivered</strong>','Amenity-led apartments','<strong>Documented carpet-area complaint</strong>; developer satisfaction described as very low',sid_('S12')],
 ['Srivalli Pravas','Undavalli Constructions','2BHK to duplex on one site','&mdash;','&ldquo;Luxury apartments&rdquo;','<strong>Has stumbled into a ladder without articulating it</strong>','&mdash;'],
 ['Jayabheri The Capital','Jayabheri Group','&mdash;','&mdash;','Amenity-led','<strong>Returned no search result at all</strong> &mdash; and it anchors a density comparison','<strong>Gap</strong>'],
 ['Grand Project Capitol','Kalidindi Real Konsult','95.4/acre','&mdash;','&ldquo;68% open spaces, only 32% construction&rdquo;','<strong>Open ground, but not a low-density community</strong>','&mdash;'],
 ['Aparna Amaravati One','Aparna Constructions','612 units, ~30% occupied','Below the target band','Ready gated community','<strong>A gated community two-thirds empty is not a community</strong>','&mdash;'],
 ['TAG AIRA · KMV Vivaan · CRDA plots','Various','&mdash;','Vivaan ₹3.59&ndash;5.21 Cr','Smart homes · villas · land','Sub-scale, off-corridor, or a different product',sid_('S14')],
]))
w(co('Three claims that did not survive the evidence',
 ['<strong>&ldquo;The corridor&rsquo;s largest project&rdquo; &mdash; false.</strong> Raintree Park is 120 acres.',
  '<strong>&ldquo;The lowest density in the corridor&rsquo; &mdash; false.</strong> IJM Villas 64 runs 1.9/acre; Prime Grandeur 11.9 <span class="sid">[S13]</span>. The defensible formulation is narrower: <em>the lowest density for a community that includes apartments</em>, bounded to all 25 acres.',
  '<strong>&ldquo;The only large villa community&rdquo; &mdash; false.</strong> Prime Grandeur has 119 villas; Raintree Park Phase 1 delivered 116.']))
w('<p class="fine"><strong>Two limits on this appendix.</strong> Densities are derived from published acreage &divide; published unit counts <em>where both exist</em> &mdash; for two comparators they do not, so the density claim on slide 13 must be footnoted rather than asserted. And <strong>no velocity or absorption data was obtained for any competitor</strong>, because the RERA tier returned nothing.</p>')
endapx()

# ═══ D — BUDGET MODEL ═══
apx('apxD','D','Detailed budget model',
 'The full line-item build, the reclassification that separates four kinds of money, and the tranche schedule.')
w('<h3 class="sh">The reclassification &mdash; why ₹31.75 Cr is not a marketing budget</h3>')
w(table(['Category','#Amount','#% of total','Nature','Whose P&amp;L'],[
 (['<strong>TOTAL COMMERCIAL BUDGET</strong>','<strong>₹31.75 Cr</strong>','100%','<strong>A planning ceiling, not an ask</strong>','&mdash;'],'tot'),
 (['<strong>True marketing OPEX</strong>','<strong>₹23.80 Cr</strong>','75.0%','Operating expense','<strong>Marketing</strong>'],'hl'),
 ['Cost of sale','₹4.04 Cr','12.7%','Channel-partner commission + referral &mdash; <strong>paid only on performance</strong>','Sales'],
 ['Sales infrastructure capex','₹3.15 Cr','9.9%','A building &mdash; an asset, amortised','Capex'],
 ['Technology capex','₹0.76 Cr','2.4%','A system &mdash; an asset, amortised','Capex'],
]))
w('<h3 class="sh">Inside the ₹23.80 Cr of marketing opex</h3>')
w(table(['#','Line','#Amount','#% of opex','Fixed / variable','Controllable?','KPI'],[
 (['1','<strong>Digital performance media</strong>','<strong>₹9.84 Cr</strong>','41.3%','Variable','Partly &mdash; <strong>the auction price is not</strong>','CPQL, CPSV'],'hl2'),
 ['2','Outdoor (OOH)','₹2.13 Cr','8.9%','<strong>Fixed once committed</strong>','No &mdash; contracted','Recall, geo holdout'],
 ['3','Content production','₹2.44 Cr','10.3%','Semi-fixed','Yes','Hook rate, CPQL by variant'],
 ['4','Performance agency fee','₹1.18 Cr','5.0%','Variable with media','Yes','Blended CPQL vs target'],
 ['5','Events / experiences','₹1.17 Cr','4.9%','Semi-fixed','Yes','Site visits generated'],
 ['6','Print','₹1.17 Cr','4.9%','<strong>Fixed per insertion</strong>','No &mdash; rate card','Recall, holdout'],
 ['7','NRI infrastructure','₹1.05 Cr','4.4%','Semi-fixed','Yes','B&rsquo;s qualified-to-visit rate'],
 ['8','Telugu OTT + YouTube brand','₹0.99 Cr','4.2%','Variable','Yes','Assisted conversions'],
 ['9','Brand agency retainer','₹0.81 Cr','3.4%','Fixed','Yes','Output SLA'],
 ['10','PR','₹0.75 Cr','3.2%','Fixed','Partly','Earned coverage'],
 ['11','Collateral + sales training','₹0.47 Cr','2.0%','Semi-fixed','Yes','Site-visit-to-booking'],
 ['12','Launch digital burst','₹0.40 Cr','1.7%','Variable','Yes','Launch-window CPQL'],
 ['13','CRM / marketing automation','₹0.33 Cr','1.4%','Fixed','Yes','Lead-to-qualified rate'],
 ['14','Technology <i>(opex)</i>','₹0.33 Cr','1.4%','Fixed','Yes','LP conversion rate'],
 ['15','Brand identity + design system','₹0.30 Cr','1.3%','Fixed, one-time','Yes','Delivery milestone'],
 ['16','Channel / broker enablement','₹0.16 Cr','0.7%','Semi-fixed','Yes','CP bookings, discount discipline'],
 (['17','<strong>Research &amp; experiments</strong>','<strong>₹0.25 Cr</strong>','1.1%','Variable','Yes','<strong>Gate pass / fail</strong>'],'hl'),
 (['18','<strong>Internal team</strong>','<strong>₹1.53&ndash;3.06 Cr</strong>','6&ndash;11%','Fixed','Yes','<strong>Working assumption &mdash; a range, not a quote</strong>'],'hl'),
 (['19','<strong>Contingency reserve</strong>','<strong>₹1.90 Cr</strong>','8.0%','&mdash;','<strong>No &mdash; finance-held</strong>','Released on a named event only'],'hl'),
]))
w(table(['','#Amount','Note'],[
 (['<strong>MEDIA total</strong>','<strong>₹14.65 Cr</strong>','62% of opex · 46% of the total commercial budget · <strong>₹32.6 lakh a month across 45 months</strong>'],'hl2'),
 ['<strong>NON-MEDIA total</strong>','<strong>₹9.15 Cr</strong>','Plus the internal-team range'],
 (['<strong>REVISED ENVELOPE</strong> <i>(with internal team)</i>','<strong>₹25.33&ndash;26.86 Cr</strong>','All-in ₹33.28&ndash;34.81 Cr · CAC ₹8.85&ndash;9.26 L · <strong>both ends inside the 30%-of-gross-profit ceiling</strong>'],'tot'),
]))
w('<h3 class="sh">Tranche schedule</h3>')
w(table(['Phase','#Release','#% opex','#Cumulative','Gate'],[
 (['<strong>0 · Validation</strong>','<strong>₹0.25 Cr</strong>','1.0%','₹0.25 Cr','CPL ≤ ₹1,550 · CPQSV ≤ ₹42,000'],'hl'),
 ['1 · Launch prep','₹2.60 Cr','10.9%','₹2.85 Cr','CRM live · attribution mandatory · WhatsApp integrated · figures reconciled'],
 ['2 · Market entry','₹4.20 Cr','17.6%','₹7.05 Cr','≥ 55 bookings · CPL within +25% · show rate ≥ 60%'],
 ['3 · Scale','₹8.10 Cr','34.0%','₹15.15 Cr','V2B ≥ 5.5% over two quarters · CAC ≤ ₹9.5 L'],
 ['4 · Optimise','₹5.05 Cr','21.2%','₹20.20 Cr','Referral ≥ 0.15/owner-year · CAC falling QoQ'],
 ['5 · Clearance','₹1.70 Cr','7.1%','₹21.90 Cr','Inventory &lt; 15% · referral ≥ 25% of bookings'],
 (['<strong>Deployable core</strong>','<strong>₹21.90 Cr</strong>','<strong>92.0%</strong>','','&mdash;'],'tot'),
 ['Contingency reserve','₹1.90 Cr','8.0%','','<strong>Finance-held.</strong> Named event only'],
 (['<strong>MARKETING OPEX</strong>','<strong>₹23.80 Cr</strong>','<strong>100%</strong>','','<i>before the internal-team line</i>'],'tot'),
]))
w('<h3 class="sh">Community allocation</h3>')
w(table(['','#A','#B','#C','#D'],[
 ['Marketing opex','<strong>₹4.26 Cr</strong> <i>(17.9%)</i>','<strong>₹9.47 Cr</strong> <i>(39.8%)</i>','<strong>₹3.78 Cr</strong> <i>(15.9%)</i>','<strong>₹6.28 Cr</strong> <i>(26.4%)</i>'],
 ['Opex per unit','₹2.52 L','<strong>₹11.28 L</strong>','₹6.31 L','₹9.97 L'],
 ['As % of its own revenue','3.38%','<strong>8.42%</strong>','3.47%','3.96%'],
 ['Target CAC','₹3.4 L','₹15.0 L','₹8.4 L','₹13.3 L'],
]))
w('<p class="fine"><strong>Allocation principle.</strong> Directly attributable costs are traced &mdash; performance media by community, the agency fee pro-rata, and the NRI infrastructure that serves B alone. <strong>Everything shared is allocated by revenue share</strong>, because the brand, the site, the technology and the launch serve all four. Allocating by unit count instead would load Community A with 45% of the shared cost for 25% of the revenue.</p>')
w(co('Scenario sensitivity &mdash; media held constant in all three cases',
 ['<strong>Conservative</strong> &mdash; 194 net units, ₹240.9 Cr, CAC ₹16.09 L, ROMI 1.16&times;, <strong>CAC at 46.3% of gross profit.</strong> This breaches the policy ceiling and should not be funded as planned.',
  '<strong>Base</strong> &mdash; 346 net units, ₹466.2 Cr, CAC ₹9.23 L, ROMI 3.09&times;. <strong>Note this is ₹40.5 Cr below the ₹506.7 Cr plan target, because cancellation was never modelled.</strong>',
  '<strong>Upside</strong> &mdash; 572 net units, ₹793.6 Cr, CAC ₹5.66 L, ROMI 5.86&times;.',
  '<strong>Margin sensitivity, base case:</strong> ROMI reads <strong>2.99&times; at a 25% gross margin, 3.47&times; at 28% and 3.95&times; at 31%</strong> &mdash; a 32% swing on an assumption nobody has tested. <strong>Break-even is the statement that survives it: 94 / 84 / 76 bookings of 376.</strong>',
  '<strong>The spread between conservative and upside is ₹552.6 crore &mdash; 109% of the base case. Establishing which world this is, is what the ₹25 lakh buys.</strong>'],'calc'))
endapx()

open('/tmp/claude-0/-home-user/a5dd8d44-0929-5495-aca9-31c380eaeac4/scratchpad/deck_f.html','w',encoding='utf-8').write('\n'.join(P)+'\n')
print('appendices A-D written')
