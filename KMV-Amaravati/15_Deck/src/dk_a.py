# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/claude-0/-home-user/a5dd8d44-0929-5495-aca9-31c380eaeac4/scratchpad')
from dk_lib import *
from dk_css import CSS
P=[]; w=P.append

w(CSS)
w('<div class="deck">')
w('''<nav class="nav" aria-label="Deck contents"><div class="nav-in">
<a href="#s01" class="nb">Cover</a><a href="#s02">02 Summary</a><a href="#s03">03 Basis</a>
<a href="#s04">04 Market</a><a href="#s05">05 Infrastructure</a><a href="#s06">06 Competitors</a>
<a href="#s07">07 Audience</a><a href="#s08">08 Communities</a><a href="#s09">09 Positioning</a>
<a href="#s10">10 GTM</a><a href="#s11">11 Funnel</a><a href="#s12">12 Channels</a>
<a href="#s13">13 Creative</a><a href="#s14">14 CRM</a><a href="#s15">15 KPIs</a>
<a href="#s16">16 ₹25L test</a><a href="#s17">17 Investment</a><a href="#s18">18 Governance</a>
<a href="#s19">19 Attribution</a><a href="#s20">20 Gaps</a><a href="#s21">21 Risk</a>
<a href="#s22">22 Roadmap</a><a href="#s23">23 Decisions</a><a href="#s24" class="nb">24 Recommendation</a>
<a href="#apxA">App. A–G</a>
</div></nav>''')

# ═══════════════ 01 COVER ═══════════════
o,_ = slide('s01','','', cls='cover', h='h1')
P.extend(o[:3])  # section, snum, sbody open
w('''    <p class="cover-mark">Marketing strategy assignment · KMV Spaces</p>
    <h1>Fifteen to the acre.</h1>
    <p class="csub">A marketing and growth strategy for a 25-acre, four-community residential development on the Amaravati&ndash;Mangalagiri corridor &mdash; and a governed way to fund it.</p>
    <div class="cmeta">
      <div><span class="ck">Prepared by</span><b>Kiran Basa</b></div>
      <div><span class="ck">Submitted to</span><b>Mr. Anudeep</b></div>
      <div><span class="ck">Scope</span>~25 acres · ~₹500 Cr project context · four communities, 2BHK to villas</div>
      <div><span class="ck">The ask</span><b>₹25 lakh</b> released against a governed envelope</div>
    </div>
    <div class="disc"><strong>How to read this deck.</strong> Every slide carries a source strip. Four labels are used throughout and never blurred: <span class="lab lab-g">Assignment assumption</span> what I was given &nbsp;·&nbsp; <span class="lab lab-r">Researched</span> with a source ID &nbsp;·&nbsp; <span class="lab lab-d">Derived calculation</span> my own arithmetic on stated inputs &nbsp;·&nbsp; <span class="lab lab-w">Working assumption</span> requires KMV validation. <strong>No figure here has been confirmed by KMV Spaces.</strong> The exact location, product mix, launch dates, approvals, pricing, inventory and commercial assumptions were not provided, and nothing in this deck should be read as a KMV fact.</div>''')
w('  </div>\n</section>')

# ═══════════════ 02 EXECUTIVE SUMMARY ═══════════════
o,_ = slide('s02','Executive summary','The whole argument, before the evidence for it',
  'Six positions. Each is defended in the slides that follow, and each names what would falsify it.')
P.extend(o)
w(cards([
 ('01 · The opportunity is real, and narrower than it looks',
  '<p>Amaravati&rsquo;s capital status is now <strong>statutory</strong>, and capital works are funded and active <span class="sid">[S01][S02]</span>. But of 300+ listed corridor projects, <strong>eleven</strong> genuinely compete &mdash; and the corridor is <strong>crowded at the bottom, thin at the top</strong>.</p>','ev'),
 ('02 · Four communities are four businesses',
  '<p>Differentiated by <strong>buyer constraint, not finish level.</strong> The binding constraint is <strong>cash at purchase</strong>, not income &mdash; ₹17.6 lakh for A rising to ₹74.1 lakh for D. One media plan across four communities would misprice all four.</p>','ev'),
 ('03 · The position must be provable, not aspirational',
  '<p>&ldquo;Luxury&rdquo;, &ldquo;premium&rdquo; and &ldquo;close to the capital&rdquo; are universal in this corridor and therefore worthless. <strong>I would position on one computable fact and an invitation to check it.</strong></p>','ev'),
 ('04 · The headline budget is not a marketing budget',
  '<p>₹31.75 Cr bundles four economically different things. <strong>True marketing operating expense is ₹23.80 Cr</strong>; media is ₹14.65 Cr &mdash; <strong>₹32.6 lakh a month</strong> across a 45-month sell window.</p>','warn'),
 ('05 · Site-visit conversion, not media price, is the lever',
  '<p>The conversion rates are multiplicative and therefore equally sensitive &mdash; but they differ in cost to fix. <strong>One point of site-visit-to-booking is worth ₹39.4 Cr at zero additional media.</strong> No media buy returns that.</p>','warn'),
 ('06 · So I would not release the money on a forecast',
  '<p><strong>I would ask for ₹25 lakh</strong> &mdash; about 1% of the envelope &mdash; to establish cost per lead, cost per qualified lead and cost per qualified site visit, <strong>with the stop condition agreed before the money moves.</strong></p>','warn'),
], 'g3'))
w(co('The sentence this deck exists to earn',
 ['<span class="big">Marketing investment should be earned by performance, not committed by forecast.</span>']))
w(strip([('Sources', sid_('S01','S02')),
         ('Basis', 'Positions 1&ndash;3 rest on researched evidence; 4&ndash;6 on derived calculation over stated assumptions'),
         ('Status', 'Recommendation &mdash; not a KMV decision')]))

# ═══════════════ 03 ASSIGNMENT BASIS ═══════════════
o,_ = slide('s03','Assignment basis &amp; research boundary','What I was given, what I researched, and what I assumed',
  'This slide exists so nothing later can be mistaken for a KMV-confirmed fact. <strong>The three columns never mix.</strong>')
P.extend(o)
w('<div class="g3">')
w('''  <div class="card"><h4 style="color:var(--given)">1 · Given &mdash; the assignment</h4>
  <ul><li><strong>~25-acre</strong> residential development</li>
  <li><strong>~₹500 Cr</strong> project value / budget context</li>
  <li><strong>Amaravati&ndash;Mangalagiri</strong> region</li>
  <li><strong>Four communities</strong> &mdash; A, B, C, D</li>
  <li>Product spectrum <strong>2BHK apartments &rarr; premium residences &rarr; villas</strong></li></ul>
  <p style="margin-top:.55rem;color:var(--ink-3);font-size:.77rem"><strong>Not given:</strong> exact location, product mix, launch dates, approvals, final pricing, inventory, construction status, or any commercial assumption.</p></div>''')
w('''  <div class="card" style="border-color:var(--evidence)"><h4>2 · Researched &mdash; with sources</h4>
  <ul><li>Regional market and capital status <span class="sid">[S01][S02][S18]</span></li>
  <li>Infrastructure, graded asset by asset <span class="sid">[S03][S04][S09][S10]</span></li>
  <li>Competitive field &mdash; 11 of 300+ projects clear the screen <span class="sid">[S12][S13][S15]</span></li>
  <li>Pricing evidence, bottom-up <span class="sid">[S11][S12][S13][S15]</span></li>
  <li>KMV public presence and the AIIMS credential <span class="sid">[S05][S16][S17]</span></li>
  <li>Land pooling &mdash; the S4 audience signal <span class="sid">[S07][S08]</span></li></ul>
  <p style="margin-top:.55rem;color:var(--ink-3);font-size:.77rem"><strong>The retrieval limit:</strong> search worked, page retrieval did not. Every URL resolves; <strong>none was opened.</strong> See Appendix G.</p></div>''')
w('''  <div class="card calc"><h4>3 · Derived or assumed &mdash; mine, not KMV&rsquo;s</h4>
  <ul><li>Inventory <strong>376 units</strong> · density 15.0/acre</li>
  <li>Unit mix A 169 · B 84 · C 60 · D 63</li>
  <li>Price ladder ₹5,150&ndash;7,200/sq ft · blended <strong>₹6,098</strong></li>
  <li>Revenue <strong>₹506.7 Cr</strong> · gross margin <strong>28%</strong> (a placeholder)</li>
  <li>All conversion rates · all funnel volumes</li>
  <li>Marketing investment, allocation, CAC, CPL, CPQL, CPSV</li>
  <li>Site-visit and booking assumptions · cancellation 8% · ROMI</li></ul>
  <p style="margin-top:.55rem;color:var(--decision);font-size:.77rem"><strong>Every item in this column requires KMV validation. None is a finding.</strong></p></div>''')
w('</div>')
w(co('The one thing I would not let a deck hide',
 ['<strong>No primary buyer research exists anywhere behind this work</strong> &mdash; no surveys, interviews, CRM data or walk-in analysis. Every behavioural attribute across eight segments is hypothesis. <strong>No transaction data was obtained either: every price I quote is an asking price.</strong>',
  'That is why the recommendation is a ₹25 lakh test rather than a media plan.']))
w(strip([('Sources', sid_('S01','S02','S03','S04','S05','S07','S08','S09','S10','S11','S12','S13','S15','S16','S17','S18')),
         ('Labels', 'Given · Researched · Derived — used on every slide that follows'),
         ('Register', 'Appendix A assumptions · Appendix F sources · Appendix G limitations')]))

w(band('Part one','The market, honestly graded','Everything in this section is researched and sourced. Where the evidence would not carry a claim, the claim is dropped rather than softened.'))

# ═══════════════ 04 MARKET OPPORTUNITY ═══════════════
o,_ = slide('s04','Market opportunity','The strongest fact available &mdash; and what it still does not prove',
  'Amaravati&rsquo;s status changed in law in April 2026. That is a genuine change in the risk profile of this corridor. <strong>It is not, by itself, evidence of housing demand.</strong>')
P.extend(o)
w('<div class="gsplit">\n<div>')
w(table(['What the evidence establishes','Grade','Source'],[
 ['<strong>Amaravati is Andhra Pradesh&rsquo;s sole capital, by Act of Parliament</strong>','<strong>Confirmed</strong>',sid_('S01')],
 ['Capital works active and funded &mdash; ₹57,821 Cr in progress, ₹15,000 Cr in the 2025&ndash;26 budget','<strong>Confirmed</strong>',sid_('S02')],
 ['AIIMS Mangalagiri operational, ~3 km from the corridor','<strong>Confirmed</strong>',sid_('S03')+sid_('S04')],
 ['Land pooling phase 2 authorised &mdash; 16,666.57 acres, 7 named villages','Confirmed <i>(authorised)</i>',sid_('S07')+sid_('S08')],
 [('<strong>No verified 2026 count of people working in Amaravati exists</strong>'),'<strong>Gap</strong>','&mdash;'],
]))
w('</div>\n<div>')
w(co('Three cautions I would put in front of any investment committee', [
 '<strong>1 · Statutory status is not population.</strong> No verified count exists of people living in the capital region as a result.',
 '<strong>2 · The relocation evidence is nine years stale.</strong> The only headcount figures found &mdash; ~2,000 secretariat staff against a 15,000 target &mdash; are 2016 reporting <span class="sid">[S19]</span>. I have de-weighted the government segment accordingly.',
 '<strong>3 · Construction spend is not consumer demand.</strong> ₹57,821 crore of works generates contractor and labour activity. It does not establish that anyone will buy a ₹2.5 crore villa.',
]))
w('<p class="fine"><strong>Why this matters for the budget.</strong> A capital-status narrative is the cheapest story in this corridor to tell and the easiest to over-fund. Three competitors already carry &ldquo;Amaravati&rdquo; or &ldquo;Capital&rdquo; in their project name. <strong>I would not build the position on it.</strong></p>')
w('</div>\n</div>')
w(strip([('Sources', sid_('S01','S02','S03','S04','S07','S08','S19')),
         ('Basis','Researched. The three cautions are my inference from the evidence, not a source claim'),
         ('Falsified by','A current, verified capital-region headcount showing material in-migration')]))

# ═══════════════ 05 INFRASTRUCTURE ═══════════════
o,_ = slide('s05','Location &amp; infrastructure reality','I would grade every asset before any of it reaches a hoarding',
  'Indian real-estate marketing overstates infrastructure more reliably than anything else. <strong>A brand positioned on being checkable cannot.</strong> This is the grading I would enforce.')
P.extend(o)
w(table(['Asset','Grade','What may be said','Source'],[
 (['<strong>Amaravati as sole capital</strong>','<strong>CONFIRMED</strong>','State it plainly &mdash; the strongest fact available',sid_('S01')],'hl2'),
 (['<strong>AIIMS Mangalagiri, operational</strong>','<strong>CONFIRMED</strong>','An operational hospital ~3 km away',sid_('S03')+sid_('S04')],'hl2'),
 (['<strong>Capital works active and funded</strong>','<strong>CONFIRMED</strong>','Works are active, with figures',sid_('S02')],'hl2'),
 ['Bangalore&ndash;Vijayawada Expressway','UNDER CONSTRUCTION','&ldquo;Under construction&rdquo; &mdash; never &ldquo;complete&rdquo;',sid_('S10')],
 (['<strong>Amaravati Outer Ring Road</strong> &mdash; 189 km, ₹16,000 Cr','<strong>APPROVED</strong>','<strong>&ldquo;Approved, land acquisition begun.&rdquo; Never &ldquo;coming&rdquo;</strong>',sid_('S09')],'hl'),
 (['<strong>Amaravati greenfield airport</strong>','<strong>SPECULATIVE</strong>','<strong>Do not mention at all.</strong> No DPR or notification found in two separate searches','&mdash;'],'hl'),
 (['<strong>Metro</strong>','<strong>NOT ESTABLISHED</strong>','<strong>Do not mention.</strong> No 2026 status found','&mdash;'],'hl'),
]))
w('<div class="g2">')
w(co('The ORR is the discipline test, and it is the one most likely to be failed',
 ['It is <strong>genuinely approved</strong>, genuinely 189 km, genuinely ₹16,000 crore &mdash; and <strong>genuinely not built</strong>, with land acquisition only beginning.',
  'The category routinely presents exactly this status as an existing amenity. <strong>The distinction is one word: approved, not coming.</strong> I would hold every asset to it.']))
w(co('What I would not do',
 ['<strong>Assume future infrastructure creates demand.</strong> The corridor already contains projects marketing an unbuilt airport. Joining them costs the one asset this brand would have &mdash; that its claims can be checked.'],'ev'))
w('</div>')
w(strip([('Sources', sid_('S01','S02','S03','S04','S09','S10')),
         ('Basis','Researched. Grades applied by me against a stated six-level rubric'),
         ('Rule','Nothing graded PROPOSED, REPORTED or SPECULATIVE may appear in any published claim')]))

open('/tmp/claude-0/-home-user/a5dd8d44-0929-5495-aca9-31c380eaeac4/scratchpad/deck_a.html','w',encoding='utf-8').write('\n'.join(P)+'\n')
print('part A written:', sum(len(x) for x in P), 'chars')
