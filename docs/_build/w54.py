import io
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_p5.py'
g=io.open(p,encoding='utf-8').read()
old = "rows8_zh, rows8_en, body8, gal(z8['processed'][:2]),"
new = ("rows8_zh, rows8_en, body8,\n"
       "    gal(z8['processed'][:2], caps=[(z8['paras'][1], e8['paras'][1]),\n"
       "                                    (z8['paras'][2], e8['paras'][2])]),")
print('works slice found:', old in g)
g = g.replace(old, new)
io.open(p,'w',encoding='utf-8',newline='\n').write(g)
print('works caps patched:', "paras'][1], e8['paras'][1]" in g)