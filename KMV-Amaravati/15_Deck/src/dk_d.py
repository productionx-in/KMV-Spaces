# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/claude-0/-home-user/a5dd8d44-0929-5495-aca9-31c380eaeac4/scratchpad')
from dk_lib import *
import dk_lib
dk_lib._N[0] = 14
P=[]; w=P.append

# ═══════════════ 15 KPI FRAMEWORK ═══════════════
o,_ = slide('s15','KPI framework','Leading indicators release money. Lagging indicators confirm it was right',
  'Every metric below names the decision it triggers. <strong>A metric that cannot change a decision is not on this dashboard</strong> &mdash; which is why impressions, reach, followers and page views appear nowhere.')
P.extend(o)
w('<div class="gsplit">\n<div>')
w('<h3 class="sh" style="margin-top:0;color:var(--decision)">Leading &mdash; read weekly, and these release the next tranche</h3>')
w(table(['Metric','Formula','#Target','Triggers'],[
 (['<strong>CPQL</strong>','Media &divide; qualified leads','<strong>₹7,889</strong><br><i>max ₹10,576</i>','<strong>Campaign optimisation; tranche release</strong>'],'hl'),
 (['<strong>Cost per qualified site visit</strong>','Media &divide; visits held','<strong>₹33,676</strong><br><i>max ₹45,144</i>','<strong>The Phase 0 decision metric</strong>'],'hl'),
 (['<strong>Site-visit-to-booking</strong>','Bookings &divide; visits held','<strong>≥ 6.9%</strong>','<strong>The single most important number</strong>'],'hl'),
 ['CPL','Media &divide; leads','₹1,247<br><i>max ₹1,672</i>','Channel reallocation'],
 ['MQL rate · lead-to-visit','Stage &divide; prior stage','45% · 23.4%','Qualification criteria'],
 ['Site-visit velocity','Visits held per week','≥ 15','Capacity and staffing'],
 ['Show rate','Held &divide; booked','≥ 60%','Confirmation process'],
 ['Follow-up latency','Hours from visit to contact','&lt; 24h','Coaching'],
 ['CTR · CPC · hook rate','Platform','≥1.2% · &mdash; · ≥25%','Creative refresh'],
 ['Creative fatigue','CPL drift vs 30-day baseline','&lt; 20%','<strong>Automatic refresh</strong>'],
]))
w('</div>\n<div>')
w('<h3 class="sh" style="margin-top:0;color:var(--evidence)">Lagging &mdash; read monthly or quarterly; these confirm, they do not steer</h3>')
w(table(['Metric','Formula','#Target','Owner'],[
 (['<strong>CAC</strong>','Total acquisition &divide; net units','<strong>₹8.44 L</strong><br><i>max ₹11.32 L</i>','CFO'],'hl2'),
 (['<strong>ROMI</strong>','<strong>(Gross profit &minus; marketing) &divide; marketing</strong>','<strong>≥ 3.0&times;</strong>','CFO'],'hl2'),
 ['Cost per booking','Media &divide; bookings','₹4.90 L','Marketing lead'],
 ['Revenue recognised','Net units &times; achieved ticket','₹506.7 Cr','CFO'],
 ['Gross profit','Revenue &times; margin','₹141.9 Cr <i>@28%</i>','CFO'],
 ['Marketing as % of GDV','Opex &divide; GDV','4.70%','CFO'],
 ['Achieved price vs list','Achieved &divide; list, by community','≥ 95%','CEO'],
 ['Cancellation rate','Cancelled &divide; gross bookings','≤ 8%','Sales'],
 ['Referral rate','Referrals per owner-year','≥ 0.15','Marketing lead'],
 (['<strong>ROAS</strong> <i>(media only)</i>','Revenue &divide; media','<strong>Diagnostic only</strong>','<strong>Never a decision metric</strong>'],'dim'),
]))
w(co('Which metrics gate the money',
 ['<strong>Only the leading column releases a tranche.</strong> By the time CAC and ROMI are readable, the money is spent. <strong>Phase 0 and Phase 2 gates are set on CPL, CPQL and cost per qualified site visit</strong>, because those are the numbers a quarter can actually produce.']))
w('</div>\n</div>')
w(strip([('Basis','<b>Derived.</b> Targets are calculated from the modelled funnel; ceilings from a 30%-of-gross-profit policy'),
         ('Requires validation','Historical CPL, CAC and cancellation rate &mdash; each would replace a target with an observation'),
         ('Rule','Compare within a layer, never across')]))

# ═══════════════ 16 ₹25L TEST ═══════════════
o,_ = slide('s16','The ₹25 lakh validation test','A validation tranche &mdash; not a small version of the campaign',
  'Eight weeks: two setup, six live. <strong>The distinction matters: a miniature campaign is judged on results; a validation tranche is judged on what it settles.</strong>')
P.extend(o)
w('<div class="gsplit">\n<div>')
w(table(['','#Amount','Channel / item','What it answers'],[
 (['<strong>Media</strong>','<strong>₹18.00 L</strong>','',''],'tot'),
 ['','₹6.30 L','<strong>Meta</strong> &mdash; 6 variants','Volume audiences; <strong>establishes the CPL floor</strong>'],
 ['','₹5.40 L','<strong>Google Search</strong> &mdash; 3 ad groups','Intent capture; <strong>tests branded defence</strong>'],
 ['','₹3.60 L','<strong>LinkedIn</strong> &mdash; S3 diaspora','The most expensive audience &mdash; <strong>is it viable at all?</strong>'],
 ['','₹1.80 L','One portal','Rented vs owned demand'],
 ['','₹0.90 L','YouTube retargeting','Cheapest re-engagement'],
 (['<strong>Non-media</strong>','<strong>₹7.00 L</strong>','',''],'tot'),
 ['','₹2.50 L','Landing pages, 2 per audience','<strong>Gated vs ungated price sheet</strong>'],
 ['','₹2.20 L','12 creative variants','Price / proof / density territory'],
 ['','₹1.50 L','Tracking + CRM setup','<strong>Without this the test measures nothing</strong>'],
 ['','₹0.80 L','Analyst time','Weekly readout'],
]))
w('</div>\n<div>')
w('<h3 class="sh" style="margin-top:0">What the sample can and cannot support</h3>')
w(table(['Metric','#Events','#95% CI','Verdict'],[
 (['<strong>CPL</strong>','1,443','<strong>±5.2%</strong>','<strong>Measurable</strong>'],'hl2'),
 (['<strong>Lead &rarr; qualified</strong>','1,443','<strong>±12.3%</strong>','<strong>Measurable</strong>'],'hl2'),
 (['<strong>CPQL</strong>','228','<strong>±13.0%</strong>','<strong>Measurable</strong>'],'hl2'),
 ['Qualified &rarr; visit','228','±30.9%','Directional'],
 ['Cost per qualified site visit','53','±26.8%','Directional'],
 (['<strong>Cost per booking</strong>','<strong>3.7</strong>','<strong>±102%</strong>','<strong>NOT MEASURABLE</strong>'],'hl'),
]))
w(co('The measurement decision I would state in advance',
 ['<strong>A ₹25 lakh test cannot establish a booking rate.</strong> Measuring site-visit-to-booking to ±25% would need <strong>~832 held site visits &mdash; roughly 22 months of continuous spend.</strong>',
  '<strong>So the test is judged on cost per qualified site visit.</strong> Booking rate is carried as a stated assumption and monitored as a secondary indicator across the first two quarters of live trading.',
  '<strong>Saying that now is the difference between a measurement exercise and a soft launch that quietly becomes the launch.</strong>']))
w('</div>\n</div>')
w('<h3 class="sh">Kill and scale criteria &mdash; agreed before the money moves, not after the result</h3>')
w('<div class="gate">')
for nm,val,desc,cls in [
  ('Scale','CPL ≤ ₹1,550','and CPQSV ≤ ₹42,000 &rarr; <strong>release Phase 1 in full</strong>','now'),
  ('Partial','CPL ₹1,550&ndash;1,900','&rarr; release Phase 1 at <strong>70%</strong>; re-test the two weakest audiences',''),
  ('Kill','CPL &gt; ₹1,900','&rarr; <strong>stop and re-base.</strong> Do not proceed at reduced scale',''),
  ('Kill','CPQSV &gt; ₹52,000','&rarr; <strong>stop.</strong> The funnel is broken, not the media',''),
  ('Cut','Audience &gt; 2&times; best','&rarr; remove that audience from the launch plan',''),
  ('Adopt','Ungated ≥ gated','&rarr; <strong>publish pricing ungated.</strong> The position is validated commercially','')]:
    w('  <div class="gt %s"><span class="gn">%s</span><span class="gv">%s</span><span class="gd">%s</span></div>' % (cls,nm,val,desc))
w('</div>')
w(strip([('Basis','<b>Derived.</b> Volumes from the modelled funnel; confidence intervals calculated on those volumes'),
         ('Method','Poisson relative CI for counts; normal approximation for proportions'),
         ('Ask','<b>₹25 lakh &mdash; approximately 1% of the envelope, released against a written stop condition</b>')]))

# ═══════════════ 17 INVESTMENT ARCHITECTURE ═══════════════
o,_ = slide('s17','Marketing investment architecture','₹31.75 crore is not a marketing budget &mdash; it is four kinds of money under one label',
  'This is the single most important correction in the deck. <strong>Presented as one number it reads reckless; separated properly it is an ordinary regional budget with two capital items attached.</strong>')
P.extend(o)
w('<div class="gsplit">\n<div>')
w(table(['Category','#Amount','#Share','What it actually is, and whose P&amp;L it belongs in'],[
 (['<strong>Total commercial budget</strong>','<strong>₹31.75 Cr</strong>','100%','<strong>The planning ceiling &mdash; not the ask</strong>'],'tot'),
 (['<strong>True marketing OPEX</strong>','<strong>₹23.80 Cr</strong>','75.0%','<strong>The only line a marketing lead should be accountable for</strong> &nbsp;<i>&rarr; marketing</i>'],'hl'),
 ['&nbsp;&nbsp;&mdash; of which <strong>media</strong>','<strong>₹14.65 Cr</strong>','46.1%','<strong>62% of opex · ₹32.6 lakh a month</strong> across 45 months &nbsp;<i>&rarr; marketing</i>'],
 ['&nbsp;&nbsp;&mdash; of which agency, content, tech, research','₹9.15 Cr','28.8%','People, production, platforms, validation &nbsp;<i>&rarr; marketing</i>'],
 ['<strong>Cost of sale</strong>','₹4.04 Cr','12.7%','Channel-partner commission and referral &mdash; <strong>paid only on performance</strong> &nbsp;<i>&rarr; sales</i>'],
 ['<strong>Sales infrastructure capex</strong>','₹3.15 Cr','9.9%','<strong>A building.</strong> An asset, amortised &nbsp;<i>&rarr; capex</i>'],
 ['<strong>Technology capex</strong>','₹0.76 Cr','2.4%','<strong>A system.</strong> An asset, amortised &nbsp;<i>&rarr; capex</i>'],
 (['<strong>Contingency reserve</strong> <i>(inside opex)</i>','₹1.90 Cr','8.0% of opex','<strong>Finance-held, not marketing-held.</strong> Released on a named event only &nbsp;<i>&rarr; finance</i>'],'hl2'),
]))
w('<p class="tnote">₹23.80 + ₹4.04 + ₹3.15 + ₹0.76 = ₹31.75 Cr. The reserve sits inside the ₹23.80 Cr opex, alongside a ₹21.90 Cr deployable core.</p>')
w('</div>\n<div>')
w(figs([
 ('₹6.33','lakh · per unit','<b>Marketing opex per unit</b> once reclassified','ev'),
 ('₹8.44','lakh · per unit','<b>All-in acquisition cost (CAC)</b>, every category included','key'),
]))
w(co('The convergence that tells me the reclassification is right',
 ['Two corrections arrived at independently land on the same number. <strong>Stripping cost of sale and capex out gives ₹6.33 lakh per unit. The allowable ceiling the analysis had set for itself was ₹6.30 lakh.</strong> A 0.5% difference.',
  'Put the other way: <strong>the overshoot against the allowable is ₹8.06 crore, and the misclassified money is ₹7.95 crore. They are the same ₹8 crore.</strong>'],'calc'))
w(co('And the correction that raises the number, which I would rather bring than have found',
 ['<strong>The model carries agency fees and no internal marketing headcount.</strong> I have not invented KMV&rsquo;s team size &mdash; no such information was available. But the line cannot be zero.',
  '<strong>Adding a labelled range for two people over the window takes the envelope up, not down: ₹25.33&ndash;26.86 Cr of marketing opex</strong>, ₹33.28&ndash;34.81 Cr all-in, CAC ₹8.85&ndash;9.26 L. <strong>Both ends stay inside a 30%-of-gross-profit ceiling.</strong>']))
w('</div>\n</div>')
w(strip([('Basis','<b>Derived calculation on stated assumptions.</b> Reclassification is mine; no vendor quote underlies any line'),
         ('Not a KMV figure','<b>No estimate is offered anywhere for KMV&rsquo;s actual budget, spend, headcount or historical CPL</b> &mdash; none was available'),
         ('Requires validation','Internal team structure, agency contracts, and whether the sales office is capex or leased')]))

# ═══════════════ 18 GOVERNANCE ═══════════════
o,_ = slide('s18','Budget governance','The envelope is a planning ceiling. Only ₹25 lakh is an ask',
  'I would not release ₹23.80 crore against a forecast. <strong>I would release it in six tranches, each against a KPI gate, a named decision-maker and a written stop condition.</strong>')
P.extend(o)
w('<div class="gsplit">\n<div>')
TR=[('Phase 0 · Validation','2 months','₹0.25 Cr','1.0%',25,'now'),
    ('Phase 1 · Launch prep','months 3&ndash;6','₹2.60 Cr','10.9%',260,''),
    ('Phase 2 · Market entry','months 7&ndash;15','₹4.20 Cr','17.6%',420,''),
    ('Phase 3 · Scale','months 16&ndash;30','₹8.10 Cr','34.0%',810,''),
    ('Phase 4 · Optimise','months 31&ndash;42','₹5.05 Cr','21.2%',505,''),
    ('Phase 5 · Clearance','months 43&ndash;51','₹1.70 Cr','7.1%',170,''),
    ('Contingency reserve','CFO-held','₹1.90 Cr','8.0%',190,'res')]
for nm,win,amt,pc,v,cls in TR:
    w('<div class="tr"><span class="tr-k"><b>%s</b>%s</span><span class="tr-t"><span class="tr-f %s" style="width:%.1f%%"></span></span><span class="tr-v">%s <i>· %s</i></span></div>'
      % (nm,win,cls,v/810.0*92.0,amt,pc))
w('<p class="tnote">Deployable core ₹21.90 Cr (92.0%) + reserve ₹1.90 Cr (8.0%) = <strong>₹23.80 Cr marketing opex</strong>. Before the internal-team line on slide 17.</p>')
w('</div>\n<div>')
w(figs([('1.0','% of opex','<b>What I am actually asking for today</b> &mdash; ₹25 lakh, and 0.8% of the ₹31.75 Cr headline','key')]))
w(cards([
 ('Three rules across every tranche',
  ul(['<strong>A saving is never banked.</strong> Underspend moves to the highest-leverage stage &mdash; the site visit',
      '<strong>A missed gate cuts inventory before it cuts price, and cuts inventory before it raises budget</strong>',
      '<strong>A gate missed twice consecutively releases nothing</strong>, regardless of explanation']),'warn'),
 ('Why this is strategically safer than approving the total',
  ul(['<strong>The largest risk is not overspending &mdash; it is spending correctly against a wrong price assumption.</strong> A tranche structure detects that in weeks, not at year end',
      'Only <strong>₹14.65 Cr is genuinely variable.</strong> Outdoor, print, retainers and CRM are fixed or contracted once committed &mdash; <strong>so a mid-flight 30% cut lands almost entirely on the one line that generates leads</strong>',
      'Which is an argument for committing to outdoor and print <em>later</em> &mdash; not for cutting media <em>first</em>']),'ev'),
], 'g2'))
w('</div>\n</div>')
w(strip([('Basis','<b>Derived.</b> Tranche sizes, windows and gates are my recommendation'),
         ('Governance','Phase 0 and 4&ndash;5 at marketing level with CFO notified; Phases 1&ndash;3 require CEO + CFO'),
         ('Status','<b>A controlled investment framework, not a commitment</b>')]))

# ═══════════════ 19 MEASUREMENT & ATTRIBUTION ═══════════════
o,_ = slide('s19','Measurement &amp; attribution','Three reading rules, in the reporting template before the first review',
  'Attribution arguments are always won by whoever wrote the template. <strong>I would write it before the spend, not when the spend is challenged.</strong>')
P.extend(o)
w('<div class="g3">')
w(cards([
 ('Rule 1 · Compare within a layer, never across',
  '<p>Judging brand against performance on cost per booking <strong>defunds ₹10.25 crore of the highest-value spend.</strong> It is the most common way a sound budget is destroyed by a reasonable-sounding question.</p>','warn'),
 ('Rule 2 · Judge demand generation on CPQL',
  '<p>Not CPL. <strong>Cheap leads that fail the cash gate are a cost, not a result.</strong> Reporting CPL as the headline optimises the media buy against the business.</p>','warn'),
 ('Rule 3 · Judge brand, outdoor and the site on holdouts',
  '<p><strong>First-touch and geo holdouts &mdash; never last click.</strong> Last click will always find in favour of the search line and against everything that made the search happen.</p>','warn'),
], 'g3'))
w('</div>')
w('<div class="gsplit" style="margin-top:1rem">\n<div>')
w('<h3 class="sh" style="margin-top:0">The attribution model I would install</h3>')
w(table(['Layer','Attribution method','Why'],[
 ['<strong>Performance media</strong>','<strong>First-touch, mandatory CRM picklist</strong>','The check on ₹9.84 Cr of allocation. Values must reconcile to the budget lines'],
 ['<strong>Brand, outdoor, OTT, print</strong>','<strong>Geo or time-based holdout, agreed in advance</strong>','Cannot be defended under click reporting and will be the first line cut in a bad quarter'],
 ['<strong>Referral and channel partner</strong>','Source field at booking + discount register','Referral is the cheapest revenue in the model; it must not be mis-credited to media'],
 ['<strong>Site and experience centre</strong>','Visit debrief, by consultant','The ₹39.4 Cr-per-point stage. Unmeasured from day one, it stays unmeasured'],
]))
w('</div>\n<div>')
w(co('What I would report, and what I would refuse to report',
 ['<strong>Report revenue at risk, not spend efficiency.</strong> &ldquo;CPL improved 12%&rdquo; is not a result. <strong>&ldquo;Site-visit conversion moved 0.4 points, worth ₹15.8 crore&rdquo;</strong> is.',
  '<strong>Deliberately absent from every report: impressions, reach, followers, page views.</strong> None of them can change a decision, and each of them can be used to defend a bad quarter.'],'calc'))
w(co('And the honest caveat on ROI',
 ['<strong>Revenue &divide; spend would read 16.0&times;.</strong> It is meaningless &mdash; most of that revenue pays for land, construction and finance. <strong>Any development deck showing 16&times; should be disbelieved, including this one.</strong>',
  '<strong>ROMI here is (gross profit &minus; marketing) &divide; marketing: 3.47&times; at an assumed 28% margin</strong> &mdash; <strong>2.99&times; at 25% and 3.95&times; at 31%.</strong> The margin is a placeholder, because no construction cost data exists anywhere behind this work, <strong>so the ROMI figure moves 32% across a range nobody has tested.</strong>']))
w('</div>\n</div>')
w(strip([('Basis','<b>Recommended.</b> The ₹10.25 Cr and ₹39.4 Cr figures are derived from the modelled funnel'),
         ('Requires validation','A 28% gross margin &mdash; <b>the single largest unvalidated input in the entire model</b>'),
         ('Rule','Attribution method is agreed before the spend, never after the challenge')]))

open('/tmp/claude-0/-home-user/a5dd8d44-0929-5495-aca9-31c380eaeac4/scratchpad/deck_d.html','w',encoding='utf-8').write('\n'.join(P)+'\n')
print('part D written; last slide =', dk_lib._N[0])
