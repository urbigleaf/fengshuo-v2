import io
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_p3.py'
g=io.open(p,encoding='utf-8').read()
i=g.find("'<div class=\"exh\"'")
if i<0: i=g.find('<div class="exh">')
# show the surrounding structure with line numbers to plan a safe patch
lines=g[:i+200].count('\n')+1
print('approx line', lines)
seg=g[max(0,i-700):i+2600]
for n,l in enumerate(seg.split('\n')): print('%4d| %s'%(lines-8+n, l[:110]))