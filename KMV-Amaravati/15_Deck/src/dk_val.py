# -*- coding: utf-8 -*-
import re, sys, os, glob
sys.path.insert(0,'/tmp/claude-0/-home-user/a5dd8d44-0929-5495-aca9-31c380eaeac4/scratchpad')
from dk_lib import SOURCES
D='/tmp/claude-0/-home-user/a5dd8d44-0929-5495-aca9-31c380eaeac4/scratchpad/'
R='/home/user/KMV-Spaces/KMV-Amaravati/'
s=open(D+'kmv-deck.html',encoding='utf-8').read()
repo=''
for f in glob.glob(R+'**/*.md', recursive=True):
    repo += open(f,encoding='utf-8').read()

FAIL=[]; OK=[]
def chk(c,m): (OK if c else FAIL).append(m)

# ── 1. structure ──────────────────────────────────────────────
for t in ['<!doctype','<html','<head>','</head>','<body','</body>']:
    chk(t not in s.lower(), 'no %s tag'%t)
m=re.search(r'<title>(.*?)</title>',s); chk(bool(m),'has <title>')
print('TITLE:', m.group(1) if m else '—')
chk(s.find('<title')<8192,'<title> in first 8KB')

nums=re.findall(r'<span class="snum">(\d+)</span>',s)
chk(nums==['%02d'%i for i in range(1,25)],'24 numbered slides in sequence, got %d'%len(nums))
ids=re.findall(r'<section class="slide[^"]*" id="(s\d+)"',s)
chk(ids==['s%02d'%i for i in range(1,25)],'slide ids s01..s24')
apxids=re.findall(r'<section class="apx" id="(apx[A-G])"',s)
chk(apxids==['apx'+c for c in 'ABCDEFG'],'appendices A-G, got %s'%apxids)
bands=len(re.findall(r'class="slide band"',s))
chk(bands>=4,'part dividers present (%d)'%bands)

# nav anchors resolve
nav=re.findall(r'<nav class="nav".*?</nav>',s,re.S)[0]
for href in re.findall(r'href="#([^"]+)"',nav):
    chk(('id="%s"'%href) in s, 'nav anchor #%s resolves'%href)

# ── 2. tag balance ────────────────────────────────────────────
for tag in ['section','div','table','thead','tbody','tr','td','th','ul','li','p','span','nav','footer','h1','h2','h3','h4','b','strong','i','em']:
    o=len(re.findall(r'<%s[ >]'%tag,s)); c=len(re.findall(r'</%s>'%tag,s))
    chk(o==c,'balanced <%s> %d/%d'%(tag,o,c))

# ── 3. table column consistency ───────────────────────────────
bad=[]
for ti,tbl in enumerate(re.findall(r'<table>(.*?)</table>',s,re.S)):
    hd=re.search(r'<thead>(.*?)</thead>',tbl,re.S)
    if not hd: continue
    hrow=re.findall(r'<tr[^>]*>(.*?)</tr>',hd.group(1),re.S)[0]
    ncol=0
    for a in re.findall(r'<th([^>]*)>',hrow):
        mm=re.search(r'colspan="(\d+)"',a); ncol += int(mm.group(1)) if mm else 1
    bd=re.search(r'<tbody>(.*?)</tbody>',tbl,re.S)
    if not bd: continue
    carry=0
    for ri,row in enumerate(re.findall(r'<tr[^>]*>(.*?)</tr>',bd.group(1),re.S)):
        n=carry; newc=0
        for a in re.findall(r'<t[dh]([^>]*)>',row):
            mm=re.search(r'colspan="(\d+)"',a); k=int(mm.group(1)) if mm else 1
            if re.search(r'rowspan="(\d+)"',a): newc+=k
            n+=k
        if n!=ncol: bad.append('table %d row %d: %d cells vs %d cols'%(ti,ri,n,ncol))
        carry=newc
chk(not bad,'table columns consistent; %s'%(bad[:6] or 'all ok'))

# ── 4. CSS classes all defined ────────────────────────────────
css='\n'.join(re.findall(r'<style>(.*?)</style>',s,re.S))
defined=set(re.findall(r'\.([a-zA-Z][\w-]*)',css))
used=set()
for cl in re.findall(r'class="([^"]+)"',s): used.update(cl.split())
chk(not (used-defined),'all CSS classes defined; undefined=%s'%sorted(used-defined))

# ── 5. theme structure ────────────────────────────────────────
chk('prefers-color-scheme: dark' in css,'dark media query')
chk(':root:not([data-theme="light"])' in css,'light-guard on dark media query')
chk(':root[data-theme="dark"]' in css,'explicit dark stamp')
chk(re.search(r'body\{[^}]*background:var\(--paper\)',css) is not None,'body background from token')
def blocks(t,pat):
    out=[]
    for mm in re.finditer(pat,t):
        i=mm.end()-1; d=0
        for j in range(i,len(t)):
            if t[j]=='{': d+=1
            elif t[j]=='}':
                d-=1
                if d==0: out.append(t[mm.start():j+1]); break
    return out
scoped=blocks(css,r'@media[^{]*\{')+blocks(css,r':root\[data-theme[^{]*\{')
base=css
for b in scoped: base=base.replace(b,'')
vs=set(re.findall(r'(--[\w-]+)\s*:', '\n'.join(scoped)))
vb=set(re.findall(r'(--[\w-]+)\s*:', base))
chk(not (vs-vb),'no token defined only inside media/[data-theme]: %s'%sorted(vs-vb))
# tokens used with a fallback (e.g. var(--pz,1)) are set inline per element
with_fb=set(re.findall(r'var\((--[\w-]+)\s*,',css))
undef=set(re.findall(r'var\((--[\w-]+)',css))-vb-vs-with_fb
chk(not undef,'no undefined tokens; %s'%sorted(undef))
chk('--pz' in with_fb and 'style="--pz:' in s,'print page-fit scale set inline per slide, with a fallback')

# ── 6. source IDs ─────────────────────────────────────────────
ids_used=set(re.findall(r'\[(S\d\d)\]',s))
ids_def=set(x[0] for x in SOURCES)
chk(ids_used<=ids_def,'every [Sxx] used is defined; orphans=%s'%sorted(ids_used-ids_def))
chk(len(ids_def)==20,'20 source IDs')
chk(sum(len(x[4]) for x in SOURCES)==40,'40 URLs in register')
# every source id appears in appendix F
apxF=s[s.index('id="apxF"'):s.index('id="apxG"')]
for sid_ in ids_def: chk('[%s]'%sid_ in apxF,'%s listed in Appendix F'%sid_)
# every url in register also exists in the repo source register
srcreg=open(R+'13_Sources/source-register.md',encoding='utf-8').read()
missing_urls=[]
for x in SOURCES:
    for u in x[4]:
        u2=u.replace('&amp;','&')
        if u2 not in srcreg: missing_urls.append(u2)
chk(not missing_urls,'every URL traces to the repo register; missing=%s'%missing_urls[:3])

# ── 7. figures verified against the repository ────────────────
FIG = ['₹31.75','₹23.80','₹14.65','₹4.04','₹3.15','₹0.76','₹1.90','₹21.90','₹25.33','26.86','₹33.28','34.81',
 '8.85','9.26','₹6.33','₹8.44','₹11.32','₹9.84','₹9.5 L',
 '6,573,000','78,880','35,496','19,523','12,474','2,922','574','409','376','169','84','60','63',
 '₹1,247','₹7,889','₹33,676','₹1,71,429','₹1,672','₹10,576','₹45,144','2,29,810','₹4.90 L',
 '2.65','2.99','3.47','3.95','1.16','3.09','5.86','16.0','84 units',
 '194','346','572','₹240.9','₹466.2','₹793.6','₹16.09','₹9.23','₹5.66',
 '₹4.26','₹9.47','₹3.78','₹6.28','₹11.28','46.3','₹40.5','32.6','1,443','228','3.7','832',
 '4,062','5,150','5,700','6,500','7,200','5,100','6,098','₹268','₹39.4','₹552.6','4.70','6.27','8.40',
 '17.6','74.1','₹126.2','₹112.5','₹109.2','₹158.8','₹41.5','₹50.7','₹17.2','₹10.25','₹12.63','₹11.02',
 '4.20','4.05','3.90','3.20','2.95','2.45','₹1,550','₹42,000','₹1,900','₹52,000','15.81','10,143','₹3.75']
miss=[f for f in FIG if f not in s]
chk(not miss,'all %d key figures present in deck; missing=%s'%(len(FIG),miss))
mrepo=[f for f in FIG if f not in repo]
chk(not mrepo,'all key figures traceable to repo markdown; missing=%s'%mrepo)

# ── 8. arithmetic ─────────────────────────────────────────────
chk(abs(23.80+4.04+3.15+0.76-31.75)<1e-9,'23.80+4.04+3.15+0.76 = 31.75')
chk(abs(0.25+2.60+4.20+8.10+5.05+1.70-21.90)<1e-9,'tranches sum to 21.90')
chk(abs(21.90+1.90-23.80)<1e-9,'core+reserve = 23.80')
chk(abs(4.26+9.47+3.78+6.28-23.79)<0.02,'community opex sums to ~23.80')
chk(abs(126.2+112.5+109.2+158.8-506.7)<0.05,'community revenue sums to 506.7')
chk(169+84+60+63==376,'unit counts sum to 376')
chk(abs(376/25.0-15.04)<0.05,'376/25 acres = 15.0/acre')
chk(abs(9.84e7/78880-1247)<2,'CPL = 9.84Cr/78,880')
chk(abs(9.84e7/12474-7889)<3,'CPQL = 9.84Cr/12,474')
chk(abs(9.84e7/2922-33676)<10,'CPQSV = 9.84Cr/2,922 held visits')
chk(abs(9.84e7/4870-20205)<15,'cost per booked visit = 9.84Cr/4,870')
chk(abs(2922/0.60-4870)<1,'4,870 booked x 60% show = 2,922 held')
chk(abs(2922/12474*100-23.4)<0.05,'2,922/12,474 = 23.4%')
chk(abs(574/2922*100-19.6)<0.1,'574/2,922 = 19.6%')
chk(abs(376/0.92-409)<1,'376 net / 0.92 = 409 gross')
chk(abs(23.80e7/376-6.33e5)<3e3,'opex/376 = 6.33 L')
chk(abs(31.75e7/376-8.44e5)<3e3,'total/376 = 8.44 L')
chk(abs(14.65/23.80*100-61.6)<1.0,'media ~62% of opex')
chk(abs(14.65/31.75*100-46.1)<0.5,'media ~46% of total')
chk(abs(14.65e7/45-32.56e5)<2e4,'media/45mo = ~32.6 L per month')
chk(abs(0.25/23.80*100-1.05)<0.1,'0.25/23.80 = ~1.0% of opex')
chk(abs(0.25/31.75*100-0.79)<0.05,'0.25/31.75 = ~0.8% of headline')
chk(abs(2922/(45*4.33)-15.0)<0.1,'2,922 held visits = 15.0/week over 45 months')
chk(abs(506.7-466.2-40.5)<0.05,'cancellation shortfall = 40.5 Cr')
chk(abs(793.6-240.9-552.7)<0.2,'scenario spread = 552.6 Cr')
chk(abs(11.32/8.44-1.341)<0.005,'CAC headroom 1.34x')
chk(abs(506.7*0.28-141.9)<0.1,'gross profit @28% = 141.9 Cr')
chk(abs(((141.9-31.75)/31.75)-3.47)<0.02,'ROMI 3.47x = (141.9-31.75)/31.75')
chk(abs(506.7/31.75-15.96)<0.1,'revenue/spend would read ~16.0x')
chk(abs(18.00+7.00-25.00)<1e-9,'25L test: 18 media + 7 non-media')
chk(abs(6.30+5.40+3.60+1.80+0.90-18.00)<1e-9,'test media lines sum to 18.00 L')
chk(abs(2.50+2.20+1.50+0.80-7.00)<1e-9,'test non-media lines sum to 7.00 L')
chk(abs(2.5+4.0+3.5+12.0+17.5+2.0-41.5)<1e-9,'gap actions sum to 41.5 L')
chk(abs(41.5/3175*100-1.307)<0.02,'41.5 L = 1.3% of 31.75 Cr')

# ── 9. language rules ─────────────────────────────────────────
BAN = ['as an AI','according to Claude','generated using Claude','I researched this with AI',
       'I have managed','I have delivered','KMV should spend','KMV will ','KMV has ',
       'Currently KMV spends','Chief Marketing Officer','CMO strategy','CMO framework',
       'executive-level strategy','real estate companies spend','industry standard is']
hit=[b for b in BAN if b.lower() in s.lower()]
chk(not hit,'no banned phrases; found=%s'%hit)
chk('CMO' not in s,'no CMO designation anywhere in the deck')
chk('Marketing lead' in s,'governance roles named neutrally')
chk(s.count('I would')>=15,'first-person conditional voice used throughout (%d)'%s.count('I would'))
chk('Prepared by' in s and 'Kiran Basa' in s,'attribution present')
chk('Mr. Anudeep' in s,'submitted-to present')
chk(s.count('Kiran Basa')>=3,'Kiran Basa named on cover, close and appendix G')

# ── 10. budget framing rules ──────────────────────────────────
chk('is not a marketing budget' in s,'31.75 explicitly framed as NOT a marketing budget')
chk('planning ceiling' in s.lower(),'31.75 framed as a planning ceiling')
chk('validation tranche' in s or 'validation investment' in s or 'Validation' in s,'25L framed as validation')
chk('NOT MEASURABLE' in s and '±102%' in s,'booking rate stated as not measurable at the test sample')
chk('gross profit, never on revenue' in s or 'not revenue' in s or 'on gross profit' in s,'ROMI on gross profit')
chk('Diagnostic only' in s,'ROAS marked diagnostic only')
chk('Meaningless' in s or 'meaningless' in s,'revenue/spend called out')

# ── 11. evidence labels present and used ──────────────────────
for lab,name in [('lab-g','Assignment assumption'),('lab-r','Researched'),('lab-d','Derived calculation'),('lab-w','Working assumption')]:
    chk(lab in s,'label %s (%s) used'%(lab,name))
strips=len(re.findall(r'<div class="strip">',s))
chk(strips==23,'source strip on all 23 content slides (cover excluded), got %d'%strips)

# ── 12. hypothetical / no-KMV-confirmation discipline ─────────
chk('has been confirmed by KMV' in s,'explicit no-KMV-confirmation statement')
chk(s.count('requires KMV validation')+s.count('Requires KMV validation')+s.count('Requires validation')+s.count('requires validation')>=6,
    'validation-required flagged repeatedly')
chk('Proposed positioning architecture' in s,'community architecture framed as proposed, not confirmed')
chk('Not found' in s,'gaps named as not found')

print('\n'.join('  ok  '+o for o in OK if o))
print()
if FAIL: print('\n'.join('FAIL  '+f for f in FAIL))
print('\n%d passed, %d failed'%(len([o for o in OK if o]),len(FAIL)))
