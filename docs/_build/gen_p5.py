# -*- coding: utf-8 -*-
import json, os, html
from gen_p3 import *

BJ = r'D:\user\Documents\GitHub\fengshuo_v1\_build'
ZH = json.load(open(os.path.join(BJ,'exh_clean.json'), encoding='utf-8'))
EN = json.load(open(os.path.join(BJ,'exh_en.json'), encoding='utf-8'))

def esc(t): return html.escape(t, quote=False)

def dual(zh_paras, en_paras):
    """Chinese and English paragraph blocks, toggled by data-lang."""
    zb = ''.join('<p>%s</p>' % esc(p) for p in zh_paras)
    eb = ''.join('<p>%s</p>' % esc(p) for p in en_paras)
    return ('<div data-lang="zh">%s</div><div data-lang="en" lang="en">%s</div>' % (zb, eb))

def gal(imgs, caps=None):
    cells = []
    for idx, im in enumerate(imgs):
        src = '../assets/img/exh/%s-%d.jpg' % (im['base'], max(im['widths']))
        cap = ''
        if caps and idx < len(caps) and caps[idx]:
            cz, ce = caps[idx]
            cap = ('<figcaption class="exhfig__cap">'
                   '<span data-lang="zh">%s</span>'
                   '<span data-lang="en" lang="en">%s</span></figcaption>') % (esc(cz), esc(ce))
        cells.append('<figure class="exhfig"><img src="%s" width="%d" height="%d" '
                     'loading="lazy" decoding="async" alt="">%s</figure>'
                     % (src, im['w'], im['h'], cap))
    return '<div class="exhgal">%s</div>' % ''.join(cells)

def meta_rows_obj(rows):
    return ''.join('<dt>%s</dt><dd>%s</dd>' % (esc(k), esc(v)) for k, v in rows)

def page_html(key, tzh, ten, subzh, suben, rows_zh, rows_en, body, works, gallery, poster, credit):
    """rows_zh / rows_en: label+value lists for each language."""
    mz = '<dl data-lang="zh">%s</dl>' % meta_rows_obj(rows_zh)
    me = '<dl data-lang="en" lang="en">%s</dl>' % meta_rows_obj(rows_en)
    poster_html = ''
    if poster:
        poster_html = ('<figure class="exhposter"><img src="../assets/img/exh/%s" width="512" height="1024" '
                       'decoding="async" alt=""></figure>' % poster)
    content = (
      '<div class="page-head"><div class="wrap">'
      '<span class="kicker">%s</span>'
      '<h1 class="page-head__title"><span data-lang="zh">%s</span><span data-lang="en">%s</span></h1>'
      '<p class="page-head__sub"><span data-lang="zh">%s</span><span data-lang="en">%s</span></p>'
      '</div></div>'
      '<section class="sect"><div class="wrap"><div class="exh-meta">%s%s</div></div></section>'
      '<section class="sect sect--text"><div class="wrap">'
      '<div class="exhbody">%s</div></div></section>'
      '%s'
      '<section class="sect"><div class="wrap">'
      '<h2 class="sect-title"><span data-lang="zh">展出作品</span><span data-lang="en">Works in the exhibition</span></h2>'
      '%s</div></section>'
      '<section class="sect"><div class="wrap">'
      '<h2 class="sect-title"><span data-lang="zh">展览现场</span><span data-lang="en">Installation views</span></h2>'
      '%s</div></section>'
      '<section class="sect"><div class="wrap"><p class="credit">%s</p>'
      '<p class="sect-back"><a class="link-arrow" href="./"><span data-lang="zh">&larr; 返回展览</span>'
      '<span data-lang="en">&larr; All exhibitions</span></a></p></div></section>'
    ) % (esc(key), esc(tzh), esc(ten), esc(subzh), esc(suben), mz, me, body,
         ('<section class="sect"><div class="wrap">%s</div></section>' % poster_html) if poster_html else '',
         works, gallery, esc(credit))
    return page(content, 1, '../', '%s — 冯硕' % tzh, '%s — Feng Shuo' % ten, subzh, suben)

# ---- 2008 Tales -------------------------------------------------------
z8 = ZH['2008']; e8 = EN['2008']
# Chinese preface paras = index 4..7 ; English: drop the generic Marlborough
# boilerplate (p3 announcement/p12 book list) and keep the essay + credit
body8 = dual(z8['paras'][4:7], e8['paras'][6:11])
rows8_zh = [('展览时间','2008-04-17 — 2008-05-17'),('地区','美国 · 纽约'),
            ('主办 / 地点','马乐伯画廊 Marlborough Gallery'),
            ('地址','545 West 25th Street, New York, NY 10001'),
            ('开幕酒会','2008-04-17 18:00—20:00'),('电话','(001) 212-541-4900')]
rows8_en = [('Dates','April 17 – May 17, 2008'),('Location','New York, USA'),
            ('Venue','Marlborough Gallery'),
            ('Address','545 West 25th Street, New York, NY 10001'),
            ('Reception','April 17, 2008, 6:00 – 8:00 pm'),('Tel','(001) 212-541-4900')]
w("exhibitions/2008-tales.html", page_html('2008','寓言','Tales',
    '2008 年纽约马乐伯画廊个展','Solo exhibition at Marlborough Chelsea, New York',
    rows8_zh, rows8_en, body8,
    gal(z8['processed'][:2], caps=[(z8['paras'][1], e8['paras'][1]),
                                    (z8['paras'][2], e8['paras'][2])]),
    gal(z8['processed'][2:], caps=[None, None, (z8['paras'][7], e8['paras'][13])]), None,
    '图片来源：fengshuo.cc 原始站点存档 / 作品与现场照片承蒙艺术家提供'))

# ---- 2012 Carnivalesque ----------------------------------------------
z12 = ZH['2012']; e12 = EN['2012']
body12 = dual(z12['paras'][1:10], e12['paras'][1:10])
rows12_zh = [('展览','狂欢 — 冯硕作品展'),('展览时间','2011.09.06 — 2011.10.05'),
             ('开幕酒会','2011.09.06 16:00'),('地点','M Art Center')]
rows12_en = [('Exhibition','The Carnivalesque — A Solo Exhibition by Feng Shuo'),
             ('Dates','6 September – 5 October 2011'),
             ('Reception','6 September 2011, 16:00'),('Venue','M Art Center')]
w("exhibitions/2012-carnival.html", page_html('2012','狂欢','The Carnivalesque',
    '2011 年 M Art Center 个展','A Solo Exhibition by Feng Shuo at M Art Center',
    rows12_zh, rows12_en, body12, '', gal(z12['processed'][1:]), 'poster-2012-512.jpg',
    '© Tony Godfrey 2011　中文翻译：王凯梅　图片来源：fengshuo.cc 原始站点存档'))
print('exhibition pages rebuilt')
