# -*- coding: utf-8 -*-
"""Generate the fengshuo_v1 static site from works-images.json."""
import io, json, os, html, datetime

ROOT = r'D:\user\Documents\GitHub\fengshuo_v1'
SITE = 'https://fengshuo.art'
NOW  = datetime.date.today().isoformat()

def w(rel, s):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with io.open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(s)
    return p

def e(t):
    return html.escape(str(t), quote=True)

# ---------------------------------------------------------------- partials
IC = 'fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"'

def head(title_zh, title_en, desc_zh, desc_en, depth, extra=''):
    root = '../' * depth
    return f'''<!DOCTYPE html>
<html lang="zh" data-lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title_zh)}</title>
<meta name="description" content="{e(desc_zh)}">
<link rel="canonical" href="{SITE}/">
<link rel="icon" href="{root}favicon.ico" sizes="any">
<meta property="og:type" content="website">
<meta property="og:site_name" content="冯硕 Feng Shuo">
<meta property="og:title" content="{e(title_en)}">
<meta property="og:description" content="{e(desc_en)}">
<meta name="theme-color" content="#16191c">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Marcellus&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/site.css">
<script src="{root}assets/js/site.js" defer></script>
{extra}</head>'''

def header(depth, active):
    root = '../' * depth
    def a(href, key, zh, en):
        cur = ' aria-current="page"' if key == active else ''
        return (f'<a href="{root}{href}"{cur} data-lang="zh">{zh}</a>'
                f'<a href="{root}{href}"{cur} data-lang="en">{en}</a>')
    nav = (a('works/', 'works', '作品', 'Works')
         + a('exhibitions/', 'exh', '展览', 'Exhibitions')
         + a('about/', 'about', '艺术家', 'Artist'))
    dnav = (a('works/', 'workd', '作品', 'Works')
          + a('exhibitions/', 'exhd', '展览', 'Exhibitions')
          + a('about/', 'aboutd', '艺术家', 'Artist'))
    return f'''<header class="site-head">
  <div class="wrap site-head__in">
    <a class="brand" href="{root}index.html" aria-label="冯硕 Feng Shuo">
      <span class="brand__zh">冯硕</span><span class="brand__en">Feng Shuo</span>
    </a>
    <nav class="nav" aria-label="Main">{nav}</nav>
    <div class="head-tools">
      <button class="lang-toggle" type="button" data-lang-toggle aria-pressed="false" aria-label="Switch to English">
        <span data-lang-cur="zh" class="is-on">中</span><span aria-hidden="true">/</span><span data-lang-cur="en">EN</span>
      </button>
      <button class="icon-btn" type="button" data-theme-toggle aria-label="切换明暗 Reversal">
        <svg width="18" height="18" viewBox="0 0 24 24" {IC} aria-hidden="true">
          <circle cx="12" cy="12" r="8.5"/><path d="M12 3.5v17"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17z" fill="currentColor" stroke="none"/></svg>
      </button>
      <button class="icon-btn burger" type="button" data-drawer-open aria-label="Menu">
        <svg width="20" height="20" viewBox="0 0 24 24" {IC} aria-hidden="true"><path d="M3 7h18M3 12h18M3 17h18"/></svg>
      </button>
    </div>
  </div>
</header>
<div class="drawer" id="drawer" hidden>
  <div class="drawer__in">
    <div class="drawer__top">
      <span class="brand"><span class="brand__zh">冯硕</span></span>
      <button class="icon-btn" type="button" data-drawer-close aria-label="Close">
        <svg width="20" height="20" viewBox="0 0 24 24" {IC} aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>
      </button>
    </div>
    <nav class="drawer__links" aria-label="Mobile">{dnav}</nav>
    <div class="drawer__foot">b. 1970 Beijing · 中央美术学院 1994</div>
  </div>
</div>'''

def footer(depth):
    root = '../' * depth
    return f'''<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="foot-brand__zh">冯硕</div>
        <div class="foot-brand__en">Feng Shuo · Painting</div>
      </div>
      <div class="foot-col">
        <h4><span data-lang="zh">浏览</span><span data-lang="en">Browse</span></h4>
        <ul>
          <li><a href="{root}works/"><span data-lang="zh">全部作品</span><span data-lang="en">All works</span></a></li>
          <li><a href="{root}exhibitions/"><span data-lang="zh">展览</span><span data-lang="en">Exhibitions</span></a></li>
          <li><a href="{root}about/"><span data-lang="zh">艺术家</span><span data-lang="en">Artist</span></a></li>
        </ul>
      </div>
      <div class="foot-col">
        <h4><span data-lang="zh">年份</span><span data-lang="en">By year</span></h4>
        <ul>
          <li><a href="{root}works/?year=2008">2008</a></li>
          <li><a href="{root}works/?year=2010">2010</a></li>
          <li><a href="{root}works/?year=2011">2011</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-base">
      <span>© <span data-lang="zh">冯硕。图像版权归艺术家所有。</span><span data-lang="en">Feng Shuo. All images © the artist.</span></span>
      <span><span data-lang="zh">北京</span><span data-lang="en">Beijing</span></span>
    </div>
  </div>
</footer>'''

def lightbox():
    return '''<div class="lb" id="lightbox" hidden role="dialog" aria-modal="true" aria-label="Image viewer" tabindex="-1">
  <button class="lb__close" type="button" data-lb-close aria-label="Close">
    <svg width="20" height="20" viewBox="0 0 24 24" ''' + IC + ''' aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>
  </button>
  <img class="lb__img" alt="">
  <div class="lb__cap"></div>
</div>'''

def picture(work, root, sizes, cls='', lazy=True):
    """<picture> with AVIF/WebP/JPG plus srcset across widths."""
    vs = work['variants']
    def srcset(ext):
        return ','.join(f"{root}assets/img/{v['stem']}.{ext} {v['w']}w" for v in vs)
    biggest = vs[-1]
    lz = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high" decoding="async"'
    return (f'<picture>'
            f'<source type="image/avif" srcset="{srcset("avif")}" sizes="{sizes}">'
            f'<source type="image/webp" srcset="{srcset("webp")}" sizes="{sizes}">'
            f'<img src="{root}assets/img/{biggest["stem"]}.jpg" srcset="{srcset("jpg")}" '
            f'sizes="{sizes}" width="{biggest["w"]}" height="{biggest["h"]}" '
            f'alt="{e(work["zh"])} · {e(work["en"])}"{lz}{(" class=" + cls) if cls else ""}>'
            f'</picture>')

# ---------------------------------------------------------------- data
works = json.load(io.open(os.path.join(ROOT, '_build', 'works-images.json'), encoding='utf-8'))
works.sort(key=lambda x: (x['year'], x['id']))
years = sorted({w_['year'] for w_ in works})

def dims(w_):
    return f'{w_["w"]} × {w_["h"]} cm'

def meta_line(w_):
    return f'{dims(w_)} · {w_["year"]}'

print('loaded', len(works), 'works')

# keep for later steps
json.dump({'years': years}, io.open(os.path.join(ROOT,'_build','meta.json'),'w',encoding='utf-8'))