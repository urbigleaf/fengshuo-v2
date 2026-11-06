# -*- coding: utf-8 -*-
import io, os
ROOT = r'D:\user\Documents\GitHub\fengshuo_v1'
css = r'''
/* ==========================================================================
   冯硕 · Feng Shuo — Studio Archive
   Palette derived from the paintings: lacquer-ink ground (闪念), pigment silk
   (bare canvas margins), terracotta red (黑日), arsenic green (非乐园),
   muted celadon for the lotus works.
   ========================================================================== */

:root{
  --ink:#16191c; --ink-2:#1d2226; --ink-3:#262c31;
  --silk:#e7e1d3; --silk-dim:#bcb4a2; --silk-soft:#f2eee4;
  --terracotta:#b8452f; --terracotta-lt:#d2694c;
  --arsenic:#6f8f6a; --celadon:#9fb8ad; --ochre:#c2954f;

  --bg:var(--ink); --surface:var(--ink-2);
  --text:var(--silk-soft); --text-muted:#a9a294;
  --line:rgba(231,225,211,.14); --line-strong:rgba(231,225,211,.30);
  --accent:var(--terracotta-lt);

  --font-display:"Marcellus","Songti SC","Noto Serif SC",Georgia,serif;
  --font-body:"Inter",ui-sans-serif,system-ui,-apple-system,"Segoe UI",
              "PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;

  --step:clamp(14px,1.55vw,16px);
  --gutter:clamp(18px,4vw,64px);
  --maxw:1560px;
  --ease:cubic-bezier(.22,.61,.36,1);
  --dur:.6s;
}
:root[data-theme="paper"]{
  --bg:var(--silk-soft); --surface:#faf7f0;
  --text:#1b1e21; --text-muted:#6b6357;
  --line:rgba(27,30,33,.13); --line-strong:rgba(27,30,33,.30);
  --accent:var(--terracotta);
}

*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  *,*::before,*::after{animation-duration:.001ms!important;transition-duration:.001ms!important}
}
body{
  margin:0;background:var(--bg);color:var(--text);
  font-family:var(--font-body);font-size:var(--step);line-height:1.65;
  font-feature-settings:"kern" 1,"liga" 1;
  -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;
  overflow-x:hidden;
  transition:background .5s var(--ease),color .5s var(--ease);
}
img,svg,video{display:block;max-width:100%;height:auto}
a{color:inherit;text-decoration:none}
button{font:inherit;color:inherit;background:none;border:0;cursor:pointer}
::selection{background:var(--accent);color:#fff}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;
  clip:rect(0 0 0 0);white-space:nowrap;border:0}

/* ---- language switching ---- */
html[lang="zh"] [data-lang="en"],
html[lang="en"] [data-lang="zh"]{display:none!important}

/* ---- layout ---- */
.wrap{width:min(100% - (var(--gutter) * 2),var(--maxw));margin-inline:auto}
.wrap-narrow{width:min(100% - (var(--gutter) * 2),860px);margin-inline:auto}
section{position:relative}

/* ---- header ---- */
.site-head{
  position:sticky;top:0;z-index:80;
  background:color-mix(in srgb,var(--bg) 88%,transparent);
  backdrop-filter:blur(16px) saturate(1.2);
  -webkit-backdrop-filter:blur(16px) saturate(1.2);
  border-bottom:1px solid var(--line);
}
.site-head__in{
  display:flex;align-items:center;justify-content:space-between;
  gap:clamp(12px,2vw,32px);min-height:66px;
}
.brand{display:flex;align-items:baseline;gap:.6em;line-height:1}
.brand__zh{font-family:var(--font-display);font-size:1.5rem;letter-spacing:.14em}
.brand__en{font-size:.66rem;letter-spacing:.24em;text-transform:uppercase;color:var(--text-muted)}

.nav{display:flex;align-items:center;gap:clamp(10px,1.6vw,26px)}
.nav a{
  position:relative;font-size:.82rem;letter-spacing:.1em;text-transform:uppercase;
  color:var(--text-muted);padding-block:.35em;transition:color .3s var(--ease);
}
.nav a::after{
  content:"";position:absolute;left:0;bottom:0;height:1px;width:0;
  background:var(--accent);transition:width .36s var(--ease);
}
.nav a:hover,.nav a[aria-current="page"]{color:var(--text)}
.nav a:hover::after,.nav a[aria-current="page"]::after{width:100%}

.head-tools{display:flex;align-items:center;gap:8px}
.icon-btn{
  display:grid;place-items:center;width:40px;height:40px;border-radius:50%;
  border:1px solid var(--line);color:var(--text-muted);
  transition:color .3s var(--ease),border-color .3s var(--ease),background .3s var(--ease);
}
.icon-btn:hover{color:var(--text);border-color:var(--line-strong);background:var(--surface)}
.lang-toggle{
  display:flex;align-items:center;gap:.35em;height:40px;padding-inline:.85em;
  border:1px solid var(--line);border-radius:999px;
  font-size:.74rem;letter-spacing:.14em;text-transform:uppercase;color:var(--text-muted);
  transition:color .3s var(--ease),border-color .3s var(--ease);
}
.lang-toggle:hover{color:var(--text);border-color:var(--line-strong)}
.lang-toggle b{color:var(--accent);font-weight:600}

.burger{display:none}

@media (max-width:900px){
  .nav{display:none}
  .burger{display:grid}
}

/* ---- mobile drawer ---- */
.drawer{
  position:fixed;inset:0;z-index:120;display:grid;
  background:var(--bg);transform:translateY(-100%);
  transition:transform .5s var(--ease);overscroll-behavior:contain;
}
.drawer[hidden]{display:none}
.drawer.is-open{transform:translateY(0)}
.drawer__in{display:flex;flex-direction:column;padding:20px var(--gutter) 40px;height:100%}
.drawer__top{display:flex;justify-content:space-between;align-items:center;min-height:46px}
.drawer__links{display:flex;flex-direction:column;gap:.2em;margin-top:8vh}
.drawer__links a{
  font-family:var(--font-display);font-size:clamp(1.8rem,8vw,2.6rem);
  letter-spacing:.04em;padding-block:.16em;border-bottom:1px solid var(--line);
}
.drawer__links a:last-child{border-bottom:0}
.drawer__foot{margin-top:auto;color:var(--text-muted);font-size:.8rem}
'''
with io.open(os.path.join(ROOT,'assets','css','site.css'),'w',encoding='utf-8') as f:
    f.write(css)
print('part1 ok', len(css))