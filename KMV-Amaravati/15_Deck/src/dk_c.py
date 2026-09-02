# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/claude-0/-home-user/a5dd8d44-0929-5495-aca9-31c380eaeac4/scratchpad')
from dk_lib import *
import dk_lib
dk_lib._N[0] = 9
P=[]; w=P.append

w(band('Part two','The plan I would run','From here on the labels change. Almost everything is derived or assumed &mdash; and it is marked that way on every slide.'))

# ═══════════════ 10 GO-TO-MARKET ═══════════════
o,_ = slide('s10','Go-to-market strategy','Six phases across 45 months &mdash; each one a gate, not a date',
  'The sell window is a <strong>working assumption</strong> derived from 376 units at a modelled velocity. <strong>Every phase releases capital only when the previous phase&rsquo;s KPI gate is met.</strong>')
P.extend(o)
w(table(['Phase','Window','Objective','Primary channels','Gate to unlock the next release','Decides'],[
 (['<strong>0 · Intelligence &amp; validation</strong>','Months 1&ndash;2','<strong>Discover the economics. Not to generate sales</strong>','Meta · Google Search · one portal · YouTube. <strong>Nothing else</strong>','CPL ≤ <strong>₹1,550</strong> · cost per qualified site visit ≤ <strong>₹42,000</strong>','Marketing lead sign-off; CFO notified'],'hl'),
 ['<strong>1 · Launch preparation</strong>','Months 3&ndash;6','Build what the funnel cannot work without','<strong>Not a media phase.</strong> CRM, tracking, website, first show home, sales training','CRM live · first-touch attribution mandatory · WhatsApp API integrated · all figures reconciled. <strong>All four, binary</strong>','CEO + CFO'],
 ['<strong>2 · Controlled market entry</strong>','Months 7&ndash;15','Prove the funnel converts at viable cost, at real scale','Digital performance. Outdoor capped at <strong>2 boards.</strong> No large event','≥ <strong>55 bookings</strong> · CPL within +25% of Phase 0 · show rate ≥ 60%','CEO + CFO'],
 ['<strong>3 · Scale</strong>','Months 16&ndash;30','Scale what proved, on validated economics','Full mix. <strong>Outdoor and print unlock only now</strong>','Site-visit-to-booking ≥ <strong>5.5%</strong> over two quarters · CAC ≤ ₹9.5 L','CEO + CFO, quarterly'],
 ['<strong>4 · Optimisation</strong>','Months 31&ndash;42','Shift the mix from paid to earned as referral compounds','Referral, owner community, channel partners; paid declining','Referral ≥ <strong>0.15 per owner-year</strong> · CAC falling quarter on quarter','Marketing lead; CFO notified'],
 ['<strong>5 · Inventory clearance</strong>','Months 43&ndash;51','Final demand capture on residual inventory','Retargeting, channel partners, owner referral','Inventory &lt; 15% · referral ≥ 25% of bookings','Marketing lead'],
]))
w('<div class="g3">')
w(co('If Phase 0 fails',
 ['<strong>Stop. Re-base the model before any launch commitment.</strong> I would not proceed at reduced scale on a failed cost per lead &mdash; <strong>a bad unit economic does not improve with volume.</strong>']))
w(co('If a later gate fails',
 ['<strong>Cut inventory release before raising budget.</strong> A community missing its gate has its release reduced, not its spend increased.']))
w(co('If a gate fails twice',
 ['<strong>Nothing releases</strong>, regardless of explanation. Agreed now, because it will not be agreeable later.']))
w('</div>')
w(strip([('Basis','<b>Derived.</b> Phase windows, gates and thresholds are my proposal on a modelled 45-month sell window'),
         ('Requires validation','Construction and handover milestones, approvals status, and the launch date'),
         ('Rule','Capital is released against evidence, not calendar')]))

# ═══════════════ 11 FUNNEL ═══════════════
o,_ = slide('s11','The marketing funnel','Eleven stages &mdash; and the two that were missing from my own first model',
  'Raw leads are not success. <strong>66,406 leads are lost at the top of this funnel and they are the least valuable losses in it.</strong>')
P.extend(o)
w('<div class="gsplit">\n<div>')
FN = [('Reach','<i>unique individuals</i>','6,573,000',100,None,'pale'),
      ('Engagement &amp; leads','','78,880',58,'1.20%',''),
      ('MQL','<i>contactable + intent</i>','35,496',43,'45.0%',''),
      ('SQL','<i>sales-accepted</i>','19,523',34,'55.0%',''),
      ('Qualified lead','<i>cash gate verified</i>','12,474',27,'63.9%',''),
      ('Site visit booked','','4,870',22,'39.0%',''),
      ('Qualified site visit','<i>held &amp; debriefed</i>','2,922',17,'60.0%',''),
      ('Negotiation','','574',10,'19.6%',''),
      ('Booking &mdash; all sources','<i>gross</i>','409',8,'&mdash;','warm'),
      ('Sale <i>(agreement)</i>','<i>net of 8% cancellation</i>','376',7,'92.0%','warm'),
      ('Referral','<i>per owner-year</i>','0.15',4,'&mdash;','pale')]
w('<div class="fn-l">')
for nm,sub,val,wd,rate,cls in FN:
    w('  <div class="fn-r"><span class="fn-k"><b>%s</b>%s</span><span class="fn-b %s" style="width:%d%%">%s</span><span class="fn-c">%s</span></div>'
      % (nm,sub,cls,wd,val,('<b>%s</b>'%rate) if rate and rate!='&mdash;' else (rate or '')))
w('</div>')
w('<p class="tnote">A 60% show rate converts 4,870 booked visits into <strong>2,922 held and debriefed</strong> &mdash; 23.4% of qualified leads, and 15.0 held visits a week across the modelled window. Bookings are shown gross of cancellation; 409 gross nets 376. Every rate is a working assumption.</p>')
w('</div>\n<div>')
w(co('Why I would judge the plan on CPQL, not CPL',
 ['<strong>Cheap leads that fail the cash gate are a cost, not a result.</strong> CPL is a buying metric; CPQL is a business metric.',
  'At the modelled rates, media buys a lead for <strong>₹1,247</strong> and a qualified lead for <strong>₹7,889</strong>. <strong>A campaign optimised to CPL will find the cheapest audience, which is the one that cannot clear ₹17.6 lakh in cash.</strong>'],'calc'))
w(co('And why the qualified site visit is the metric that matters most',
 ['The conversion rates are <strong>multiplicative</strong>, so a 25% move in any of them changes bookings by the same 25%. What separates them is <strong>cost to fix and who controls them.</strong>',
  '<strong>Cost per lead is set by the auction and by competitors.</strong> Lead-to-qualified and qualified-to-visit are process, and cost almost nothing to move. And the last one is the largest opportunity:'],'calc'))
w(figs([('₹39.4','crore per point','<b>One point of site-visit-to-booking</b> &mdash; 6.9% to 7.9% &mdash; at zero additional media','key')]))
w('</div>\n</div>')
w(strip([('Basis','<b>Derived calculation on stated assumptions.</b> Every conversion rate is a working assumption'),
         ('Not evidenced','Reach is an <i>output</i> of the lead rate, not an input &mdash; the weakest number in the model'),
         ('Requires validation','24 months of historical lead, source and cost data')]))

# ═══════════════ 12 CHANNELS ═══════════════
o,_ = slide('s12','Channel strategy','Twenty-two channels evaluated; five cut, three capped',
  'I would not recommend every channel equally. <strong>Each one earns a role, a funnel stage, a KPI and a stop condition &mdash; or it does not run.</strong>')
P.extend(o)
w(table(['Tier','Channel','Role','Funnel stage','KPI','Scale when','Stop when'],[
 (['<strong>1</strong>','<strong>Site / experiential</strong>','The product, not collateral','Visit &rarr; booking','Visit-to-booking','<strong>Always &mdash; ₹39.4 Cr per point</strong>','Never; fix it instead'],'hl2'),
 (['<strong>1</strong>','<strong>Referral</strong>','The compounding asset','Advocacy','Referral per owner-year','Once owners exist','Never'],'hl2'),
 (['<strong>1</strong>','<strong>Channel partners</strong>','28% of bookings, paid on performance','Lead &rarr; booking','CP bookings; discount discipline','Discount ≤ direct +1.0 pt','Discount discipline breaks'],'hl2'),
 (['<strong>1</strong>','<strong>WhatsApp</strong>','Primary channel for three segments','Nurture &rarr; visit','Response latency','Day one','Never &mdash; but useless un-integrated'],'hl2'),
 ['2','<strong>Meta</strong>','Volume engine for A and B; affinity reach for S3, S7','Reach &rarr; lead','CPQL','CPQL ≤ ₹7,889','CPQL &gt; ₹10,576'],
 ['2','<strong>Google Search</strong>','Intent capture &mdash; the highest-quality lead','Lead &rarr; qualified','CPQL, branded share','Branded share &lt; 90%','&mdash;'],
 ['2','Website + landing pages','The verification surface','Lead','LP conversion ≥ 6%','Day one','&mdash;'],
 ['2','Outdoor','Local legitimacy at 25-acre scale','Reach','Recall, geo holdout','<strong>Phase 3 only</strong>','Cannot be held out'],
 ['3','YouTube · SEO · Print · PR · Email','One specific job each, for one or two segments','Various','Assisted conversions','&mdash;','&mdash;'],
 (['<strong>4</strong>','<strong>Property portals</strong>','<strong>Presence is mandatory; lead volume is not</strong>','Lead','CPQL','<strong>Capped ₹1.00 Cr</strong>','&mdash;'],'hl'),
 (['<strong>4</strong>','<strong>LinkedIn</strong>','S3 and S7 precisely, and nobody else','Reach','CPQL','<strong>Capped ₹0.50 Cr</strong>','&mdash;'],'hl'),
 (['<strong>5</strong>','<strong>Google Display prospecting</strong>','<strong>Cut.</strong> Inflates lead count, depresses lead-to-qualified','&mdash;','&mdash;','<strong>Retargeting only, ₹0.30 Cr</strong>','&mdash;'],'hl'),
 (['<strong>5</strong>','<strong>Influencers · off-site lead events · broad email acquisition</strong>','<strong>Cut or deferred.</strong> Unmeasurable before attribution exists','&mdash;','&mdash;','<strong>Phase 3, tracked links only</strong>','&mdash;'],'hl'),
]))
w(co('The correction verification forced on my own channel plan',
 ['Portals are the corridor&rsquo;s dominant organic surface <strong>and they are rented.</strong> Capping portal spend only works <strong>if owned branded search is defended at the same time</strong> &mdash; otherwise capping the rented channel while leaving the owned one intercepted loses both.'],'ev'))
w(strip([('Sources','Channel roles derived; portal dominance observed via '+sid_('S11','S12','S13')),
         ('Basis','<b>Derived.</b> Caps and thresholds are my recommendation'),
         ('Rule','Compare channels within a funnel layer, never across &mdash; see slide 19')]))

# ═══════════════ 13 CREATIVE ═══════════════
o,_ = slide('s13','Creative as a growth system','Creative is the only lever that improves every downstream metric at once',
  'It is not decoration and it is not a taste argument. <strong>It is the one input that raises hook rate, lead quality, visit rate and close rate without buying more media.</strong>')
P.extend(o)
w('<div class="gsplit">\n<div>')
w(table(['Link in the chain','What creative does','Metric','#Target'],[
 ['<strong>Attention</strong>','Stops the scroll','Hook rate <i>(3-sec / impression)</i>','≥ 25%'],
 ['','','CTR','≥ 1.2%'],
 ['<strong>Qualified demand</strong>','Attracts the right person, <strong>repels the wrong one</strong>','Landing-page conversion','≥ 6%'],
 (['','','<strong>CPQL by variant</strong>','<strong>≤ ₹7,889</strong>'],'hl2'),
 ['<strong>Trust</strong>','Makes the claim checkable','Lead quality &mdash; % passing the cash gate','≥ 45%'],
 (['<strong>Site visit</strong>','Converts interest into travel','<strong>Qualified-to-visit by creative</strong>','<strong>≥ 23%</strong>'],'hl2'),
 ['<strong>Conversion</strong>','Arms the sales conversation','Booking by first-touch creative','Tracked'],
]))
w('</div>\n<div>')
w(cards([
 ('Creative pillars &mdash; three territories, tested not chosen',
  '<p><strong>Price-led</strong> &mdash; the ungated sheet. <strong>Proof-led</strong> &mdash; carpet area, handover dates, progress. <strong>Density-led</strong> &mdash; the arithmetic. <strong>Twelve variants, three per audience, in Phase 0. The market decides which territory is right, not the room.</strong></p>','ev'),
 ('The discipline that makes it commercial',
  '<p>A variant is judged on <strong>cost per qualified site visit</strong>, never on whether it is liked. <strong>A variant above 2&times; the best variant&rsquo;s CPQL is cut, regardless of who made it.</strong> Fatigue is a trigger, not an opinion: frequency ceiling plus CPL drift &gt;20% forces an automatic refresh.</p>','warn'),
], 'g2'))
w(co('Where I would spend creative effort first',
 ['<strong>The landing page and the price sheet</strong>, because the boldest decision in the strategy is cheap to test: <strong>gated versus ungated pricing</strong>, two pages per audience, ₹2.5 lakh. If ungated wins on CPQL, the transparency position is validated commercially rather than argued.'],'calc'))
w(co('One thing I would fix before any of it runs',
 ['The campaign&rsquo;s signature claim &mdash; <strong>fifteen to the acre</strong> &mdash; is <strong>false against two named villa competitors</strong> unless bounded to all 25 acres, apartments included <span class="sid">[S13]</span>. And the two density comparators I would cite <strong>have no published unit count.</strong>',
  '<strong>I would bound the claim and write the footnote before the first impression, not after the first challenge.</strong>']))
w('</div>\n</div>')
w(strip([('Sources', sid_('S13')+' &mdash; the competitor density evidence that bounds the claim'),
         ('Basis','<b>Derived.</b> Targets are my proposal; the variant test is designed to replace them with observed values'),
         ('Note','Creative supports the strategy here. It is not the strategy')]))

# ═══════════════ 14 CRM ═══════════════
o,_ = slide('s14','Lead qualification, CRM and the sales handover','I would qualify on cash at purchase, and build the measurement before the media',
  'Five of the six metrics I would read weekly <strong>require CRM discipline that does not exist yet.</strong> That makes the measurement system a pre-launch dependency, not a reporting task.')
P.extend(o)
w('<div class="g2">')
w(cards([
 ('The qualification gate',
  '<p><strong>Cash at purchase, not income.</strong> ₹17.6 L for A rising to ₹74.1 L for D. Two households on identical incomes clear it differently.</p>'
  +ul(['<strong>Three required fields at capture:</strong> budget band, timeline, and <strong>country / origin district</strong>',
       'Criteria <strong>written down and owned by a named person</strong> &mdash; today neither exists',
       'Origin district is free to collect and re-cuts the entire NRI budget at quarter two']),'ev'),
 ('Non-negotiable on day one',
  ul(['<strong>WhatsApp Business API integrated.</strong> Un-integrated it is a liability, not a channel &mdash; conversation history cannot be reconstructed',
      '<strong>First-touch attribution as a mandatory picklist</strong>, with values that reconcile to the budget lines',
      '<strong>A named CRM owner.</strong> The CRM owns the lead-to-qualified rate, worth ₹17.2 Cr per point',
      '<strong>A structured visit debrief</strong> with a closed objection taxonomy &mdash; not a free-text box']),'warn'),
], 'g2'))
w('</div>')
w('<h3 class="sh">Where marketing ends and sales begins &mdash; and the one number that spans both</h3>')
w('<div class="chain">'
  + ''.join('<div class="ch mk">%s</div>' % s for s in ['Reach','Lead','MQL','SQL','Qualified lead','Visit booked'])
  + '<div class="ch sa">Visit held</div>'
  + ''.join('<div class="ch sa">%s</div>' % s for s in ['Consultation','Negotiation','Booking','Agreement'])
  + '<div class="ch">Referral</div></div>')
w('<div class="g2">')
w(co('The handover rule',
 ['<strong>Marketing owns everything up to the booked visit. Sales owns the visit onward. Both are read on the same number</strong> &mdash; site-visit-to-booking rate, weekly, by community and by consultant &mdash; <strong>so neither can blame the other&rsquo;s stage.</strong>']))
w(co('Two stages that are currently fictional',
 ['<strong>Consultation and negotiation are modelled but have no defined trigger.</strong> They sit inside aggregates, which means <strong>the sales team&rsquo;s own contribution is invisible.</strong> I would promote both to counted CRM gates before go-live. It costs nothing and it decomposes the model&rsquo;s most sensitive variable.'],'calc'))
w('</div>')
w(strip([('Basis','<b>Derived and recommended.</b> Cash-gate figures are my calculation from the proposed ladder'),
         ('Requires validation','What CRM exists today, who owns it, and whether WhatsApp is integrated'),
         ('Determines','Whether Phase 1 is four weeks or four months')]))

open('/tmp/claude-0/-home-user/a5dd8d44-0929-5495-aca9-31c380eaeac4/scratchpad/deck_c.html','w',encoding='utf-8').write('\n'.join(P)+'\n')
print('part C written; last slide =', dk_lib._N[0])
