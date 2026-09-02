import asyncio, os, re, json
from playwright.async_api import async_playwright
CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
def wrap(src):
    return ('<!doctype html><html><head><meta charset="utf-8">'
     '<meta name="viewport" content="width=device-width,initial-scale=1">'
     '<style>:root{color-scheme:light}body{margin:0;font:14px system-ui;background:#faf9f7}'
     'img{max-width:100%}[hidden]{display:none!important}</style></head><body>'+src+'</body></html>')
async def measure(path):
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path=CHROME,args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':1278,'height':718})
        await pg.goto('file://'+os.path.abspath(path))
        await pg.emulate_media(media='print'); await pg.wait_for_timeout(2200)
        r=await pg.evaluate("""()=>{const P=190/25.4*96;const o={};
          document.querySelectorAll('.slide[id]').forEach(el=>{o[el.id]=el.getBoundingClientRect().height;});
          return {P, o};}""")
        await b.close(); return r
async def main():
    src=open('kmv-deck.html',encoding='utf-8').read()
    open('deck-preview.html','w',encoding='utf-8').write(wrap(src))
    r=await measure('deck-preview.html'); P=r['P']
    zooms={}
    for sid,h in r['o'].items():
        z=1.0 if h<=P-4 else round((P-6)/h,3)
        zooms[sid]=max(z,0.55)
    out=re.sub(r'\s+style="--pz:[^"]*"','',src)
    def inject(m):
        sid=m.group(2); z=zooms.get(sid,1.0)
        if z>=0.999: return m.group(0)
        return '<section class="slide %s" id="%s" style="--pz:%.3f">'%(m.group(1),sid,z)
    out=re.sub(r'<section class="slide ([^"]*)" id="(s\d+)">', inject, out)
    open('kmv-deck.html','w',encoding='utf-8').write(out)
    open('deck-preview.html','w',encoding='utf-8').write(wrap(out))
    scaled={k:v for k,v in zooms.items() if v<0.999}
    print('slides scaled for print:',len(scaled),'| range %.2f-%.2f'%(min(scaled.values()),max(scaled.values())) if scaled else '')
    r2=await measure('deck-preview.html')
    over=[(k,round(v)) for k,v in r2['o'].items() if v>r2['P']+2]
    print('still over one page:',over or 'none')
asyncio.run(main())
