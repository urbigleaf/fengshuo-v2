import io,os
code = '''# -*- coding: utf-8 -*-
from gen_p3 import *

# ---------------- 404
notfound = (
'<div class="page-head"><div class="wrap"><span class="kicker">404</span>'
'<h1 class="page-head__title"><span data-lang="zh">页面不在这里</span><span data-lang="en">This page is not here</span></h1>'
'<p class="page-head__sub"><span data-lang="zh">你要找的页面可能已被移动。可以从下面继续。</span>'
'<span data-lang="en">The page you are looking for may have moved. Continue below.</span></p></div></div>'
'<section class="sect"><div class="wrap"><div class="exh-list">'
'<a class="exh" href="/works/"><span class="exh__year">&rarr;</span><span><span class="exh__t" data-lang="zh">全部作品</span>'
'<span class="exh__t" data-lang="en">All works</span></span><span class="exh__arrow">&rarr;</span></a>'
'<a class="exh" href="/exhibitions/"><span class="exh__year">&rarr;</span><span><span class="exh__t" data-lang="zh">展览</span>'
'<span class="exh__t" data-lang="en">Exhibitions</span></span><span class="exh__arrow">&rarr;</span></a>'
'<a class="exh" href="/about/"><span class="exh__year">&rarr;</span><span><span class="exh__t" data-lang="zh">艺术家</span>'
'<span class="exh__t" data-lang="en">Artist</span></span><span class="exh__arrow">&rarr;</span></a>'
'</div></div></section>')
w("404.html", page(notfound, 0, "", "页面未找到 — 冯硕", "Not found — Feng Shuo",
   "页面未找到。", "Page not found."))

# ---------------- robots + sitemap
w("robots.txt", "User-agent: *\\nAllow: /\\nSitemap: %s/sitemap.xml\\n" % SITE)
urls = [("", "1.0"), ("works/", "0.9"), ("about/", "0.8"), ("exhibitions/", "0.8")]
urls += [("works/%s.html" % x["slug"], "0.6") for x in works]
entries = "".join(
    "  <url><loc>%s/%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>\\n" % (SITE, u, NOW, p)
    for u, p in urls)
w("sitemap.xml",
  '<?xml version="1.0" encoding="UTF-8"?>\\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\\n'
  + entries + "</urlset>\\n")
print("404/robots/sitemap ok:", len(urls), "urls")
'''
io.open(r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_p4.py','w',encoding='utf-8').write(code)
print('p4 written')