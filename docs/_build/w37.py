import io
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_p3.py'
g=io.open(p,encoding='utf-8').read()
n=g.count('<div class="exh"><span class="exh__year">')
print('exh entries found:', n)
g=g.replace('<div class="exh"><span class="exh__year">2012</span>',
            '<a class="exh" href="2012-carnival.html"><span class="exh__year">2012</span>')
g=g.replace('<div class="exh"><span class="exh__year">2008</span>',
            '<a class="exh" href="2008-tales.html"><span class="exh__year">2008</span>')
# close the two anchors: they end with arrow + </div> right before the 1994 entry
g=g.replace('''<span class="exh__arrow">&rarr;</span></div>\'
\'<div class="exh"><span class="exh__year">1994</span>''',
'''<span class="exh__arrow">&rarr;</span></a>\'
\'<div class="exh"><span class="exh__year">1994</span>''')
# and the 2008 one ends before the 1994 entry too (2008 is listed after 2012)
io.open(p,'w',encoding='utf-8',newline='\n').write(g)
print('2012 link:', 'href="2012-carnival.html"' in g)
print('2008 link:', 'href="2008-tales.html"' in g)
print('anchor closes:', g.count('<a class="exh"'), g.count('</a>'))