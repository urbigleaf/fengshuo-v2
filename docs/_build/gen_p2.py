# -*- coding: utf-8 -*-
from gen_p1 import *
from gen_p1 import card, grid, page, by_slug

# ---------------- works index
chips = ('<button class="chip" type="button" data-year="all" aria-pressed="true">'
         '<span data-lang="zh">全部</span><span data-lang="en">All</span></button>')
chips += "".join('<button class="chip" type="button" data-year="%s" aria-pressed="false">%s</button>' % (y, y) for y in years)

blocks = []
for y in years:
    items = [x for x in works if x["year"] == y]
    blocks.append(
      '<section class="sect sect--tight" data-year-group="%s"><div class="wrap">'
      '<div class="sect-head"><div class="sect-head__l"><span class="kicker">%s</span>'
      '<h2 class="sect-title">%d <span data-lang="zh">件</span><span data-lang="en">works</span></h2>'
      '</div></div>%s</div></section>' % (y, y, len(items), grid(items, "../")))

works_page = (
'<div class="page-head"><div class="wrap">'
'<span class="kicker"><span data-lang="zh">图录</span><span data-lang="en">Catalogue</span></span>'
'<h1 class="page-head__title"><span data-lang="zh">作品</span><span data-lang="en">Works</span></h1>'
'<p class="page-head__sub"><span data-lang="zh">%d 件作品，%s—%s。按年份排列；点击图片可放大，进入详情可见尺寸与相邻作品。</span>'
'<span data-lang="en">%d works, %s—%s. Sorted by year; click an image to enlarge, open a work for dimensions and neighbours.</span></p>'
'</div></div>'
'<div class="wrap" style="padding-top:clamp(20px,3vw,34px)">'
'<div class="filters" data-filters role="group" aria-label="Filter by year">%s</div></div>'
) % (len(works), years[0], years[-1], len(works), years[0], years[-1], chips) + "".join(blocks)

w("works/index.html", page(works_page, 1, "works",
  "作品 — 冯硕", "Works — Feng Shuo",
  "冯硕绘画作品图录，%s—%s，共 %d 件。" % (years[0], years[-1], len(works)),
  "Catalogue of Feng Shuo paintings, %s—%s, %d works." % (years[0], years[-1], len(works))))
print("works index ok")

# ---------------- detail pages
KEYS = ["一往而深","末日","活着","最后的晚餐","罪天使","盘中餐","想不通","无题 180x60","经济学",
        "黑日","藕花深处","头像","不看","不说","不听","假装谈恋爱","跳绳","非乐园","羊妞","鹅太太","神探","那样"]

def prevnext(i):
    out = []
    if i > 0:
        p_ = works[i-1]
        out.append('<a class="pager__prev" href="%s.html" data-nav-prev><svg viewBox="0 0 24 24" %s aria-hidden="true"><path d="M19 12H5M11 6l-6 6 6 6"/></svg><span data-lang="zh">%s</span><span data-lang="en">%s</span></a>'
                   % (p_["slug"], IC, e(p_["zh"]), e(p_["en"])))
    else:
        out.append("<span></span>")
    if i < len(works)-1:
        n_ = works[i+1]
        out.append('<a class="pager__next" href="%s.html" data-nav-next><span data-lang="zh">%s</span><span data-lang="en">%s</span><svg viewBox="0 0 24 24" %s aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>'
                   % (n_["slug"], IC, e(n_["zh"]), e(n_["en"])))
    else:
        out.append("<span></span>")
    return "".join(out)

count = 0
for i, wk in enumerate(works):
    big = wk["variants"][-1]
    same = [x for x in works if x["year"] == wk["year"] and x["slug"] != wk["slug"]][:4]
    body = (
    '<div class="wrap" style="padding-top:clamp(24px,4vw,52px)">'
    '<nav class="kicker" aria-label="Breadcrumb" style="margin-bottom:clamp(14px,2.4vw,26px)">'
    '<a href="../works/"><span data-lang="zh">作品</span><span data-lang="en">Works</span></a>'
    '<span aria-hidden="true">/</span><span>%s</span></nav>'
    '<div class="detail">'
    '<figure class="detail__stage" style="margin:0">%s'
    '<figcaption class="sr-only">%s · %s</figcaption></figure>'
    '<div class="detail__side">'
    '<div><h1 class="detail__zh" data-lang="zh">%s</h1>'
    '<p class="detail__zh" data-lang="en" style="font-size:clamp(1.4rem,3vw,2rem)">%s</p>'
    '<p class="detail__en">%s</p></div>'
    '<dl class="dl">'
    '<dt><span data-lang="zh">年份</span><span data-lang="en">Year</span></dt><dd>%s</dd>'
    '<dt><span data-lang="zh">尺寸</span><span data-lang="en">Dimensions</span></dt><dd>%s</dd>'
    '<dt><span data-lang="zh">材质</span><span data-lang="en">Medium</span></dt>'
    '<dd><span data-lang="zh">布面油画</span><span data-lang="en">Oil on canvas</span></dd>'
    '<dt><span data-lang="zh">编号</span><span data-lang="en">Ref.</span></dt><dd>FS-%03d</dd>'
    '</dl>'
    '<div class="pager">%s</div>'
    '</div></div></div>'
    '%s'
    ) % (wk["year"], picture(wk, "../", "(max-width:900px) 92vw,58vw", lazy=False),
         e(wk["zh"]), e(wk["en"]), e(wk["zh"]), e(wk["en"]),
         "%s · %s" % (dims(wk), wk["year"]), wk["year"], dims(wk), wk["id"],
         prevnext(i),
         ('<section class="sect sect--tight" data-year-group="%s"><div class="wrap">'
          '<div class="sect-head"><div class="sect-head__l"><span class="kicker">%s</span>'
          '<h2 class="sect-title"><span data-lang="zh">同年作品</span><span data-lang="en">Same year</span></h2></div></div>'
          '%s</div></section>' % (wk["year"], wk["year"], grid(same, "../"))) if same else "")
    w("works/%s.html" % wk["slug"], page(body, 1, "workd",
      "%s — 冯硕" % wk["zh"], "%s — Feng Shuo" % wk["en"],
      "%s，%s，%s。" % (wk["zh"], dims(wk), wk["year"]),
      "%s, %s, %s." % (wk["en"], dims(wk), wk["year"])))
    count += 1
print("detail pages", count)
