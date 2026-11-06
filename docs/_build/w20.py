import io,re
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_lib.py'
g=io.open(p,encoding='utf-8').read()
for m in re.finditer(r'\{root\}', g):
    s=max(0,m.start()-120); print('...', g[s:m.end()+40].replace('\n','\\n')[-170:])
print('---- head signature ----')
m=re.search(r'def head\([^)]*\):', g)
print(g[m.start():m.start()+260] if m else 'no head def')