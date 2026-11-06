import io
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_p3.py'
g=io.open(p,encoding='utf-8').read()
# the stale block used href="NAME.html" inside about/ ; earlier patch added ../exhibitions/ correctly
# but an earlier run already emitted the bare form. Normalise any bare form to ../exhibitions/.
for nm in ('2012-carnival.html','2008-tales.html'):
    g=g.replace('href="%s"'%nm, 'href="../exhibitions/%s"'%nm)
io.open(p,'w',encoding='utf-8',newline='\n').write(g)
print('bare refs left:', sum(g.count('href="%s"'%n) for n in ('2012-carnival.html','2008-tales.html')))
print('../exhibitions refs:', g.count('../exhibitions/20'))