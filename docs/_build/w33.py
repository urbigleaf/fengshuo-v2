import io,re
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_p3.py'
g=io.open(p,encoding='utf-8').read()
i=g.find('exh-list')
print(g[max(0,i-1500):i+700])