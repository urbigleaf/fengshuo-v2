import io,os
P=r'D:\user\Documents\GitHub\fengshuo_v1\_build'
b=io.open(os.path.join(P,'gen_lib.py'),encoding='utf-8').read()
old='    p = os.path.join(ROOT, rel)'
new='    p = rel if os.path.isabs(rel) else os.path.join(ROOT, rel)'
print('found', old in b)
b=b.replace(old,new)
io.open(os.path.join(P,'gen_lib.py'),'w',encoding='utf-8').write(b)
print('patched', new in io.open(os.path.join(P,'gen_lib.py'),encoding='utf-8').read())