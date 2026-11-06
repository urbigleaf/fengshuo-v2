import io
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_lib.py'
g=io.open(p,encoding='utf-8').read()
bad1='<link rel="preload" href="{root}assets/fonts/f07.woff2" as="font" type="font/woff2" crossorigin>'
bad2='<link rel="stylesheet" href="{root}assets/css/fonts.css">'
print('literal-{root} font lines present:', bad1 in g, bad2 in g)
g=g.replace(bad1,'<link rel="preload" href="'+'{root}'+'assets/fonts/f07.woff2" as="font" type="font/woff2" crossorigin>')
io.open(p,'w',encoding='utf-8',newline='\n').write(g)
print('done - lines kept as f-string placeholders (they live inside f-string)')
# confirm they are inside the f-string returned by head()
i=g.find('f07.woff2')
seg=g[max(0,i-900):i]
print('inside f-string?', seg.count("f'''")>0 or "f'''" in seg)