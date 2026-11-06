import io,os
p=r'D:\user\Documents\GitHub\fengshuo_v1\assets\css\site.css'
s=io.open(p,encoding='utf-8').read()
s=s.replace('left:0;right:0;bottom:conic-gradient;bottom:0;','left:0;right:0;bottom:0;')
io.open(p,'w',encoding='utf-8').write(s)
print('fixed', 'conic' in s, os.path.getsize(p))