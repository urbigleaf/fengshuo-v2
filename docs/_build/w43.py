import io
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_p3.py'
g=io.open(p,encoding='utf-8').read()
i=g.find('href="#tales"')
j=g.find('href="#carnival"')
print('tales ctx:', repr(g[i-80:i+140]))
print()
print('carnival ctx:', repr(g[j-40:j+330]))