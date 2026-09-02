import asyncio, os
from playwright.async_api import async_playwright
SRC=open('kmv-deck.html',encoding='utf-8').read()
PAGE=('<!doctype html><html><head><meta charset="utf-8">'
 '<meta name="viewport" content="width=device-width,initial-scale=1">'
 '<style>:root{color-scheme:light}body{margin:0;font:14px system-ui;background:#faf9f7}'
 'img{max-width:100%}[hidden]{display:none!important}</style></head><body>'+SRC+'</body></html>')
open('deck-preview.html','w',encoding='utf-8').write(PAGE)
CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path=CHROME,args=['--no-sandbox'])
        for w,h,tag in [(1440,900,'desk'),(390,844,'mob')]:
            pg=await b.new_page(viewport={'width':w,'height':h})
            errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
            await pg.goto('file://'+os.path.abspath('deck-preview.html'))
            await pg.wait_for_timeout(1800)
            res=await pg.evaluate("""()=>{
              const de=document.documentElement,out=[];
              document.querySelectorAll('*').forEach(el=>{
                const st=getComputedStyle(el);
                if(['auto','scroll','hidden'].includes(st.overflowX))return;
                const r=el.getBoundingClientRect();
                if(r.right<=de.clientWidth+0.5&&r.left>=-0.5)return;
                let p=el.parentElement,g=false;
                while(p&&p!==document.body){const ps=getComputedStyle(p);
                  if(['auto','scroll','hidden'].includes(ps.overflowX)){g=true;break;}p=p.parentElement;}
                if(!g)out.push(el.tagName+'.'+(el.className||'').toString().slice(0,38)+' r='+Math.round(r.right));
              });
              // text clipped by a fixed-height ancestor
              const clip=[];
              document.querySelectorAll('.slide,.apx,.card,.fig,.co,.gt,.dxr').forEach(el=>{
                if(el.scrollHeight>el.clientHeight+2 && getComputedStyle(el).overflowY!=='auto')
                  clip.push(el.className+' '+el.scrollHeight+'>'+el.clientHeight);
              });
              return {sw:de.scrollWidth,cw:de.clientWidth,h:document.body.scrollHeight,
                      slides:document.querySelectorAll('.slide').length,
                      apx:document.querySelectorAll('.apx').length,
                      tables:document.querySelectorAll('table').length,
                      overflow:[...new Set(out)].slice(0,8),clipped:[...new Set(clip)].slice(0,8)};
            }""")
            print(tag,res)
            if errs: print('  JS ERRORS:',errs[:3])
            await pg.close()
        # PDF export : 16:9 pages
        pg=await b.new_page(viewport={'width':1400,'height':790})
        await pg.goto('file://'+os.path.abspath('deck-preview.html'))
        await pg.wait_for_timeout(2500)
        await pg.emulate_media(media='print')
        await pg.pdf(path='kmv-deck.pdf',width='338mm',height='190mm',
                     print_background=True,margin={'top':'0','bottom':'0','left':'0','right':'0'})
        print('pdf written')
        await b.close()
asyncio.run(main())
