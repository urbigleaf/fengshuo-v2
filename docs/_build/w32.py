import io,re
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_p4.py'
g=io.open(p,encoding='utf-8').read()
print('len',len(g))
for k in ['#tales','#carnival','exh-list','def build_exh','exhibitions/index.html','2008-tales','2012-carnival']:
    print('%-24s -> %s' % (k, g.count(k)))