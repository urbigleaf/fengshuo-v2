import io,os
code = '''# -*- coding: utf-8 -*-
from gen_lib import *

# ---------------- cards
def card(wk, root, idx):
    ar = round(wk["w"]/wk["h"], 4)
    cap_zh = "%s — %s，%s" % (wk["zh"], dims(wk), wk["year"])
    big = wk["variants"][-1]
    zoom = "%sassets/img/%s.jpg" % (root, big["stem"])
    return (
        '<a class="card" href="%sworks/%s.html" data-work-year="%s" data-reveal '
        'style="--ar:%s" data-zoom="%s" data-zoom-cap="%s">'
        '<span class="card__no">%02d</span>'
        '<span class="card__frame">%s</span>'
        '<span class="card__body">'
        '<span class="card__zh" data-lang="zh">%s</span>'
        '<span class="card__zh" data-lang="en">%s</span>'
        '<span class="card__meta">%s · %s</span>'
        '</span></a>'
    ) % (root, wk["slug"], wk["year"], ar, zoom, e(cap_zh), idx,
         picture(wk, root, "(max-width:640px) 46vw,(max-width:1100px) 31vw,300px"),
         e(wk["zh"]), e(wk["en"]), dims(wk), wk["year"])

def grid(items, root, start=1):
    return '<div class="grid">' + "".join(card(x, root, start+i) for i, x in enumerate(items)) + "</div>"

def page(body, depth, active, tz, te, dz, de):
    return (head(tz, te, dz, de, depth)
            + chr(10) + '<body data-title-zh="%s" data-title-en="%s">' % (e(tz), e(te)) + chr(10)
            + header(depth, active) + chr(10) + "<main>" + chr(10) + body + chr(10) + "</main>" + chr(10)
            + footer(depth) + chr(10) + lightbox() + chr(10) + "</body>" + chr(10) + "</html>" + chr(10))

by_slug = {w["slug"]: w for w in works}

# ---------------- home
hero = by_slug["black-sun"]
feat = [by_slug[s] for s in ("economics","non-paradise","black-sun","not-listening","goat-girl","divine-detective") if s in by_slug]
recent = sorted(works, key=lambda x: (-x["year"], -x["id"]))[:8]

home = (
'<section class="hero">'
'<div class="hero__media">' + picture(hero, "", "100vw", lazy=False) + "</div>"
'<div class="wrap hero__in">'
'<p class="hero__eyebrow"><span data-lang="zh">绘画 · 2005—2016</span><span data-lang="en">Paintings · 2005—2016</span></p>'
'<h1 class="hero__title"><span data-lang="zh">冯硕</span><span data-lang="en">Feng&nbsp;Shuo</span></h1>'
'<p class="hero__sub">'
'<span data-lang="zh">寓言与狂欢之间——以动物、孩童与身体的图像，追问权力、观看与共谋的日常伦理。</span>'
'<span data-lang="en">Between fable and carnival — animal, child and body imagery probing the everyday ethics of power, looking and complicity.</span>'
'</p>'
'<div class="hero__meta">'
'<span data-lang="zh">1970 生于北京</span><span data-lang="en">b. Beijing, 1970</span>'
'<span data-lang="zh">中央美术学院油画系 1994</span><span data-lang="en">Oil Painting, CAFA 1994</span>'
'<span data-lang="zh">任教于中央戏剧学院</span><span data-lang="en">Central Academy of Drama</span>'
'</div></div>'
'<a class="hero__scroll" href="#works" aria-label="Scroll to works"><svg width="16" height="16" viewBox="0 0 24 24" ' + IC + ' aria-hidden="true"><path d="M12 5v14M6 13l6 6 6-6"/></svg></a>'
'</section>'
'<section class="sect" id="works"><div class="wrap">'
'<div class="sect-head"><div class="sect-head__l">'
'<span class="kicker"><span data-lang="zh">作品选</span><span data-lang="en">Selected works</span></span>'
'<h2 class="sect-title"><span data-lang="zh">寓言、罪与狂欢</span><span data-lang="en">Fable, Guilt and Carnival</span></h2>'
'</div><a class="sect-link" href="works/">'
'<span data-lang="zh">全部 ' + str(len(works)) + ' 件</span><span data-lang="en">All ' + str(len(works)) + ' works</span>'
'<svg viewBox="0 0 24 24" ' + IC + ' aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a></div>'
+ grid(feat, "") +
'</div></section>'
'<section class="sect sect--tight"><div class="wrap"><div class="facts">'
'<div class="fact"><span class="fact__n">' + str(len(works)) + '</span><span class="fact__l"><span data-lang="zh">收录作品</span><span data-lang="en">Works catalogued</span></span></div>'
'<div class="fact"><span class="fact__n">2005—16</span><span class="fact__l"><span data-lang="zh">创作年份</span><span data-lang="en">Years of practice</span></span></div>'
'<div class="fact"><span class="fact__n">2</span><span class="fact__l"><span data-lang="zh">个展文献</span><span data-lang="en">Solo exhibitions</span></span></div>'
'<div class="fact"><span class="fact__n">CAFA</span><span class="fact__l"><span data-lang="zh">1994 毕业</span><span data-lang="en">Graduated 1994</span></span></div>'
'</div></div></section>'
'<section class="sect"><div class="wrap">'
'<div class="sect-head"><div class="sect-head__l">'
'<span class="kicker"><span data-lang="zh">近期</span><span data-lang="en">Recent</span></span>'
'<h2 class="sect-title"><span data-lang="zh">近年作品</span><span data-lang="en">Later works</span></h2>'
'</div></div>'
+ grid(recent, "") +
'</div></section>')

w("index.html", page(home, 0, "home",
  "冯硕 — 绘画作品", "Feng Shuo — Paintings",
  "冯硕（1970 生于北京）绘画作品档案：寓言、罪与狂欢系列，含展览文献与作品图录。",
  "Feng Shuo (b.1970, Beijing) — painting archive with exhibitions and catalogue."))
print("index ok")
'''
io.open(r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_p1.py','w',encoding='utf-8').write(code)
print('p1 written', len(code))