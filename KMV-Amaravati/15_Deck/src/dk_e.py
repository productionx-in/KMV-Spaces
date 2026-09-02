# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/claude-0/-home-user/a5dd8d44-0929-5495-aca9-31c380eaeac4/scratchpad')
from dk_lib import *
import dk_lib
dk_lib._N[0] = 19
P=[]; w=P.append

w(band('Part three','The decision, and what would change it'))

# ═══════════════ 20 GAPS ═══════════════
o,_ = slide('s20','Gaps &amp; what I would fix first','Thirty-six gaps across twelve domains &mdash; and eighteen close for ₹41.5 lakh',
  'Prioritised by <strong>impact &times; urgency &divide; effort.</strong> Eleven of the first thirteen actions cost nothing at all &mdash; they are decisions, not budgets.')
P.extend(o)
w('<div class="gsplit">\n<div>')
w('<h3 class="sh" style="margin-top:0">Free &mdash; do these before any money commits</h3>')
w(table(['Domain','Action','What it settles'],[
 ['<strong>Brand</strong>','Consolidate domain and social identity','Splits authority every day it waits'],
 ['<strong>Measurement</strong>','Reconcile every published project figure','A transparency launch over contradictory numbers'],
 ['<strong>CX</strong>','Reverse the site photography restriction, publicly','A live review complaint that contradicts the position'],
 ['<strong>Content</strong>','Bound the density claim and write the footnote','<strong>The campaign&rsquo;s central claim</strong>'],
 ['<strong>Attribution</strong>','Specify first-touch, consultation and negotiation as CRM events','<strong>₹9.84 Cr of allocation</strong>, and a diagnosable funnel'],
 ['<strong>CRM</strong>','Name the CRM owner; write the qualification criteria','<strong>₹17.2 Cr per point</strong>'],
 ['<strong>Performance</strong>','Put the three reading rules in the reporting template','<strong>₹10.25 Cr of defensible spend</strong>'],
]))
w('</div>\n<div>')
w('<h3 class="sh" style="margin-top:0">Paid &mdash; ₹41.5 lakh total, and it buys evidence, not media</h3>')
w(table(['Action','#Cost','What it settles'],[
 ['IGRS registration series, 24 months, two mandals','₹2.5 L','Up to <strong>₹50.7 Cr</strong> of price risk'],
 ['Segment sizing from registration and institutional data','₹4.0 L','Six of eight segments'],
 ['Competitor velocity in the ₹2.2&ndash;2.8 Cr band, 8 weeks','₹3.5 L','<strong>₹158.8 Cr</strong> &mdash; the largest open question'],
 ['30&ndash;40 depth interviews + landowner families','₹12.0 L','The behavioural attributes of all eight segments'],
 (['<strong>Paid media test across four community audiences</strong>','<strong>₹17.5 L</strong>','<strong>The CPLs underwriting ₹11.02 Cr</strong>'],'hl'),
 ['Twenty proxy visits on an existing project','₹2.0 L','<strong>₹12.63 Cr</strong> of Community B budget'],
 (['<strong>Total</strong>','<strong>₹41.5 L</strong>','<strong>= 1.3% of the ₹31.75 Cr planning envelope</strong>'],'tot'),
]))
w(co('The honest framing',
 ['<strong>₹41.5 lakh does not de-risk ₹158.8 crore.</strong> It tells you whether ₹158.8 crore is real <em>before</em> you spend ₹31.75 crore finding out.',
  '<strong>Those are different claims and only the second one is honest.</strong>'],'calc'))
w('</div>\n</div>')
w(strip([('Basis','<b>Derived.</b> Every cost is my assumption; a quote would replace it'),
         ('Overlap','The ₹17.5 L media test is the media component of the ₹25 lakh validation tranche on slide 16'),
         ('Sequence','Free actions first, then the paid ones, then any launch commitment')]))

# ═══════════════ 21 RISK ═══════════════
o,_ = slide('s21','Risks &amp; mitigation','Ten risks &mdash; each with an early signal that fires without a meeting',
  '<strong>The two critical risks are both pricing risks, and neither is a marketing risk.</strong> That is the honest hierarchy: the largest threats sit above the marketing function, and marketing&rsquo;s first job is to detect them cheaply.')
P.extend(o)
w(table(['#','Risk','Tier','Early signal','Mitigation / kill trigger'],[
 (['1','<strong>The price ladder does not clear</strong> &mdash; a 50% premium to the locality asking average, untested','<span class="lab lab-w">Critical</span>','Achieved sits &gt;12% below list in any band','<strong>Test before Phase 1. Re-cut that band</strong>'],'hl'),
 (['2','<strong>The ₹2.2&ndash;2.8 Cr band is thin</strong> &mdash; ₹268 Cr of the plan sits in it','<span class="lab lab-w">Critical</span>','Competitor absorption &lt; 1.5 units/month','<strong>Re-cut D toward C before launch</strong>'],'hl'),
 ['3','<strong>CPL is materially worse than assumed</strong> &mdash; the media line is derived, never quoted','High','Observed CPL &gt;30% above assumption','<strong>Stop and re-base.</strong> Not reduced scale'],
 ['4','<strong>Conservative scenario materialises</strong> &mdash; CAC at 46.3% of gross profit','High','CAC &gt; ₹11.32 L for two quarters','<strong>Halt tranche release</strong>'],
 ['5','<strong>Lead quality collapses</strong> &mdash; volume holds, cash-gate pass rate falls','High','Lead-to-qualified drifts below 12%','Tighten qualification and creative, <strong>not media spend</strong>'],
 ['6','<strong>Sales follow-up fails</strong> &mdash; the highest-leverage stage is not marketing-controlled','High','Follow-up latency &gt; 24h; show rate &lt; 60%','Coaching and confirmation process, weekly by consultant'],
 ['7','<strong>Over-dependence on paid media</strong> &mdash; only ₹14.65 Cr is genuinely variable','Medium','Referral below 0.15/owner-year at Phase 4','<strong>Cap outdoor and print until Phase 3</strong>'],
 ['8','<strong>The brand credential cannot be documented</strong> at the scope implied <span class="sid">[S05][S17]</span>','Medium','No work order produced on request','<strong>Fall back to density arithmetic and ungated pricing</strong> &mdash; both provable without credentials'],
 ['9','<strong>Attribution never gets installed</strong> &mdash; spend without learning','Medium','Phase 1 gates are binary','<strong>No CRM, no Phase 2</strong>'],
 ['10','<strong>Budget leakage</strong> &mdash; discounting by channel partners erodes achieved price','Medium','Partner discount &gt; direct +1.0 pt','Discount register reviewed monthly; <strong>partner termination</strong>'],
]))
w(strip([('Sources', sid_('S05','S17')+' for risk 8; all others derived from the model'),
         ('Basis','<b>Derived.</b> Tiers and triggers are my assessment'),
         ('Design principle','A register whose entries need a judgement call under stress is a list, not a control')]))

# ═══════════════ 22 ROADMAP ═══════════════
o,_ = slide('s22','45-month growth roadmap','What changes quarter by quarter &mdash; and what the mix looks like at each stage',
  '<strong>Year one is not steady state.</strong> Referral requires prior owners, and in year one there are none &mdash; so year one must carry more demand generation than the 45-month average implies.')
P.extend(o)
w(table(['Stage','Months','What the marketing function is doing','Mix','Leading metric','#Cumulative release'],[
 (['<strong>Validate</strong>','1&ndash;2','Discover the economics. Twelve creative variants, four audiences, five channels','<strong>100% test media</strong>','Cost per qualified site visit','<strong>₹0.25 Cr</strong>'],'hl'),
 ['<strong>Build</strong>','3&ndash;6','CRM, attribution, website, price sheet, first show home, sales training','<strong>0% media</strong>','Binary readiness gates','₹2.85 Cr'],
 ['<strong>Enter</strong>','7&ndash;15','Controlled launch. Digital performance only; two outdoor boards','~70% digital','Bookings; CPL vs Phase 0','₹7.05 Cr'],
 ['<strong>Scale</strong>','16&ndash;30','Full mix unlocks. Outdoor, print, OTT, PR added on validated economics','~55% digital, 25% brand','Site-visit-to-booking','₹15.15 Cr'],
 ['<strong>Compound</strong>','31&ndash;42','Referral and owner community take share from paid; CAC should fall','~40% digital, rising referral','CAC quarter on quarter','₹20.20 Cr'],
 ['<strong>Clear</strong>','43&ndash;51','Residual inventory. Retargeting, partners, resale, owner referral','Mostly earned','Inventory &lt; 15%','<strong>₹21.90 Cr</strong>'],
]))
w('<div class="g3">')
w(co('Community sequencing',
 ['<strong>C first, then D, then A, then B.</strong> C is the lowest-risk business in the portfolio and it proves the site. D needs seeded buyers before its first visit converts. <strong>B is last because its capability must be piloted first.</strong>'],'calc'))
w(co('The year-one correction',
 ['The model assumes <strong>18.5% referral across the whole period.</strong> That is structurally back-loaded. I would model referral <strong>ramping from ~0% in year one</strong> rather than flat &mdash; and fund year one accordingly.']))
w(co('What re-bases the roadmap',
 ['A failed Phase 0. A price test that comes back &gt;12% below list. A construction timeline that moves. <strong>The roadmap is a sequence of gates, not a calendar commitment.</strong>'],'ev'))
w('</div>')
w(strip([('Basis','<b>Derived.</b> The 45-month window follows from 376 units at the modelled velocity'),
         ('Requires validation','Construction and handover milestones, and approvals status'),
         ('Note','Sequencing is my recommendation; it is not a KMV release plan')]))

# ═══════════════ 23 DECISION FRAMEWORK ═══════════════
o,_ = slide('s23','Executive decision framework','The diagnostic that tells you <em>which</em> problem you have',
  'Every funnel number falls into one of five states. <strong>Each state has one correct response, and three incorrect ones that all look reasonable in a meeting.</strong>')
P.extend(o)
w('<div class="dx">')
for iff, then in [
 ('<b>CPQL within target</b> AND qualified site visits healthy AND sales follow-up SLA met','<b>Increase spend.</b> Release the next tranche'),
 ('<b>CPL is good but CPQL is poor</b>','You are buying the wrong people. <b>Fix targeting, qualification criteria and creative</b> &mdash; not budget'),
 ('<b>CPQL is good but site visits are poor</b>','The offer or the process is failing. <b>Fix scheduling, follow-up, trust and the reason to travel</b>'),
 ('<b>Site visits are strong but bookings are weak</b>','This is not a marketing problem. <b>Investigate pricing, product, sales capability and the offer</b>'),
 ('<b>Everything is weak</b>','<b>Stop.</b> The model is wrong, not the execution. Re-base before spending more'),
]:
    w('  <div class="dxr"><span class="if">%s</span><span class="ar">&rarr;</span><span class="th">%s</span></div>' % (iff, then))
w('</div>')
w('<div class="gsplit" style="margin-top:1.1rem">\n<div>')
w('<h3 class="sh" style="margin-top:0">The governance loop</h3>')
w('<div class="chain">'
  + '<div class="ch sa">TEST</div><div class="ch">&rarr;</div><div class="ch sa">VALIDATE</div><div class="ch">&rarr;</div>'
  + '<div class="ch mk">SCALE</div><div class="ch">&rarr;</div><div class="ch mk">OPTIMISE</div><div class="ch">&rarr;</div>'
  + '<div class="ch sa">RELEASE NEXT TRANCHE</div></div>')
w(table(['Cadence','Who is in the room','What is decided'],[
 ['<strong>Weekly</strong>','Marketing + Sales Head','CPQL, cost per qualified site visit, visit-to-booking, follow-up latency. <strong>Channel and creative reallocation</strong>'],
 ['<strong>Monthly</strong>','Marketing + Sales + Finance','CAC, conversion by source and community, discount register, cancellation. <strong>Inventory release</strong>'],
 ['<strong>Quarterly</strong>','CEO + CFO + Marketing','Gate pass/fail, ROMI, envelope review. <strong>Tranche release &mdash; or halt</strong>'],
]))
w('</div>\n<div>')
w('<h3 class="sh" style="margin-top:0">Who owns what</h3>')
w(table(['Function','Owns','Is measured on'],[
 ['<strong>Marketing</strong>','Everything up to the <strong>booked</strong> visit','CPQL · cost per qualified site visit'],
 ['<strong>Sales</strong>','The visit onward','<strong>Site-visit-to-booking</strong>, by consultant'],
 ['<strong>CRM</strong>','Lead-to-qualified rate','Data quality; attribution completeness'],
 ['<strong>Channel partners</strong>','28% of bookings, paid on performance','Bookings <strong>and discount discipline</strong>'],
 ['<strong>Finance</strong>','The reserve and the gates','CAC ceiling; tranche release'],
 ['<strong>Management</strong>','Price, product, inventory release','<strong>Achieved price vs list</strong>'],
]))
w(co('The rule that makes this work',
 ['<strong>Marketing and sales are read on the same number</strong> &mdash; site-visit-to-booking, weekly, by community and by consultant &mdash; <strong>so neither can blame the other&rsquo;s stage.</strong>']))
w('</div>\n</div>')
w(strip([('Basis','<b>Recommended framework.</b> The diagnostic states follow from the funnel arithmetic'),
         ('Not derived from','Any KMV organisational structure &mdash; none was provided'),
         ('Purpose','So that a bad quarter produces a diagnosis, not an argument')]))

# ═══════════════ 24 CLOSING ═══════════════
o,_ = slide('s24','Final recommendation','I would not release the full investment upfront',
  'Not because the number is wrong. <strong>Because releasing it against a forecast, rather than against evidence, is the avoidable risk in a ₹500 crore project.</strong>')
P.extend(o)
w('<div class="gsplit">\n<div>')
w(table(['','My recommendation'],[
 ['<strong>1</strong>','<strong>Establish a planning envelope</strong> &mdash; ₹23.80 Cr of marketing opex, rising to <strong>₹25.33&ndash;26.86 Cr</strong> once an internal team line is added. Book cost of sale and capex separately'],
 (['<strong>2</strong>','<strong>Validate with ₹25 lakh</strong> &mdash; about 1% of the envelope &mdash; with the kill condition agreed in advance'],'hl'),
 ['<strong>3</strong>','<strong>Measure CPL, CPQL and cost per qualified site visit.</strong> Not cost per booking &mdash; the sample cannot support it'],
 ['<strong>4</strong>','<strong>Validate audience, proposition and channel fit</strong> across four community audiences and three creative territories'],
 ['<strong>5</strong>','<strong>Release budget in tranches</strong> &mdash; six of them, each against a KPI gate with a named decision-maker'],
 ['<strong>6</strong>','<strong>Scale only when the gates are achieved.</strong> A missed gate cuts inventory before it raises budget'],
 ['<strong>7</strong>','<strong>Keep the reserve under finance control</strong> &mdash; ₹1.90 Cr, released on a named event only'],
 ['<strong>8</strong>','<strong>Reallocate continuously on marginal return</strong>, comparing within a funnel layer and never across'],
]))
w('</div>\n<div>')
w(figs([
 ('₹25','lakh · released now','<b>The ask.</b> 1.0% of the marketing opex envelope, 0.8% of the ₹31.75 Cr headline','key'),
 ('₹23.80','crore · planning envelope','<b>Not a commitment.</b> A ceiling under governance, released in six gated tranches','ev'),
]))
w(co('What I would ask you to judge',
 ['Not whether the numbers are right &mdash; <strong>most of them are labelled assumptions and I have said so on every slide.</strong>',
  '<strong>Whether the framework protects the capital.</strong> If a quarter goes badly, you would know within weeks rather than at year end, and the response is written down before the money moves.']))
w(co('And what this deck does not claim',
 ['<strong>No estimate of KMV&rsquo;s actual marketing budget, spend, headcount, historical CPL, sales velocity or inventory position</strong> appears anywhere. None was available.',
  '<strong>No industry benchmark has been manufactured.</strong> Where a published rate exists it is cited; where none exists, a range is labelled as an assumption.',
  '<strong>The revenue base itself is unproven.</strong> A 50% premium to the locality asking average sits underneath every figure here. If it does not hold, this entire strategy re-bases.'],'ev'))
w('</div>\n</div>')
w(strip([('Status','<b>A recommendation prepared for discussion.</b> Nothing here has been confirmed by KMV Spaces'),
         ('Next step','Fifteen questions for management &mdash; Appendix A. Several are free and settle more than any test'),
         ('Prepared by','Kiran Basa · submitted to Mr. Anudeep')]))

# ═══════════════ CLOSING BAND ═══════════════
w('''
<section class="slide band" id="close">
  <div class="sbody">
    <p class="seyebrow">In closing</p>
    <h1 class="stitle">Marketing investment should be earned by performance, not committed by forecast.</h1>
    <p class="sdek">This strategy is intentionally designed as a <strong>decision framework, not a fixed media plan.</strong> The objective is to validate the market, earn the right to scale, and connect every additional rupee of marketing investment to a measurable commercial outcome.</p>
    <div class="cmeta" style="border-top-color:rgba(245,245,241,.22);margin-top:1.6rem">
      <div><span class="ck" style="color:rgba(245,245,241,.5)">Prepared by</span><b style="color:var(--band-ink)">Kiran Basa</b></div>
      <div><span class="ck" style="color:rgba(245,245,241,.5)">Assignment</span><span style="color:rgba(245,245,241,.8)">Marketing Strategy &mdash; KMV Spaces, Amaravati / Mangalagiri</span></div>
      <div><span class="ck" style="color:rgba(245,245,241,.5)">Submitted to</span><b style="color:var(--band-ink)">Mr. Anudeep</b></div>
    </div>
  </div>
</section>''')

open('/tmp/claude-0/-home-user/a5dd8d44-0929-5495-aca9-31c380eaeac4/scratchpad/deck_e.html','w',encoding='utf-8').write('\n'.join(P)+'\n')
print('part E written; last slide =', dk_lib._N[0])
