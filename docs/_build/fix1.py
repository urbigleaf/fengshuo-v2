import io,json,re,os
B=r'D:\user\Documents\GitHub\fengshuo_v1\_build'
R=os.path.dirname(B)
css=io.open(os.path.join(B,'gf.css'),encoding='utf-8').read()
m=json.load(io.open(os.path.join(B,'fontmap.json'),encoding='utf-8-sig'))
for u,n in m.items():
    css=css.replace('url(%s)'%u,'url(../fonts/%s)'%n)
css='/* Self-hosted fonts: Marcellus (display) + Inter (300/400/500).\n   Latin + Latin-Ext only; CJK falls through to system fonts. */\n'+css
io.open(os.path.join(R,'assets','css','fonts.css'),'w',encoding='utf-8',newline='\n').write(css)
print('fonts.css', len(css), 'bytes; refs', css.count('../fonts/'))

# patch generator: domain + self-hosted font link
p=os.path.join(B,'gen_lib.py')
g=io.open(p,encoding='utf-8').read()
g=g.replace("SITE = 'https://fengshuo.art'","SITE = 'https://fengshuo.cc'")
old='''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Marcellus&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">'''
new='''<link rel="preload" href="{root}assets/fonts/f07.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}assets/css/fonts.css">'''
print('site patched:', "fengshuo.cc" in g, '| fonts block found:', old in g)
if old in g: g=g.replace(old,new)
io.open(p,'w',encoding='utf-8',newline='\n').write(g)