# -*- coding: utf-8 -*-
"""Shared helpers + the canonical source register for the KMV deck."""

# ---- evidence labels -------------------------------------------------
GIVEN = '<span class="lab lab-g">Assignment assumption</span>'
RSRCH = '<span class="lab lab-r">Researched</span>'
DERIV = '<span class="lab lab-d">Derived calculation</span>'
WORK  = '<span class="lab lab-w">Working assumption</span>'

def L(k):
    return {'G':GIVEN,'R':RSRCH,'D':DERIV,'W':WORK}[k]

# ---- source register -------------------------------------------------
# id -> (tier, name, what it supports, [urls], date)
SOURCES = [
 ('S01','1 — Government / official','Prasar Bharati / NewsOnAir (Govt of India)',
  'Amaravati granted statutory status as Andhra Pradesh&rsquo;s sole capital',
  ['https://www.newsonair.gov.in/parliament-clears-capf-general-administration-also-grants-statutory-status-to-amaravati-as-andhra-pradeshs-sole-capital'],'2 Apr 2026'),
 ('S02','1 — Government / official','Prasar Bharati / NewsOnAir',
  'Capital-city construction works active; APCRDA progress briefings to the Chief Minister',
  ['https://www.newsonair.gov.in/andhra-pradesh-cm-holds-high-level-review-of-ongoing-capital-city-construction-works-at-his-camp-office-in-amaravati',
   'https://www.newsonair.gov.in/apcrda-updates-cm-chandrababu-naidu-on-amaravati-development-progress',
   'https://www.newsonair.gov.in/andhra-pradesh-chief-minister-n-chandrababu-naidu-to-chair-review-meeting-at-state-secretariat'],'Feb–Apr 2026'),
 ('S03','1 — Government / official','Press Information Bureau, Government of India',
  'AIIMS Mangalagiri — dedication to the nation',['https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2008922&amp;reg=48&amp;lang=2'],'Feb 2024'),
 ('S04','1 — Government / official','Prasar Bharati / NewsOnAir',
  'PRAGATI review of the AIIMS Mangalagiri project',['https://www.newsonair.gov.in/pms-flagship-platform-pragati-accelerates-aiims-mangalagiri-project-in-andhra-pradesh/'],'21 Jan 2026'),
 ('S05','1 — Government / official','Ministry of Health &amp; Family Welfare — PMSSY tender',
  '<strong>Names HSCC as executing agency for the AIIMS Guntur/Mangalagiri package</strong> — the document that puts the KMV credential in question',
  ['https://pmssy.mohfw.gov.in/files/tender/GUNTUR_RFP.pdf'],'undated'),
 ('S06','1 — Government / official','MoEFCC environment-clearance filing',
  'KMV Vivaan — Form 1 filing, establishing the project&rsquo;s existence and location',
  ['https://environmentclearance.nic.in/writereaddata/FormB/EC/FORM_1/020620163BFNM71GKMVVivaanForms.pdf'],'2016'),
 ('S07','6 — Major business / news','ThePrint','APCRDA returnable-plot allotment to Amaravati farmers by e-lottery',
  ['https://theprint.in/india/crda-allots-returnable-plots-to-amaravati-farmers-through-e-lottery/2835222/'],'23 Jan 2026'),
 ('S08','6 — Major business / news','Deccan Herald','Amaravati relaunch; second-phase land pooling (16,666.57 acres across 7 villages)',
  ['https://www.deccanherald.com/india/andhra-pradesh/amaravati-relaunch-farmers-rejoice-at-revival-of-their-capital-city-dream-after-a-more-than-5-year-fight-3522352',
   'https://www.deccanherald.com/india/andhra-pradesh/andhra-pradesh-gets-ready-for-another-round-of-land-pooling-for-amaravati-3817447',
   'https://www.deccanherald.com/india/andhra-pradesh/farmers-ready-to-offer-36000-acres-under-second-phase-land-pooling-for-amaravati-minister-3568780'],'2025–26'),
 ('S09','6 — Major business / news','Indian Infrastructure · Construction World',
  'Amaravati Outer Ring Road — 189 km, ₹16,000 Cr, MoRTH approval of 140 m width. <strong>Approved; land acquisition begun</strong>',
  ['https://indianinfrastructure.com/2025/01/16/centre-approves-amaravati-outer-ring-road-project/',
   'https://indianinfrastructure.com/2025/05/05/morth-approves-140-m-of-width-for-amaravati-six-lane-outer-ring-road-in-andhra-pradesh/',
   'https://www.constructionworld.in/transport-infrastructure/highways-and-roads-infrastructure/centre-approves-amaravati-outer-ring-road-project/67638/'],'2025'),
 ('S10','6 — Major business / news','BlackRidge Research','Bangalore–Vijayawada Expressway — under construction',
  ['https://www.blackridgeresearch.com/project-profiles/bangalore-vijayawada-expressway-length-route-map-cost-contractors-current-status-completion-date-updates'],'Jan 2025'),
 ('S11','5 — Property portals','SquareYards — locality data','Mangalagiri locality asking average ₹4,062/sq ft (and the ₹4,098 / ₹4,805 / ₹5,489 series)',
  ['https://www.squareyards.com/property-rates/mangalagiri-vijayawada'],'Sept 2025 · page dated Mar 2026'),
 ('S12','5 — Property portals','SquareYards · CommonFloor','Manjeera Monarch — <strong>delivered apartment comparable at ₹5,100/sq ft</strong>, and its documented carpet-area complaint',
  ['https://www.squareyards.com/vijayawada-residential-property/manjeera-monarch/10076/project',
   'https://www.commonfloor.com/manjeera-monarch-vijayawada/povp-iot2f8'],'2026'),
 ('S13','5 — Property portals','99acres · SquareYards','IJM Raintree Park Dwaraka Krishna and IJM Villas 64 — 33.69 ac, 64 villas, <strong>1.9 units/acre</strong>, from ₹3.75 Cr',
  ['https://www.99acres.com/ijm-rtpdk-villas-64-mangalagiri-guntur-npxid-r438456',
   'https://www.squareyards.com/vijayawada-residential-property/ijm-township/45093/project',
   'https://www.99acres.com/villas-in-mangalagiri-guntur-ffid'],'2026'),
 ('S14','5 — Property portals','99acres · Regrob','KMV Vivaan villas — <strong>asking ₹3.59 Cr (Ph I) and ₹5.21 Cr (Ph II)</strong>; located Poranki/Penamaluru, east Vijayawada — not the corridor',
  ['https://www.99acres.com/kmv-vivaan-villas-penamaluru-vijayawada-npxid-r370665',
   'https://regrob.com/project/kmv-vivaan-villas-poranki-vijayawada/'],'2026'),
 ('S15','5 — Property portals','SquareYards','SLV Amaravathi Pride — ₹4,210/sq ft',
  ['https://www.squareyards.com/vijayawada-residential-property/slv-amaravathi-pride/102855/project'],'2026'),
 ('S16','3 — Official developer','KMV Spaces (official site)','Villa product pages, Vijayawada',
  ['https://www.kmvspaces.com/projects/villas-in-vijayawada',
   'https://www.kmvspaces.com/projects/luxury-villas-for-sale-in-vijayawada'],'undated'),
 ('S17','3 — Official developer','KMV Projects (official site)','The AIIMS Mangalagiri credential as the group states it — <strong>scope not defined on the page</strong>',
  ['https://www.kmvprojects.com/building-factories/all-india-institute-of-medical-and-sciences-(aiims),-mangalagiri',
   'https://www.kmvprojects.com/building-factories',
   'https://www.kmvspaces.com/about-us'],'undated'),
 ('S18','7 — Credible local','The South First','Capital-status timelines; land-pooling grievance resolution timelines',
  ['https://thesouthfirst.com/andhrapradesh/as-overhang-on-capital-status-lifts-naidu-sets-clock-ticking-for-amaravati/',
   'https://thesouthfirst.com/andhrapradesh/amaravati-land-pooling-government-sets-tight-timelines-to-resolve-decade-long-farmer-grievances/'],'2026'),
 ('S19','6 — Major business / news','Deccan Chronicle','Secretariat staff relocation — ~2,000 staff, a 15,000 target. <strong>Nine years stale; the only headcount evidence found</strong>',
  ['https://www.deccanchronicle.com/nation/current-affairs/021016/andhra-pradesh-staff-begin-to-shift-to-secretariat-in-amaravati.html'],'2 Oct 2016'),
 ('S20','7–8 — Corroboration only','CellIT · Wikipedia · Topline Realty · others','Secondary corroboration only — AIIMS OPD commencement, land-rate context. <strong>Never load-bearing</strong>',
  ['https://cellit.in/aiims-mangalagiri-to-commence-opd-services-from-12th-march/',
   'https://en.wikipedia.org/wiki/All_India_Institute_of_Medical_Sciences,_Mangalagiri',
   'https://crda.toplinerealty.in/amaravathi-land-rates/',
   'https://orramaravati.in/','https://www.youtube.com/watch?v=5_zfst5xEYY',
   'https://pollent.co.in/project/shared-time-human-resources-management/',
   'https://www.sitaramgroup.org/villas-sale-guntur-amaravati.html'],'2026'),
]
SRC_IDS = [s[0] for s in SOURCES]

# ---- slide scaffolding ----------------------------------------------
_N = [0]
def slide(sid, eyebrow, title, dek=None, cls='', h='h2'):
    _N[0] += 1
    n = _N[0]
    out = ['\n<section class="slide %s" id="%s">' % (cls, sid)]
    out.append('  <span class="snum">%02d</span>' % n)
    out.append('  <div class="sbody">')
    if eyebrow: out.append('    <p class="seyebrow">%s</p>' % eyebrow)
    out.append('    <%s class="stitle">%s</%s>' % (h, title, h))
    if dek: out.append('    <p class="sdek">%s</p>' % dek)
    return out, n

def strip(items):
    """items: list of (label, text) — rendered as the persistent source strip."""
    bits = []
    for k, v in items:
        bits.append('<span><b>%s</b> %s</span>' % (k, v))
    return '  </div>\n  <div class="strip">%s</div>\n</section>' % (''.join(bits))

def sid_(*ids):
    return ' '.join('<span class="sid">[%s]</span>' % i for i in ids)

def band(eyebrow, title, dek=None):
    out = ['\n<section class="slide band">']
    out.append('  <div class="sbody">')
    out.append('    <p class="seyebrow">%s</p>' % eyebrow)
    out.append('    <h1 class="stitle">%s</h1>' % title)
    if dek: out.append('    <p class="sdek">%s</p>' % dek)
    out.append('  </div>\n</section>')
    return '\n'.join(out)

def table(headers, rows, cls='', note=None, aligns=None):
    """headers: list of str (prefix '#' for right-align). rows: list of list."""
    o = ['<div class="tw %s"><table>' % cls, '  <thead><tr>']
    for h in headers:
        r = h.startswith('#')
        o.append('    <th%s>%s</th>' % (' class="n"' if r else '', h[1:] if r else h))
    o.append('  </tr></thead>\n  <tbody>')
    for row in rows:
        rc = ''
        if isinstance(row, tuple) and len(row) == 2 and isinstance(row[1], str) and row[1] in ('tot','hl','hl2','dim'):
            row, rc = row[0], row[1]
        o.append('    <tr%s>' % (' class="%s"' % rc if rc else ''))
        for i, c in enumerate(row):
            r = headers[i].startswith('#') if i < len(headers) else False
            o.append('      <td%s>%s</td>' % (' class="n"' if r else '', c))
        o.append('    </tr>')
    o.append('  </tbody></table></div>')
    if note: o.append('<p class="tnote">%s</p>' % note)
    return '\n'.join(o)

def figs(items):
    """items: list of (num, unit, desc, cls)"""
    o = ['<div class="figs">']
    for n, u, d, c in items:
        o.append('  <div class="fig %s"><span class="fn">%s</span><span class="fu">%s</span><span class="fd">%s</span></div>' % (c, n, u, d))
    o.append('</div>')
    return '\n'.join(o)

def cards(items, grid='g3'):
    """items: list of (heading, html_body, cls)"""
    o = ['<div class="%s">' % grid]
    for h, b, c in items:
        o.append('  <div class="card %s"><h4>%s</h4>%s</div>' % (c, h, b))
    o.append('</div>')
    return '\n'.join(o)

def ul(items):
    return '<ul>' + ''.join('<li>%s</li>' % i for i in items) + '</ul>'

def co(label, paras, cls=''):
    return '<div class="co %s"><span class="col">%s</span>%s</div>' % (
        cls, label, ''.join('<p>%s</p>' % p for p in paras))
