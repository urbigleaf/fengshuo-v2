import io
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_p3.py'
g=io.open(p,encoding='utf-8').read()
i=g.find('exh__year">2012')
print('REPR around 2012 entry:')
print(repr(g[i-90:i+120]))
print()
j=g.find('exh__year">2008')
print('REPR around 2008 entry:')
print(repr(g[j-90:j+120]))