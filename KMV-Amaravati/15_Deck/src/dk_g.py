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

# ═══ E — KPI DEFINITIONS ═══
apx('apxE','E','KPI definitions',
 'Every metric used in this deck, with its formula and its target. <strong>Targets are derived from the modelled funnel; ceilings are derived from a 30%-of-gross-profit policy, not from an industry norm.</strong>')
w(table(['Metric','Formula','#Target','#Ceiling','Reads as'],[
 ['Reach','Unique individuals exposed','6,573,000','&mdash;','<span class="lab lab-d">Derived</span> <strong>an output, not an input</strong>'],
 ['Impressions','Total ad deliveries','Not targeted','&mdash;','Diagnostic only'],
 ['CTR','Clicks &divide; impressions','≥ 1.2%','&mdash;','Leading'],
 ['CPC','Media &divide; clicks','Platform-dependent','&mdash;','Diagnostic'],
 ['Hook rate','3-second views &divide; impressions','≥ 25%','&mdash;','Leading &mdash; creative'],
 ['Leads','CRM records created','78,880','&mdash;','Volume'],
 (['<strong>CPL</strong>','Media &divide; leads','<strong>₹1,247</strong>','₹1,672','Leading &mdash; <strong>a buying metric, not a business metric</strong>'],'hl2'),
 ['MQL rate','MQL &divide; leads','45.0%','&mdash;','Leading'],
 ['SQL rate','SQL &divide; MQL','55.0%','&mdash;','Leading'],
 ['Qualification rate','Qualified &divide; SQL','63.9%','&mdash;','Leading'],
 (['<strong>CPQL</strong>','Media &divide; qualified leads','<strong>₹7,889</strong>','<strong>₹10,576</strong>','<strong>Leading &mdash; the metric campaigns are optimised against</strong>'],'hl'),
 ['Lead-to-visit','Visits held &divide; leads','3.7%','&mdash;','Leading'],
 ['Qualified-to-visit rate','Visits held &divide; qualified leads','23.4%','&mdash;','Leading'],
 ['Site-visit show rate','Held &divide; booked','≥ 60%','&mdash;','Leading'],
 ['Cost per site visit <i>(booked)</i>','Media &divide; visits booked','₹20,205','&mdash;','Leading'],
 (['<strong>Cost per qualified site visit</strong>','Media &divide; visits held','<strong>₹33,676</strong>','<strong>₹45,144</strong>','<strong>Leading &mdash; the Phase 0 decision metric</strong>'],'hl'),
 ['Cost per opportunity','Media &divide; negotiations','₹1,71,429','₹2,29,810','Leading &mdash; late funnel'],
 (['<strong>Visit-to-booking</strong>','Bookings &divide; visits held','<strong>≥ 6.9%</strong>','&mdash;','<strong>Leading &mdash; one point is worth ₹39.4 Cr</strong>'],'hl'),
 ['Cost per booking <i>(media only)</i>','Media &divide; marketing-sourced bookings','₹4.90 L','&mdash;','Lagging'],
 (['<strong>CAC</strong>','<strong>Total acquisition cost &divide; net units sold</strong>','<strong>₹8.44 L</strong>','<strong>₹11.32 L</strong>','<strong>Lagging &mdash; the board number</strong>'],'hl'),
 ['Marketing cost per booking <i>(opex only)</i>','Marketing opex &divide; net units','₹6.33 L','&mdash;','Lagging'],
 ['Revenue','Net units &times; achieved ticket','₹506.7 Cr at plan','&mdash;','Lagging'],
 ['Gross profit','Revenue &times; gross margin','₹141.9 Cr <i>@28%</i>','&mdash;','Lagging <span class="lab lab-w">margin is a placeholder</span>'],
 ['Marketing investment','Marketing opex','₹23.80 Cr','&mdash;','Lagging'],
 (['<strong>ROMI</strong>','<strong>(Gross profit &minus; marketing investment) &divide; marketing investment</strong>','<strong>3.47&times;</strong> <i>@28%</i>','≥ 3.0&times;','<strong>Lagging &mdash; on gross profit, never on revenue</strong>'],'hl'),
 (['ROAS <i>(media only)</i>','Revenue &divide; media','<strong>Diagnostic only</strong>','&mdash;','<strong>Never a decision metric</strong>'],'dim'),
 (['Revenue &divide; marketing spend','Revenue &divide; marketing opex','<strong>Would read 16.0&times;</strong>','&mdash;','<strong>Meaningless. Not ROMI. Do not present it</strong>'],'dim'),
 ['Break-even','Bookings needed for gross profit to cover marketing','<strong>84 units of 376</strong> <i>@28%</i>','&mdash;','Lagging &mdash; <strong>the statement that survives every margin</strong>'],
 ['Incremental return','Bookings needed per ₹1 Cr of marketing','<strong>2.65</strong> <i>@28%</i>','&mdash;','The test for any additional crore'],
 ['Payback','Months to recover CAC from gross profit','≤ 9 months','&mdash;','Lagging'],
 ['Cancellation rate','Cancelled &divide; gross bookings','≤ 8%','12%','Lagging'],
 ['Referral rate','Referrals per owner-year','≥ 0.15','&mdash;','Lagging &mdash; the compounding asset'],
 ['Marketing % of GDV','Marketing opex &divide; GDV','4.70% <i>(opex)</i> · 6.27% <i>(all-in)</i>','8.40%','<strong>Stated last because it is the least useful</strong>'],
]))
w(co('Three reading rules that belong in the reporting template',
 ['<strong>1 · Compare within a layer, never across.</strong> Judging brand against performance on cost per booking defunds ₹10.25 Cr of the highest-value spend.',
  '<strong>2 · Judge demand generation on CPQL, not CPL.</strong> Cheap leads that fail the cash gate are a cost, not a result.',
  '<strong>3 · Judge brand, outdoor and the site on holdouts and first-touch, never on last click.</strong>']))
w('<p class="fine"><strong>Deliberately absent from the dashboard: impressions, reach, followers and page views as reported metrics.</strong> None of them can change a decision, and each can be used to defend a bad quarter.</p>')
endapx()

# ═══ F — SOURCES ═══
apx('apxF','F','Source register',
 'Twenty source IDs covering <strong>forty distinct URLs</strong> across six tiers. Every [Sxx] reference in this deck resolves here.')
w('<div class="tw"><table>')
w('  <thead><tr><th>ID</th><th>Tier</th><th>Source</th><th>What it supports</th><th>Date</th></tr></thead>\n  <tbody>')
for sid, tier, name, supports, urls, date in SOURCES:
    w('    <tr class="srcrow"><td>[%s]</td><td>%s</td><td><strong>%s</strong></td><td>%s<div class="url">%s</div></td><td>%s</td></tr>'
      % (sid, tier, name, supports, '<br>'.join(urls), date))
w('  </tbody></table></div>')
w('<div class="g2">')
w(table(['Tier','#URLs','Status'],[
 ['<strong>1 &mdash; Government / official</strong>','8','Used'],
 (['<strong>2 &mdash; RERA / regulatory</strong>','<strong>0</strong>','<strong>Empty</strong>'],'hl'),
 ['<strong>3 &mdash; Official developer</strong>','5','Used'],
 (['<strong>4 &mdash; Established research</strong>','<strong>0</strong>','<strong>Empty</strong>'],'hl'),
 ['<strong>5 &mdash; Property portals</strong>','9','Used &mdash; <strong>asking prices only</strong>'],
 ['<strong>6 &mdash; Major business / news</strong>','9','Used'],
 ['<strong>7 &mdash; Credible local</strong>','3','Used'],
 ['<strong>8 &mdash; Secondary</strong>','6','<strong>Corroboration only</strong>'],
 (['<strong>Total</strong>','<strong>40</strong>','across six tiers'],'tot'),
]))
w(co('What the two empty tiers cost',
 ['<strong>RERA / regulatory</strong> would have settled achieved prices, absorption, unsold inventory, published unit counts and the legitimacy of every named competitor.',
  '<strong>Established research</strong> would have given corridor-level demand and supply, velocity, and an independent price series to test the portal figures against.',
  '<strong>Their absence is why Appendix B cannot escape asking prices and Appendix C cannot establish velocity.</strong> Both are obtainable and neither is expensive.']))
w('</div>')
endapx()

# ═══ G — LIMITATIONS ═══
apx('apxG','G','Research limitations',
 'Stated plainly, because a strategy that hides its own limits is not one.')
w('<div class="g2">')
w(co('1 &mdash; Search worked. Page retrieval did not',
 ['<strong>Every URL in Appendix F is real and resolves. Not one of them was opened.</strong> Outbound page fetches returned <span class="mono">EGRESS_BLOCKED</span>, and direct requests to <span class="mono">crda.ap.gov.in</span> and <span class="mono">rera.ap.gov.in</span> returned <span class="mono">403</span> policy denials.',
  'Claim content therefore comes from search-result summaries, not from reading the source. <strong>A Tier 1 domain means the domain is authoritative &mdash; not that the document was verified.</strong>']))
w(co('2 &mdash; No primary buyer research exists',
 ['<strong>No surveys, interviews, focus groups, CRM data or walk-in analysis of any kind.</strong> Every behavioural attribute across all eight segments is hypothesis, and the priority scores are a weighted judgement, not a measurement.']))
w(co('3 &mdash; Every price is an asking price',
 ['<strong>No transaction or registration data was obtained.</strong> The 50% locality premium underneath the whole revenue model is therefore untested, and Community A prices above a delivered comparable with no delivery record to justify it.']))
w(co('4 &mdash; No construction cost data',
 ['<strong>The 28% gross margin is a placeholder.</strong> Every ROI, ROMI, break-even and CAC-ceiling figure in this deck is arithmetic on that placeholder. Contractor quotations are the only fix.']))
w('</div>')
w('<h3 class="sh">Five things this research searched for and could not find</h3>')
w(table(['What was sought','Why it matters','Status'],[
 ['<strong>A verified 2026 headcount for people working in Amaravati</strong>','The government segment is sized against 2016 reporting <span class="sid">[S19]</span> &mdash; nine years stale','<strong>Not found.</strong> Segment de-weighted'],
 ['<strong>Project-level evidence of ₹2.2&ndash;2.8 Cr villa depth</strong>','<strong>₹268 Cr of the plan is priced into that band</strong>','<strong>Not found across eight rounds.</strong> Weak evidence of absence'],
 ['<strong>A DPR or notification for an Amaravati greenfield airport</strong>','It appears in competitor marketing','<strong>Not found in two separate searches. Excluded entirely</strong>'],
 ['<strong>Corroboration of a net-zero-energy villa claim</strong>','It would be a creative pillar','<strong>Not found.</strong> Not used'],
 ['<strong>KMV&rsquo;s contractual scope on AIIMS Mangalagiri</strong>','The Ministry names HSCC as executing agency <span class="sid">[S05]</span>; the group&rsquo;s own page does not define scope <span class="sid">[S17]</span>','<strong>Not established.</strong> The credential is not claimed anywhere in this deck'],
]))
w(co('The single most valuable next step is not more analysis',
 ['It is <strong>three conversations.</strong> KMV on the AIIMS work order and the Vivaan booking book; a records agent on 24 months of IGRS registrations; a mystery shopper on two villa projects.',
  '<strong>Between them they close the four items that carry more risk than everything else in this deck combined</strong> &mdash; and two of the three are free.'],'calc'))
w('<p class="fine" style="margin-top:1.3rem"><strong>Prepared by Kiran Basa.</strong> Marketing Strategy Assignment &mdash; KMV Spaces, Amaravati / Mangalagiri. Submitted to Mr. Anudeep. <strong>Nothing in this deck has been confirmed by KMV Spaces</strong>, and no figure here should be represented as a KMV fact. The project described is the hypothetical one set out in the assignment brief.</p>')
endapx()

w('''<footer class="close">
  <p><strong>Marketing Strategy Assignment &mdash; KMV Spaces, Amaravati / Mangalagiri.</strong> Prepared by Kiran Basa, submitted to Mr. Anudeep.</p>
  <p>The exact project location, product mix, launch dates, approvals, final pricing, inventory, construction status and commercial assumptions were not provided in the brief. <strong>Everything derived from them is labelled Derived calculation or Working assumption and requires KMV validation.</strong> No industry benchmark has been manufactured, and no estimate is offered anywhere for KMV&rsquo;s actual marketing budget, spend, headcount, cost per lead, sales velocity or inventory position &mdash; none was available.</p>
</footer>
</div>''')

open('/tmp/claude-0/-home-user/a5dd8d44-0929-5495-aca9-31c380eaeac4/scratchpad/deck_g.html','w',encoding='utf-8').write('\n'.join(P)+'\n')
print('appendices E-G + close written')
