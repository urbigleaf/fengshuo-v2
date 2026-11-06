# -*- coding: utf-8 -*-
import io, os
ROOT = r'D:\user\Documents\GitHub\fengshuo_v1'
css = r'''
/* ---- artwork detail ---- */
.detail{display:grid;gap:clamp(24px,4vw,64px);align-items:start;
  grid-template-columns:minmax(0,1.55fr) minmax(0,.85fr)}
@media (max-width:900px){ .detail{grid-template-columns:1fr} }
.detail__stage{position:relative}
.detail__img{
  width:100%;height:auto;max-height:min(82svh,940px);object-fit:contain;
  background:var(--surface);box-shadow:0 30px 80px -40px rgba(0,0,0,.7)}
.detail__side{position:sticky;top:96px;display:flex;flex-direction:column;gap:1.4em}
@media (max-width:900px){ .detail__side{position:static} }
.detail__zh{
  margin:0;font-family:var(--font-display);font-weight:400;
  font-size:clamp(1.7rem,4vw,2.6rem);line-height:1.08;letter-spacing:.02em}
.detail__en{
  margin:.3em 0 0;font-size:.76rem;letter-spacing:.2em;text-transform:uppercase;
  color:var(--text-muted)}
.dl{display:grid;grid-template-columns:auto 1fr;gap:.55em 1.4em;margin:0;
  padding-top:1.2em;border-top:1px solid var(--line);font-size:.82rem}
.dl dt{color:var(--text-muted);letter-spacing:.1em;text-transform:uppercase;font-size:.7rem;
  padding-top:.16em}
.dl dd{margin:0;font-variant-numeric:tabular-nums}
.pager{display:flex;justify-content:space-between;gap:12px;margin-top:1.2em;
  padding-top:1.1em;border-top:1px solid var(--line)}
.pager a{
  display:flex;align-items:center;gap:.55em;font-size:.74rem;letter-spacing:.1em;
  text-transform:uppercase;color:var(--text-muted);max-width:46%;
  transition:color .3s var(--ease)}
.pager a:hover{color:var(--text)}
.pager a svg{width:15px;height:15px;flex:0 0 auto}
.pager a span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.pager__next{margin-left:auto;text-align:right}

/* ---- prose (essays) ---- */
.prose{max-width:74ch}
.prose > * + *{margin-top:1.05em}
.prose p{margin:0;font-size:clamp(.92rem,1.55vw,1.04rem);line-height:1.82;color:var(--text)}
.prose h2,.prose h3{
  font-family:var(--font-display);font-weight:400;line-height:1.2;letter-spacing:.01em;
  margin-top:2.1em}
.prose h2{font-size:clamp(1.25rem,2.6vw,1.75rem)}
.prose h3{font-size:clamp(1.05rem,2.1vw,1.3rem)}
.prose blockquote{
  margin:2em 0;padding-left:1.3em;border-left:2px solid var(--accent);
  font-family:var(--font-display);font-size:1.06em;line-height:1.7;color:var(--text)}
.prose figure{margin:2.2em 0}
.prose figcaption{font-size:.74rem;letter-spacing:.1em;color:var(--text-muted);margin-top:.7em}
.prose--zh p{line-height:1.95;text-align:justify;text-justify:inter-ideograph}
.prose--zh{max-width:64ch}
.drop::first-letter{
  float:left;font-family:var(--font-display);font-size:3.4em;line-height:.86;
  padding:.06em .12em 0 0;color:var(--accent)}

/* ---- exhibition cards ---- */
.exh-list{display:grid;gap:0}
.exh{
  display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:clamp(14px,3vw,40px);
  align-items:center;padding-block:clamp(18px,3vw,30px);border-bottom:1px solid var(--line);
  transition:background .35s var(--ease)}
.exh:first-child{border-top:1px solid var(--line)}
.exh:hover{background:linear-gradient(90deg,var(--surface),transparent 70%)}
.exh__year{font-family:var(--font-display);font-size:clamp(1.3rem,3vw,2rem);color:var(--accent);
  font-variant-numeric:tabular-nums;min-width:4ch}
.exh__t{font-family:var(--font-display);font-size:clamp(1.05rem,2.4vw,1.6rem);line-height:1.2}
.exh__m{font-size:.76rem;letter-spacing:.1em;color:var(--text-muted);margin-top:.3em}
.exh__arrow{color:var(--text-muted);transition:transform .35s var(--ease),color .35s var(--ease)}
.exh:hover .exh__arrow{transform:translateX(5px);color:var(--text)}
@media (max-width:640px){
  .exh{grid-template-columns:auto minmax(0,1fr);gap:12px}
  .exh__arrow{display:none}
}

/* ---- stats / facts strip ---- */
.facts{
  display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));
  gap:1px;background:var(--line);border:1px solid var(--line)}
.fact{background:var(--bg);padding:clamp(16px,2.6vw,30px);display:flex;flex-direction:column;gap:.3em}
.fact__n{font-family:var(--font-display);font-size:clamp(1.6rem,3.6vw,2.5rem);line-height:1;
  color:var(--accent);font-variant-numeric:tabular-nums}
.fact__l{font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;color:var(--text-muted)}

/* ---- two-column split ---- */
.split{display:grid;gap:clamp(24px,4.5vw,72px);grid-template-columns:minmax(0,1fr) minmax(0,1.25fr);
  align-items:center}
.split--rev{grid-template-columns:minmax(0,1.25fr) minmax(0,1fr)}
@media (max-width:860px){ .split,.split--rev{grid-template-columns:1fr} }
.split__media{position:relative}
.split__media img{width:100%;box-shadow:0 28px 70px -38px rgba(0,0,0,.75)}

/* ---- lightbox ---- */
.lb{
  position:fixed;inset:0;z-index:200;display:grid;place-items:center;
  background:rgba(10,12,14,.96);opacity:0;pointer-events:none;
  transition:opacity .35s var(--ease)}
.lb[hidden]{display:none}
.lb.is-open{opacity:1;pointer-events:auto}
.lb__img{max-width:94vw;max-height:88svh;object-fit:contain;box-shadow:0 30px 90px -30px #000}
.lb__cap{
  position:absolute;left:0;right:0;bottom:conic-gradient;bottom:0;padding:18px var(--gutter) 22px;
  display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;
  background:linear-gradient(to top,rgba(10,12,14,.94),transparent);
  color:var(--silk-soft);font-size:.8rem;letter-spacing:.08em}
.lb__close{position:absolute;top:14px;right:var(--gutter);
  display:grid;place-items:center;width:44px;height:44px;border-radius:50%;
  border:1px solid rgba(242,238,228,.3);color:var(--silk-soft)}
.lb__close:hover{background:rgba(242,238,228,.12)}

/* ---- footer ---- */
.site-foot{border-top:1px solid var(--line);padding-block:clamp(34px,5vw,60px) clamp(24px,4vw,40px)}
.foot-grid{display:grid;gap:clamp(20px,4vw,48px);
  grid-template-columns:minmax(0,1.4fr) repeat(auto-fit,minmax(140px,1fr))}
.foot-brand__zh{font-family:var(--font-display);font-size:1.4rem;letter-spacing:.14em}
.foot-brand__en{font-size:.64rem;letter-spacing:.24em;text-transform:uppercase;color:var(--text-muted);
  margin-top:.5em}
.foot-col h4{margin:0 0 .8em;font-size:.66rem;letter-spacing:.2em;text-transform:uppercase;
  color:var(--text-muted);font-weight:500}
.foot-col ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:.5em;
  font-size:.84rem}
.foot-col a{color:var(--text);opacity:.85;transition:opacity .3s var(--ease)}
.foot-col a:hover{opacity:1;color:var(--accent)}
.foot-base{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;
  margin-top:clamp(26px,4vw,44px);padding-top:18px;border-top:1px solid var(--line);
  font-size:.7rem;letter-spacing:.08em;color:var(--text-muted)}

/* ---- reveal on scroll ---- */
[data-reveal]{opacity:0;transform:translateY(18px);
  transition:opacity .8s var(--ease),transform .8s var(--ease)}
[data-reveal].is-in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){ [data-reveal]{opacity:1;transform:none} }

/* ---- print ---- */
@media print{
  .site-head,.site-foot,.lb,.hero__scroll,.pager,.filters{display:none!important}
  body{background:#fff;color:#000}
  .detail{grid-template-columns:1fr}
}
'''
p=os.path.join(ROOT,'assets','css','site.css')
with io.open(p,'a',encoding='utf-8') as f: f.write(css)
print('ok', os.path.getsize(p))