import io,re
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_p3.py'
g=io.open(p,encoding='utf-8').read()
# 1) make the two list entries clickable -> link to standalone pages
a1 = '''\'<div class="exh"><span class="exh__year">2012</span>\''''
b1 = '''\'<a class="exh" href="2012-carnival.html"><span class="exh__year">2012</span>\''''
a2 = '''\'<div class="exh"><span class="exh__year">2008</span>\''''
b2 = '''\'<a class="exh" href="2008-tales.html"><span class="exh__year">2008</span>\''''
print('found 2012 entry:', a1 in g)
print('found 2008 entry:', a2 in g)
g=g.replace(a1,b1).replace(a2,b2)
# closing tags for these two entries
g=g.replace('''<span class="exh__arrow">&rarr;</span></div>\'
\'<a class="exh"''','''<span class="exh__arrow">&rarr;</span></a>\'
\'<a class="exh"''')
io.open(p,'w',encoding='utf-8',newline='\n').write(g)
print('patched list entries')