import io,re
R=r'D:\user\Documents\GitHub\fengshuo_v1'
a=io.open(R+r'\about\index.html',encoding='utf-8').read()
for m in re.finditer(r'href="([^"]*2012-carnival\.html)"', a):
    s=max(0,m.start()-170)
    print('REF:', m.group(1), '| ctx:', repr(a[s:m.end()+20]))
    print()