import io
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_p5.py'
g=io.open(p,encoding='utf-8').read()
# 1) gal() gains optional captions: list aligned to imgs, each (zh, en) or None
old_gal = '''def gal(imgs):
    cells = []
    for im in imgs:
        src = '../assets/img/exh/%s-%d.jpg' % (im['base'], max(im['widths']))
        cells.append('<figure class="exhfig"><img src="%s" width="%d" height="%d" '
                     'loading="lazy" decoding="async" alt=""></figure>' % (src, im['w'], im['h']))
    return '<div class="exhgal">%s</div>' % ''.join(cells)'''
new_gal = '''def gal(imgs, caps=None):
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
    return '<div class="exhgal">%s</div>' % ''.join(cells)'''
print('gal found:', old_gal in g)
g = g.replace(old_gal, new_gal)
# 2) 2008 body: drop last paragraph (photo caption)
g = g.replace("body8 = dual(z8['paras'][4:8], e8['paras'][6:12])",
              "body8 = dual(z8['paras'][4:7], e8['paras'][6:11])")
# 3) attach caption to the 3rd installation photo (index 2 of the gallery slice)
g = g.replace("rows8_zh, rows8_en, body8, gal(z8['processed'][:2]), gal(z8['processed'][2:]), None,",
  "rows8_zh, rows8_en, body8, gal(z8['processed'][:2]),\n"
  "    gal(z8['processed'][2:], caps=[None, None, (z8['paras'][7], e8['paras'][13])]), None,")
io.open(p,'w',encoding='utf-8',newline='\n').write(g)
print('body8 patched:', "paras'][4:7]" in g)
print('caps patched:', 'caps=[None, None,' in g)