# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/claude-0/-home-user/a5dd8d44-0929-5495-aca9-31c380eaeac4/scratchpad')
from dk_lib import *
import dk_lib
dk_lib._N[0] = 5          # continue numbering after slide 05
P=[]; w=P.append

# ═══════════════ 06 COMPETITORS ═══════════════
o,_ = slide('s06','Competitive landscape','Of 300+ listed projects, eleven actually compete',
  'The screen is itself the finding: <strong>the corridor is crowded at the bottom and thin at the top.</strong> Four projects overlap on all six screening dimensions.')
P.extend(o)
w('<div class="gsplit">\n<div>')
w(table(['Competitor','Scale &amp; density','Price evidence','Where it is weak'],[
 ['<strong>IJM Raintree Park</strong> <i>(Dwaraka Krishna)</i>','120 ac · ~3,300 planned','Apartments ~₹3,900/sq ft; villas to ₹10,143','<strong>Has the full ladder and has never marketed it as one</strong> &mdash; built over 18 years under five names'],
 ['<strong>IJM Villas 64</strong>','33.69 ac · 64 villas · <strong>1.9/acre</strong>','From <strong>₹3.75 Cr</strong>','Owns the top outright. ₹3.75 Cr floor excludes almost the entire corridor buyer base'],
 ['<strong>Prime Grandeur</strong>','10 ac · 119 villas · 11.9/acre','₹1.34&ndash;1.82 Cr · ₹5,394&ndash;5,403/sq ft','<strong>The most direct competitor.</strong> Value-led, no proof layer'],
 ['<strong>Manjeera Monarch</strong>','Apartments · 113/acre','<strong>₹5,100/sq ft &mdash; delivered</strong>','Documented carpet-area complaint: <i>&ldquo;the area advertised is not what residents actually get&rdquo;</i>'],
 ['Srivalli Pravas · Jayabheri · Grand Project Capitol · Aparna · TAG AIRA · KMV Vivaan · CRDA plots','&mdash;','&mdash;','Seven further entrants; none publishes delivery evidence'],
], note='Sources: '+sid_('S12','S13','S15')+' &mdash; portal-published asking prices and project pages. Density figures are derived from published acreage &divide; published unit counts where both exist.'))
w('</div>\n<div>')
w(co('Where I judge KMV can win &mdash; and where it cannot',
 ['<strong>Not on scale.</strong> Raintree Park is 120 acres. <strong>Not on lowest density</strong> &mdash; IJM Villas 64 runs 1.9/acre and Prime Grandeur 11.9. <strong>Not on luxury, premium, amenities or proximity to the capital</strong> &mdash; all four are universal here and therefore say nothing.',
  '<strong>Two spaces survive the test of being unoccupied, valuable and hard to copy inside 24 months:</strong>']))
w(cards([
 ('White space 1 &mdash; the ladder in one address',
  '<p>Nobody in this corridor sells <strong>a community you can move within.</strong> It needs 25+ contiguous acres and a mixed masterplan committed from day one &mdash; it cannot be retrofitted onto a 5-acre tower cluster.</p>','ev'),
 ('White space 2 &mdash; delivery proof <i>(cheapest to occupy)</i>',
  '<p>The complaints across the set are consistent &mdash; carpet area, maintenance, unfulfilled amenity promises, late handover &mdash; and <strong>not one competitor markets against them.</strong> A competitor carrying those complaints cannot credibly follow.</p>','ev'),
], 'g2'))
w('</div>\n</div>')
w(strip([('Sources', sid_('S12','S13','S15')),
         ('Basis','Researched. The screen, the density arithmetic and the white-space test are mine'),
         ('Caution','<strong>Jayabheri The Capital returned no search result at all</strong>, and unit counts for two density comparators are unpublished &mdash; see slide 13')]))

# ═══════════════ 07 AUDIENCE ═══════════════
o,_ = slide('s07','Customer &amp; audience architecture','I would prioritise on cash at purchase, not on income',
  'The binding constraint in this catchment is <strong>the down payment, not the EMI</strong> &mdash; ₹17.6 lakh for Community A rising to ₹74.1 lakh for D. Two households on identical incomes can have completely different ability to clear it.')
P.extend(o)
w(table(['#','Segment','Priority score','Horizon','Community fit','Why it ranks here'],[
 (['1','<strong>S3 &mdash; US / developed-market Telugu diaspora</strong>','<strong>4.20</strong>','Mid','B and C','Highest revenue per unit; buys remotely; the visit is the constraint, not the money'],'hl2'),
 (['2','<strong>S4 &mdash; Amaravati land-pooling landowners</strong>','<strong>4.05</strong>','Long','D and C, via exchange','<strong>Best-evidenced population, no competitor contesting it</strong> <span class="sid">[S07][S08]</span>. Needs an exchange structure, not a price list'],'hl2'),
 (['3','<strong>S1 &mdash; Vijayawada / Guntur trade families</strong>','<strong>4.05</strong>','Near','C and D','Deepest purchase-ready cash pool. Runs on referral, not advertising'],'hl2'),
 ['4','S7 &mdash; Hyderabad Telugu households with AP roots','3.90','Mid','B and C','Large, wealthy, four hours away, and unaddressed by the competitive set'],
 ['5','S2 &mdash; Senior institutional medical professionals','3.90','Near','A through C','Highest reachability; the only genuinely digital-first audience; dated purchase triggers'],
 ['6','S6 &mdash; Vijayawada salaried upgraders','3.20','Near','A and B','<strong>Most contested and least valuable</strong> &mdash; 21% of units, 13.7% of revenue'],
 (['7','<strong>S5 &mdash; Government / capital workforce</strong>','2.95','Near','A','<strong>De-weighted.</strong> Its sizing rests on 2016 reporting <span class="sid">[S19]</span> &mdash; nine years stale'],'hl'),
 ['8','S8 &mdash; Gulf remittance households','2.45','Long','A and B','Different income, product fit, language and channel from S3. <strong>One campaign cannot serve both</strong>'],
], note='Priority score is a weighted composite I built &mdash; cash-gate clearance 20%, reachability 15%, and four further criteria. <strong>Scores, segment sizes and every behavioural attribute are working assumptions: no primary buyer research exists.</strong>'))
w('<div class="g2">')
w(co('The check I would run on any prioritisation',
 ['<strong>Does the priority order reconcile to where the revenue is?</strong> Here it does: the three HIGH segments deliver <strong>53.8% of revenue from 43% of units.</strong>',
  'And the arithmetic settles a debate that otherwise becomes an opinion: <strong>every rupee spent winning a contested S6 sale buys less than half the revenue of an uncontested S3 sale</strong> &mdash; ₹0.83 Cr per unit against ₹1.96 Cr.'],'calc'))
w(co('What I would not assume',
 ['<strong>&ldquo;NRI&rdquo; is not a segment.</strong> It splits into S3 and S8, which differ in income, purpose, product, language and channel. <strong>Every competitor in the set collapses them into one.</strong>',
  '<strong>&ldquo;HNI&rdquo; is not a segment here either</strong> &mdash; and the product is not an HNI product. Community D tops out at ₹2.74 Cr. Marketing to &ldquo;HNIs&rdquo; would promise a tier the price sheet does not deliver.']))
w('</div>')
w(strip([('Sources', sid_('S07','S08','S19')),
         ('Basis','Segment definitions researched; <b>scoring, sizing and revenue split are derived</b>'),
         ('Requires validation','24 months of CRM lead data by source, and a current capital-region headcount')]))

# ═══════════════ 08 COMMUNITIES ═══════════════
o,_ = slide('s08','Project &amp; community architecture','Proposed positioning architecture &mdash; four buyer constraints, not four finish levels',
  '<strong>This is a proposal, not a product fact.</strong> Unit counts, sizes, prices and mix are my derivation from a 25-acre parcel and researched competitor pricing. <strong>All of it requires KMV validation.</strong>')
P.extend(o)
w('<div class="mx">' + table(
 ['','A','B','C','D'],[
 ['<strong>Proposed product</strong>','Low-rise garden apartments','Managed residences','Compact detached villas','Estate villas'],
 ['<strong>Units · revenue</strong>','169 · ₹126.2 Cr','84 · ₹112.5 Cr','60 · ₹109.2 Cr','63 · ₹158.8 Cr'],
 ['<strong>Ticket</strong>','₹59&ndash;90 L','₹1.23&ndash;1.45 Cr','₹1.69&ndash;1.95 Cr','₹2.30&ndash;2.74 Cr'],
 ['<strong>Cash at purchase</strong>','<strong>~₹17.6 L</strong>','~₹31.5 L','~₹52.0 L','<strong>~₹74.1 L</strong>'],
 ['<strong>Customer</strong>','Junior medical, local upgraders, government','<strong>US / developed-market diaspora</strong>','Trade families, senior medical','Trade families, <strong>land-pooling landowners</strong>'],
 ['<strong>The need it answers</strong>','<i>&ldquo;Can I own here at all?&rdquo;</i>','<i>&ldquo;Can I own this from 12,000 km away?&rdquo;</i>','<i>&ldquo;Can I have land without ₹2.5 crore?&rdquo;</i>','<i>&ldquo;Is this the last house I buy?&rdquo;</i>'],
 ['<strong>Positioning</strong>','Entry, rental logic, proximity','<strong>Management and absence</strong>','Land and privacy at a reachable ticket','Scale and permanence'],
 ['<strong>Message</strong>','&ldquo;The address you were told you could not afford&rdquo;','&ldquo;Owned from anywhere. Looked after here&rdquo;','&ldquo;Your own ground, without the villa premium&rdquo;','&ldquo;Built to be inherited&rdquo;'],
 ['<strong>Channel mix</strong>','Meta, portals, local outdoor','<strong>LinkedIn, diaspora networks, video walkthrough</strong>','Google Search, referral, site','<strong>Referral, village relationships, private visits</strong>'],
 ['<strong>Conversion event</strong>','Site visit &rarr; token','<strong>Proxy visit &rarr; remote booking file</strong>','Site visit &rarr; plot selection','Private visit &rarr; family consultation'],
 ['<strong>Sales cycle</strong>','2&ndash;4 months','<strong>6&ndash;12 months</strong>','4&ndash;8 months','6&ndash;14 months'],
]).replace('<div class="tw ">','').replace('</div>','',1) + '</div>')
w('<div class="g2" style="margin-top:1rem">')
w(co('Two structural rules, not promotional ones',
 ['<strong>B never above ₹1.50 Cr. C never below ₹1.65 Cr.</strong> Without them B and C collapse into one product and the ladder becomes a price list.',
  '<strong>B is defined by service; C is defined by land.</strong> A buyer choosing between them is choosing between two different products, not two price points.']))
w(co('Why they cannot share a campaign',
 ['Different <strong>cash gate</strong> (4.2&times; from A to D), different <strong>cycle</strong> (2 months to 14), different <strong>objection</strong>, and different <strong>proof</strong>. A shared campaign optimises to the cheapest lead, which is Community A &mdash; the community with the least pricing headroom.'],'ev'))
w('</div>')
w(strip([('Sources','Ticket bands derived from researched competitor pricing '+sid_('S12','S13','S15')),
         ('Basis','<b>Derived and assumed throughout.</b> Not a KMV product specification'),
         ('Requires validation','Masterplan, unit mix, approvals, and the price sheet')]))

# ═══════════════ 09 POSITIONING ═══════════════
o,_ = slide('s09','Positioning strategy','One computable fact, and an invitation to check it',
  'The corridor&rsquo;s advertising is generic and proof-free. <strong>In a market where nobody publishes evidence, the strongest available position is to publish it.</strong>')
P.extend(o)
w('<div class="gsplit">\n<div>')
w('<p class="lede">Not &ldquo;luxury&rdquo;. Not &ldquo;premium&rdquo;. Not &ldquo;close to the capital&rdquo;. <strong>Fifteen homes to the acre, across twenty-five acres &mdash; and everything else is open to inspection.</strong></p>')
w(table(['Dimension','Fact','Marketing narrative','Future possibility'],[
 ['<strong>Density</strong>','<strong>15.0 units/acre across 25 acres</strong> <span class="lab lab-d">Derived</span>','&ldquo;A community you can count&rdquo;','&mdash;'],
 ['<strong>Capital</strong>','Statutory sole capital <span class="sid">[S01]</span>','&ldquo;The city is now certain; the question is where in it&rdquo;','Population growth &mdash; <strong>unevidenced</strong>'],
 ['<strong>AIIMS</strong>','Operational, ~3 km <span class="sid">[S03]</span>','&ldquo;Your workplace is the anchor of the neighbourhood&rdquo;','&mdash;'],
 ['<strong>ORR</strong>','Approved; land acquisition begun <span class="sid">[S09]</span>','&ldquo;Approved &mdash; and we will say so until it is built&rdquo;','Travel-time change &mdash; <strong>do not model it</strong>'],
 (['<strong>Airport / metro</strong>','<strong>Nothing found</strong>','<strong>Silence</strong>','<strong>Not ours to sell</strong>'],'hl'),
 ['<strong>Delivery</strong>','Category complaints documented <span class="sid">[S12]</span>','&ldquo;We publish carpet area, handover dates and progress&rdquo;','&mdash;'],
]))
w('</div>\n<div>')
w(co('The credential I would not build on until it documents',
 ['The strongest brand asset available would be construction lineage &mdash; the group&rsquo;s own site presents an AIIMS Mangalagiri credential <span class="sid">[S17]</span>.',
  '<strong>But the Ministry&rsquo;s own tender document names HSCC as executing agency</strong> <span class="sid">[S05]</span>, and no source I found establishes the group&rsquo;s contractual scope.',
  '<strong>I would not publish it until a work order defines it &mdash; and then I would claim exactly that scope, in those words.</strong>']))
w(co('And the fallback, which is not a retreat',
 ['If the credential does not document, the position falls back to two things that are <strong>provable without any credential at all</strong>: <strong>the density arithmetic</strong> and <strong>an ungated price sheet.</strong>',
  'That is a deliberate design choice. <strong>A position that collapses when one document is missing is not a position.</strong>'],'ev'))
w('</div>\n</div>')
w(strip([('Sources', sid_('S01','S03','S05','S09','S12','S17')),
         ('Basis','Researched facts; <b>the positioning and the fallback are my recommendation</b>'),
         ('Falsified by','The density comparators failing to source, or the locality refusing the price premium')]))

open('/tmp/claude-0/-home-user/a5dd8d44-0929-5495-aca9-31c380eaeac4/scratchpad/deck_b.html','w',encoding='utf-8').write('\n'.join(P)+'\n')
print('part B written; last slide number =', dk_lib._N[0])
