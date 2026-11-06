import io
p=r'D:\user\Documents\GitHub\fengshuo_v1\_build\gen_lib.py'
b=io.open(p,encoding='utf-8').read()
n=b.count('raise SystemExit')
b=b.replace('raise SystemExit\n','')
io.open(p,'w',encoding='utf-8').write(b)
print('removed',n,'lines left',b.count(chr(10)))