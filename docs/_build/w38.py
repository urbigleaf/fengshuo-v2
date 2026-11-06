import io
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_p3.py'
g=io.open(p,encoding='utf-8').read()
# find each of the two anchors and ensure the matching close is </a>, not </div>
for yr in ('2012','2008'):
    i=g.find('href="%s-'%yr)
    s=g.rfind('<a class="exh"',0,i)
    e=g.find("</div>'",s)
    seg=g[s:e+8]
    print(yr,'->',repr(seg[-90:]))