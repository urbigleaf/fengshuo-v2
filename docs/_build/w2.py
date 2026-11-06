# -*- coding: utf-8 -*-
import io, os
ROOT = r'D:\user\Documents\GitHub\fengshuo_v1'
css = r'''
/* ---- hero ---- */
.hero{position:relative;isolation:isolate;overflow:hidden;background:var(--ink)}
.hero__media{position:absolute;inset:0;z-index:-2}
.hero__media img{width:100%;height:100%;object-fit:cover;object-position:52% 38%;
  opacity:.72;transform:scale(1.04);animation:heroIn 1.6s var(--ease) both}
@keyframes heroIn{from{opacity:0;transform:scale(1.1)}to{opacity:.72;transform:scale(1.04)}}
.hero::after{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none;
  background:
    radial-gradient(120% 85% at 78% 18%,transparent 0%,rgba(16,19,22,.45) 55%,rgba(16,19,22,.92) 100%),
    linear-gradient(to top,rgba(16,19,22,.97) 4%,rgba(16,19,22,.55) 38%,rgba(16,19,22,.25) 100%)}
.hero__in{
  position:relative;display:flex;flex-direction:column;justify-content:flex-end;
  min-height:min(92svh,860px);padding-block:clamp(48px,9vh,110px) clamp(34px,5vh,64px);
  color:var(--silk-soft)}
.hero__eyebrow{
  display:flex;align-items:center;gap:.85em;margin:0 0 clamp(14px,2vh,26px);
  font-size:.7rem;letter-spacing:.3em;text-transform:uppercase;color:var(--silk-dim)}
.hero__eyebrow::before{content:"";width:34px;height:1px;background:var(--terracotta-lt)}
.hero__title{
  margin:0;font-family:var(--font-display);font-weight:400;
  font-size:clamp(2.9rem,11vw,9.4rem);line-height:.9;letter-spacing:.02em;color:var(--silk-soft);
  text-wrap:balance}
.hero__title em{font-style:normal;color:var(--terracotta-lt)}
.hero__sub{
  margin:clamp(16px,2.4vh,30px) 0 0;max-width:46ch;
  font-size:clamp(.95rem,1.9vw,1.18rem);line-height:1.62;color:rgba(242,238,228,.8)}
.hero__meta{
  display:flex;flex-wrap:wrap;gap:10px clamp(14px,2.2vw,30px);
  margin-top:clamp(22px,3.4vh,40px);padding-top:18px;border-top:1px solid rgba(242,238,228,.2);
  font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--silk-dim)}
.hero__scroll{
  position:absolute;right:var(--gutter);bottom:clamp(18px,3vh,30px);
  display:grid;place-items:center;width:44px;height:44px;border-radius:50%;
  border:1px solid rgba(242,238,228,.3);color:var(--silk-soft);
  transition:background .3s var(--ease),border-color .3s var(--ease)}
.hero__scroll:hover{background:rgba(242,238,228,.12);border-color:rgba(242,238,228,.6)}
@media (max-width:640px){ .hero__scroll{display:none} }

/* ---- section chrome ---- */
.sect{padding-block:clamp(48px,8vw,110px)}
.sect--tight{padding-block:clamp(32px,5vw,64px)}
.sect-head{
  display:flex;align-items:flex-end;justify-content:space-between;gap:24px;
  padding-bottom:18px;margin-bottom:clamp(24px,4vw,48px);border-bottom:1px solid var(--line)}
.sect-head__l{display:flex;flex-direction:column;gap:.5em}
.kicker{
  display:flex;align-items:center;gap:.7em;
  font-size:.68rem;letter-spacing:.28em;text-transform:uppercase;color:var(--text-muted)}
.kicker::before{content:"";width:22px;height:1px;background:var(--accent)}
.sect-title{
  margin:0;font-family:var(--font-display);font-weight:400;
  font-size:clamp(1.55rem,3.6vw,2.7rem);line-height:1.1;letter-spacing:.01em;text-wrap:balance}
.sect-link{
  display:inline-flex;align-items:center;gap:.5em;flex:0 0 auto;
  font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;color:var(--text-muted);
  border-bottom:1px solid transparent;padding-bottom:2px;
  transition:color .3s var(--ease),border-color .3s var(--ease)}
.sect-link:hover{color:var(--text);border-color:var(--line-strong)}
.sect-link svg{width:14px;height:14px}
@media (max-width:520px){ .sect-head{flex-direction:column;align-items:flex-start;gap:14px} }

/* ---- work grid ---- */
.grid{
  display:grid;gap:clamp(14px,2.4vw,36px) clamp(12px,1.9vw,28px);
  grid-template-columns:repeat(auto-fill,minmax(clamp(150px,20vw,300px),1fr))}
.card{
  position:relative;display:flex;flex-direction:column;gap:.7em;
  background:linear-gradient(175deg,var(--surface),transparent 72%);
  padding:0;overflow:hidden}
.card__frame{
  position:relative;overflow:hidden;background:var(--surface);
  aspect-ratio:var(--ar,1);display:grid;place-items:center}
.card__frame img{
  width:100%;height:100%;object-fit:contain;
  transition:transform .8s var(--ease),filter .6s var(--ease);
  filter:saturate(.96)}
.card:hover .card__frame img,.card:focus-visible .card__frame img{
  transform:scale(1.045);filter:saturate(1.06)}
.card__frame::after{
  content:"";position:absolute;inset:0;box-shadow:inset 0 0 0 1px var(--line);
  pointer-events:none;transition:box-shadow .4s var(--ease)}
.card:hover .card__frame::after{box-shadow:inset 0 0 0 1px var(--line-strong)}
.card__body{display:flex;flex-direction:column;gap:.15em;padding:0 .1em}
.card__zh{
  font-family:var(--font-display);font-size:1.02rem;letter-spacing:.06em;line-height:1.35}
.card__en{
  font-size:.72rem;letter-spacing:.09em;text-transform:uppercase;color:var(--text-muted);
  line-height:1.4}
.card__meta{
  font-size:.7rem;letter-spacing:.1em;color:var(--text-muted);font-variant-numeric:tabular-nums}
.card__no{
  position:absolute;top:10px;left:11px;z-index:2;
  font-size:.62rem;letter-spacing:.16em;color:var(--text-muted);
  opacity:0;transform:translateY(-4px);transition:opacity .35s var(--ease),transform .35s var(--ease);
  text-shadow:0 1px 6px rgba(0,0,0,.4)}
.card:hover .card__no{opacity:1;transform:none}

/* ---- year filter ---- */
.filters{
  display:flex;flex-wrap:wrap;gap:8px;margin-bottom:clamp(22px,3.4vw,40px)}
.chip{
  display:inline-flex;align-items:center;height:34px;padding-inline:.95em;border-radius:999px;
  border:1px solid var(--line);font-size:.74rem;letter-spacing:.12em;color:var(--text-muted);
  font-variant-numeric:tabular-nums;
  transition:color .3s var(--ease),border-color .3s var(--ease),background .3s var(--ease)}
.chip:hover{color:var(--text);border-color:var(--line-strong)}
.chip[aria-pressed="true"]{
  color:#fff;background:var(--accent);border-color:var(--accent)}

/* ---- page header ---- */
.page-head{
  padding-block:clamp(44px,7vw,96px) clamp(26px,4vw,46px);
  border-bottom:1px solid var(--line)}
.page-head__title{
  margin:.12em 0 0;font-family:var(--font-display);font-weight:400;
  font-size:clamp(2.1rem,6.4vw,4.6rem);line-height:1;letter-spacing:.01em;text-wrap:balance}
.page-head__sub{
  margin:clamp(14px,2vw,22px) 0 0;max-width:62ch;color:var(--text-muted);
  font-size:clamp(.92rem,1.7vw,1.06rem)}
'''
p=os.path.join(ROOT,'assets','css','site.css')
with io.open(p,'a',encoding='utf-8') as f: f.write(css)
print('ok', os.path.getsize(p))