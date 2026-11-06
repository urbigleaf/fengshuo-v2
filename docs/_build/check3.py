import io,os,re,glob
R=r'D:\user\Documents\GitHub\fengshuo_v1'
pages=[p for p in glob.glob(os.path.join(R,'**','*.html'),recursive=True) if '_build' not in p]
ext=sum(1 for p in pages if re.search(r'fonts\.(googleapis|gstatic)', io.open(p,encoding='utf-8').read()))
old=sum(1 for p in pages if 'fengshuo.art' in io.open(p,encoding='utf-8').read())
new=sum(1 for p in pages if 'fengshuo.cc' in io.open(p,encoding='utf-8').read())
fc=sum(1 for p in pages if 'assets/css/fonts.css' in io.open(p,encoding='utf-8').read())
print('pages', len(pages), '| google-fonts refs', ext, '| old domain', old, '| fengshuo.cc', new, '| fonts.css linked', fc)
css=io.open(os.path.join(R,'assets','css','site.css'),encoding='utf-8').read()
for k in ['column-width','break-inside:avoid','height:auto','aspect-ratio:var(--ar']:
    print(' css', k, '->', k in css)
# card markup no longer needs --ar
s=io.open(os.path.join(R,'works','index.html'),encoding='utf-8').read()
print('cards:', s.count('class="card"'), '| statement --ar inline:', s.count('--ar:'))
sm=io.open(os.path.join(R,'sitemap.xml'),encoding='utf-8').read()
print('sitemap urls:', sm.count('<loc>'), '| cc domain:', 'fengshuo.cc' in sm)