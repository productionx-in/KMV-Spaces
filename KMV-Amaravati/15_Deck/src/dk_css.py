# -*- coding: utf-8 -*-
CSS = r'''<title>Fifteen to the Acre</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600;6..72,700&display=swap">
<style>
/* ============ tokens : light is the base, complete ============ */
:root{
  --paper:#F5F5F1; --surface:#FFFFFF; --surface-2:#EFEFE9; --surface-3:#E7E8E0;
  --ink:#16191B; --ink-2:#4C5459; --ink-3:#7C858A; --ink-4:#9BA3A7;
  --rule:#E0E1DA; --rule-2:#CACCC2; --rule-3:#B4B7AB;
  --evidence:#2C5164;      /* slate : researched, external, factual */
  --evidence-soft:#E4EAEE;
  --decision:#B06A18;      /* ochre : decision, gate, risk, the ask */
  --decision-soft:#F6EADA;
  --derived:#5E6A57;       /* olive : our own arithmetic */
  --derived-soft:#E7EBE4;
  --given:#5A4A6B;         /* plum : handed to me by the assignment */
  --given-soft:#EDE8F1;
  --band:#1B1F21;          /* dark divider slides */
  --band-ink:#F5F5F1;
  --shadow:0 1px 2px rgba(20,24,26,.05), 0 6px 18px -8px rgba(20,24,26,.10);
  --f-d:"Newsreader",ui-serif,Georgia,"Times New Roman",serif;
  --f-b:"Archivo",system-ui,-apple-system,"Segoe UI",sans-serif;
  --f-m:"IBM Plex Mono",ui-monospace,"SFMono-Regular",Menlo,monospace;
  --measure:74ch;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --paper:#101315; --surface:#191D1F; --surface-2:#1F2426; --surface-3:#262B2E;
    --ink:#EDEEE9; --ink-2:#B6BCBE; --ink-3:#8B9396; --ink-4:#6C7478;
    --rule:#2B3134; --rule-2:#3A4145; --rule-3:#4A5257;
    --evidence:#7FB0CB; --evidence-soft:#1B2A33;
    --decision:#DE9A46; --decision-soft:#33261492;
    --derived:#9BAE92; --derived-soft:#1E2620;
    --given:#B79FCB; --given-soft:#241E2B;
    --band:#000000; --band-ink:#EDEEE9;
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 6px 20px -8px rgba(0,0,0,.6);
  }
}
:root[data-theme="dark"]{
  --paper:#101315; --surface:#191D1F; --surface-2:#1F2426; --surface-3:#262B2E;
  --ink:#EDEEE9; --ink-2:#B6BCBE; --ink-3:#8B9396; --ink-4:#6C7478;
  --rule:#2B3134; --rule-2:#3A4145; --rule-3:#4A5257;
  --evidence:#7FB0CB; --evidence-soft:#1B2A33;
  --decision:#DE9A46; --decision-soft:#332614;
  --derived:#9BAE92; --derived-soft:#1E2620;
  --given:#B79FCB; --given-soft:#241E2B;
  --band:#000000; --band-ink:#EDEEE9;
  --shadow:0 1px 2px rgba(0,0,0,.4), 0 6px 20px -8px rgba(0,0,0,.6);
}

*,*::before,*::after{box-sizing:border-box}
body{background:var(--paper);color:var(--ink);font-family:var(--f-b);
  font-size:16px;line-height:1.55;-webkit-font-smoothing:antialiased;
  font-feature-settings:"kern" 1;margin:0}
:focus-visible{outline:2px solid var(--decision);outline-offset:2px;border-radius:2px}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important;scroll-behavior:auto!important}}

/* ============ deck frame ============ */
.deck{max-width:1180px;margin:0 auto;padding:1.6rem 1.1rem 4rem}
.slide{background:var(--surface);border:1px solid var(--rule);border-radius:3px;
  box-shadow:var(--shadow);margin:0 0 1.15rem;padding:2.5rem 2.7rem 1.1rem;
  position:relative;display:flex;flex-direction:column;min-height:33.5rem;scroll-margin-top:3.1rem}
.slide.band{background:var(--band);border-color:var(--band);color:var(--band-ink);min-height:16rem;justify-content:center}
.slide.cover{min-height:41rem;justify-content:center}
.slide.tight{min-height:0}
.sbody{flex:1;display:flex;flex-direction:column;min-width:0}

/* slide chrome : the plot number, the eyebrow, the one idea */
.snum{position:absolute;top:1.15rem;right:1.5rem;font-family:var(--f-m);font-size:.66rem;
  letter-spacing:.14em;color:var(--ink-4);font-variant-numeric:tabular-nums}
.slide.band .snum{color:var(--ink-3);opacity:.7}
.seyebrow{font-family:var(--f-m);font-size:.63rem;letter-spacing:.19em;text-transform:uppercase;
  color:var(--ink-3);margin:0 0 .7rem}
.slide.band .seyebrow{color:var(--decision)}
h1.stitle{font-family:var(--f-d);font-weight:600;font-size:clamp(1.7rem,3.5vw,2.45rem);
  line-height:1.12;letter-spacing:-.017em;margin:0 0 .35rem;text-wrap:balance;color:var(--ink)}
.slide.band h1.stitle{color:var(--band-ink);font-size:clamp(1.9rem,4.4vw,3rem)}
h2.stitle{font-family:var(--f-d);font-weight:600;font-size:clamp(1.45rem,2.9vw,2.05rem);
  line-height:1.15;letter-spacing:-.015em;margin:0 0 .3rem;text-wrap:balance;color:var(--ink)}
.sdek{font-size:.95rem;line-height:1.5;color:var(--ink-2);margin:0 0 1.35rem;max-width:64ch}
.sdek strong{color:var(--ink);font-weight:600}
.slide.band .sdek{color:var(--band-ink);opacity:.72;max-width:60ch}

/* ============ the source strip : present on every content slide ============ */
.strip{margin-top:auto;padding-top:.85rem;border-top:1px solid var(--rule);
  display:flex;flex-wrap:wrap;gap:.4rem .9rem;align-items:baseline;
  font-family:var(--f-m);font-size:.63rem;line-height:1.6;color:var(--ink-3)}
.strip b{font-weight:500;color:var(--ink-2)}
.strip .sid{color:var(--evidence);font-weight:500}

/* ============ evidence-label chips ============ */
.lab{font-family:var(--f-m);font-size:.575rem;font-weight:600;letter-spacing:.09em;
  text-transform:uppercase;padding:.14rem .42rem;border-radius:2px;display:inline-block;
  white-space:nowrap;vertical-align:.06em;border:1px solid transparent}
.lab-g{background:var(--given-soft);color:var(--given);border-color:var(--given)}
.lab-r{background:var(--evidence-soft);color:var(--evidence);border-color:var(--evidence)}
.lab-d{background:var(--derived-soft);color:var(--derived);border-color:var(--derived)}
.lab-w{background:var(--decision-soft);color:var(--decision);border-color:var(--decision)}

/* ============ generic type ============ */
.slide p{margin:0 0 .75rem;max-width:var(--measure)}
.slide p:last-child{margin-bottom:0}
.slide strong{font-weight:600;color:var(--ink)}
.slide em{font-style:italic}
h3.sh{font-family:var(--f-b);font-size:.7rem;font-weight:600;letter-spacing:.15em;
  text-transform:uppercase;color:var(--ink-3);margin:1.5rem 0 .6rem}
h3.sh:first-child{margin-top:0}
.lede{font-family:var(--f-d);font-size:1.22rem;line-height:1.42;color:var(--ink);
  font-weight:400;margin:0 0 1.1rem;max-width:58ch;text-wrap:balance}
.big{font-family:var(--f-d);font-size:clamp(1.35rem,2.7vw,1.85rem);line-height:1.28;
  font-weight:500;letter-spacing:-.012em;color:var(--ink);margin:0;text-wrap:balance;max-width:30ch}
.slide.band .big{color:var(--band-ink)}
.fine{font-size:.8rem;line-height:1.5;color:var(--ink-3);max-width:70ch}
.fine strong{color:var(--ink-2)}
code,.mono{font-family:var(--f-m);font-size:.9em;color:var(--ink-2)}

/* ============ tables ============ */
.tw{overflow-x:auto;margin:0 0 1rem;border:1px solid var(--rule);border-radius:3px;background:var(--surface)}
table{border-collapse:collapse;width:100%;font-size:.8rem;line-height:1.42}
thead th{background:var(--surface-2);font-family:var(--f-m);font-size:.6rem;font-weight:500;
  letter-spacing:.1em;text-transform:uppercase;color:var(--ink-3);text-align:left;
  padding:.5rem .7rem;border-bottom:1px solid var(--rule-2);white-space:nowrap;vertical-align:bottom}
tbody td{padding:.44rem .7rem;border-bottom:1px solid var(--rule);color:var(--ink-2);vertical-align:top}
tbody tr:last-child td{border-bottom:0}
td.n,th.n{text-align:right;font-family:var(--f-m);font-variant-numeric:tabular-nums;white-space:nowrap}
td strong{color:var(--ink)}
tr.tot td{background:var(--surface-2);border-top:1px solid var(--rule-2);color:var(--ink)}
tr.hl td{background:var(--decision-soft)}
tr.hl2 td{background:var(--evidence-soft)}
tr.dim td{color:var(--ink-3)}
.tnote{font-family:var(--f-m);font-size:.63rem;line-height:1.55;color:var(--ink-3);margin:-.5rem 0 1rem}

/* ============ column grids ============ */
.g2{display:grid;grid-template-columns:repeat(auto-fit,minmax(17rem,1fr));gap:1.1rem}
.g3{display:grid;grid-template-columns:repeat(auto-fit,minmax(13rem,1fr));gap:.85rem}
.g4{display:grid;grid-template-columns:repeat(auto-fit,minmax(10.5rem,1fr));gap:.75rem}
.gsplit{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);gap:1.6rem;align-items:start}

/* ============ card ============ */
.card{border:1px solid var(--rule);border-radius:3px;background:var(--surface);padding:.85rem 1rem}
.card.q{background:var(--surface-2)}
.card h4{font-family:var(--f-m);font-size:.6rem;font-weight:600;letter-spacing:.12em;
  text-transform:uppercase;color:var(--evidence);margin:0 0 .5rem}
.card.warn{border-color:var(--decision)} .card.warn h4{color:var(--decision)}
.card.calc{border-color:var(--rule-2)} .card.calc h4{color:var(--derived)}
.card p{font-size:.83rem;line-height:1.5;margin:0 0 .5rem;max-width:none}
.card ul{margin:0;padding-left:.95rem;font-size:.83rem;line-height:1.5;color:var(--ink-2)}
.card li{margin:0 0 .34rem} .card li:last-child{margin-bottom:0}
.card li::marker{color:var(--ink-4)}

/* ============ the big number ============ */
.figs{display:grid;grid-template-columns:repeat(auto-fit,minmax(9.5rem,1fr));gap:.75rem;margin:0 0 1.1rem}
.fig{border:1px solid var(--rule);border-radius:3px;background:var(--surface);padding:.85rem .95rem}
.fig.key{border-color:var(--decision);background:var(--decision-soft)}
.fig.ev{border-color:var(--evidence)}
.fig .fn{font-family:var(--f-d);font-weight:600;font-size:1.95rem;line-height:1;letter-spacing:-.028em;
  color:var(--ink);font-variant-numeric:tabular-nums;display:block}
.fig.key .fn{color:var(--decision)}
.fig.ev .fn{color:var(--evidence)}
.fig .fu{font-family:var(--f-m);font-size:.575rem;letter-spacing:.11em;text-transform:uppercase;
  color:var(--ink-3);display:block;margin:.4rem 0 .35rem}
.fig .fd{font-size:.775rem;line-height:1.42;color:var(--ink-2)}
.fig .fd b{color:var(--ink);font-weight:600}

/* ============ callout ============ */
.co{border-left:2px solid var(--decision);background:var(--surface-2);padding:.8rem 1rem;
  border-radius:0 3px 3px 0;margin:0 0 1rem}
.co.ev{border-left-color:var(--evidence)}
.co.calc{border-left-color:var(--derived)}
.co .col{font-family:var(--f-m);font-size:.6rem;font-weight:600;letter-spacing:.12em;
  text-transform:uppercase;color:var(--decision);display:block;margin-bottom:.35rem}
.co.ev .col{color:var(--evidence)} .co.calc .col{color:var(--derived)}
.co p{font-size:.86rem;line-height:1.52;margin:0 0 .45rem;max-width:none}
.co p:last-child{margin-bottom:0}

/* ============ funnel ============ */
.fn-l{display:flex;flex-direction:column;gap:.16rem}
.fn-r{display:grid;grid-template-columns:minmax(6.4rem,8.4rem) minmax(0,1fr) 4.6rem;gap:.6rem;align-items:center}
.fn-k{font-size:.775rem;line-height:1.24;color:var(--ink-2);text-align:right}
.fn-k b{display:block;color:var(--ink);font-weight:600}
.fn-b{height:1.55rem;background:var(--evidence);border-radius:0 2px 2px 0;
  display:flex;align-items:center;padding:0 .5rem;color:var(--surface);
  font-family:var(--f-m);font-size:.7rem;font-variant-numeric:tabular-nums;min-width:2.6rem}
.fn-b.warm{background:var(--decision)}
.fn-b.pale{background:var(--evidence-soft);color:var(--evidence);border:1px solid var(--evidence)}
.fn-c{font-family:var(--f-m);font-size:.66rem;color:var(--ink-3);font-variant-numeric:tabular-nums;text-align:right}
.fn-c b{color:var(--decision);font-weight:500}

/* ============ tranche ladder ============ */
.tr{display:grid;grid-template-columns:minmax(7.5rem,10.5rem) minmax(0,1fr) 5.4rem;
  gap:.65rem;align-items:center;padding:.32rem 0;border-bottom:1px solid var(--rule)}
.tr:last-child{border-bottom:0}
.tr-k{font-size:.79rem;line-height:1.26;color:var(--ink-2)}
.tr-k b{display:block;color:var(--ink);font-weight:600}
.tr-t{height:1.35rem;display:flex;align-items:center}
.tr-f{height:1.05rem;background:var(--evidence);border-radius:0 2px 2px 0}
.tr-f.now{background:var(--decision)}
.tr-f.res{background:transparent;border:1.5px dashed var(--rule-3);box-sizing:border-box}
.tr-v{font-family:var(--f-m);font-size:.76rem;font-variant-numeric:tabular-nums;text-align:right;color:var(--ink)}
.tr-v i{font-style:normal;color:var(--ink-3)}

/* ============ gate flow ============ */
.gate{display:grid;grid-template-columns:repeat(auto-fit,minmax(8.2rem,1fr));gap:.55rem}
.gt{border:1px solid var(--rule);border-radius:3px;padding:.7rem .8rem;background:var(--surface);position:relative}
.gt.now{border-color:var(--decision);background:var(--decision-soft)}
.gt .gn{font-family:var(--f-m);font-size:.58rem;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-3);display:block}
.gt.now .gn{color:var(--decision)}
.gt .gv{font-family:var(--f-m);font-size:1.02rem;font-weight:600;color:var(--ink);display:block;margin:.28rem 0 .3rem;font-variant-numeric:tabular-nums}
.gt .gd{font-size:.73rem;line-height:1.38;color:var(--ink-2)}

/* ============ diagnostic ladder (if/then) ============ */
.dx{display:flex;flex-direction:column;gap:.4rem}
.dxr{display:grid;grid-template-columns:minmax(0,1fr) 1.4rem minmax(0,1fr);gap:.5rem;align-items:center;
  border:1px solid var(--rule);border-radius:3px;background:var(--surface);padding:.6rem .8rem}
.dxr .if{font-size:.81rem;line-height:1.4;color:var(--ink-2)} .dxr .if b{color:var(--ink);font-weight:600}
.dxr .ar{font-family:var(--f-m);color:var(--decision);text-align:center;font-size:.9rem}
.dxr .th{font-size:.81rem;line-height:1.4;color:var(--ink-2)} .dxr .th b{color:var(--ink);font-weight:600}

/* ============ operating-model chain ============ */
.chain{display:flex;flex-wrap:wrap;gap:.3rem;align-items:stretch;margin:0 0 1rem}
.ch{border:1px solid var(--rule);border-radius:2px;background:var(--surface);padding:.4rem .55rem;
  font-family:var(--f-m);font-size:.66rem;color:var(--ink-2);display:flex;align-items:center;flex:1 1 auto;
  justify-content:center;text-align:center;min-width:5rem}
.ch.mk{border-color:var(--evidence);color:var(--evidence);background:var(--evidence-soft)}
.ch.sa{border-color:var(--decision);color:var(--decision);background:var(--decision-soft)}

/* ============ matrix ============ */
.mx{overflow-x:auto;border:1px solid var(--rule);border-radius:3px}
.mx table{font-size:.755rem}
.mx thead th{background:var(--surface-2)}
.mx td:first-child{font-weight:600;color:var(--ink);background:var(--surface-2);white-space:nowrap}

/* ============ cover ============ */
.cover-mark{font-family:var(--f-m);font-size:.66rem;letter-spacing:.24em;text-transform:uppercase;
  color:var(--ink-3);margin:0 0 2.2rem}
.cover h1{font-family:var(--f-d);font-weight:600;font-size:clamp(2.3rem,6.2vw,4.1rem);line-height:1.03;
  letter-spacing:-.028em;margin:0 0 1rem;color:var(--ink);text-wrap:balance;max-width:19ch}
.cover .csub{font-family:var(--f-d);font-size:clamp(1.05rem,2.4vw,1.4rem);line-height:1.4;color:var(--ink-2);
  font-weight:400;margin:0 0 2.4rem;max-width:44ch}
.cmeta{display:grid;grid-template-columns:repeat(auto-fit,minmax(11rem,1fr));gap:1rem 1.6rem;
  padding-top:1.4rem;border-top:1px solid var(--rule-2);max-width:52rem}
.cmeta div{font-size:.85rem;line-height:1.45;color:var(--ink-2)}
.cmeta .ck{font-family:var(--f-m);font-size:.58rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--ink-3);display:block;margin-bottom:.28rem}
.cmeta b{color:var(--ink);font-weight:600}
.disc{margin-top:1.6rem;padding:.85rem 1rem;background:var(--surface-2);border-left:2px solid var(--rule-3);
  font-size:.79rem;line-height:1.55;color:var(--ink-2);max-width:60rem;border-radius:0 3px 3px 0}
.disc strong{color:var(--ink)}

/* ============ nav rail ============ */
.nav{position:sticky;top:0;z-index:30;background:var(--paper);border-bottom:1px solid var(--rule);
  margin:-1.6rem -1.1rem 1.15rem;padding:.5rem 1.1rem}
.nav-in{max-width:1180px;margin:0 auto;display:flex;gap:.7rem;align-items:center;
  overflow-x:auto;scrollbar-width:thin}
.nav a{font-family:var(--f-m);font-size:.63rem;letter-spacing:.06em;color:var(--ink-3);
  text-decoration:none;white-space:nowrap;padding:.22rem .1rem;border-bottom:1.5px solid transparent}
.nav a:hover{color:var(--decision);border-bottom-color:var(--decision)}
.nav .nb{color:var(--ink);font-weight:500}

/* ============ appendix ============ */
.apx{background:var(--surface);border:1px solid var(--rule);border-radius:3px;
  padding:1.9rem 2.1rem;margin:0 0 1.15rem;scroll-margin-top:3.1rem}
.apx h2{font-family:var(--f-d);font-size:1.5rem;font-weight:600;margin:0 0 .25rem;letter-spacing:-.012em;color:var(--ink)}
.apx .ax{font-family:var(--f-m);font-size:.62rem;letter-spacing:.17em;text-transform:uppercase;
  color:var(--decision);margin:0 0 .55rem}
.apx .sdek{margin-bottom:1.2rem}
.srcrow td:first-child{font-family:var(--f-m);font-weight:500;color:var(--evidence);white-space:nowrap}
.url{font-family:var(--f-m);font-size:.66rem;word-break:break-all;color:var(--ink-3);line-height:1.45}

/* ============ close ============ */
.close{padding:2.4rem 0 0;border-top:1px solid var(--rule);margin-top:.6rem;
  font-size:.79rem;line-height:1.6;color:var(--ink-3);max-width:74ch}
.close strong{color:var(--ink-2)}

/* ============ responsive ============ */
@media (max-width:820px){
  .slide{padding:1.7rem 1.25rem .9rem;min-height:0}
  .slide.cover{min-height:0;padding:2.2rem 1.25rem}
  .apx{padding:1.4rem 1.25rem}
  .gsplit{grid-template-columns:minmax(0,1fr);gap:1.1rem}
  .fn-r{grid-template-columns:minmax(4.7rem,6rem) minmax(0,1fr) 3.5rem;gap:.4rem}
  .fn-k{font-size:.7rem}
  .tr{grid-template-columns:minmax(0,1fr) 5rem;row-gap:.2rem}
  .tr-t{grid-column:1 / -1}
  .dxr{grid-template-columns:minmax(0,1fr);row-gap:.3rem}
  .dxr .ar{text-align:left}
  .deck{padding:1.1rem .55rem 3rem}
  .nav{margin:-1.1rem -.55rem 1.1rem;padding:.45rem .55rem}
}

/* ============ print / PDF : one slide per page, 16:9 ============ */
@media print{
  @page{size:338mm 190mm;margin:0}
  body{background:#fff;color:#16191B}
  .nav{display:none}
  .deck{max-width:none;padding:0;margin:0}
  .slide,.apx{break-after:page;page-break-after:always;break-inside:avoid;
    margin:0;border:0;border-radius:0;box-shadow:none;min-height:190mm;
    padding:10mm 13mm 7mm;background:#fff}
  /* each slide is scaled at build time to land on exactly one page */
  .slide{zoom:var(--pz,1)}
  .slide.band{zoom:1}
  .slide.band{background:#1B1F21;-webkit-print-color-adjust:exact;print-color-adjust:exact}
  .apx{break-inside:auto;page-break-inside:auto;min-height:0}
  .close{break-after:auto;page-break-after:auto}
  *{-webkit-print-color-adjust:exact;print-color-adjust:exact}
}
</style>
'''
