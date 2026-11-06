# -*- coding: utf-8 -*-
import io, os
ROOT = r'D:\user\Documents\GitHub\fengshuo_v1'
P = os.path.join(ROOT,'_build')

gen = r'''
# ---------------------------------------------------------------- cards
def card(wk, root, idx):
    ar = round(wk['w']/wk['h'], 4)
    cap_zh = f'{wk["zh"]} — {dims(wk)}，{wk["year"]}'
    cap_en = f'{wk["en"]} — {dims(wk)}, {wk["year"]}'
    big = wk['variants'][-1]
    zoom = f'{root}assets/img/{big["stem"]}.jpg'
    return f'''<a class="card" href="{root}works/{wk['slug']}.html"
   data-work-year="{wk['year']}" data-reveal
   style="--ar:{ar}"
   data-zoom="{zoom}" data-zoom-cap="{e(cap_zh)}">
  <span class="card__no">{idx:02d}</span>
  <span class="card__frame">{picture(wk, root, "(max-width:640px) 46vw,(max-width:1100px) 31vw,300px")}</span>
  <span class="card__body">
    <span class="card__zh" data-lang="zh">{e(wk['zh'])}</span>
    <span class="card__zh" data-lang="en">{e(wk['en'])}</span>
    <span class="card__meta">{dims(wk)} · {wk['year']}</span>
  </span>
</a>'''

def grid(items, root, start=1):
    return ('<div class="grid">'
            + ''.join(card(x, root, start+i) for i, x in enumerate(items))
            + '</div>')

def page(body, depth, active, tz, te, dz, de, cls=''):
    return (head(tz, te, dz, de, depth)
            + f'\n<body class="{cls}" data-title-zh="{e(tz)}" data-title-en="{e(te)}">\n'
            + header(depth, active) + '\n<main>\n' + body + '\n</main>\n'
            + footer(depth) + '\n' + lightbox() + '\n</body>\n</html>\n')

# ---------------------------------------------------------------- home
hero = next(w for w in works if w['slug'] == 'black-sun')
feat = [w for w in works if w['slug'] in
        ('economics','non-paradise','black-sun','not-listening','goat-girl','divine-detective')]
recent = sorted(works, key=lambda x: (-x['year'], -x['id']))[:8]

home = f'''<section class="hero">
  <div class="hero__media">{picture(hero, '', '100vw', lazy=False)}</div>
  <div class="wrap hero__in">
    <p class="hero__eyebrow">
      <span data-lang="zh">绘画 · 2005—2016</span>
      <span data-lang="en">Paintings · 2005—2016</span>
    </p>
    <h1 class="hero__title">
      <span data-lang="zh">冯硕</span>
      <span data-lang="en">Feng&nbsp;Shuo</span>
    </h1>
    <p class="hero__sub">
      <span data-lang="zh">寓言与狂欢之间——以动物、孩童与身体的图像，追问权力、观看与共谋的日常伦理。</span>
      <span data-lang="en">Between fable and carnival — animal, child and body imagery probing the everyday ethics of power, looking and complicity.</span>
    </p>
    <div class="hero__meta">
      <span data-lang="zh">1970 生于北京</span><span data-lang="en">b. Beijing, 1970</span>
      <span data-lang="zh">中央美术学院油画系 1994</span><span data-lang="en">Oil Painting, CAFA 1994</span>
      <span data-lang="zh">任教中央戏剧学院</span><span data-lang="en">Central Academy of Drama</span>
    </div>
  </div>
  <a class="hero__scroll" href="#works" aria-label="Scroll to works">
    <svg width="16" height="16" viewBox="0 0 24 24" {IC} aria-hidden="true"><path d="M12 5v14M6 13l6 6 6-6"/></svg>
  </a>
</section>

<section class="sect" id="works">
  <div class="wrap">
    <div class="sect-head">
      <div class="sect-head__l">
        <span class="kicker"><span data-lang="zh">作品选</span><span data-lang="en">Selected works</span></span>
        <h2 class="sect-title"><span data-lang="zh">寓言、罪与狂欢</span><span data-lang="en">Fable, Guilt and Carnival</span></h2>
      </div>
      <a class="sect-link" href="works/">
        <span data-lang="zh">全部 {len(works)} 件</span><span data-lang="en">All {len(works)} works</span>
        <svg viewBox="0 0 24 24" {IC} aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </a>
    </div>
    {grid(feat, '')}
  </div>
</section>

<section class="sect sect--tight">
  <div class="wrap">
    <div class="facts">
      <div class="fact"><span class="fact__n">{len(works)}</span>
        <span class="fact__l"><span data-lang="zh">收录作品</span><span data-lang="en">Works catalogued</span></span></div>
      <div class="fact"><span class="fact__n">2005—16</span>
        <span class="fact__l"><span data-lang="zh">创作年份</span><span data-lang="en">Years of practice</span></span></div>
      <div class="fact"><span class="fact__n">2</span>
        <span class="fact__l"><span data-lang="zh">个展文献</span><span data-lang="en">Solo exhibitions</span></span></div>
      <div class="fact"><span class="fact__n">CAFA</span>
        <span class="fact__l"><span data-lang="zh">1994 毕业</span><span data-lang="en">Graduated 1994</span></span></div>
    </div>
  </div>
</section>

<section class="sect">
  <div class="wrap">
    <div class="sect-head">
      <div class="sect-head__l">
        <span class="kicker"><span data-lang="zh">近期</span><span data-lang="en">Recent</span></span>
        <h2 class="sect-title"><span data-lang="zh">近年作品</span><span data-lang="en">Later works</span></h2>
      </div>
    </div>
    {grid(recent, '')}
  </div>
</section>'''

w('index.html', page(home, 0, 'home',
    '冯硕 — 绘画作品', 'Feng Shuo — Paintings',
    '冯硕（1970 生于北京）绘画作品档案：寓言、罪与狂欢系列，含展览文献与作品图录。',
    'Feng Shuo (b.1970, Beijing) — painting archive with exhibitions and catalogue.'))
print('index ok')

# ---------------------------------------------------------------- works index
exh_prev = next(w for w in works if w['slug']=='black-sun')
chips = ('<button class="chip" type="button" data-year="all" aria-pressed="true">'
         '<span data-lang="zh">全部</span><span data-lang="en">All</span></button>')
chips += ''.join(f'<button class="chip" type="button" data-year="{y}" aria-pressed="false">{y}</button>'
                 for y in years)
by_year = []
for y in years:
    items = [w for w in works if w['year']==y]
    by_year.append(f'''<section class="sect sect--tight">
  <div class="wrap">
    <div class="sect-head">
      <div class="sect-head__l">
        <span class="kicker">{y}</span>
        <h2 class="sect-title">{len(items)} <span data-lang="zh">件作品</span><span data-lang="en">works</span></h2>
      </div>
    </div>
    {grid(items, '../')}
  </div>
</section>''')

works_page = f'''<div class="page-head">
  <div class="wrap">
    <span class="kicker"><span data-lang="zh">图录</span><span data-lang="en">Catalogue</span></span>
    <h1 class="page-head__title"><span data-lang="zh">作品</span><span data-lang="en">Works</span></h1>
    <p class="page-head__sub">
      <span data-lang="zh">{len(works)} 件作品，{years[0]}—{years[-1]}。按年份排列，点击可放大，进入详情可见尺寸与相邻作品。</span>
      <span data-lang="en">{len(works)} works, {years[0]}—{years[-1]}. Sorted by year; click to enlarge, open a work for dimensions and neighbours.</span>
    </p>
  </div>
</div>
<div class="wrap" style="padding-top:clamp(20px,3vw,34px)">
  <div class="filters" data-filters role="group" aria-label="Filter by year">{chips}</div>
</div>
{''.join(by_year)}'''

w('works/index.html', page(works_page, 1, 'works',
    '作品 — 冯硕', 'Works — Feng Shuo',
    f'冯硕绘画作品图录，{years[0]}—{years[-1]}，共 {len(works)} 件。',
    f'Catalogue of Feng Shuo paintings, {years[0]}—{years[-1]}, {len(works)} works.'))
print('works index ok')
'''
io.open(os.path.join(P,'gen_pages1.py'),'w',encoding='utf-8').write(gen)
# concatenate base+pages so it runs as one program
base = io.open(os.path.join(P,'gen_base.py'),encoding='utf-8').read()
io.open(os.path.join(P,'gen_all.py'),'w',encoding='utf-8').write(base + gen)
print('built gen_all.py')