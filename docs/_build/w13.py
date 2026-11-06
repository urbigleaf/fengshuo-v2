import io,os
code = r'''# -*- coding: utf-8 -*-
import json, os, html
from gen_p3 import *

D = json.load(open(os.path.join(BUILD,'exh_clean.json'), encoding='utf-8'))

def esc(t): return html.escape(t, quote=False)
def paras(txt):
    blocks=[]
    for chunk in txt.split('\n'):
        chunk=chunk.strip()
        if chunk: blocks.append('<p>%s</p>' % esc(chunk))
    return ''.join(blocks)

def gal(imgs, start=0):
    cells=[]
    for im in imgs:
        w=im['w']; h=im['h']
        src='../assets/img/exh/%s-%d.jpg' % (im['base'], max(im['widths']))
        cells.append(
          '<figure class="exhfig"><img src="%s" width="%d" height="%d" loading="lazy" decoding="async" alt="">'
          '</figure>' % (src, w, h))
    return '<div class="exhgal">%s</div>' % ''.join(cells)

def build(key, title_zh, title_en, sub, meta_rows, body_paras, work_imgs, gallery_imgs, credit):
    meta = ''.join('<dt>%s</dt><dd>%s</dd>' % (esc(k), esc(v)) for k,v in meta_rows)
    body = ''.join('<p>%s</p>' % esc(p) for p in body_paras)
    works = gal(work_imgs)
    gallery = gal(gallery_imgs)
    content = (
      '<div class="page-head"><div class="wrap">'
      '<span class="kicker">%s</span>'
      '<h1 class="page-head__title"><span data-lang="zh">%s</span><span data-lang="en">%s</span></h1>'
      '<p class="page-head__sub"><span data-lang="zh">%s</span></p>'
      '</div></div>'
      '<section class="sect"><div class="wrap"><div class="exh-meta"><dl>%s</dl></div></div></section>'
      '<section class="sect"><div class="wrap">%s</div></section>'
      '<section class="sect"><div class="wrap"><h2 class="sect-title"><span data-lang="zh">展出作品</span>'
      '<span data-lang="en">Works in the exhibition</span></h2>%s</div></section>'
      '<section class="sect"><div class="wrap"><h2 class="sect-title"><span data-lang="zh">展览现场</span>'
      '<span data-lang="en">Installation views</span></h2>%s</div></section>'
      '<section class="sect"><div class="wrap"><p class="credit">%s</p></div></section>'
    ) % (esc(key), esc(title_zh), esc(title_en), esc(sub), meta, body, works, gallery, esc(credit))
    return page(content, 0, '../', '%s — 冯硕' % title_zh, '%s — Feng Shuo' % title_en, sub, sub)

d08=D['2008']; d12=D['2012']
meta08=[('展览时间','2008-04-17 — 2008-05-17'),('地区','美国 · 纽约'),
        ('主办 / 地点','马乐伯画廊 Marlborough Gallery'),
        ('地址','545 West 25th Street, New York, NY 10001'),
        ('开幕酒会','2008-04-17 18:00—20:00'),('电话','(001) 212-541-4900')]
meta12=[('展览时间','2012'),('地区','中国'),('展览','冯硕个人作品展「狂欢」')]

w("exhibitions/2008-tales.html", build('2008','寓言','Tales','2008 年纽约马乐伯画廊个展',
    meta08, d08['paras'][4:8], d08['processed'][:2], d08['processed'][2:],
    '图片来源：fengshuo.cc 原始站点存档'))
w("exhibitions/2012-carnival.html", build('2012','狂欢','The Carnivalesque','2012 年冯硕个人作品展',
    meta12, d12['paras'][1:10], d12['processed'][:1], d12['processed'][1:],
    d12['paras'][10]))
print('exhibition pages ok')
'''
io.open(r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_p5.py','w',encoding='utf-8').write(code)
print('p5 written')